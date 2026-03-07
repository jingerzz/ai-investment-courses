# Week 4: Reference Solution — Portfolio Monitoring Agent

Compare what Claude Code built for you against this reference.

---

## What the Monitor Does

The monitoring script checks your portfolio and classifies findings:

```
$ uv run python monitor.py

Portfolio Monitor — 2026-03-15 10:30:00 ET
==========================================

ALERTS (2):
  [URGENT] NVDA position at 22.3% — exceeds 20% single-stock limit
    → Consider trimming ~50 shares to bring to 18%
    → Rule: breaching_position_limit → URGENT

  [ALERT] XOM down -4.2% today on unusual volume (2.8x average)
    → Review for news. Consider whether thesis still holds.
    → Rule: price_move_3_to_5pct → ALERT

WARNINGS (1):
  [WARNING] Technology sector at 33.8% — approaching 35% limit
    → Monitor closely. NVDA trim would also reduce sector weight.
    → Rule: approaching_sector_limit → ALERT

All clear on 7 other positions.
Full log written to monitor_log.json (15 entries).
```

---

## Approval Levels

This is the rules configuration that governs the monitor:

```
Level       | Meaning                              | Examples
------------|--------------------------------------|---------------------------
SILENT      | Runs automatically, logged only       | Routine price check, no move
ALERT       | Notifies you, you decide              | 3-5% move, approaching limit
URGENT      | Notifies you immediately              | 5%+ move, limit breach
BLOCKED     | Never automated, human action only    | Placing trades, changing limits
```

**Why BLOCKED is permanent:**

The monitor can say "trim 50 shares of NVDA." It can even calculate the
exact order. But it never places the trade. This isn't because the code
can't — it's a deliberate design choice. In finance:

- Regulations require human oversight of trading decisions
- A wrong alert is harmless; a wrong trade is expensive
- Building trust with AI systems is incremental — you don't start with
  execution and hope for the best

---

## Audit Log Structure

Each entry in `monitor_log.json`:

```json
{
  "timestamp": "2026-03-15T10:30:00Z",
  "check_type": "position_concentration",
  "ticker": "NVDA",
  "current_value": 22.3,
  "threshold": 20.0,
  "unit": "percent_of_portfolio",
  "classification": "alert",
  "approval_level": "URGENT",
  "suggested_action": "Consider trimming ~50 shares to bring position to 18% of portfolio",
  "data_source": "yfinance",
  "run_id": "2026-03-15T10:30:00Z"
}
```

**Why log everything, even "all clear"?**

If NVDA was fine at 10:00 AM and breached the limit at 10:30 AM, the
log shows exactly when it crossed. Without the "all clear" entries, you'd
only know it breached, not when.

**The --summary flag:**

```
$ uv run python monitor.py --summary

Monitor Summary — Past 7 Days
==============================
Total checks: 45
Total alerts: 8
Total warnings: 12

Most frequent alerts:
  NVDA concentration: 5 alerts (ongoing)
  XOM price moves: 2 alerts
  Unusual volume: 1 alert

Trend: Alert frequency INCREASING (3 alerts Mon-Wed → 5 alerts Thu-Fri)
```

This summary helps you spot patterns. "NVDA has triggered 5 concentration
alerts this week" is more actionable than seeing each individual alert.

---

## MCP Tool: `get_monitor_alerts()`

This tool makes monitoring data available to Claude Desktop:

**What it returns (when alerts exist):**

```json
{
  "status": "alerts_found",
  "alert_count": 2,
  "warning_count": 1,
  "alerts": [
    {
      "classification": "URGENT",
      "check_type": "position_concentration",
      "ticker": "NVDA",
      "message": "Position at 22.3% exceeds 20% limit",
      "suggested_action": "Consider trimming ~50 shares",
      "approval_level": "URGENT",
      "timestamp": "2026-03-15T10:30:00Z"
    },
    {
      "classification": "ALERT",
      "check_type": "daily_price_move",
      "ticker": "XOM",
      "message": "Down -4.2% today on 2.8x average volume",
      "suggested_action": "Review for news",
      "approval_level": "ALERT",
      "timestamp": "2026-03-15T10:30:00Z"
    }
  ],
  "warnings": [
    {
      "classification": "WARNING",
      "check_type": "sector_concentration",
      "ticker": "XLK",
      "message": "Technology at 33.8%, approaching 35% limit",
      "suggested_action": "Monitor closely",
      "approval_level": "ALERT",
      "timestamp": "2026-03-15T10:30:00Z"
    }
  ],
  "last_check": "2026-03-15T10:30:00Z",
  "data_source": "monitor_log.json",
  "as_of": "2026-03-15T10:32:00Z"
}
```

**What it returns (when all clear):**

```json
{
  "status": "all_clear",
  "alert_count": 0,
  "warning_count": 0,
  "last_check": "2026-03-15T10:30:00Z",
  "message": "All positions within limits. No unusual activity detected.",
  "data_source": "monitor_log.json",
  "as_of": "2026-03-15T10:32:00Z"
}
```

**How Claude Desktop uses it:**

When you ask "Any alerts on my portfolio?", Claude calls this tool and
responds with something like:

> You have 2 alerts and 1 warning:
>
> **URGENT: NVDA concentration at 22.3%** — This is above your 20%
> single-stock limit. Consider trimming about 50 shares to bring it
> to 18%. Note: this would also help with the Technology sector
> concentration warning below.
>
> **ALERT: XOM down 4.2% on high volume** — Volume is 2.8x average,
> which may indicate news. Worth reviewing whether your thesis still holds.
>
> **WARNING: Tech sector approaching limit** — Technology is at 33.8% of
> your portfolio, nearing the 35% cap. The NVDA trim would address this too.

Notice how Claude cross-references the NVDA concentration alert with the
sector warning — this is the AI synthesis value that a raw alert log can't
provide.

---

## The Autonomy Progression

How to build trust with your monitoring system over time:

```
Day 1:
  Everything is ALERT level. You review every finding manually.
  This validates that the classifications make sense.

Week 2:
  Move routine checks to SILENT. You've verified that "no move"
  entries are correctly classified. No point in reviewing them.

Month 1:
  You trust the alert thresholds. Consider connecting to email
  or Slack for URGENT alerts so you see them immediately.

Month 3:
  You've reviewed 50+ alerts. You know the system works. Consider
  adding a daily digest tool that summarizes the day's monitoring
  in Claude Desktop.

Never:
  BLOCKED items stay BLOCKED. The system never places trades or
  changes limits, no matter how much you trust it.
```

---

## End-of-Course Summary

Over 4 weeks, you built:

| Week | What | Pattern |
|------|------|---------|
| 1 | Stock watchlist MCP server | Tool-use: AI calls structured functions |
| 2 | Morning briefing with guardrails | Synthesis: AI cross-references tools |
| 3 | Multi-server architecture | Separation: independent domains |
| 4 | Monitoring agent with audit trail | Autonomy: AI proposes, human decides |

The key insight: **you built all of this by describing what you wanted to
Claude Code.** The Python files are artifacts Claude produced. Your skill
is knowing what to ask for, how to evaluate the result, and how to iterate
when it's not right.

That skill transfers to any domain — portfolio analytics, risk management,
research automation, client reporting. The pattern is always:

1. Describe the workflow to Claude Code
2. Claude builds the MCP tools
3. Connect to Claude Desktop
4. Use AI with access to your data
5. Iterate and improve
