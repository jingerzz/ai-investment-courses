# Week 2: Did It Work? Checklist

Test your daily report system against these checks.

---

## New Tools Work Correctly

- [ ] **get_market_overview** returns real market data (SPY, QQQ, etc.)
  with pre-computed daily changes and a status label.

- [ ] **get_sector_check** returns sectors sorted by performance with
  notable sectors flagged.

- [ ] **get_watchlist_movers** returns your stocks sorted by performance
  with sector comparison and notable activity flags.

## Pre-Formatted Report

- [ ] **get_report_formatted** returns a `formatted_section` field with
  a table containing exact numbers.

- [ ] **present_verbatim flag** is set to `true` in the return.

- [ ] **Claude Desktop shows the table exactly.** When you ask for a
  report, the numbers in the table match exactly what the tool
  returned — no rounding, no rewording.

## Safety Checks Working

- [ ] **No AI math.** Ask Claude Desktop "What's the average return of
  my stocks?" — the answer should use a pre-computed value from a tool,
  not try to calculate it.

- [ ] **Stale data warning appears.** Run the report in the evening
  or on a weekend. Claude Desktop should mention that the market is
  closed and the data is from the last trading day.

- [ ] **No warning during market hours.** During trading hours, no
  stale data warning should appear.

## Cross-Referencing

- [ ] **Market status connects to stocks.** The report mentions whether
  it's a good day or rough day and relates that to how your stocks
  are doing.

- [ ] **Sectors connect to stocks.** If a stock is down and its sector
  is also down, the report notes the connection.

- [ ] **Notable movers get context.** If a stock moved a lot, the
  report tries to explain why (sector weakness, unusual volume, etc.).

## Guide Tool Updated

- [ ] **All new tools described.** The guide tool lists every tool
  including the new ones from this week.

- [ ] **Report flow documented.** The guide includes the recommended
  order for generating a report.

- [ ] **Safety rules included.** The guide tells the AI to present
  pre-formatted sections as-is and never do math.

---

## How to Test

1. **Run the MCP inspector first** — check that raw tool output looks right
2. **Test in Claude Desktop** — check that the AI uses the data correctly
3. **Try to break it** — ask questions that might cause math errors
4. **Fix problems through Claude Code** — describe the issue, let Claude fix it
5. **Retest** — make sure the fix works

This test-find-fix-retest cycle is how you build reliable AI tools.
