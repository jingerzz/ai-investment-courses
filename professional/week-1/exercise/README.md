# Week 1 Exercise: Install and Explore the SPY/TLT Strategy Server

## What You'll Do

You'll install a pre-built MCP server that connects Claude Desktop to a
real trading strategy with live market data. When you're done, you'll be
able to open Claude Desktop and have conversations like:

- "What's today's signal?"
- "Give me a trade briefing"
- "What happened the last time we saw three Blue days in a row?"
- "How has this strategy performed since 2002?"

...and Claude will answer using real data computed by real tools — not
from its training data.

## Time: 30 minutes

## What You Need

- A Mac or PC with at least 8GB RAM
- Claude Desktop installed ([claude.ai/download](https://claude.ai/download))
- A terminal application (Terminal on Mac, PowerShell on Windows)

---

## Step 1: Install the Package Manager (3 min)

We use `uv` — a fast Python package manager. You don't need to know
Python; `uv` just handles the installation plumbing.

**Mac (paste into Terminal):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (paste into PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen your terminal after installing. Verify it works:
```bash
uv --version
```

You should see a version number like `uv 0.7.x`. If you get "command
not found", try opening a new terminal window.

## Step 2: Download the Course Server (3 min)

The SPY/TLT Course Edition server is included in your course materials.
Navigate to it:

```bash
cd ~/ai-investment-courses/professional/servers/spy-tlt-course
```

Install the server and its dependencies:

```bash
uv sync
```

This downloads Python (if needed) and installs four packages: `mcp`,
`numpy`, `yfinance`, and `pandas`. Takes about 30 seconds.

Verify the server works:
```bash
uv run spy-tlt-server &
```

You should see the server start without errors. Press `Ctrl+C` to stop
it (or close the terminal).

## Step 3: Connect to Claude Desktop (5 min)

Now tell Claude Desktop where to find your server.

**Open your Claude Desktop config file:**

The easiest way: in Claude Desktop, go to **Settings > Developer >
Edit Config**. This opens the config file in your default text editor.

If that option isn't available, find the file manually:
- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

If the file doesn't exist, create it. If it already exists and has
content, you'll add to the existing `mcpServers` section.

**Before you edit, verify your path.** In your terminal, run:

Mac:
```bash
ls ~/ai-investment-courses/professional/servers/spy-tlt-course/
```

Windows:
```
dir %USERPROFILE%\ai-investment-courses\professional\servers\spy-tlt-course\
```

You should see `pyproject.toml` and a `data/` folder. If you see
"No such file or directory," your course files are in a different
location — find the correct path before proceeding.

**Add this to the config file** (replace `YOUR_USERNAME` with your
actual username):

Mac example:
```json
{
  "mcpServers": {
    "spy-tlt-course": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/YOUR_USERNAME/ai-investment-courses/professional/servers/spy-tlt-course",
        "run",
        "spy-tlt-server"
      ]
    }
  }
}
```

Windows example:
```json
{
  "mcpServers": {
    "spy-tlt-course": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\YOUR_USERNAME\\ai-investment-courses\\professional\\servers\\spy-tlt-course",
        "run",
        "spy-tlt-server"
      ]
    }
  }
}
```

**Restart Claude Desktop** completely (quit and reopen, not just close
the window). When you start a new conversation, you should see the
SPY/TLT tools available — look for a hammer icon (🔨) at the bottom
of the chat input area. Click it to see the list of available tools.

**If you don't see tools after restarting,** the most common cause is a
wrong path. Double-check that the `--directory` path matches the output
from the `ls` command above.

## Step 4: Your First Conversation (5 min)

Open a new conversation in Claude Desktop and try these prompts. After
each one, observe what happens — which tools Claude calls, what data
comes back, how Claude presents it.

**Start with orientation:**
```
What tools do you have available from the SPY/TLT strategy server?
```

Claude should call `get_strategy_guide()` and explain the 14 available
tools.

**Get today's signal:**
```
Refresh the data, then tell me what today's signal is.
```

Watch Claude call `refresh_data()` first (pulling the latest from Yahoo
Finance), then `get_current_signal()`. It will report the color, any
active signal, and the recommended exposure.

**Ask for a briefing:**
```
Give me a complete trade briefing.
```

Claude calls `get_trade_briefing()` and presents a pre-formatted
markdown section with pivot levels, support/resistance, and a trade
plan. Notice: every number was computed by Python. Claude is presenting
it, not calculating it.

## Step 5: Explore the Design Principles (7 min)

Now look for the four design principles from the reading. Each prompt
below highlights a specific principle.

**Principle 1 — Pre-computed results:**
```
What are today's key SPY levels?
```

Claude calls `get_trading_levels()`. Look at the response: pivot points,
R1-R3, S1-S3, SMAs, ATR — all pre-computed. The AI didn't calculate
any of this. It received finished numbers and explained what they mean.

**Principle 2 — Context metadata:**
```
What's the current signal? (Don't refresh the data first.)
```

If the data is stale (you haven't refreshed recently, or the market is
closed), look for the `stale_data_warning` field. Claude should mention
it: "Note: this data is from [date] and may not reflect current prices."

**Principle 3 — One tool per question:**
```
How has the strategy performed since 2020?
```

Claude calls `get_backtest_summary(start_date="2020-01-01")` — just
one focused tool for this specific question. It doesn't need to load
signal history or trading levels.

**Principle 4 — The guide tool:**
```
What's the recommended workflow for a morning briefing?
```

Claude calls `get_strategy_guide(topic="workflow")` and returns the
exact sequence: refresh → briefing → present verbatim.

## Step 6: Try Real Analysis (7 min)

Now use the tools for actual investment analysis. These prompts go
beyond single tool calls — they show how the AI synthesizes across
multiple data sources.

**Pattern analysis:**
```
Have we seen a Blue-Red-Blue pattern recently? What usually happens
after that sequence?
```

Claude calls `analyze_pattern(sequence="Blue,Red,Blue")` and reports:
how many times this pattern occurred historically, what percentage of
the time the market was up the next day, and the average forward return.

**Signal education:**
```
Explain the T1_BOTH_STRONG_BLUE signal. When does it fire, why is
it Tier 1, and what are the risks?
```

Claude calls `explain_signal("T1_BOTH_STRONG_BLUE")` and returns a
detailed explanation including the trigger conditions, the sizing
rationale, the statistical framing, and the risk factors.

**Historical context:**
```
Show me SPY's streak patterns. What typically happens after 4+
consecutive down days?
```

Claude calls `spy_streaks()` and walks you through winning/losing
streak data, including "what happens next" analysis.

**Cross-referencing:**
```
Given today's signal and the current technical levels, what's the
risk/reward on this setup? Walk me through the logic.
```

This is where the AI adds real value. It pulls together the signal
(from `get_current_signal`), the levels (from `get_trading_levels`),
and the trade plan — then explains how they connect.

---

## What You Learned

- How to install an MCP server and connect it to Claude Desktop
- How Claude discovers and calls tools automatically based on your questions
- How pre-computed results prevent the AI from making math errors
- How stale data warnings help the AI qualify its statements
- How the guide tool orients Claude in a new session
- How Claude synthesizes across multiple tools for cross-referenced analysis

## If You Get Stuck

**"uv: command not found"** — Close your terminal and open a new one.
The installer added `uv` to your PATH, but the current terminal doesn't
see it yet.

**"Tools don't appear in Claude Desktop"** — Make sure you restarted
Claude Desktop completely (quit the app, not just close the window).
Check that the path in `claude_desktop_config.json` points to the
correct directory.

**"Tool call failed"** — The most common cause is a wrong path in the
config file. Double-check that the `--directory` path matches where you
actually installed the course materials.

**"Data is stale"** — Ask Claude to `refresh_data()`. This fetches the
latest prices from Yahoo Finance.

## Next Week

In Week 2, you'll use Claude Code to **build your own** MCP server —
a watchlist tracker with a morning briefing and guardrails. You'll also
set up a private document Q&A system for SEC filings. The SPY/TLT
server you installed today serves as your reference implementation:
when you're evaluating what Claude Code built, you can compare it to
what you've experienced here.
