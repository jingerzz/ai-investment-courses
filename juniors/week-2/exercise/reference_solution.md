# Week 2: Reference Solution — Daily Report with Safety Checks

Compare what Claude Code built for you against this reference. Focus on
the patterns, not the exact code.

---

## What the Complete Server Looks Like

After Week 2, your server should have about 7-8 tools:

| Tool | From | Purpose |
|------|------|---------|
| `get_stock_snapshot` | Week 1 | Single stock detail |
| `get_watchlist_summary` | Week 1 | Quick watchlist overview |
| `get_stock_comparison` | Week 1 | Compare two stocks |
| `get_market_overview` | Week 2 | Market status |
| `get_sector_check` | Week 2 | Sector performance |
| `get_watchlist_movers` | Week 2 | Stocks in market context |
| `get_report_formatted` | Week 2 | Pre-built report section |
| `get_strategy_guide` | Week 1 (updated) | Tool menu + rules |

---

## New Tool: `get_market_overview()`

**What it returns:**

```json
{
  "indices": [
    {
      "symbol": "SPY",
      "name": "S&P 500",
      "price": 512.30,
      "daily_change_pct": -0.65
    },
    {
      "symbol": "QQQ",
      "name": "Nasdaq 100",
      "price": 438.50,
      "daily_change_pct": -0.92
    }
  ],
  "market_status": "meh",
  "status_explanation": "Market is slightly down today but nothing dramatic.",
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z",
  "stale_data_warning": null
}
```

**Why `market_status` matters:**

Without it, the AI would need to look at SPY's number and decide if
the market is having a good day or bad day. With a pre-computed label
("good day", "rough day", "meh"), the AI can immediately use it.

---

## Safety Check: Pre-Formatted Report Section

**What `get_report_formatted()` returns:**

```json
{
  "formatted_section": "## Your Stocks — March 15, 2026\n\n| Stock | Price | Daily Change | vs Sector |\n|-------|-------|--------------|-----------|\n| RBLX | $59.80 | +1.65% | +1.2% above XLK |\n| DUOL | $97.42 | +0.38% | +0.0% vs XLK |\n| CROX | $80.49 | +0.12% | -0.3% below XLY |\n| SPOT | $517.31 | -0.45% | +0.1% above XLK |\n| SNAP | $4.86 | -2.21% | -0.9% below XLK |\n\n**Market Status:** Meh (slightly down day)\n**Your Average Return:** -0.10%\n**Notable:** RBLX elevated volume (1.5x average)",
  "present_verbatim": true,
  "ai_notes": "Roblox is the standout — strong day with elevated volume while the broader market is slightly down. Snapchat's weakness is sharper than its sector, worth watching. The market status is 'meh', not alarming.",
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z",
  "stale_data_warning": null
}
```

**How this protects against mistakes:**

The `formatted_section` contains a table with exact numbers that the
code calculated. The AI shows this table exactly as-is — no chance of
rounding $178.50 to $179 or saying "about 3%" instead of "+3.21%".

The `ai_notes` tells the AI what's interesting. The AI adds its own
commentary based on these notes, but the numbers in the table stay
exactly as the code made them.

**What the report looks like in Claude Desktop:**

> ## Your Stocks — March 15, 2026
>
> | Stock | Price | Daily Change | vs Sector |
> |-------|-------|--------------|-----------|
> | RBLX | $59.80 | +1.65% | +1.2% above XLK |
> | DUOL | $97.42 | +0.38% | +0.0% vs XLK |
> | CROX | $80.49 | +0.12% | -0.3% below XLY |
> | SPOT | $517.31 | -0.45% | +0.1% above XLK |
> | SNAP | $4.86 | -2.21% | -0.9% below XLK |
>
> **Market Status:** Meh (slightly down day)
> **Your Average Return:** -0.10%
> **Notable:** RBLX elevated volume (1.5x average)
>
> Roblox is your standout today — up 1.65% with elevated volume, even
> while the overall market is slightly down. That kind of strength
> against a weak market is worth paying attention to. Snapchat is down
> 2.21%, underperforming its sector by about a percent — that's more
> of a SNAP-specific issue than a market-wide problem.

Notice: the table has exact code-calculated numbers. The paragraph below
is the AI connecting the dots. Both are valuable, but the numbers are
guaranteed accurate.

---

## Safety Check: Stale Data Warning

**During market hours** (no warning):

```json
{
  "stale_data_warning": null
}
```

**After hours / weekends:**

```json
{
  "stale_data_warning": "Market closed. Prices are from the most recent trading day (Friday, March 15, 2026 at 4:00 PM ET)."
}
```

**How the AI handles it:**

When `stale_data_warning` is present, the AI starts with:

> **Heads up:** The market is closed right now. The prices below are
> from Friday at 4:00 PM ET.

This prevents you from thinking you're seeing live prices when the
market is actually closed.

---

## Updated Guide Tool

The guide tool should now include the daily report flow:

```json
{
  "overview": "Stock watchlist tracker with market context and daily report tools.",
  "recommended_flows": {
    "quick_check": [
      "get_stock_snapshot(ticker) — one stock, quick answer"
    ],
    "daily_report": [
      "1. get_market_overview() — overall market status",
      "2. get_sector_check() — which sectors are up and down",
      "3. get_watchlist_movers() — your stocks in context",
      "4. get_report_formatted() — pre-built summary (show exactly as-is)"
    ],
    "comparison": [
      "get_stock_comparison(ticker1, ticker2) — head-to-head"
    ]
  },
  "rules": [
    "When get_report_formatted returns present_verbatim=true, show the formatted_section exactly as returned. Do not round or change any numbers.",
    "If any tool returns a stale_data_warning, mention it at the top of your response before any data.",
    "Never calculate percentages, averages, or totals from raw numbers. Always use pre-computed fields from tool returns."
  ]
}
```

---

## The Three Safety Check Patterns

| Pattern | What It Prevents | How It Works |
|---------|-----------------|-------------|
| Pre-formatted section | AI rounding or changing numbers | Code builds a table with exact numbers; AI shows it as-is |
| Stale data warning | AI showing old data as if it's live | Tool checks if market is open; includes warning when closed |
| No-calculation rule | AI doing math wrong | All averages and totals pre-computed; guide tool forbids AI math |

These three patterns prevent the most common accuracy problems in AI
tools that work with numbers.
