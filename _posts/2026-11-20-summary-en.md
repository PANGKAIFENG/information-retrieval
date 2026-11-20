---
layout: default
title: "Horizon Summary: 2026-11-20 (EN)"
date: 2026-11-20
lang: en
---

> From 14 items, 10 important content pieces were selected

---

1. [Critical Buffer Overflow in OpenSSL's EVP_EncodeBlock() Detected](#item-1) ⭐️ 9.0/10
2. [AI Model Claude Solves Black Hole Physics Problems](#item-2) ⭐️ 9.0/10
3. [PostgreSQL 19 Release](#item-3) ⭐️ 9.0/10
4. [Anthropic's Nasdaq Debut](#item-4) ⭐️ 7.0/10
5. [Onlook: Open-Source Tool for Designers](#item-5) ⭐️ 7.0/10
6. [The 98% Slot Machine: How Paid Advertising Became an Extraction Tax](#item-6) ⭐️ 7.0/10
7. [AI Token Fraud on Platforms](#item-7) ⭐️ 7.0/10
8. [llm-gemini 0.38 Release and Google Gemini 4 Neon Pricing Update](#item-8) ⭐️ 7.0/10
9. [datasette-arrows 0.1a0 Released](#item-9) ⭐️ 7.0/10
10. [Curl Library Rewrite in Rust by Daniel Stenberg](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Critical Buffer Overflow in OpenSSL's EVP_EncodeBlock() Detected](https://github.com/openssl/openssl/pull/33652) ⭐️ 9.0/10

A critical buffer overflow vulnerability has been identified in OpenSSL's EVP_EncodeBlock() function, with a potential for significant exploitation. This vulnerability affects the security of widely-used technologies and could have a significant impact on systems relying on OpenSSL. The vulnerability is in the base64 encoding function EVP_EncodeBlock() and can be exploited if untrusted input is used.

hackernews · JacobHenner · Nov 20, 02:01 · [Discussion](https://news.ycombinator.com/item?id=50569226)

**Background**: OpenSSL is a widely-used cryptographic library that provides security functions for various applications. A buffer overflow occurs when a program tries to write data beyond the allocated buffer, potentially leading to system instability or security breaches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/OpenSSL">OpenSSL - Wikipedia</a></li>
<li><a href="https://github.com/openssl/openssl">GitHub - openssl / openssl : General purpose TLS and crypto library</a></li>
<li><a href="https://en.m.wikipedia.org/wiki/Common_Vulnerability_Scoring_System">Common Vulnerability Scoring System - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight concerns about the severity of the vulnerability and the need for timely patching, with some suggesting that the CVSS score may be exaggerated.

**Tags**: `#OpenSSL`, `#Security Vulnerability`, `#CVE-2026-121481`, `#Buffer Overflow`, `#Software Security`

---

<a id="item-2"></a>
## [AI Model Claude Solves Black Hole Physics Problems](https://www.anthropic.com/research/claude-black-hole-physics) ⭐️ 9.0/10

The AI model Claude has solved two open problems in the physics of black holes, contributing to the understanding of quantum mechanics and relativity. This breakthrough could have significant implications for the broader field of theoretical physics, potentially leading to new insights into the fundamental nature of the universe. The solutions involve complex calculations and theoretical models, and they were developed using Anthropic's AI model Claude.

hackernews · cybermango · Nov 19, 17:30 · [Discussion](https://news.ycombinator.com/item?id=50563148)

**Background**: The study of black holes is a critical area in theoretical physics, involving the intersection of quantum mechanics and general relativity. AI has been increasingly used to tackle complex problems in physics.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/">Claude by Anthropic | The AI for problem solvers</a></li>
<li><a href="https://moleculs.ai/model/claude">Claude AI Online — AI Chatbot | Moleculs. ai</a></li>
<li><a href="https://eu.36kr.com/en/p/4045367967470721">Is Physics About to Be Conquered by AI ? 5 Unsolved Quantum ...</a></li>
<li><a href="https://scispace.com/papers/boltzmann-machines-and-quantum-many-body-problems-1h8l8gwk">(PDF) Boltzmann machines and quantum many-body problems (2023)</a></li>
<li><a href="https://physicstoday.scitation.org/doi/full/10.1063/PT.3.4164?cookieSet=1">Machine learning meets quantum physics : Physics Today: Vol 72...</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight concerns about the anthropomorphizing of AI and the need for transparency in AI development processes.

**Tags**: `#AI Research`, `#Quantum Physics`, `#Black Hole`, `#Theoretical Physics`, `#Machine Learning`

---

<a id="item-3"></a>
## [PostgreSQL 19 Release](https://www.postgresql.org/docs/release/19.0/) ⭐️ 9.0/10

PostgreSQL 19 has been released, a major update to the widely-used open-source relational database system, featuring new features and improvements. The release of PostgreSQL 19 is significant as it brings performance enhancements and new features that could impact the database management landscape. PostgreSQL 19 introduces 'read-your-writes' consistency with the new 'WAIT FOR LSN' command, improving data consistency for applications sending reads to standbys.

hackernews · linzhangrun · Nov 20, 03:45 · [Discussion](https://news.ycombinator.com/item?id=50569890)

**Background**: PostgreSQL is a powerful, open-source object-relational database system known for its reliability, feature robustness, and performance, with over 35 years of active development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PostgreSQL">PostgreSQL - Wikipedia</a></li>
<li><a href="https://www.postgresql.org/">PostgreSQL : The world's most advanced open source database</a></li>

</ul>
</details>

**Discussion**: Community discussions indicate high engagement and interest, with users noting the improved reliability and new features like 'read-your-writes' consistency.

**Tags**: `#PostgreSQL`, `#Database`, `#Open Source`, `#Database Management`, `#Software Update`

---

<a id="item-4"></a>
## [Anthropic's Nasdaq Debut](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) ⭐️ 7.0/10

Anthropic's historic debut on the Nasdaq marks a significant milestone for the AI industry, as the company enters the public market with a valuation that reflects its potential impact on technology and the job market. The event is significant as it highlights the growing importance of AI companies in the tech sector and raises questions about the future of AI development and its implications for the job market. Anthropic's valuation at the time of its IPO was a notable figure, reflecting both the company's potential and the high expectations placed on AI companies by investors.

hackernews · wslh · Nov 19, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50562754)

**Background**: Anthropic is an AI research and development company known for its work on large language models. Its debut on the stock market is a testament to the rapid growth of AI companies and the increasing interest in AI technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>
<li><a href="https://claude.com/">Claude by Anthropic | The AI for problem solvers</a></li>

</ul>
</details>

**Discussion**: Community discussions reflect a mix of excitement and concern, with some worried about the impact on the job market and others questioning the valuation of AI companies.

**Tags**: `#AI Industry`, `#Stock Market`, `#Anthropic`, `#AI Impact`, `#Tech News`

---

<a id="item-5"></a>
## [Onlook: Open-Source Tool for Designers](https://github.com/onlook-dev/onlook/) ⭐️ 7.0/10

Onlook, an open-source developer tool for designers, allows direct design in code, gaining over 25,000 supporters and 100+ contributors, and being the #1 trending repo twice. Onlook could significantly impact collaboration between designers and developers, potentially revolutionizing the design process and streamlining workflows. Onlook provides a canvas on top of the real codebase, enabling designers to work on multiple simultaneous worktrees and review changes as PRs.

hackernews · D_R_Farrell · Nov 19, 16:34 · [Discussion](https://news.ycombinator.com/item?id=50562320)

**Background**: Agentic design tools are designed to work the way designers do, focusing on exploration and divergent thinking. They often integrate with real codebases to provide a more seamless design and development process.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kdnuggets.com/agentic-system-design-a-self-study-roadmap">Agentic System Design : A Self-Study Roadmap - KDnuggets</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/">Top 4 Agentic AI Design Patterns</a></li>
<li><a href="https://link.springer.com/book/10.1007/978-3-032-01402-3">Agentic Design Patterns: A Hands-On Guide to Building Intelligent...</a></li>
<li><a href="https://www.merriam-webster.com/dictionary/does">DOES Definition & Meaning - Merriam-Webster</a></li>
<li><a href="https://does.dc.gov/">Washington, D.C. - | does</a></li>
<li><a href="https://eslteacher.org/do-vs-does/">Do vs. Does : How to Use Do and Does in English - ESL Teachers</a></li>
<li><a href="/url?opi=89978449&q=CAESigEBxCJF1xL3z6bnhoYe3iwAtfVRl3e-A8d-rVKUBI2dugGKSQ9qPhiwszIa4lryb0YtmfaytB39JAu2qYXKQj6_R8XFqTSxQodhwEIV0b0xZmmnfTUdrVHNML2-GFxbJlA4o6rWsJGt3fuoMQjmB-FxDQzFWqkYCOgsD-MRaoLSQdycDTQSyPXwFR4&sa=U&uoh=3&ved=2ahUKEwjbg8Hni5aYAxVGPUQIHdASL2oQFnoECAYQAg&usg=AOvVaw28t0v1u-PjsFAePlLfhaoH">From code to Figma and back. Prototyping in your real design system</a></li>
<li><a href="/url?opi=89978449&q=CAESagHEIkXX8y8t_r-OKmTbFGzlRVFCbwFX7lqNXicGscMGJcI6Vsap6lHGMp1WFTI-Yv9kaBjGkFBc0XqZNwePfGS1Nrv4QvoNte0sYe6m60uMlI_z1IDs5aAtu0uptFtMDgn_geld8LgR8VU&sa=U&uoh=3&ved=2ahUKEwjbg8Hni5aYAxVGPUQIHdASL2oQFnoECAkQAg&usg=AOvVaw2xpB17Hc21Fhw-nH3EVQTD">Onlook (YC W25) – An open-source developer tool for designers</a></li>
<li><a href="/url?opi=89978449&q=CAESsgEBxCJF1-4KXHvG1Z9So5wAsy_OEH_eo2mpUYeNax8KBv3CvgwwHTOBeXepLG_k8BZODyQ_gbBP1DbdMVaVGY7OiZL7LxKhRg96Pmv8uOBiymMz6ypRBhJjINWNdz5AHuBMYxggpRwuJekwbQH47_uUcWZs204-8KcxhSLImfAhfN4qlzUdFtdVM1ek_gpd-emoC0IU5iyfTXM1dbj7WAONv3C7dxYpMdvPoKD34uiQ9QCr&sa=U&uoh=3&ved=2ahUKEwjbg8Hni5aYAxVGPUQIHdASL2oQFnoECAcQAg&usg=AOvVaw3tdlkWlmIJl390Ak09X0oR">Designers use canvas to explore design directions with AI-built ...</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed, with some praising the tool's potential and others questioning its practicality and integration with existing workflows.

**Tags**: `#Developer Tools`, `#Design Collaboration`, `#Open Source`, `#Software Engineering`, `#Design`

---

<a id="item-6"></a>
## [The 98% Slot Machine: How Paid Advertising Became an Extraction Tax](https://globalcommercegraph.com/writing/the-ninety-eight-percent-slot-machine) ⭐️ 7.0/10

This article analyzes the functioning of paid advertising, comparing it to a slot machine, focusing on the dynamics of ad auctions and their impact on advertisers. The article highlights the significant impact of ad auctions on advertisers, sparking a discussion about the broader implications of digital advertising on the advertising industry and consumer behavior. The article discusses the concept of ad auctions as a marketplace where advertisers bid for ad space, and the potential for manipulation in this system.

hackernews · dev1one1 · Nov 19, 18:35 · [Discussion](https://news.ycombinator.com/item?id=50564159)

**Background**: Ad auctions are a key component of digital marketing, where advertisers bid for ad space on various platforms. The concept of an 'extraction tax' refers to the idea that advertisers are paying for ad space without necessarily seeing a return on investment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.publift.com/blog/google-adx-vs-google-adsense">Google AdX vs AdSense: Differences, Requirements and Revenue</a></li>
<li><a href="https://www.shopify.com/blog/search-engine-marketing">Search Engine Marketing (SEM): Complete Guide + Expert... - Shopify</a></li>
<li><a href="https://www.webfx.com/social-media/pricing/how-much-does-facebook-advertising-cost/">How Much Do Facebook Ads Cost in 2026?</a></li>

</ul>
</details>

**Discussion**: Community comments reflect mixed opinions, with some arguing that the analogy is flawed and others suggesting that there are ways to manipulate the system to achieve better results.

**Tags**: `#Advertising`, `#Digital Marketing`, `#Economics`, `#Technology`

---

<a id="item-7"></a>
## [AI Token Fraud on Platforms](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/) ⭐️ 7.0/10

Claire Vo, founder of ChatPRD, reports a surge in token fraud involving the abuse of free trials for commercial gain, including reselling tokens and running commercial enterprises on top of the ChatPRD agent. This fraud highlights the need for robust security measures in AI platforms and the potential impact on product management and AI usage, as it can lead to financial loss and compromised data integrity. The abuse includes the use of free trials to build Roblox and Fortnite maps, and the creation of prompts like SVGs of pelicans riding bicycles to test underlying models, indicating sophisticated methods used by scammers.

rss · Simon Willison · Nov 20, 02:49

**Background**: Token fraud in AI platforms refers to the unauthorized use of AI resources, often through fraudulent means, which can lead to significant financial and operational losses for companies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=ZDpP7JXPlhc">How I fight token fraud as an AI founder - YouTube</a></li>
<li><a href="https://www.chatprd.ai/">ChatPRD - The #1 AI Platform for Product Managers</a></li>

</ul>
</details>

**Discussion**: Community discussions indicate a mix of concern and agreement on the severity of the issue, with some suggesting stricter verification processes for free trials.

**Tags**: `#AI Ethics`, `#Product Management`, `#Cybersecurity`, `#AI Fraud`, `#AI Platforms`

---

<a id="item-8"></a>
## [llm-gemini 0.38 Release and Google Gemini 4 Neon Pricing Update](https://simonwillison.net/2026/Nov/18/llm-gemini/) ⭐️ 7.0/10

llm-gemini 0.38 has been released, and Google has introduced Gemini 4 Neon with revised pricing for its AI models. This update is significant for AI and machine learning enthusiasts as it brings new features and pricing changes that could impact the market. llm-gemini 0.38 includes new features and improvements, while Google's Gemini 4 Neon offers different pricing tiers for various use cases.

rss · Simon Willison · Nov 18, 23:59

**Background**: llm-gemini is an open-source large language model, and Google's Gemini is a suite of AI models designed for various applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.merriam-webster.com/dictionary/does">DOES Definition & Meaning - Merriam-Webster</a></li>

</ul>
</details>

**Discussion**: Community discussions are focused on the potential impact of the new pricing and the benefits of the updated llm-gemini version.

**Tags**: `#AI`, `#Machine Learning`, `#Software Development`, `#Pricing`, `#Technology Updates`

---

<a id="item-9"></a>
## [datasette-arrows 0.1a0 Released](https://simonwillison.net/2026/Nov/18/datasette-arrows/) ⭐️ 7.0/10

The release of datasette-arrows 0.1a0 introduces a plugin for Datasette that leverages Apache Arrow's streaming format for efficient data handling. This development enhances Datasette's capabilities for handling large datasets, which is crucial for data-intensive applications and web development. The plugin uses the Apache Arrow streaming format to enable efficient data handling, and it is compatible with various tools like DuckDB, pandas, and Polars.

rss · Simon Willison · Nov 18, 17:09

**Background**: Datasette is a web-based tool for exploring and publishing data, while Apache Arrow is a columnar in-memory data format designed for high-performance data processing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacamp.com/tutorial/apache-arrow">Apache Arrow : A Beginner’s Guide with Practical Examples | DataCamp</a></li>
<li><a href="https://arrow.apache.org/">Apache Arrow | Apache Arrow</a></li>
<li><a href="https://www.ozercemkelahmet.com/tools/apache-arrow">Apache Arrow : in-memory columnar data and zero-copy exchange...</a></li>
<li><a href="https://arrow.apache.org/">Apache Arrow | Apache Arrow</a></li>
<li><a href="https://makerstack.co/reviews/datasette-review/">Datasette Review 2026: 7.6/10, Free and Open Source</a></li>
<li><a href="https://medium.com/@hadiyolworld007/one-dataset-two-runtimes-with-shared-arrow-fe3f5eb66f0a">One Dataset, Two Runtimes with Shared Arrow | Medium</a></li>

</ul>
</details>

**Discussion**: The community seems to be positively responding to the new plugin, with some highlighting its potential for improving data handling in web applications.

**Tags**: `#Datasette`, `#Apache Arrow`, `#Data Handling`, `#Web Development`, `#Plugin Development`

---

<a id="item-10"></a>
## [Curl Library Rewrite in Rust by Daniel Stenberg](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

Daniel Stenberg discusses the conversion of the curl library from C to Rust, noting improvements and bug fixes made during the rewrite process. This rewrite is significant as it could lead to improved performance, security, and maintainability of the curl library, benefiting the Rust community and users of the curl library. The conversion involved converting 185,000 lines of C code into 340,000 lines of Rust code, with over 300 commits and 200 bug fixes.

rss · Simon Willison · Nov 18, 15:58

**Background**: Curl is a widely-used command-line tool for transferring data using various protocols. Rust is a systems programming language known for its performance and safety features.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust ( programming language ) - Wikipedia</a></li>
<li><a href="https://www.designveloper.com/blog/rust-vs-c-plus-plus/">Rust Vs C ++ Performance: Speed, Safety, And Real-World Tradeoffs</a></li>
<li><a href="https://www.w3schools.com/rust/rust_intro.php">Introduction to Rust</a></li>

</ul>
</details>

**Discussion**: The community discussion focuses on the benefits of using Rust for security, with some highlighting the improved performance and safety of the curl library.

**Tags**: `#daniel-stenberg`, `#curl`, `#rust`, `#security`, `#programming`

---