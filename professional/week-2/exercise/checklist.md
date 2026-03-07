# Week 2: Evaluation Checklist

Test your morning briefing system against these criteria.

---

## New Tools Work Correctly

- [ ] **get_market_overview** returns real index data (SPY, QQQ, etc.) with
  pre-computed daily changes and a regime label (risk-on/risk-off/mixed).

- [ ] **get_sector_heatmap** returns all 11 sectors sorted by performance
  with notable sectors flagged.

- [ ] **get_watchlist_movers** returns your stocks sorted by performance
  with sector comparison and notable activity flags.

## Pre-Formatted Briefing

- [ ] **get_briefing_formatted** returns a `formatted_section` field with
  a markdown table containing exact numbers.

- [ ] **present_verbatim flag** is set to `true` in the return.

- [ ] **Claude Desktop shows the table as-is.** When you ask for a briefing,
  the numbers in the table match exactly what the tool returned — no
  rounding, no rewording.

## Guardrails Working

- [ ] **No AI math.** Ask Claude Desktop "What's the average return of my
  watchlist?" — the answer should use a pre-computed value from a tool,
  not calculate from individual returns.

- [ ] **Stale data warning appears.** Run the briefing outside market hours.
  Claude Desktop should say something like "Note: market is closed, these
  prices are from the most recent trading session."

- [ ] **Stale data warning absent during market hours.** During trading
  hours, no stale data warning should appear.

## Cross-Referencing

- [ ] **Regime connects to stocks.** The briefing mentions whether the
  market regime is favorable or unfavorable for your positions.

- [ ] **Sectors connect to stocks.** If a stock is down and its sector is
  also down, the briefing notes the connection (sector-wide weakness,
  not stock-specific).

- [ ] **Notable movers get context.** If a stock moved more than 3%,
  the briefing tries to explain it in context of the broader market.

## Guide Tool Updated

- [ ] **All new tools described.** The guide tool lists every tool
  including the new ones from this week.

- [ ] **Morning briefing flow documented.** The guide includes the
  recommended sequence for generating a briefing.

- [ ] **Verbatim rule included.** The guide tells the AI to present
  `formatted_section` content exactly as returned.

---

## Testing Methodology

1. **Run the MCP inspector first** — verify raw tool output is correct
2. **Test in Claude Desktop** — verify the AI interprets correctly
3. **Try to break it** — ask questions that probe guardrail gaps
4. **Fix gaps through Claude Code** — describe the problem, let Claude fix it
5. **Retest** — confirm the fix works

This test → find problem → fix → retest cycle is the core workflow for
building reliable AI tools.
