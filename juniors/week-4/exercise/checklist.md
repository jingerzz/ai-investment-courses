# Week 4: Did It Work? Checklist

Check your monitoring system and audit trail.

---

## Monitor Script

- [ ] **Runs without errors.** `uv run python monitor.py` completes
  and prints a summary.

- [ ] **Checks all stocks.** Every stock in your watchlist is checked
  for price moves and volume.

- [ ] **Classifications make sense.** A 1% move is SILENT, a 4% move
  is ALERT, a 6% move is URGENT. Spot-check a few entries.

- [ ] **Only shows important stuff.** Terminal output shows alerts and
  urgent items, not routine SILENT entries.

## Audit Trail

- [ ] **Log file exists.** `monitor_log.json` is created after running
  the monitor.

- [ ] **Entries have all fields.** Each entry includes timestamp, ticker,
  check type, value, threshold, classification, and suggestion.

- [ ] **Log is append-only.** Running the monitor twice creates more
  entries — doesn't overwrite the first run.

- [ ] **Summary works.** `uv run python monitor.py --summary` shows
  alerts from the past week.

## Rules and Levels

- [ ] **Rules are defined.** The script has a rules section with clear
  thresholds and classifications.

- [ ] **BLOCKED items exist.** Buying/selling stocks is marked as
  BLOCKED — never automated.

- [ ] **Rules are visible.** Each alert shows its classification level
  and the rule that triggered it.

## Claude Desktop Integration

- [ ] **get_monitor_alerts works.** Asking Claude "Any alerts?" returns
  data from the monitor log.

- [ ] **Filters correctly.** Only alerts and urgent items are returned,
  not routine entries.

- [ ] **All clear works.** If no alerts, the tool returns a clear
  "all_clear" status.

- [ ] **Claude gives useful summaries.** Claude Desktop provides a
  natural language summary of alerts with suggested actions.

## Key Principles

- [ ] **AI suggests, humans decide.** Nothing in your system buys or
  sells stocks. The monitor only alerts and recommends.

- [ ] **Everything is logged.** Even routine "all clear" checks are
  recorded. You can see exactly what happened at any time.

- [ ] **Thresholds are visible.** Every alert has a clear threshold
  that you can review and adjust.

---

## End-of-Course Self-Check

After all four weeks, you should be able to:

- [ ] **Describe what you want** to Claude Code and get a working tool
- [ ] **Check** whether what Claude built is correct
- [ ] **Fix things** when something isn't right — describe the problem,
  let Claude fix it
- [ ] **Connect tools to Claude Desktop** and use them in conversation
- [ ] **Add safety checks** that keep AI honest (pre-computed numbers,
  stale data warnings, verbatim sections)
- [ ] **Design a multi-server system** with clear boundaries
- [ ] **Build monitoring** with audit trails and alert levels
- [ ] **Explain why** AI should suggest but never decide when it comes
  to investing
