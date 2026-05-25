<p align="center">
  <img src="assets/banner.svg" width="100%" alt="AI Agents Safe Coding Skills" />
</p>

<p align="center">
  <a href="https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills/stargazers"><img src="https://img.shields.io/github/stars/administrakt0r/AI-Agents-Safe-Coding-Skills?style=for-the-badge&logo=github&color=f59e0b&labelColor=0d1117" alt="Stars"></a>
  <a href="https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills"><img src="https://img.shields.io/badge/1,300+-SKILL.md_Playbooks-8b5cf6?style=for-the-badge&labelColor=0d1117" alt="Skills"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&labelColor=0d1117" alt="MIT"></a>
  <a href="https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills/discussions"><img src="https://img.shields.io/badge/Discussions-Ask_Questions-3b82f6?style=for-the-badge&labelColor=0d1117" alt="Discussions"></a>
</p>

<p align="center">
  <b>Copy. Paste. Go.</b> — A universal skill library any AI agent can load in seconds.<br>
  <sub>Works with Claude Code · Cursor · Gemini CLI · Codex CLI · OpenCode · Copilot · any AI tool</sub>
</p>

---

## 👋 Send This To Your AI Agent

Copy the block below and paste it to **any** AI coding agent. It tells the agent exactly where to get skills and how to use them.

```text
I want you to load the AI Agents Safe Coding Skills library from GitHub:
https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills

For every skill I name with a @ prefix, read the matching SKILL.md file from the
skills/ folder in that repository and follow it as your operating instructions.

Example: if I say @brainstorming, read this file and follow it:
https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills/blob/main/skills/brainstorming/SKILL.md

Available skills I may request: @brainstorming, @architecture, @systematic-debugging,
@test-driven-development, @security-auditor, @frontend-developer, @api-design-principles,
@app-builder, @database-design, @docker-expert, @deployment-procedures,
@verification-before-completion, and 1,300+ more (full list in CATALOG.md).

Work in phases: plan → implement → test → verify → summarize.
```

> **That's it.** Your agent now knows this repository exists and how to load any skill you name.

---

## ⚡ Quick Start Prompts

These prompts tell your agent to load specific skills for common tasks. Just pick one and send it to your AI.

### 🆕 Project From Scratch

```text
Load these skills from https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills:
@brainstorming @concise-planning @app-builder @backend-dev-guidelines
@frontend-developer @database-design @test-driven-development @verification-before-completion

I want to build [describe your app]. Choose the simplest stack, make a plan,
scaffold the project, implement the first end-to-end slice, and add tests.
```

### 🔍 Debug Something Broken

```text
Load these skills from https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills:
@systematic-debugging @test-fixing @browser-automation @verification-before-completion

This is broken: [paste error]. Reproduce, isolate root cause, implement the
smallest fix, and verify. Do NOT refactor unrelated code.
```

### 🔒 Security Hardening

```text
Load these skills from https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills:
@architect-review @security-auditor @deployment-procedures
@observability-engineer @verification-before-completion

Review this codebase for architecture gaps, security risks, deployment issues,
and observability blind spots. Fix high-value issues and give me a release checklist.
```

---

## 📖 How Skills Work

Each skill lives in `skills/<skill-name>/SKILL.md` — a markdown file that teaches an AI agent *how* to do something well.

| If You Say This | The Agent Reads This | And Does This |
|----------------|---------------------|---------------|
| `@brainstorming` | `skills/brainstorming/SKILL.md` | Structured product/feature planning |
| `@test-driven-development` | `skills/test-driven-development/SKILL.md` | Red-green-refactor TDD cycle |
| `@security-auditor` | `skills/security-auditor/SKILL.md` | Security review checklist |
| `@systematic-debugging` | `skills/systematic-debugging/SKILL.md` | Reproduce → isolate → fix → verify |

No installers, no config files, no dependencies. Just a URL and a skill name.

---

## 🧰 Who Is This For?

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-@skill_name-7c3aed?style=for-the-badge&labelColor=0d1117" alt="Claude Code">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Cursor-@skill_name-f97316?style=for-the-badge&labelColor=0d1117" alt="Cursor">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Gemini_CLI-Use_skill-4285f4?style=for-the-badge&labelColor=0d1117" alt="Gemini CLI">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Codex_CLI-Use_skill-10a37f?style=for-the-badge&labelColor=0d1117" alt="Codex CLI">
  <br><br>
  <img src="https://img.shields.io/badge/OpenCode-opencode_run-6b7280?style=for-the-badge&labelColor=0d1117" alt="OpenCode">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Copilot-Paste_skill-0284c7?style=for-the-badge&labelColor=0d1117" alt="Copilot">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Any_Agent-Just_ask-8b5cf6?style=for-the-badge&labelColor=0d1117" alt="Any Agent">
</p>

Every tool works. The pattern is the same everywhere:

> **Name the skill. The agent reads it from GitHub. The agent follows the instructions.**

| Tool | How To Invoke | Example |
|------|--------------|---------|
| Claude Code | `Use @skill-name to...` or `/skill-name` | `Use @brainstorming to plan my app` |
| Cursor | `@skill-name do this...` | `@brainstorming plan a SaaS MVP` |
| Gemini CLI | `Use skill-name to...` | `Use brainstorming to design the architecture` |
| Codex CLI | `Use skill-name to...` | `Use test-driven-development to add this feature` |
| OpenCode | `opencode run @skill-name` | `opencode run @security-auditor "review ./src"` |
| GitHub Copilot | Paste the command in chat | `Use the brainstorming skill to plan this` |
| Any AI Agent | Mention the skill + repo URL | `Load these skills: @skill-name` |

---

## 🌟 Featured Skills

<p align="center">
  <a href="skills/brainstorming/SKILL.md"><img src="https://img.shields.io/badge/🧠_brainstorming-Plan_anything-8b5cf6?style=for-the-badge&labelColor=0d1117&logoWidth=0" alt="brainstorming"></a>
  <a href="skills/architecture/SKILL.md"><img src="https://img.shields.io/badge/🏗️_architecture-System_design-3b82f6?style=for-the-badge&labelColor=0d1117" alt="architecture"></a>
  <a href="skills/test-driven-development/SKILL.md"><img src="https://img.shields.io/badge/🧪_tdd-Test_first-22c55e?style=for-the-badge&labelColor=0d1117" alt="tdd"></a>
  <a href="skills/systematic-debugging/SKILL.md"><img src="https://img.shields.io/badge/🔍_debugging-Find_fixes-ef4444?style=for-the-badge&labelColor=0d1117" alt="debugging"></a>
</p>

<p align="center">
  <a href="skills/security-auditor/SKILL.md"><img src="https://img.shields.io/badge/🔒_security--auditor-Harden_your_app-f59e0b?style=for-the-badge&labelColor=0d1117" alt="security-auditor"></a>
  <a href="skills/frontend-developer/SKILL.md"><img src="https://img.shields.io/badge/🎨_frontend--developer-Build_UI-ec4899?style=for-the-badge&labelColor=0d1117" alt="frontend-developer"></a>
  <a href="skills/api-design-principles/SKILL.md"><img src="https://img.shields.io/badge/🔌_api--design-Clean_APIs-06b6d4?style=for-the-badge&labelColor=0d1117" alt="api-design"></a>
  <a href="skills/docker-expert/SKILL.md"><img src="https://img.shields.io/badge/🐳_docker--expert-Containerize_it-0ea5e9?style=for-the-badge&labelColor=0d1117" alt="docker-expert"></a>
</p>

| Domain | Skills | What They Do |
|--------|--------|-------------|
| 🏗️ **Architecture** | `architecture`, `c4-context`, `senior-architect`, `microservices-patterns` | System design, ADRs, scalable patterns |
| 🎨 **Frontend** | `frontend-developer`, `frontend-design`, `react-patterns`, `web-design-guidelines` | UI development, accessibility, responsive design |
| ⚙️ **Backend** | `backend-dev-guidelines`, `api-patterns`, `database-design`, `docker-expert` | APIs, data modeling, containers |
| 🧪 **Testing** | `test-driven-development`, `testing-patterns`, `test-fixing`, `browser-automation` | TDD, QA, E2E testing |
| 🔒 **Security** | `security-auditor`, `api-security-best-practices`, `vulnerability-scanner` | AppSec, pentesting, compliance |
| 🚀 **DevOps** | `deployment-procedures`, `aws-serverless`, `vercel-deployment`, `observability-engineer` | CI/CD, cloud, monitoring |
| 🧠 **AI/ML** | `prompt-engineer`, `rag-engineer`, `ai-agent-development`, `langgraph` | LLM apps, agents, RAG pipelines |
| 📈 **Growth** | `copywriting`, `seo-audit`, `pricing-strategy`, `ab-testing` | Marketing, CRO, analytics |

> **[Browse the full catalog →](CATALOG.md)** · **[Role-based bundles →](docs/users/bundles.md)**

---

## 🧩 Copy-Paste Workflow Recipes

### Add a Feature to an Existing App

```text
Load from https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills:
@brainstorming @concise-planning @backend-dev-guidelines @frontend-developer
@api-patterns @database-design @test-driven-development @verification-before-completion

Add [feature] to this codebase. Inspect first, propose the smallest plan,
then implement backend, frontend, and tests. Reuse existing patterns.
```

### Redesign Without Breaking Things

```text
Load from https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills:
@architect-review @frontend-design @frontend-developer @react-patterns
@web-design-guidelines @verification-before-completion

Redesign this product's UI without breaking existing functionality.
Audit the current state first, propose a direction, implement incrementally,
and verify everything still works.
```

### Pre-Launch Checklist

```text
Load from https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills:
@architect-review @security-auditor @deployment-procedures
@observability-engineer @verification-before-completion

Give me a full pre-launch hardening pass. Review architecture, security,
deployment readiness, and monitoring. Fix critical issues and deliver
a consolidated release checklist.
```

---

## 🚀 Project Structure

```
📦 AI-Agents-Safe-Coding-Skills
 ┣ 📂 skills/           ← 1,300+ SKILL.md playbooks (the library)
 ┣ 📂 docs/             ← Guides, bundles, workflows
 ┣ 📂 tools/            ← Validators and support scripts
 ┣ 📂 assets/           ← Images and banners
 ┣ 📂 data/             ← Indexes and generated metadata
 ┣ 📜 CATALOG.md        ← Browsable list of every skill
 ┣ 📜 LICENSE           ← MIT License
 ┗ 📜 README.md         ← You are here
```

---

## 🌐 More From The Author

<p align="center">
  <a href="https://github.com/administrakt0r"><img src="https://img.shields.io/badge/GitHub-@administrakt0r-ec4899?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117" alt="GitHub"></a>
  <a href="https://x.com/administrakt0r"><img src="https://img.shields.io/badge/X-@administrakt0r-1d9bf0?style=for-the-badge&logo=x&logoColor=white&labelColor=0d1117" alt="X"></a>
  <a href="https://buymeacoffee.com/administrakt0r"><img src="https://img.shields.io/badge/Buy_Me_A_Coffee-Support-ff813f?style=for-the-badge&logo=buymeacoffee&logoColor=white&labelColor=0d1117" alt="Buy me a coffee"></a>
</p>

<br>

<table>
<tr>
<td align="center" width="33%">

### 🤖 **LLM.Kiwi**
*AI Tools Directory*

The best AI tools directory on the internet. Find, compare, and launch AI tools for coding, content, automation, and more.

[**Visit llm.kiwi →**](https://llm.kiwi)

</td>
<td align="center" width="33%">

### 🌐 **WPineu**
*Web Development & WordPress*

Professional web development, custom themes, plugins, and high-performance websites tailored to your business.

[**Visit wpineu.com →**](https://wpineu.com)

</td>
<td align="center" width="33%">

### 📞 **CallerHouse**
*Enterprise VoIP Solutions*

Cloud PBX, SIP trunking, and business phone systems that scale with your organization's needs.

[**Visit callerhouse.com →**](https://callerhouse.com)

</td>
</tr>
</table>

---

## 🤝 Contribute

Found a gap? Want to add a skill? PRs are welcome.

```
1. mkdir -p skills/your-skill
2. Copy docs/contributors/skill-template.md as SKILL.md
3. Write the playbook
4. Open a pull request
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full guide.

---

## 🛡️ Security

This repository is actively maintained. Skills are instruction playbooks and can describe risky operations by design — they tell agents *how* to work, not *what* to avoid.

- `SKILL.md` files are scanned for high-risk command patterns
- Prompt injection and unsafe tool chaining are reviewed
- Stale or unsafe skills are revised or removed

See [`SECURITY.md`](SECURITY.md) for details.

---

## 📜 License

<p align="center">
  <img src="https://img.shields.io/badge/Code-MIT-22c55e?style=for-the-badge&labelColor=0d1117" alt="MIT">
  <img src="https://img.shields.io/badge/Content-CC_BY_4.0-3b82f6?style=for-the-badge&labelColor=0d1117" alt="CC BY 4.0">
</p>

Code and tooling: **MIT License** ([LICENSE](LICENSE)).  
Documentation: **CC BY 4.0** ([LICENSE-CONTENT](LICENSE-CONTENT)).

---

<p align="center">
  <sub>Built by <a href="https://github.com/administrakt0r">administrakt0r</a> · 
  <a href="https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills/discussions">💬 Discussions</a> · 
  <a href="https://github.com/administrakt0r/AI-Agents-Safe-Coding-Skills/issues">🐛 Issues</a></sub>
  <br><br>
  <a href="https://llm.kiwi">llm.kiwi</a> · <a href="https://wpineu.com">wpineu.com</a> · <a href="https://callerhouse.com">callerhouse.com</a>
</p>
