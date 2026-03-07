# Week 4: Evaluation Checklist

Evaluate your monitoring agent and audit trail.

---

## Monitor Script

- [ ] **Runs without errors.** `uv run python monitor.py` completes
  and prints a summary.

- [ ] **Checks all categories.** Price moves, concentration limits,
  sector limits, and unusual volume are all checked.

- [ ] **Classifications make sense.** A 1% move is "info", a 4% move
  is "alert", a limit breach is "urgent". Review a few entries and
  verify the logic.

- [ ] **Prints only alerts and warnings.** The terminal output doesn't
  drown you in routine "info" entries.

## Audit Trail

- [ ] **Log file exists.** `monitor_log.json` is created after running
  the monitor.

- [ ] **Entries have all fields.** Each log entry includes timestamp,
  check_type, ticker, current value, threshold, classification, and
  suggested action.

- [ ] **Log is append-only.** Running the monitor twice creates more
  entries — it doesn't overwrite the first run.

- [ ] **Summary flag works.** `uv run python monitor.py --summary`
  shows alerts from the past week.

## Approval Levels

- [ ] **Rules are defined.** The script has a rules section that maps
  each finding type to SILENT / ALERT / URGENT / BLOCKED.

- [ ] **BLOCKED items exist.** At minimum, "place_trade" and
  "change_risk_limits" are BLOCKED — never automated.

- [ ] **Rules are visible in output.** Each alert shows its approval
  level and the rule that triggered it.

## MCP Integration

- [ ] **get_monitor_alerts tool works.** In Claude Desktop, asking
  "Any alerts?" returns data from the monitor log.

- [ ] **Tool filters correctly.** Only alerts and warnings are returned,
  not routine info entries.

- [ ] **Status when all clear.** If no alerts exist, the tool returns
  `{"status": "all_clear"}` — not an empty or confusing response.

- [ ] **Claude interprets correctly.** Claude Desktop gives a useful
  natural language summary of the alerts, including suggested actions.

## Design Principles

- [ ] **AI proposes, human decides.** Nothing in your system executes
  a trade without human action. The monitor only alerts and suggests.

- [ ] **Everything is logged.** Even "all clear" checks are recorded.
  You can reconstruct exactly what the monitor saw at any point.

- [ ] **Thresholds are explicit.** Every alert has a clear threshold.
  No magic numbers hidden in code that you can't review.

---

## End-of-Course Self-Assessment

After completing all four weeks, you should be able to:

- [ ] **Describe a workflow to Claude Code** and get a working MCP server
- [ ] **Evaluate** whether what Claude built is correct and complete
- [ ] **Iterate** when something isn't right — describe the problem, let
  Claude fix it
- [ ] **Connect MCP tools to Claude Desktop** and use them in conversation
- [ ] **Design guardrails** that prevent the AI from making mistakes
  (pre-computed values, stale data warnings, verbatim sections)
- [ ] **Architect a multi-server system** with clear domain boundaries
- [ ] **Build monitoring with audit trails** and appropriate approval levels
- [ ] **Explain the principle** "AI proposes, humans decide" and why it
  matters in finance
