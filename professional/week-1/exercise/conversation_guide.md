# Week 1: Conversation Guide

How to talk to Claude Code to build your MCP server. These are examples —
adapt them to your own stocks and workflows.

---

## Starting the Conversation

**Good first message** (specific, structured):
```
I want to build an MCP server that tracks my stock watchlist. I follow:
AAPL, MSFT, NVDA, JPM, XOM.

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

Why the first is better: Claude Code builds exactly what you described. With
the vague version, Claude has to guess what you want and will probably build
something different from what you need.

---

## Iterating: Common Follow-Up Prompts

### Adding a new tool

```
Add a new tool called get_relative_strength that takes a ticker and returns
how it's performing relative to SPY over the last 1 week, 1 month, and
3 months. Pre-compute all the percentages.
```

### Fixing an error

```
When I call get_stock_snapshot("XOM"), I get this error:
[paste the error]
Can you fix it?
```

### Improving tool output

```
The watchlist summary is hard for the AI to interpret. Can you add a
"status" field to each stock that says "outperforming" if it's beating
SPY today and "underperforming" if it's not? The AI can then quickly
tell me which stocks are leading.
```

### Adding context fields

```
I want every tool to include a "stale_data_warning" field. Set it to null
if the data is from today. If the market is closed and the data is from
a previous trading day, set it to something like "Market closed. Data
is from 2026-03-15."
```

### Asking Claude to explain what it built

```
Can you explain what the get_stock_comparison tool does in plain English?
I want to understand what it returns without reading the code.
```

---

## Connecting to Claude Desktop

### Getting the config

```
How do I add this MCP server to Claude Desktop? My server is at
~/ai-finance-tools/server.py. Show me the exact config JSON and
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
I restarted Claude Desktop. How can I verify my MCP tools are available?
```

---

## Troubleshooting Prompts

### Python/package issues

```
I'm seeing "ModuleNotFoundError: No module named 'yfinance'" when I
run the server. Can you fix this?
```

### Data not loading

```
The get_stock_snapshot tool returns data for AAPL but returns an error
for BRK.B. I think the ticker format might be wrong. Can you handle
tickers with dots and special characters?
```

### Server won't start

```
When I run "uv run mcp dev server.py" I get this error:
[paste error]
What do I need to fix?
```

---

## Tips for Effective Communication with Claude Code

1. **Be specific about what you want.** "Add P/E ratio to the snapshot" is
   better than "make it better."

2. **Paste error messages.** Don't describe errors in your own words — paste
   the exact text. Claude Code reads error messages much better than
   paraphrased descriptions.

3. **One change at a time.** Ask for one thing, let Claude build it, test it,
   then ask for the next thing. This makes it easy to spot what went wrong
   if something breaks.

4. **Describe the *why*, not just the *what*.** "Add a notable field when
   daily change exceeds 3% so the AI can highlight unusual moves" is better
   than "add a notable field." The context helps Claude make better decisions.

5. **Ask Claude to test.** After any change, ask: "Can you run the MCP
   inspector so I can test this?" or "Can you call the get_stock_snapshot
   tool with AAPL and show me what it returns?"
