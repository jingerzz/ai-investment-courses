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
  "ticker": "RBLX",
  "company_name": "Roblox Corporation",
  "current_price": 59.80,
  "previous_close": 58.83,
  "daily_change": 0.97,
  "daily_change_pct": 1.65,
  "fifty_two_week_high": 66.50,
  "fifty_two_week_low": 30.25,
  "volume": 18420300,
  "avg_volume_10d": 12500000,
  "market_cap": 38200000000,
  "pe_ratio": null,
  "dividend_yield_pct": 0.0,
  "notable": "Elevated volume — 47% above 10-day average",
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**What's smart about this design:**

- **`daily_change_pct` is already calculated.** The code did the math
  `(59.80 - 58.83) / 58.83 * 100 = 1.65%`. The AI just reports the
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
      "ticker": "RBLX",
      "current_price": 59.80,
      "daily_change_pct": 1.65,
      "status": "hot"
    },
    {
      "ticker": "DUOL",
      "current_price": 97.42,
      "daily_change_pct": 0.38,
      "status": "steady"
    },
    {
      "ticker": "CROX",
      "current_price": 80.49,
      "daily_change_pct": 0.12,
      "status": "steady"
    },
    {
      "ticker": "SPOT",
      "current_price": 517.31,
      "daily_change_pct": -0.45,
      "status": "steady"
    },
    {
      "ticker": "SNAP",
      "current_price": 4.86,
      "daily_change_pct": -2.21,
      "status": "cold"
    }
  ],
  "best_performer": "RBLX",
  "worst_performer": "SNAP",
  "watchlist_count": 5,
  "up_count": 1,
  "down_count": 2,
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**What's smart about this design:**

- **Already sorted.** Best performer is at the top, worst at the bottom.
  The AI doesn't need to sort — it's already done.

- **`status` field makes it easy.** "hot" means up more than 1%, "cold"
  means down more than 1%, "steady" means in between. The AI can
  immediately say "Roblox is hot today" without analyzing numbers.

- **`best_performer` and `worst_performer` are pre-identified.** The AI
  can immediately say "Roblox is your best performer" without scanning
  the whole list.

---

## Tool 3: `get_stock_comparison(ticker1, ticker2)`

**When to use:** "Compare Roblox and Spotify" or "Which is better?"

**What it returns:**

```json
{
  "comparison": {
    "ticker1": {
      "ticker": "RBLX",
      "current_price": 59.80,
      "daily_change_pct": 1.65,
      "ytd_return_pct": 18.7,
      "pe_ratio": null,
      "market_cap_billions": 38.2,
      "dividend_yield_pct": 0.0
    },
    "ticker2": {
      "ticker": "SPOT",
      "current_price": 517.31,
      "daily_change_pct": -0.45,
      "ytd_return_pct": 9.2,
      "pe_ratio": 85.3,
      "market_cap_billions": 103.5,
      "dividend_yield_pct": 0.0
    }
  },
  "edge": {
    "daily_leader": "RBLX",
    "ytd_leader": "RBLX",
    "lower_pe": "SPOT",
    "higher_dividend": "neither",
    "larger_company": "SPOT"
  },
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z"
}
```

**What's smart about this design:**

- **`edge` section shows who's winning.** Instead of making the AI
  compare numbers, the code already figured out which stock leads on
  each metric. The AI just explains the result.

- **Friendly units.** Market cap is in billions (103.5) not raw numbers
  (103,500,000,000). Percentages are actual percentages (18.7, not
  0.187). This makes the AI's answers more natural.

- **YTD return** (Year-to-Date return) shows how much the stock has
  gone up or down since January 1st. This gives longer-term context
  beyond just today's movement.

---

## Tool 4: `get_strategy_guide()`

**When to use:** The AI calls this first in any new conversation.

**What it returns:**

```json
{
  "overview": "Stock watchlist tracker for RBLX, SNAP, SPOT, DUOL, CROX. Uses Yahoo Finance for real-time market data.",
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

> "Your stocks are mixed today. Roblox is your standout, up 1.65%
> with heavy volume. Snapchat is the weakest, down 2.21%. Duolingo,
> Crocs, and Spotify are all having steady days."

Notice: Claude didn't make up any numbers. Every figure came from your
tool. The AI's value is in the *interpretation* — connecting the data
into a clear summary that's easy to understand.
