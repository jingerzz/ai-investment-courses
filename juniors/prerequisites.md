# Prerequisites

Everything you need before starting the course. Budget 30-45 minutes
for first-time setup. It's totally fine to ask a parent or teacher
for help with installation.

---

## Accounts

### Anthropic Account (required)

You need an Anthropic account with a Claude plan to use Claude Desktop
and Claude Code.

1. Go to [claude.ai](https://claude.ai) and create an account
2. Subscribe to a Claude plan (Pro or Team) — a parent or guardian
   may need to help with this
3. You'll use the same account for both Claude Desktop and Claude Code

---

## Software — Main Course (Weeks 1-4)

Install these in order. Each step depends on the previous one.

### 1. Claude Desktop

The AI assistant app where you'll use the tools you build.

- Download from [claude.ai/download](https://claude.ai/download)
- Install and sign in with your Anthropic account
- Available for Mac and Windows

### 2. Node.js

Required to install Claude Code. You may already have it.

- Download the LTS version from [nodejs.org](https://nodejs.org)
- Run the installer (accept all defaults)
- To verify, open your terminal and type:
  ```bash
  node --version
  ```
  You should see a version number like `v20.x.x` or higher.

**How to open your terminal:**
- **Mac:** Press `Cmd + Space`, type `Terminal`, press Enter
- **Windows:** Press `Win + R`, type `cmd`, press Enter

### 3. Claude Code

The AI-powered tool that builds software for you. This is what you'll
use to create everything in this course.

Open your terminal and run:
```bash
npm install -g @anthropic-ai/claude-code
```

Verify it installed:
```bash
claude --version
```

### 4. uv (Python Package Manager)

Claude Code uses this behind the scenes to manage Python. You don't
need to know what Python is — Claude Code handles it all.

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

## Software — Bonus Module (Running AI on Your Computer)

Only needed if you're doing the optional bonus project after Week 2.

### 5. Ollama

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

See `bonus-local-rag/exercise/ollama_quickstart.md` for more details.

---

## Hardware

### Minimum (Weeks 1-4)
- Mac or Windows PC
- 8GB RAM
- 5GB free disk space
- Internet connection

### Recommended
- 16GB RAM (especially for the bonus Ollama project)
- 10GB free disk space (with bonus module models)

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
- [ ] `ollama ls` shows your pulled models

---

## Troubleshooting

**"npm: command not found"**
Install Node.js from [nodejs.org](https://nodejs.org), then close and
reopen your terminal.

**"claude: command not found"**
Run `npm install -g @anthropic-ai/claude-code` again. If it still fails,
try `sudo npm install -g @anthropic-ai/claude-code` (Mac) or run
your terminal as Administrator (Windows).

**"uv: command not found"**
Close and reopen your terminal after installing uv. The installer adds
uv to your path, but the current terminal session doesn't pick it up.

**Claude Code asks for an API key**
Sign in when prompted. Claude Code uses your Anthropic account — the
same one you use for Claude Desktop.

**Nothing works and I'm stuck**
Ask a parent, teacher, or tech-savvy friend for help. The setup is the
hardest part of the whole course — once it's done, everything else is
easier.
