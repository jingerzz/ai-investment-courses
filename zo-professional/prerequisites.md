# Prerequisites

You do not need to be a software engineer to take this course. You do need a Zo Computer account, basic comfort with files and folders, and a willingness to read a small amount of code without panicking. That is enough.

## Required

### 1. A Zo Computer account

Sign up using Jing's referral link:

> https://zo-computer.cello.so/8dcc6g0vZVs

The free tier is enough to complete every exercise. You can upgrade later if you want more compute or longer-running services.

### 2. The ability to find these areas inside Zo

After you log in, take a minute to open each of these areas at least once. You do not need to do anything in them yet — just confirm you can find them. They are listed in the left sidebar.

| Area | What it is for |
| --- | --- |
| Workspace | Your files. Markdown notes, scripts, datasets, anything else. |
| Terminal | A command line that runs inside your Zo. |
| Settings | Where you choose your AI model and store secrets. |
| Hosting | Where your sites and services live. |
| Automations | Where scheduled jobs are managed. |

If you are missing any of these, your account may not be fully provisioned yet. Refresh the page; if it still does not appear, contact Zo support before continuing.

### 3. An AI model selected for chat

Open `Settings → AI` and pick a model. A free-tier model is fine for most reading and Q&A. When the course asks you to build or modify a server, switch to a stronger coding-grade model (a Claude Sonnet or higher tier model is recommended). You can switch back and forth as needed.

## Recommended (but not required)

- **A Claude Sonnet-class coding model** for the build steps in Weeks 2–4. Faster and more accurate than the free tier when editing code.
- **Claude Code or Codex** as optional coding assistants. Useful if you want to make deeper edits to a server. Skippable.
- **Basic terminal comfort** — knowing what `cd`, `ls`, `python`, and `git` do, and being willing to read an error message instead of closing the window.
- **A GitHub account** if you want to fork the course repository and make your own changes. Optional.

## Not Required

You will see these terms in the course. You do **not** need any prior experience with them to start.

- Paid market data subscriptions
- A production trading account
- Prior MCP, RAG, or LLM internals knowledge
- Prior experience deploying web apps
- Prior Python expertise beyond reading short scripts

If any of those are familiar, the course will move quickly for you. If none of them are, the course was written for you specifically.

## Accounts and Access

Zo can store credentials as environment secrets. **Never paste API keys directly into course files or chat messages.** When the course needs a key, it will tell you where to put it inside Zo settings.

The course relies on free public data sources where possible:

- **Yahoo Finance** for stock and ETF price data
- **SEC EDGAR** for company filings
- **Local files and hosted services on Zo** for everything you build

You will not need a Bloomberg terminal, a Refinitiv subscription, or a paid API key to complete the exercises.

## Folder Setup

Before starting Foundations 1, create a single folder inside your Zo workspace where everything you do during the course will live:

```
AI-Investing-Course/
├── notes/         ← research notes, decisions, prompts you save
├── servers/       ← copies of the course MCP servers
├── datasets/      ← any data files or DuckDB databases
├── dashboards/    ← page specs, screenshots, sketches
└── agents/        ← scheduled-job specs and run logs
```

Keep the structure boring. The point is that the AI can find things later without asking. We will explain why this matters in Foundations 2.

If you forget what each folder is for, that is fine — Foundations 2 covers it in detail. For now, just create the folders and move on.
