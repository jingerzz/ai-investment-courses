# Prerequisites

Everything you need before starting the course. Week 1 requires
minimal setup (15 minutes). Additional tools for Week 2 can be
installed later.

---

## Accounts

### Anthropic Account (required)

You need an Anthropic account with a Claude plan to use Claude Desktop
and Claude Code.

1. Go to [claude.ai](https://claude.ai) and create an account
2. Subscribe to a Claude plan (Pro or Team)
3. You'll use the same account for both Claude Desktop and Claude Code

---

## Software for Week 1

You only need three things to start. Install these in order.

### 1. Claude Desktop

The AI assistant app where you'll use the tools you build.

- Download from [claude.ai/download](https://claude.ai/download)
- Install and sign in with your Anthropic account
- Available for Mac and Windows

### 2. A Terminal

You'll type a few commands to install the course servers. You don't
need to be a terminal expert — just copy-paste the commands shown in
each exercise.

**How to open your terminal:**
- **Mac:** Press `Cmd + Space`, type `Terminal`, press Enter
- **Windows:** Press `Win + R`, type `cmd`, press Enter

If you've never used a terminal before, [Learn Enough Command Line to
Be Dangerous](https://www.learnenough.com/command-line-tutorial/basics)
covers everything you'll need in about 10 minutes. You only need the
basics: navigating folders (`cd`) and running commands.

### 3. uv (Python Package Manager)

This installs the course servers and their dependencies. You don't
need to know Python — uv just handles the plumbing.

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

You should see a version number like `uv 0.7.x`.

### 4. Course Files

Download the course repository, which contains the MCP servers, data
files, and exercises you'll use throughout all 4 weeks.

**If you have git installed:**
```bash
git clone https://github.com/jingerzz/ai-investment-courses.git
cd ai-investment-courses/professional
```

**If you don't have git** (or aren't sure), download the ZIP instead:
1. Go to [github.com/jingerzz/ai-investment-courses](https://github.com/jingerzz/ai-investment-courses)
2. Click the green **Code** button, then **Download ZIP**
3. Unzip to your home folder and rename the folder to `ai-investment-courses`

### Week 1 Verification Checklist

Before starting Week 1, confirm:

- [ ] Claude Desktop opens and you can chat with Claude
- [ ] Terminal opens and you can type commands
- [ ] `uv --version` shows a version number
- [ ] Course files exist: `ls ~/ai-investment-courses/professional/servers/`
      shows `spy-tlt-course` and `page-index-rag-course`

That's it. You're ready for Week 1.

---

## Additional Software for Week 2

Install these before starting Week 2. Not needed for Week 1.

### 5. Node.js

Required to install Claude Code. You may already have it.

- Download the LTS version from [nodejs.org](https://nodejs.org)
- Run the installer (accept all defaults)
- To verify, open your terminal and type:
  ```bash
  node --version
  ```
  You should see a version number like `v20.x.x` or higher.

### 6. Claude Code

The AI-powered CLI that builds tools for you. In Week 2, you'll use
Claude Code to create your own MCP server.

Open your terminal and run:
```bash
npm install -g @anthropic-ai/claude-code
```

Verify it installed:
```bash
claude --version
```

### 7. Ollama (Local AI Models)

Runs AI models locally on your machine for private document Q&A. In
Week 2, you'll use Ollama with the page-index-rag server to analyze
SEC filings.

- **Mac:** `brew install ollama` or download from [ollama.com](https://ollama.com)
- **Windows:** Download from [ollama.com/download](https://ollama.com/download)
- Install and run it (you'll see a llama icon in your menu bar)

Pull the course model:

```bash
ollama pull qwen3.5:0.8b          # Default — runs on any machine (8GB+ RAM)
# ollama pull qwen3.5:4b          # Optional upgrade for 16GB RAM
# ollama pull qwen3.5:9b          # Optional upgrade for 32GB+ RAM
```

The course defaults to `qwen3.5:0.8b` — the smallest model that works.
It runs on any machine with 8GB RAM. Larger models give better answers
but use more resources. The hybrid approach helps: Ollama handles
document search, Claude Desktop does the sophisticated reasoning.

### Week 2 Verification Checklist

Before starting Week 2, confirm the Week 1 items plus:

- [ ] `claude --version` shows a version number
- [ ] `ollama --version` shows a version number
- [ ] `ollama list` shows `qwen3.5:0.8b`

---

## Hardware

| Tier | RAM | Disk | Notes |
|------|-----|------|-------|
| **Minimum** (all weeks) | 8GB | 5GB free | Mac or Windows, internet required |
| **Recommended** | 16GB | 10GB free | Can run larger local models in Week 2 |
| **Power user** | 32GB+ | 10GB free | Can run `qwen3.5:9b` for higher quality RAG |

---

## Free Data Sources (no setup needed)

These are used throughout the course. No accounts or API keys required:

| Source | What It Provides | Used In |
|--------|-----------------|---------|
| Yahoo Finance (yfinance) | Stock prices, technicals | Weeks 1-4 |
| SEC EDGAR | Public company filings (10-K, 10-Q) | Week 2+ |
| StockAnalysis.com | Financial statements, screener, ratings | Reference |
| FRED | Macro indicators, interest rates | Optional |

Python libraries are installed automatically when you run `uv sync`
for each server. You don't need to install anything manually.

---

## Recommended External Resources

These free courses complement the material and go deeper on specific
topics. All are optional.

**Terminal basics (if you've never used a command line):**
- [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial/basics) — practical, covers only what you need

**MCP and tool-use (deeper dive after Week 1):**
- [Anthropic: Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) — free official course with certificate
- [DeepLearning.AI: MCP Build Rich-Context AI Apps](https://learn.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic/lesson/fkbhh/introduction) — free course by Andrew Ng's team + Anthropic
- [MCP Official Documentation](https://modelcontextprotocol.io) — protocol spec and quickstart guides

**Claude Code (before or alongside Week 2):**
- [Anthropic: Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — free official course with certificate
- [Claude Code Documentation](https://code.claude.com/docs/en/overview) — complete reference

**Claude Desktop + MCP setup (if you get stuck in Week 1):**
- [Claude Help Center: Getting Started with Local MCP Servers](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop) — official setup guide
- [MCP Docs: Connect to Local Servers](https://modelcontextprotocol.io/docs/develop/connect-local-servers) — step-by-step with screenshots

**Going further (after the course):**
- [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course/en/unit0/introduction) — free 4-unit course, more technical
- [Anthropic: MCP Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) — production patterns, transport mechanisms

---

## Troubleshooting

**"npm: command not found"**
Install Node.js from [nodejs.org](https://nodejs.org), then close and
reopen your terminal. (Only needed for Week 2.)

**"claude: command not found"**
Run `npm install -g @anthropic-ai/claude-code` again. If it still fails,
try `sudo npm install -g @anthropic-ai/claude-code` (Mac/Linux) or run
your terminal as Administrator (Windows).

**"uv: command not found"**
Close and reopen your terminal after installing uv. The installer adds
uv to your path, but the current terminal session doesn't pick it up.

**Claude Code asks for an API key**
Sign in when prompted. Claude Code uses your Anthropic account — the
same one you use for Claude Desktop.

**"git: command not found"**
Use the ZIP download option instead (see Step 4 above).
