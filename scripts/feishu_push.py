#!/usr/bin/env python3
"""Send a Horizon summary to Feishu via Feishu App (not webhook bot).

Requires these environment variables:
  FEISHU_APP_ID       — Feishu app ID (cli_xxx)
  FEISHU_APP_SECRET   — Feishu app secret

And at least one of:
  FEISHU_RECEIVE_ID_TYPE  — "open_id" (default), "user_id", "email", or "chat_id"
  FEISHU_RECEIVE_ID       — the target user open_id / user_id / email / chat_id

Usage:
    python scripts/feishu_push.py --file docs/index.md
    python scripts/feishu_push.py --text "Hello from Horizon"
    cat summary.md | python scripts/feishu_push.py --stdin
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

FEISHU_BASE = "https://open.feishu.cn/open-apis"


def get_tenant_access_token(app_id: str, app_secret: str) -> str:
    """Obtain tenant_access_token from Feishu."""
    url = f"{FEISHU_BASE}/auth/v3/tenant_access_token/internal"
    payload = json.dumps({"app_id": app_id, "app_secret": app_secret}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if data.get("code", -1) != 0:
        raise RuntimeError(
            f"Failed to get tenant_access_token: code={data.get('code')}, msg={data.get('msg')}"
        )
    return data["tenant_access_token"]


def send_message(
    token: str,
    receive_id_type: str,
    receive_id: str,
    content: dict,
    msg_type: str = "interactive",
) -> dict:
    """Send a message to a Feishu user or group via the messaging API."""
    url = f"{FEISHU_BASE}/im/v1/messages?receive_id_type={receive_id_type}"
    payload = json.dumps(
        {
            "receive_id": receive_id,
            "msg_type": msg_type,
            "content": json.dumps(content, ensure_ascii=False),
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Feishu API HTTP {e.code}: {body}") from e


def truncate(text: str, limit: int = 28000) -> str:
    """Feishu card markdown has a ~30k char limit per element."""
    if len(text) <= limit:
        return text
    return text[:limit] + "\n\n...(内容过长已截断)"


def build_card(date_str: str, summary_markdown: str) -> dict:
    """Build a Feishu interactive card with the daily summary."""
    # Split summary into chunks of ~28000 chars if needed
    chunks = []
    remaining = summary_markdown
    while remaining:
        if len(remaining) <= 28000:
            chunks.append(remaining)
            break
        # Try to split at a paragraph boundary
        split_pos = remaining.rfind("\n\n", 0, 28000)
        if split_pos < 10000:
            split_pos = 28000
        chunks.append(remaining[:split_pos])
        remaining = remaining[split_pos:].lstrip("\n")

    elements = [
        {
            "tag": "markdown",
            "content": truncate(chunks[0]),
        }
    ]
    for chunk in chunks[1:]:
        elements.append({"tag": "hr"})
        elements.append({"tag": "markdown", "content": truncate(chunk)})

    return {
        "config": {"wide_screen_mode": True, "update_multi": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"Horizon 每日 AI 情报速递 - {date_str}"},
            "template": "blue",
        },
        "elements": elements,
    }


def main():
    parser = argparse.ArgumentParser(description="Push Horizon summary to Feishu via App")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to markdown file to send")
    group.add_argument("--text", help="Inline text to send")
    group.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--date", default=None, help="Date string (default: today)")
    args = parser.parse_args()

    # Load content
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.text:
        content = args.text
    elif args.stdin:
        content = sys.stdin.read()

    # Check env vars
    app_id = os.getenv("FEISHU_APP_ID", "")
    app_secret = os.getenv("FEISHU_APP_SECRET", "")
    receive_id = os.getenv("FEISHU_RECEIVE_ID", "")
    receive_id_type = os.getenv("FEISHU_RECEIVE_ID_TYPE", "open_id")

    if not app_id or not app_secret:
        print("ERROR: FEISHU_APP_ID and FEISHU_APP_SECRET must be set", file=sys.stderr)
        sys.exit(1)
    if not receive_id:
        print(
            "ERROR: FEISHU_RECEIVE_ID must be set (user open_id, user_id, email, or chat_id)",
            file=sys.stderr,
        )
        print(
            "  Set FEISHU_RECEIVE_ID_TYPE accordingly: open_id / user_id / email / chat_id",
            file=sys.stderr,
        )
        sys.exit(1)

    from datetime import date

    date_str = args.date or date.today().isoformat()

    print(f"Getting tenant_access_token for app {app_id}...")
    token = get_tenant_access_token(app_id, app_secret)
    print("✓ Got token")

    card = build_card(date_str, content)
    print(f"Sending card to {receive_id_type}={receive_id}...")
    result = send_message(token, receive_id_type, receive_id, card)
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if result.get("code", -1) == 0:
        print("✓ Message sent successfully!")
    else:
        print(f"✗ Failed: code={result.get('code')}, msg={result.get('msg')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
