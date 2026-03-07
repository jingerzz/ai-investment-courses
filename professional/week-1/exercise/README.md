# Week 1 Exercise: Build Your First MCP Server with Claude Code

## What You'll Build

An MCP server that gives Claude Desktop access to real stock market data for
your personal watchlist. When you're done, you'll be able to open Claude Desktop
and ask things like:

- "How has AAPL performed this month?"
- "Compare NVDA and MSFT — which has better momentum?"
- "Show me a summary of my watchlist"

...and Claude will answer using live data from your tools, not from its
training data.

## Time: 30 minutes

## What You Need

- Claude Code installed and working (see `setup.md`)
- Claude Desktop installed
- No data subscriptions needed — we use free sources

---

## Step 1: Start Claude Code in Your Project Folder (2 min)

Open your terminal and type:

```bash
cd ~/ai-finance-tools
claude
```

You're now talking to Claude Code. Everything from here is a conversation.

## Step 2: Describe What You Want (5 min)

Tell Claude Code what to build. Here's an example — **modify it to match
your actual workflow and the stocks you follow:**

```
I want to build an MCP server that helps me track a watchlist of stocks.
I follow these tickers: AAPL, MSFT, NVDA, JPM, XOM

Please build a FastMCP server in Python that has these tools:

1. get_stock_snapshot - For a given ticker, return current price, daily change,
   52-week range, volume, and market cap. Pre-compute the daily change
   percentage so the AI doesn't have to calculate it.

2. get_watchlist_summary - Return a summary of all my watchlist stocks with
   current prices and daily changes, sorted by daily performance.

3. get_stock_comparison - Compare two tickers side by side: price, YTD return,
   P/E ratio, market cap.

4. get_strategy_guide - A tool that describes all the other tools and tells
   the AI when to use each one.

Use yfinance for data (it's free, no API key needed). Every tool should return
a dict with a "data_source" field and an "as_of" timestamp. If something goes
wrong, return {"error": "description"} instead of crashing.

Put the server in a file called server.py.
```

Claude Code will:
- Create a `server.py` file
- Install the necessary Python packages (yfinance, mcp, etc.)
- Write all the tool code for you

**Don't worry about understanding the Python code.** Focus on whether Claude
understood your intent.

## Step 3: Test Your Server (5 min)

Ask Claude Code to test it:

```
Can you run the MCP inspector so I can test my server?
Run: uv run mcp dev server.py
```

Claude Code will start the MCP inspector — a web interface where you can
call each tool and see what it returns. Check:

- Does `get_stock_snapshot("AAPL")` return real data?
- Does `get_watchlist_summary()` show all your stocks?
- Does `get_stock_comparison("AAPL", "MSFT")` compare them correctly?
- Are all the numbers pre-computed (not raw data the AI would need to calculate)?

Press `Ctrl + C` in the terminal to stop the inspector when done.

## Step 4: Iterate and Improve (8 min)

The first version won't be perfect. Here are common things to fix. Tell Claude
Code what to change:

**If data is missing or wrong:**
```
The get_stock_snapshot tool doesn't include the P/E ratio. Can you add that?
Also add the dividend yield if available.
```

**If you want better context for the AI:**
```
When a stock is down more than 3% for the day, add a field called "notable"
with the value "significant daily decline". Same for up more than 3%.
Do the same if volume is more than 2x the average.
```

**If you want a new tool:**
```
Add a tool called get_sector_performance that groups my watchlist stocks by
sector and shows which sectors are up and down today.
```

**If something broke:**
```
The get_stock_comparison tool is crashing with an error about "NoneType".
Can you fix it? It should return an error dict instead of crashing.
```

## Step 5: Connect to Claude Desktop (5 min)

Now connect your server to Claude Desktop so you can use it in normal
conversations.

Ask Claude Code:

```
How do I add this MCP server to Claude Desktop? My server file is at
~/ai-finance-tools/server.py. Give me the exact JSON to add to
claude_desktop_config.json and tell me where that file is.
```

Claude Code will give you:
1. The path to your Claude Desktop config file
2. The JSON to add
3. Instructions to restart Claude Desktop

After restarting Claude Desktop, you'll see your tools available. You may see
a hammer icon or the tools listed when you start a new conversation.

## Step 6: Use It (5 min)

Open Claude Desktop and try these conversations:

- "How are my watchlist stocks doing today?"
- "Which of my stocks has the best momentum right now?"
- "Compare JPM and XOM for me — which looks stronger?"
- "Give me a quick morning summary of my portfolio"

Claude Desktop will call your MCP tools to get real data, then reason over
the results to give you a natural language answer.

**This is the payoff:** You described a workflow in English, Claude Code built
the tools, and now Claude Desktop uses them to give you data-driven answers.

---

## What You Learned

- How to describe a tool to Claude Code so it builds what you need
- How to test an MCP server using the inspector
- How to iterate when the first version isn't right
- How to connect your tools to Claude Desktop
- That Claude Desktop uses YOUR tools (real data) instead of guessing

## If You Get Stuck

Tell Claude Code what's happening:

```
I'm getting an error when I try to run the server. Here's what I see:
[paste the error message]
Can you fix it?
```

Claude Code is very good at debugging its own code. Describe the problem
and let it fix it.

## Next Week

In Week 2, you'll add more tools to this server and build a morning briefing
that cross-references multiple data points — with guardrails to prevent the
AI from getting things wrong.
