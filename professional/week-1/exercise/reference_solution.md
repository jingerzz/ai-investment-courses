# Week 1: Reference Solution — Portfolio Watchlist MCP Server

This is what a good result looks like. Compare what Claude Code built for you
against this reference. You don't need to understand every line of Python —
focus on the **structure** and **what each tool returns**.

---

## What the Server Does

This server gives Claude Desktop access to real-time stock data for a
5-stock watchlist. It has 4 tools:

| Tool | What It Does |
|------|-------------|
| `get_stock_snapshot` | Detailed view of one stock |
| `get_watchlist_summary` | Quick overview of all stocks |
| `get_stock_comparison` | Side-by-side comparison of two stocks |
| `get_strategy_guide` | Tells the AI how to use the other tools |

---

## Tool 1: `get_stock_snapshot(ticker)`

**When to use:** When you want to know about a specific stock.

**What it returns:**

```json
{
  "ticker": "AAPL",
  "company_name": "Apple Inc.",
  "current_price": 195.20,
  "previous_close": 193.55,
  "daily_change": 1.65,
  "daily_change_pct": 0.85,
  "fifty_two_week_high": 199.62,
  "fifty_two_week_low": 164.08,
  "volume": 54230100,
  "avg_volume_10d": 48500000,
  "market_cap": 2980000000000,
  "pe_ratio": 30.5,
  "dividend_yield_pct": 0.55,
  "notable": null,
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**Key design decisions:**

- **`daily_change_pct` is pre-computed.** The AI never needs to calculate
  `(195.20 - 193.55) / 193.55 * 100`. Python did it already. This prevents
  the AI from making math errors.

- **`notable` flags unusual activity.** If daily change > 3% or volume >
  2x average, this field contains a description like "Significant daily
  gain (+4.2%)" or "Unusual volume (2.8x average)". Otherwise it's null.
  This helps the AI highlight what matters without analyzing raw numbers.

- **Error case:** If you pass an invalid ticker, the tool returns:
  ```json
  {"error": "Could not find data for ticker 'ZZZZZ'. Check the symbol and try again."}
  ```
  It does NOT crash. The AI sees the error message and can tell you what
  went wrong.

---

## Tool 2: `get_watchlist_summary()`

**When to use:** Morning overview — "How are my stocks doing?"

**What it returns:**

```json
{
  "watchlist": [
    {
      "ticker": "NVDA",
      "current_price": 868.30,
      "daily_change_pct": 2.15,
      "status": "outperforming"
    },
    {
      "ticker": "AAPL",
      "current_price": 195.20,
      "daily_change_pct": 0.85,
      "status": "outperforming"
    },
    {
      "ticker": "JPM",
      "current_price": 186.40,
      "daily_change_pct": 0.32,
      "status": "underperforming"
    },
    {
      "ticker": "MSFT",
      "current_price": 415.60,
      "daily_change_pct": -0.42,
      "status": "underperforming"
    },
    {
      "ticker": "XOM",
      "current_price": 103.20,
      "daily_change_pct": -1.53,
      "status": "underperforming"
    }
  ],
  "best_performer": "NVDA",
  "worst_performer": "XOM",
  "watchlist_count": 5,
  "up_count": 2,
  "down_count": 3,
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**Key design decisions:**

- **Pre-sorted by performance.** The AI doesn't need to sort — it's already
  ordered from best to worst daily return.

- **`status` field compares to SPY.** "outperforming" means the stock is
  beating SPY today; "underperforming" means it's lagging. This gives the
  AI context without requiring it to fetch SPY separately.

- **`best_performer` and `worst_performer` are pre-identified.** The AI can
  immediately say "NVDA is your best performer today" without scanning the list.

---

## Tool 3: `get_stock_comparison(ticker1, ticker2)`

**When to use:** "Compare AAPL and MSFT" or "Which is better, JPM or XOM?"

**What it returns:**

```json
{
  "comparison": {
    "ticker1": {
      "ticker": "AAPL",
      "current_price": 195.20,
      "daily_change_pct": 0.85,
      "ytd_return_pct": 12.3,
      "pe_ratio": 30.5,
      "market_cap_billions": 2980.0,
      "dividend_yield_pct": 0.55
    },
    "ticker2": {
      "ticker": "MSFT",
      "current_price": 415.60,
      "daily_change_pct": -0.42,
      "ytd_return_pct": 8.7,
      "pe_ratio": 35.2,
      "market_cap_billions": 3090.0,
      "dividend_yield_pct": 0.72
    }
  },
  "edge": {
    "daily_leader": "AAPL",
    "ytd_leader": "AAPL",
    "lower_pe": "AAPL",
    "higher_dividend": "MSFT"
  },
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**Key design decisions:**

- **`edge` section pre-determines winners.** Instead of making the AI
  compare numbers, Python already identified which stock leads on each
  metric. The AI just narrates the result.

- **Consistent units.** Market cap is in billions (not raw numbers like
  2980000000000). Percentages are actual percentages (12.3, not 0.123).
  This makes the AI's output more natural.

---

## Tool 4: `get_strategy_guide()`

**When to use:** The AI should call this first in any new conversation to
understand what's available.

**What it returns:**

```json
{
  "overview": "Stock watchlist server with real-time data for AAPL, MSFT, NVDA, JPM, XOM. Uses Yahoo Finance for market data.",
  "tools": {
    "get_stock_snapshot": "Get detailed data for one stock. Use when the user asks about a specific ticker.",
    "get_watchlist_summary": "Get overview of all watchlist stocks. Use for morning review or 'how are my stocks doing?' questions.",
    "get_stock_comparison": "Compare two stocks side by side. Use when the user asks which stock is better or wants a comparison.",
    "get_strategy_guide": "This tool. Describes what's available."
  },
  "recommended_flow": [
    "1. Start with get_watchlist_summary() for the overall picture",
    "2. Use get_stock_snapshot(ticker) to drill into interesting stocks",
    "3. Use get_stock_comparison(ticker1, ticker2) to compare specific pairs"
  ],
  "data_notes": "Data is from Yahoo Finance (free, real-time during market hours, 15-min delay after hours). All percentages and changes are pre-computed."
}
```

**Why this tool matters:**

Without a guide tool, the AI has to read the tool definitions to figure out
what's available. With a guide tool, the AI calls it first and immediately
knows the recommended flow. This is like giving a new analyst a cheat sheet
for your desk's systems.

---

## How Claude Desktop Uses These Tools

When you ask Claude Desktop "How are my stocks doing today?", here's what
happens behind the scenes:

1. Claude sees your question and checks what tools are available
2. Claude calls `get_watchlist_summary()` — this seems like the right tool
3. Your server runs, fetches real data from Yahoo Finance, and returns the
   pre-computed summary
4. Claude reads the structured result and writes a natural language response:

> "Your watchlist is mixed today — 2 stocks up, 3 down. NVDA is your best
> performer at +2.15%, while XOM is lagging at -1.53%. NVDA and AAPL are
> both outperforming the broader market."

Notice: Claude didn't make up any numbers. Every figure came from your tool.
The AI's value is in the *interpretation* — connecting the data points into
a narrative.
