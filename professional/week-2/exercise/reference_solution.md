# Week 2: Reference Solution — Morning Briefing with Guardrails

Compare what Claude Code built for you against this reference. Focus on the
patterns, not the exact code.

---

## What the Complete Server Looks Like

After Week 2, your server should have approximately 7-8 tools:

| Tool | From | Purpose |
|------|------|---------|
| `get_stock_snapshot` | Week 1 | Single stock detail |
| `get_watchlist_summary` | Week 1 | Quick watchlist overview |
| `get_stock_comparison` | Week 1 | Compare two stocks |
| `get_market_overview` | Week 2 | Index performance + regime |
| `get_sector_heatmap` | Week 2 | Sector ETF performance |
| `get_watchlist_movers` | Week 2 | Watchlist in market context |
| `get_briefing_formatted` | Week 2 | Pre-built briefing section |
| `get_strategy_guide` | Week 1 (updated) | Tool descriptions + rules |

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
      "daily_change_pct": -0.65,
      "above_50d_sma": true,
      "distance_from_50d_pct": 2.3
    },
    {
      "symbol": "QQQ",
      "name": "Nasdaq 100",
      "price": 438.50,
      "daily_change_pct": -0.92,
      "above_50d_sma": true,
      "distance_from_50d_pct": 1.8
    }
  ],
  "regime": "mixed",
  "regime_explanation": "Indices are down today but still above 50-day moving averages. Short-term weakness within an uptrend.",
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z",
  "stale_data_warning": null
}
```

**Why the regime field matters:**

Without it, the AI would need to interpret raw numbers to decide if the
market is "risk-on" or "risk-off." With the pre-computed regime label and
explanation, the AI can immediately incorporate it into the briefing without
doing any analysis of its own.

---

## Guardrail: Pre-Formatted Briefing Section

**What `get_briefing_formatted()` returns:**

```json
{
  "formatted_section": "## Watchlist Performance — March 15, 2024\n\n| Stock | Price | Daily Change | vs Sector |\n|-------|-------|--------------|-----------|\n| NVDA | $868.30 | +2.15% | +1.8% above XLK |\n| AAPL | $195.20 | +0.85% | +0.5% above XLK |\n| JPM | $186.40 | +0.32% | -0.1% below XLF |\n| MSFT | $415.60 | -0.42% | -0.8% below XLK |\n| XOM | $103.20 | -1.53% | -0.3% below XLE |\n\n**Market Regime:** Mixed (down day, still above 50d SMA)\n**Watchlist Average Return:** -0.13%\n**Notable:** NVDA unusual volume (2.8x average)",
  "present_verbatim": true,
  "ai_interpretation_notes": "NVDA is the standout — strong day with unusual volume while the broader market is weak. XOM weakness is sector-driven (Energy is the worst sector today). The market regime is mixed, not bearish — this is a pullback within an uptrend.",
  "data_source": "yfinance",
  "as_of": "2026-03-15T16:05:00Z",
  "stale_data_warning": null
}
```

**How this works as a guardrail:**

The `formatted_section` contains a markdown table with exact numbers that
Python computed. The AI presents this table as-is — no chance of rounding
$868.30 to $868 or miscalculating the daily change.

The `ai_interpretation_notes` tells the AI what to talk about. The AI adds
its own analysis and cross-referencing based on these notes, but the numbers
in the table are sacrosanct.

**What the final briefing looks like in Claude Desktop:**

> ## Watchlist Performance — March 15, 2024
>
> | Stock | Price | Daily Change | vs Sector |
> |-------|-------|--------------|-----------|
> | NVDA | $868.30 | +2.15% | +1.8% above XLK |
> | ... | ... | ... | ... |
>
> **Market Regime:** Mixed (down day, still above 50d SMA)
> **Watchlist Average Return:** -0.13%
> **Notable:** NVDA unusual volume (2.8x average)
>
> NVDA stands out today — up 2.15% with 2.8x average volume while the
> broader market pulled back. This is notable strength. XOM's weakness
> (-1.53%) appears sector-driven, as Energy (XLE) is the worst-performing
> sector today, so this is less about XOM specifically and more about
> energy broadly. Overall, the market regime is mixed — indices are down
> but still above their 50-day moving averages, suggesting a pullback
> within an uptrend rather than a trend change.

Notice: the table has exact Python-computed numbers. The narrative below
it is the AI's interpretation. Both are valuable, but the numbers are
guaranteed accurate.

---

## Guardrail: Stale Data Warning

**During market hours** (no warning):

```json
{
  "stale_data_warning": null
}
```

**After hours / weekends:**

```json
{
  "stale_data_warning": "Market closed. Prices are from the most recent trading session (Friday, March 15, 2024 at 4:00 PM ET)."
}
```

**How the AI handles it:**

When stale_data_warning is present, the AI leads with:

> **Note:** Market is currently closed. The data below is from Friday,
> March 15, 2024 at 4:00 PM ET.

This prevents users from thinking they're seeing live prices on a Saturday
morning.

---

## Updated Guide Tool

The guide tool should now include the morning briefing flow:

```json
{
  "overview": "Stock watchlist server with market context and morning briefing tools.",
  "recommended_flows": {
    "quick_check": [
      "get_stock_snapshot(ticker) — one stock, quick answer"
    ],
    "morning_briefing": [
      "1. get_market_overview() — macro context",
      "2. get_sector_heatmap() — where money is flowing",
      "3. get_watchlist_movers() — your stocks in context",
      "4. get_briefing_formatted() — pre-built summary (present verbatim)"
    ],
    "comparison": [
      "get_stock_comparison(ticker1, ticker2) — head-to-head"
    ]
  },
  "rules": [
    "When get_briefing_formatted returns present_verbatim=true, display the formatted_section exactly as returned. Do not reformat, round, or recalculate any numbers.",
    "If any tool returns a stale_data_warning, display it prominently at the top of your response before any analysis.",
    "Never calculate percentages, averages, or P&L from raw numbers. Always use pre-computed fields from tool returns."
  ]
}
```

The `rules` section is the most important guardrail. It tells the AI:
1. Don't touch the pre-formatted section
2. Always surface stale data warnings
3. Never do math — use pre-computed values

These rules go in the guide tool because the AI reads the guide tool first
and follows its instructions throughout the conversation.

---

## The Three Guardrail Patterns

| Pattern | What It Prevents | How It Works |
|---------|-----------------|-------------|
| Pre-formatted template | AI rounding or miscalculating numbers | Python builds markdown with exact numbers; AI presents verbatim |
| Stale data warning | AI presenting old data as current | Tool checks market hours; includes warning when stale |
| No-compute rule | AI doing math incorrectly | All aggregates pre-computed; guide tool forbids AI math |

These three patterns handle the vast majority of accuracy issues in
financial AI tools.
