# Week 1: Did It Work? Checklist

Use this checklist to check what Claude Code built for you. You don't
need to read the code — just test the tools and check the results.

---

## Server Basics

- [ ] **Server starts without errors.** When you run `uv run mcp dev server.py`,
  the MCP inspector opens without error messages in the terminal.

- [ ] **Each tool returns data.** Click each tool in the inspector, type
  in any required inputs (like a ticker symbol), and verify you get
  results back.

## Tool Quality

For each tool, check:

- [ ] **Real data, not fake data.** The prices should match what you
  see on a site like Google Finance or StockAnalysis.com. If Apple
  closed at $195 yesterday, the tool should show something close to that.

- [ ] **Numbers are already calculated.** Look at the tool results. Are
  percentages already calculated? Or does it return raw prices that
  someone would need to do math on? (Already calculated is correct.)

- [ ] **data_source field.** Every tool result should include a
  `data_source` field like `"yfinance"` so the AI knows where the
  data came from.

- [ ] **as_of field.** Every tool result should include a timestamp
  showing when the data was fetched.

- [ ] **Error handling.** Try calling a tool with a fake ticker like
  `"ZZZZZ"`. Does it return `{"error": "..."}` with a helpful message?
  Or does it crash? (Returning an error message is correct.)

## Guide Tool

- [ ] **Guide tool exists.** There should be a tool called
  `get_strategy_guide` (or similar) that describes all the other tools.

- [ ] **Guide explains when to use each tool.** Not just what each tool
  does, but when the AI should call it.

- [ ] **Guide suggests an order.** Something like: "1. Start with the
  watchlist summary. 2. Look at specific stocks. 3. Compare pairs."

## Claude Desktop Integration

- [ ] **Tools appear in Claude Desktop.** After adding the config and
  restarting, your tools should be visible (look for a hammer icon
  or tool indicator).

- [ ] **Claude uses your tools.** Ask Claude Desktop "How is Apple doing
  today?" — it should call your `get_stock_snapshot` tool, not answer
  from memory.

- [ ] **Answers include real data.** The prices in Claude's response
  should match what your tools returned, not made-up numbers.

---

## How to Fix Common Issues

**Tool returns old data:**
Tell Claude Code: "The data seems to be from last week. Can you make
sure yfinance is fetching the most recent available data?"

**Tool is missing something you want:**
Tell Claude Code: "Add a `pe_ratio` field to the stock snapshot. If
P/E isn't available for that stock, set it to null instead of crashing."

**Tool crashes instead of returning an error:**
Tell Claude Code: "When I enter a fake ticker, the tool crashes. Can
you make it return an error message instead?"

**Claude Desktop doesn't see the tools:**
Tell Claude Code: "My MCP server isn't showing up in Claude Desktop.
Here's my config file: [paste it]. Can you check what's wrong?"
