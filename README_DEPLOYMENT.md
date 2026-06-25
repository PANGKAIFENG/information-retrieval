# 每日飞书 AI 产品情报雷达 — 部署指南

基于 [Horizon](https://github.com/Thysrael/Horizon) 搭建的个人 AI 产品情报雷达。

每天北京时间 **09:00** 自动运行，抓取 AI Agent / Runtime、AI 产品商业化、服装 / 设计 AI 竞品、开源工具等方向的最新动态，生成中文 Markdown 简报并推送到你的飞书群。

---

## 功能概览

- 每天自动运行（GitHub Actions cron `0 1 * * *` UTC = 北京时间 09:00）
- 生成结构化中文 Markdown 简报，包含四个固定小节：
  - **本期结论**（发生了什么）
  - **为什么值得关注**（行业意义）
  - **对我们的影响**（对我方的具体影响）
  - **后续动作**（建议的跟进）
- 推送到飞书群（Feishu collapsible card）
- 简报归档在 `outputs/summaries/`
- 支持手动触发（`workflow_dispatch`）
- 密钥全部通过环境变量 / GitHub Secrets 注入，不入库

---

## 快速部署

### 1. 配置 GitHub Secrets

在仓库 `Settings → Secrets and variables → Actions → New repository secret` 添加：

| Secret 名 | 必需 | 说明 |
|-----------|------|------|
| `OPENAI_API_KEY` | 是 | OpenAI API Key（或 OpenAI 兼容服务的 key） |
| `FEISHU_WEBHOOK_URL` | 是 | 飞书自定义机器人 webhook URL |

可选：
- `OPENAI_BASE_URL` — 如使用代理或兼容网关，在 `data/config.github.json` 的 `ai` 节点加 `"base_url_env": "OPENAI_BASE_URL"`
- `GITHUB_TOKEN` — 用于提高 GitHub API 速率限制（Actions 自动提供 `GITHUB_TOKEN`，通常无需额外配置）

### 2. 获取飞书 Webhook URL

1. 打开飞书群 → **设置** → **群机器人** → **添加机器人** → **自定义机器人**
2. 填写机器人名称和安全设置（建议启用关键词 `AI` 或签名校验）
3. 复制 webhook URL，格式类似：`https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx`
4. 把它存为 GitHub Secret `FEISHU_WEBHOOK_URL`

### 3. 验证推送

手动触发 workflow：
- 仓库 `Actions` 页 → 选择 `Daily Horizon Summary` → `Run workflow`
- 检查日志出现 webhook 发送相关输出
- 检查飞书群是否收到卡片消息

---

## 本地运行

```bash
# 安装依赖（需要 uv：https://docs.astral.sh/uv/）
uv sync

# 准备配置（GitHub Actions 用 config.github.json，本地复制为 config.json）
cp data/config.github.json data/config.json

# 设置环境变量
export OPENAI_API_KEY="sk-xxx"
export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/xxx"

# 运行（抓取最近 24 小时）
uv run horizon --hours 24

# 仅测试飞书推送（dry-run，不真实发送）
FEISHU_WEBHOOK_URL=https://example.com/webhook uv run horizon-webhook --lang zh --dry-run
```

---

## 如何修改信息源

编辑 `data/config.github.json` 的 `sources` 部分：

### RSS 源
```json
{
  "name": "你的源名",
  "url": "https://example.com/feed.xml",
  "enabled": true,
  "category": "ai-commercialization"
}
```

### GitHub Release 源
```json
{
  "type": "repo_releases",
  "owner": "组织名",
  "repo": "仓库名",
  "enabled": true
}
```

### 分类（category）
`category` 值对应 `filtering.category_groups` 的分组，用于限额和归类。当前分类：
- `agent-runtime` — Agent / Runtime
- `ai-commercialization` — AI 产品商业化
- `fashion-design-ai` — 服装 / 设计 AI 竞品
- `open-source-tools` — 开源工具
- `other` — 默认分组

---

## 如何修改阈值

编辑 `data/config.github.json` 的 `filtering` 部分：

```json
{
  "ai_score_threshold": 6.0,      // 0-10，越高越严格
  "time_window_hours": 24,        // 时间窗口
  "max_items": 15,                // 单次最多保留多少条
  "category_groups": {
    "agent-runtime": { "limit": 5 },
    "ai-commercialization": { "limit": 5 }
  }
}
```

- 觉得日报太短 → 降低 `ai_score_threshold`（如 5.0）或提高各分组 `limit`
- 觉得日报太长 / 噪音多 → 提高 `ai_score_threshold`（如 7.0）或降低 `max_items`

---

## 如何修改运行频率

编辑 `.github/workflows/daily-summary.yml`：

```yaml
on:
  schedule:
    - cron: '0 1 * * *'   # UTC 01:00 = 北京时间 09:00（每天）
```

常用 cron 示例：
- `0 1 * * *` — 每天北京时间 09:00
- `0 3 * * *` — 每天北京时间 11:00
- `0 1 * * 1` — 每周一北京时间 09:00
- `0 1 */3 * *` — 每 3 天北京时间 09:00

> 注意：GitHub Actions schedule 按 UTC 时间运行。北京时间 = UTC + 8。

---

## 简报归档

- 每日简报自动归档到 `outputs/summaries/`
- 同时部署到 GitHub Pages（`gh-pages` 分支）
- 如不希望公开归档：把仓库设为 private，或删除 workflow 中的 `Deploy to GitHub Pages` 步骤

---

## 失败排查

| 问题 | 排查方式 |
|------|---------|
| 飞书没收到消息 | 检查 `FEISHU_WEBHOOK_URL` 是否正确、机器人是否在群里、安全设置是否匹配 |
| OpenAI 调用失败 | 检查 `OPENAI_API_KEY` 是否有效、额度是否充足 |
| GitHub Actions 抓取为空 | 检查时间窗口、信息源 `enabled` 状态、RSS 是否失效 |
| 速率限制 | 配置 `GITHUB_TOKEN` 提高 GitHub API 配额 |

回滚：直接在 GitHub Actions 历史里 `Re-run` 旧版本，或 `git revert` 对应 commit。

---

## 两周复盘方法

`reviews/manual-review.csv` 用于人工复盘：

1. 每两周打开 `reviews/manual-review.csv`
2. 回顾过去两周的日报条目，判断每个信息源是否仍值得订阅
3. 记录 `keep`（yes/no）、`action`（keep / drop / monitor）、`notes`
4. 根据复盘结果调整 `data/config.github.json` 的信息源和阈值

---

## 安全说明

- 所有密钥通过环境变量 / GitHub Secrets 注入，不会出现在代码中
- 机器人 webhook URL 是唯一凭证，不要泄露
- 如 webhook 泄露，立即在飞书删除机器人并重新创建
- 仓库中不包含任何真实 API Key、webhook 或 token

---

## 技术架构

- 基于 [Horizon](https://github.com/Thysrael/Horizon)（MIT License）
- Python 3.12 + uv
- GitHub Actions 调度
- 飞书 Custom Bot（incoming webhook）
- 输出：Markdown 简报 + 飞书 collapsible card
