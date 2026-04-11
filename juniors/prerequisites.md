# Prerequisites

Everything you need before starting the course. The Foundations modules
require zero installation --- just a Claude account and a web browser.
Additional tools are installed progressively as you need them.

Budget 30-45 minutes for first-time setup of the Week 1 tools. It's
totally fine to ask a parent or teacher for help with installation.

---

## Accounts

### Anthropic Account (required)

You need an Anthropic account with a Claude plan to use Claude Desktop
and Claude Code.

1. Go to [claude.ai](https://claude.ai) and create an account
2. Subscribe to a Claude plan (Pro or Team) --- a parent or guardian
   may need to help with this
3. You'll use the same account for Claude web, Desktop, Mobile, and Code

---

## What You Need for Foundations (Modules 1-2)

**Foundations 1** requires nothing to install --- just a Claude account
and a web browser at [claude.ai](https://claude.ai).

**Foundations 2** walks you through installing Claude Desktop (the
desktop app where your AI stock tools will eventually live). You'll
also optionally set up the Claude mobile app ([iOS](https://apps.apple.com/app/claude-by-anthropic/id6473753684) / [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude)).

No terminal, no code, no command-line tools needed for either
Foundations module.

---

## Software for Week 1 (Building AI Tools)

Install these before starting Week 1. If you already installed Claude
Desktop during Foundations 2, you're ahead --- just pick up from step 2.

### 1. Claude Desktop

The AI assistant app where you'll connect to the tools you build.
You may have already installed this in Foundations 2.

- Download from [claude.ai/download](https://claude.ai/download)
- Install and sign in with your Anthropic account
- Available for Mac and Windows

### 2. Claude Code

The AI-powered tool that builds software for you. This is what you'll
use to create everything in this course --- you describe what you want,
and Claude Code writes the code.

**Mac / Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

Close and reopen your terminal, then verify:
```bash
claude --version
```

**How to open your terminal:**
- **Mac:** Press `Cmd + Space`, type `Terminal`, press Enter
- **Windows:** Press `Win + R`, type `cmd`, press Enter

### 3. uv (Python Package Manager)

Claude Code uses this behind the scenes to manage Python. You don't
need to know what Python is --- Claude Code handles it all.

**Mac / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen your terminal, then verify:
```bash
uv --version
```

---

## Software --- Bonus Module (Running AI on Your Computer)

Only needed if you're doing the optional bonus project after Week 2.

### 4. Ollama

Runs AI models on your own computer (instead of in the cloud).

- Download from [ollama.com](https://ollama.com)
- Install and run it (you'll see a llama icon in your menu bar / taskbar)
- Pull the required models:

```bash
ollama pull nomic-embed-text
ollama pull qwen3.5:4b          # 16GB RAM (recommended)
# ollama pull qwen3.5:0.8b      # 8GB RAM (lighter alternative)
# ollama pull qwen3.5:9b        # 32GB+ RAM (higher quality)
```

Not sure how much RAM your computer has?
- **Mac:** Click the Apple menu > About This Mac > look for "Memory"
- **Windows:** Right-click the Start button > System > look for "Installed RAM"

---

## Hardware

| Tier | RAM | Disk | Notes |
|------|-----|------|-------|
| **Minimum** (all weeks) | 8GB | 5GB free | Mac or Windows, internet required |
| **Recommended** | 16GB | 10GB free | Can run larger local models (bonus module) |

---

## Free Data Sources (no setup needed)

These are used throughout the course. No accounts or API keys required:

| Source | What It Provides | Used In |
|--------|-----------------|---------|
| Yahoo Finance (yfinance) | Stock prices, company info | Weeks 1-4 |
| SEC EDGAR | Company annual reports | Bonus module |
| StockAnalysis.com | Stock data for checking your work | Reference |

Claude Code installs everything automatically when it builds your
tools. You don't need to install anything manually.

---

## Verification Checklist

Before starting Week 1, make sure everything works:

- [ ] Claude Desktop opens and you can chat with Claude
- [ ] Terminal opens and you can type commands
- [ ] `claude --version` shows a version number
- [ ] `uv --version` shows a version number

If doing the bonus module:
- [ ] `ollama --version` shows a version number
- [ ] `ollama list` shows your pulled models

---

## Troubleshooting

**"claude: command not found"**
Run the installer again (see step 2 above), then close and reopen your
terminal. The installer adds Claude Code to your path, but the current
terminal session doesn't pick it up.

**"uv: command not found"**
Close and reopen your terminal after installing uv. The installer adds
uv to your path, but the current terminal session doesn't pick it up.

**Claude Code asks for an API key**
Sign in when prompted. Claude Code uses your Anthropic account --- the
same one you use for Claude Desktop.

**Nothing works and I'm stuck**
Ask a parent, teacher, or tech-savvy friend for help. The setup is the
hardest part of the whole course --- once it's done, everything else is
easier.
