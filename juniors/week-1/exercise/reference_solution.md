# Week 1: Reference Solution — Stock Tracker

This is what a good result looks like. Compare what Claude Code built
for you against this reference. You don't need to understand the code —
focus on **what each tool returns** and **why it's designed that way**.

---

## What the Server Does

This server gives Claude Desktop access to real stock data for companies
you're tracking. It has 4 tools:

| Tool | What It Does |
|------|-------------|
| `get_stock_snapshot` | Detailed view of one stock |
| `get_watchlist_summary` | Quick overview of all stocks |
| `get_stock_comparison` | Side-by-side comparison of two stocks |
| `get_strategy_guide` | Menu of all tools for the AI |

---

## Tool 1: `get_stock_snapshot(ticker)`

**When to use:** When you want to know about one specific stock.

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

**What's smart about this design:**

- **`daily_change_pct` is already calculated.** The code did the math
  `(195.20 - 193.55) / 193.55 * 100 = 0.85%`. The AI just reports the
  number. If the AI had to do this math itself, it might get it wrong.

- **`notable` flags big moves.** If a stock is up or down more than 3%,
  or if trading volume is much higher than normal, this field says
  something like "Big move today! Up 4.2%". Otherwise it's null (empty).
  This helps the AI highlight what matters.

- **Error case:** If you type a fake ticker like "ZZZZZ", the tool returns:
  ```json
  {"error": "Could not find data for ticker 'ZZZZZ'. Check the symbol and try again."}
  ```
  It doesn't crash. The AI sees the error message and explains what
  went wrong.

---

## Tool 2: `get_watchlist_summary()`

**When to use:** "How are my stocks doing?" — the morning overview.

**What it returns:**

```json
{
  "watchlist": [
    {
      "ticker": "TSLA",
      "current_price": 178.50,
      "daily_change_pct": 3.21,
      "status": "hot"
    },
    {
      "ticker": "AAPL",
      "current_price": 195.20,
      "daily_change_pct": 0.85,
      "status": "steady"
    },
    {
      "ticker": "NKE",
      "current_price": 97.80,
      "daily_change_pct": 0.12,
      "status": "steady"
    },
    {
      "ticker": "NFLX",
      "current_price": 628.40,
      "daily_change_pct": -0.35,
      "status": "steady"
    },
    {
      "ticker": "DIS",
      "current_price": 112.60,
      "daily_change_pct": -1.82,
      "status": "cold"
    }
  ],
  "best_performer": "TSLA",
  "worst_performer": "DIS",
  "watchlist_count": 5,
  "up_count": 2,
  "down_count": 3,
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**What's smart about this design:**

- **Already sorted.** Best performer is at the top, worst at the bottom.
  The AI doesn't need to sort — it's already done.

- **`status` field makes it easy.** "hot" means up more than 1%, "cold"
  means down more than 1%, "steady" means in between. The AI can
  immediately say "Tesla is hot today" without analyzing numbers.

- **`best_performer` and `worst_performer` are pre-identified.** The AI
  can immediately say "Tesla is your best performer" without scanning
  the whole list.

---

## Tool 3: `get_stock_comparison(ticker1, ticker2)`

**When to use:** "Compare Apple and Tesla" or "Which is better?"

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
      "ticker": "TSLA",
      "current_price": 178.50,
      "daily_change_pct": 3.21,
      "ytd_return_pct": -8.4,
      "pe_ratio": 62.1,
      "market_cap_billions": 568.0,
      "dividend_yield_pct": 0.0
    }
  },
  "edge": {
    "daily_leader": "TSLA",
    "ytd_leader": "AAPL",
    "lower_pe": "AAPL",
    "higher_dividend": "AAPL",
    "larger_company": "AAPL"
  },
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**What's smart about this design:**

- **`edge` section shows who's winning.** Instead of making the AI
  compare numbers, the code already figured out which stock leads on
  each metric. The AI just explains the result.

- **Friendly units.** Market cap is in billions (2980.0) not raw numbers
  (2,980,000,000,000). Percentages are actual percentages (12.3, not
  0.123). This makes the AI's answers more natural.

- **YTD return** (Year-to-Date return) shows how much the stock has
  gone up or down since January 1st. This gives longer-term context
  beyond just today's movement.

---

## Tool 4: `get_strategy_guide()`

**When to use:** The AI calls this first in any new conversation.

**What it returns:**

```json
{
  "overview": "Stock watchlist tracker for AAPL, NKE, DIS, TSLA, NFLX. Uses Yahoo Finance for real-time market data.",
  "tools": {
    "get_stock_snapshot": "Get detailed data for one stock. Use when someone asks about a specific company.",
    "get_watchlist_summary": "Get overview of all tracked stocks. Use for 'how are my stocks doing?' questions.",
    "get_stock_comparison": "Compare two stocks side by side. Use when someone asks which stock is better or wants a comparison.",
    "get_strategy_guide": "This tool. Describes what's available."
  },
  "recommended_flow": [
    "1. Start with get_watchlist_summary() for the big picture",
    "2. Use get_stock_snapshot(ticker) to look at one specific stock",
    "3. Use get_stock_comparison(ticker1, ticker2) to compare two stocks"
  ],
  "data_notes": "Data is from Yahoo Finance (free, real-time during market hours). All percentages and changes are pre-computed — do not recalculate them."
}
```

**Why this tool matters:**

Without a guide tool, the AI has to guess what your tools do and when
to use them. With a guide tool, the AI calls it first and immediately
knows the plan. It's like giving someone a menu before they order food.

---

## How Claude Desktop Uses These Tools

When you ask Claude Desktop "How are my stocks doing today?", here's
what happens behind the scenes:

1. Claude sees your question and checks what tools are available
2. Claude calls `get_watchlist_summary()` — this seems like the right tool
3. Your server runs, fetches real data from Yahoo Finance, and returns
   the summary
4. Claude reads the result and writes a natural language response:

> "Your stocks are mixed today — 2 up, 3 down. Tesla is your best
> performer, up 3.21%. Disney is lagging, down 1.82%. Apple and Nike
> are having steady days."

Notice: Claude didn't make up any numbers. Every figure came from your
tool. The AI's value is in the *interpretation* — connecting the data
into a clear summary that's easy to understand.
