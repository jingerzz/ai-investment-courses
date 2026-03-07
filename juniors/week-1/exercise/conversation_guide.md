# Week 1: Conversation Guide

How to talk to Claude Code to build your stock tracker. These are
examples — change the stocks to ones you actually care about!

---

## Starting the Conversation

**Good first message** (specific, clear):
```
I want to build an MCP server that tracks stocks I'm interested in.
I follow: AAPL (Apple), NKE (Nike), DIS (Disney), TSLA (Tesla),
NFLX (Netflix).

Please build a FastMCP server with these tools:
1. get_stock_snapshot(ticker) - current price, daily change %, 52-week range
2. get_watchlist_summary() - all stocks sorted by daily performance
3. get_stock_comparison(ticker1, ticker2) - side-by-side comparison
4. get_strategy_guide() - describes all tools for the AI

Use yfinance for data. Return dicts, never raise exceptions. Include
data_source and as_of fields in every return.
```

**Weak first message** (too vague):
```
Build me a stock tracker.
```

Why the first one is better: Claude Code builds exactly what you
described. With the vague version, Claude has to guess what you want
and will probably build something different.

---

## Iterating: Common Follow-Up Prompts

### Adding a new tool

```
Add a new tool called get_price_history that takes a ticker and shows
me the stock price from 1 week ago, 1 month ago, and 3 months ago,
plus the percentage change for each period. Calculate all the
percentages in the code.
```

### Fixing an error

```
When I call get_stock_snapshot("DIS"), I get this error:
[paste the error]
Can you fix it?
```

### Making the output more useful

```
The watchlist summary is a big wall of numbers. Can you add a "status"
field to each stock that says "hot" if it's up more than 1% today,
"cold" if it's down more than 1%, and "steady" if it's in between?
That way the AI can quickly tell me what's moving.
```

### Adding extra info

```
I want every tool to include a "market_status" field. If the stock
market is currently open, set it to "Market is open - prices are live."
If the market is closed, set it to "Market closed - showing last
closing prices."
```

### Asking Claude to explain what it built

```
Can you explain what the get_stock_comparison tool does in plain
English? I want to understand what it returns without reading the code.
```

---

## Connecting to Claude Desktop

### Getting the config

```
How do I add this MCP server to Claude Desktop? My server is at
~/ai-stock-tools/server.py. Show me the exact config JSON and
tell me where to put it.
```

### If it doesn't work

```
I added the MCP server to Claude Desktop but it's not showing up.
Here's my config file:
[paste the config]
What's wrong?
```

### Testing the connection

```
I restarted Claude Desktop. How can I verify my tools are available?
```

---

## Troubleshooting Prompts

### Package issues

```
I'm seeing "ModuleNotFoundError: No module named 'yfinance'" when I
run the server. Can you fix this?
```

### Data not loading

```
The get_stock_snapshot tool works for AAPL but returns an error for
BRK.B. I think the ticker format might be wrong. Can you handle
tickers with dots and special characters?
```

### Server won't start

```
When I run "uv run mcp dev server.py" I get this error:
[paste error]
What do I need to fix?
```

---

## Tips for Talking to Claude Code

1. **Be specific.** "Add the P/E ratio to the snapshot" is better than
   "make it show more info."

2. **Paste error messages.** Don't try to describe errors in your own
   words — paste the exact text. Claude Code reads error messages better
   than human descriptions.

3. **One change at a time.** Ask for one thing, let Claude build it,
   test it, then ask for the next thing. This makes it easy to figure
   out what went wrong if something breaks.

4. **Explain why, not just what.** "Add a 'notable' field when the daily
   change is more than 3% so the AI can highlight unusual moves" is
   better than "add a notable field." The reason helps Claude make
   better choices.

5. **Ask Claude to test.** After any change, say: "Can you run the MCP
   inspector so I can test this?" or "Can you call get_stock_snapshot
   with AAPL and show me what it returns?"
