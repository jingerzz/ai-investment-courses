# Week 1: Evaluation Checklist

Use this checklist to evaluate what Claude Code built for you. You don't need
to read the Python code — just test the tools and check the outputs.

---

## Server Basics

- [ ] **Server runs without errors.** When you run `uv run mcp dev server.py`,
  the MCP inspector opens without any error messages in the terminal.

- [ ] **Each tool returns data.** Click each tool in the inspector, provide
  any required inputs (like a ticker symbol), and verify you get results back.

## Tool Quality

For each tool, check:

- [ ] **Real data, not fake data.** The prices and numbers should match what
  you see on a site like StockAnalysis.com or Google Finance. If AAPL closed
  at $195 yesterday, the tool should show something close to that.

- [ ] **Pre-computed values.** Look at the tool returns. Are percentages,
  P&L, and changes already calculated? Or does it return raw prices that the
  AI would need to do math on? (Pre-computed is correct.)

- [ ] **data_source field.** Every tool return should include a `data_source`
  field like `"yfinance"` so the AI knows where the data came from.

- [ ] **as_of field.** Every tool return should include a timestamp showing
  when the data was fetched.

- [ ] **Error handling.** Try calling a tool with a nonsense ticker like
  `"ZZZZZ"`. Does it return `{"error": "..."}` with a helpful message? Or
  does it crash? (Returning an error dict is correct.)

## Guide Tool

- [ ] **Guide tool exists.** There should be a tool called `get_strategy_guide`
  (or similar) that describes all the other tools.

- [ ] **Guide describes when to use each tool.** Not just what each tool does,
  but when the AI should call it. For example: "Call get_stock_snapshot first
  to understand a single stock, then use get_stock_comparison to compare two."

- [ ] **Guide suggests a recommended flow.** A numbered sequence like:
  "1. Start with watchlist summary. 2. Drill into specific stocks.
  3. Compare top performers."

## Claude Desktop Integration

- [ ] **Server appears in Claude Desktop.** After adding the config and
  restarting, your MCP tools should be visible (look for a hammer icon
  or tool indicator).

- [ ] **Claude uses your tools.** Ask Claude Desktop "How is AAPL doing today?"
  — it should call your `get_stock_snapshot` tool, not answer from memory.

- [ ] **Answers include real data.** The prices and changes in Claude's
  response should match what your tools returned, not made-up numbers.

---

## How to Fix Common Issues

**Tool returns stale data:**
Tell Claude Code: "The data seems to be from last week. Can you make sure
yfinance is fetching the most recent available data?"

**Tool is missing a field you want:**
Tell Claude Code: "Add a `pe_ratio` field to the stock snapshot. If P/E
isn't available for that stock, set it to null instead of crashing."

**Tool crashes instead of returning an error:**
Tell Claude Code: "When I pass an invalid ticker, the tool crashes. Wrap
it in a try/except and return an error dict instead."

**Claude Desktop doesn't see the tools:**
Tell Claude Code: "My MCP server isn't showing up in Claude Desktop. Here's
my config file: [paste it]. Can you check what's wrong?"
