# Week 1 Exercise: Build Your First Stock Tracker with Claude Code

## What You'll Build

A tool that gives Claude Desktop access to real stock market data for
companies you care about. When you're done, you'll be able to open
Claude Desktop and ask things like:

- "How is Apple doing today?"
- "Compare Tesla and Netflix — which one is doing better?"
- "Show me a summary of all my stocks"

...and Claude will answer using real, current data — not guesses from
its training.

## Time: 30 minutes

## What You Need

- Claude Code installed and working (see `setup.md`)
- Claude Desktop installed
- No subscriptions needed --- all data is free

---

## Recommended: Let Claude Code Handle Setup

If you have Claude Code installed, you can paste one prompt and let it
do everything for you. Open your terminal, start Claude Code, and paste:

```
Help me set up a stock tracker project. Here's what I need:
1. Create a folder at ~/ai-stock-tools (skip if it exists)
2. Install uv (https://astral.sh/uv/) if I don't have it
3. Initialize a new uv project in that folder with fastmcp and
   yfinance as dependencies (run uv init, then uv add fastmcp yfinance)
4. Create a starter server.py file with a FastMCP server called
   "stock-tracker" that has one placeholder tool called get_strategy_guide
   that returns a description of the server
5. Add this server to my Claude Desktop MCP config
   (claude_desktop_config.json) so it runs via uv
6. Verify everything works, then tell me to restart Claude Desktop
```

When Claude Code finishes, restart Claude Desktop and skip to
**Step 2: Describe What You Want**.

**If you prefer to set things up manually**, continue with Step 1 below.

---

## Step 1: Start Claude Code in Your Project Folder (2 min)

Open your terminal and type:

```bash
cd ~/ai-stock-tools
claude
```

You're now talking to Claude Code. Everything from here is a conversation.

## Step 2: Describe What You Want (5 min)

Tell Claude Code what to build. Here's an example — **change the
stocks to ones you actually want to follow:**

```
I want to build an MCP server that tracks stocks I'm interested in.
I want to follow these companies: AAPL (Apple), NKE (Nike),
DIS (Disney), TSLA (Tesla), NFLX (Netflix)

Please build a FastMCP server in Python that has these tools:

1. get_stock_snapshot - For a given ticker, return current price, daily
   change, 52-week range, volume, and market cap. Pre-compute the daily
   change percentage so the AI doesn't have to calculate it.

2. get_watchlist_summary - Return a summary of all my stocks with
   current prices and daily changes, sorted from best to worst performer.

3. get_stock_comparison - Compare two tickers side by side: price,
   YTD return, P/E ratio, market cap.

4. get_strategy_guide - A tool that describes all the other tools and
   tells the AI when to use each one.

Use yfinance for data (it's free, no API key needed). Every tool should
return a dict with a "data_source" field and an "as_of" timestamp. If
something goes wrong, return {"error": "description"} instead of crashing.

Put the server in a file called server.py.
```

Claude Code will:
- Create a `server.py` file
- Install the necessary packages (yfinance, mcp, etc.)
- Write all the tool code for you

**Don't worry about understanding the code.** Focus on whether Claude
understood what you asked for.

## Step 3: Test Your Tools (5 min)

Ask Claude Code to start the testing tool:

```
Can you run the MCP inspector so I can test my server?
Run: uv run mcp dev server.py
```

Claude Code will start the MCP inspector — a web page where you can
try each tool and see what it returns. Check:

- Does `get_stock_snapshot("AAPL")` return real data?
- Does `get_watchlist_summary()` show all your stocks?
- Does `get_stock_comparison("AAPL", "TSLA")` compare them correctly?
- Are all the numbers already calculated (not raw data)?

Press `Ctrl + C` in the terminal to stop the inspector when done.

## Step 4: Make It Better (8 min)

The first version probably isn't perfect. Here are common improvements.
Tell Claude Code what to change:

**If data is missing:**
```
The get_stock_snapshot tool doesn't include the P/E ratio. Can you add
that? Also add the dividend yield if available.
```

**If you want the AI to highlight big moves:**
```
When a stock is up or down more than 3% for the day, add a field called
"notable" with a message like "Big move today! Up 4.2%". This helps the
AI point out the interesting stuff without me asking.
```

**If you want a new tool:**
```
Add a tool called get_sector_info that tells me what industry each of
my stocks is in and groups them by sector.
```

**If something broke:**
```
The get_stock_comparison tool is crashing with an error. Here's what I see:
[paste the error message]
Can you fix it?
```

## Step 5: Connect to Claude Desktop (5 min)

Now connect your tools to Claude Desktop so you can use them in normal
conversations.

Ask Claude Code:

```
How do I add this MCP server to Claude Desktop? My server file is at
~/ai-stock-tools/server.py. Give me the exact JSON to add to
claude_desktop_config.json and tell me where that file is.
```

Claude Code will give you:
1. The path to your Claude Desktop config file
2. The JSON to add
3. Instructions to restart Claude Desktop

After restarting Claude Desktop, your tools will be available. You may
see a hammer icon or tool indicator when you start a new conversation.

## Step 6: Use It! (5 min)

Open Claude Desktop and try these:

- "How are my stocks doing today?"
- "Which of my stocks has the best momentum right now?"
- "Compare Apple and Tesla for me — which looks stronger?"
- "Give me a quick summary of my watchlist"

Claude Desktop will call your tools to get real data, then give you a
natural language answer.

**This is the cool part:** You described what you wanted in English,
Claude Code built the tools, and now Claude Desktop uses them to give
you answers based on real data. No coding required.

---

## What You Learned

- How to describe a tool to Claude Code so it builds what you need
- How to test your tools using the MCP inspector
- How to improve things when the first version isn't perfect
- How to connect your tools to Claude Desktop
- That Claude Desktop uses YOUR tools (real data) instead of guessing

## If You Get Stuck

Tell Claude Code what's happening:

```
I'm getting an error when I try to run the server. Here's what I see:
[paste the error message]
Can you fix it?
```

Claude Code is very good at fixing its own code. Describe the problem
and let it handle it.

## Next Week

In Week 2, you'll add more tools and build a daily stock report — plus
you'll add safety checks that keep the AI from making mistakes.
