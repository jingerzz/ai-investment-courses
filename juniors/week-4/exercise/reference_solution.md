# Week 4: Reference Solution — Stock Monitor

Compare what Claude Code built for you against this reference.

---

## What the Monitor Does

The script checks your stocks and tells you what matters:

```
$ uv run python monitor.py

Stock Monitor — March 15, 2026 at 10:30 AM
==========================================

URGENT (1):
  TSLA down -6.2% today on high volume (2.5x average)
    → Big drop with high volume — check for news
    → Rule: big_move → URGENT

ALERTS (1):
  NKE down -3.8% today
    → Medium-sized drop, worth keeping an eye on
    → Rule: medium_move → ALERT

All clear on AAPL, DIS, NFLX.
Full log: monitor_log.json (10 entries)
```

---

## Alert Levels

Here are the rules that govern the monitor:

| Level | Meaning | Examples |
|-------|---------|---------|
| SILENT | Normal, just logged | Stock moved 0.5%, routine check |
| ALERT | Worth knowing | 3-5% move, unusual volume |
| URGENT | Needs your attention | 5%+ move, really high volume |
| BLOCKED | Never automated | Buying/selling stocks, ever |

**Why BLOCKED is permanent:**

The monitor can say "Tesla dropped 6%, you might want to sell some
shares." But it NEVER actually sells. This isn't because the code
can't — it's a choice. In investing:

- A wrong alert is harmless — you just ignore it
- A wrong trade costs real money
- AI can be confident AND wrong at the same time
- Building trust is gradual — you don't hand over control on day one

---

## Audit Log Structure

Each entry in `monitor_log.json`:

```json
{
  "timestamp": "2026-03-15T10:30:00Z",
  "ticker": "TSLA",
  "check_type": "daily_price_move",
  "current_value": -6.2,
  "threshold": 5.0,
  "unit": "percent",
  "classification": "URGENT",
  "suggested_action": "Big drop with high volume — check for news",
  "data_source": "yfinance",
  "run_id": "2026-03-15T10:30:00Z"
}
```

**Why log everything, even boring checks?**

If Tesla was fine at 9:00 AM and crashed by 10:30 AM, the log shows
exactly when things changed. Without the "all clear" entries, you'd
only know it crashed — not when or how fast.

**The --summary flag:**

```
$ uv run python monitor.py --summary

Monitor Summary — Past 7 Days
==============================
Total checks: 30
Total alerts: 4
Total urgent: 1

Most frequent alerts:
  TSLA price moves: 2 alerts
  NKE price moves: 1 alert
  DIS unusual volume: 1 alert

Trend: Normal alert level this week
```

This helps you spot patterns. "Tesla triggered alerts twice this week"
is more useful than seeing each alert by itself.

---

## MCP Tool: `get_monitor_alerts()`

This tool makes monitoring data available in Claude Desktop:

**When alerts exist:**

```json
{
  "status": "alerts_found",
  "alert_count": 1,
  "urgent_count": 1,
  "alerts": [
    {
      "classification": "ALERT",
      "ticker": "NKE",
      "message": "Down -3.8% today",
      "suggested_action": "Medium-sized drop, worth watching",
      "timestamp": "2026-03-15T10:30:00Z"
    }
  ],
  "urgent": [
    {
      "classification": "URGENT",
      "ticker": "TSLA",
      "message": "Down -6.2% today on 2.5x average volume",
      "suggested_action": "Check for news",
      "timestamp": "2026-03-15T10:30:00Z"
    }
  ],
  "last_check": "2026-03-15T10:30:00Z",
  "data_source": "monitor_log.json"
}
```

**When everything is fine:**

```json
{
  "status": "all_clear",
  "alert_count": 0,
  "urgent_count": 0,
  "message": "All stocks within normal ranges. No unusual activity.",
  "last_check": "2026-03-15T10:30:00Z",
  "data_source": "monitor_log.json"
}
```

**How Claude Desktop uses it:**

When you ask "Any alerts on my stocks?", Claude reads the monitor log
and says something like:

> You have 1 urgent item and 1 alert:
>
> **URGENT: Tesla down 6.2% on high volume** — Volume is 2.5x normal,
> which usually means something happened in the news. Worth checking.
>
> **ALERT: Nike down 3.8%** — Not as dramatic as Tesla, but notable.
> Keep an eye on it.
>
> Apple, Disney, and Netflix are all fine today.

Notice how Claude adds context and connects the dots — that's the
value AI adds on top of raw alert data.

---

## Building Trust Over Time

How your relationship with the monitor can evolve:

```
Day 1:
  Everything is ALERT level. You review every finding manually.
  This proves the classifications make sense.

Week 2:
  Move routine checks to SILENT. You've verified that normal
  checks are correctly classified. No point reviewing them.

Month 1:
  You trust the thresholds. Start checking the summary view
  instead of every individual alert.

Month 3:
  You've seen 30+ alerts. You know the system works.
  Consider adjusting thresholds based on what you've learned.

Never:
  BLOCKED items stay BLOCKED. The system never buys or sells
  stocks, no matter how much you trust it.
```

---

## What You Built Over 4 Weeks

| Week | What You Built | Key Pattern |
|------|---------------|-------------|
| 1 | Stock tracker with real data | AI calls tools for real data |
| 2 | Daily report with safety checks | AI presents pre-computed numbers honestly |
| 3 | Multi-server architecture | Separate concerns, connect with Claude |
| 4 | Monitor with audit trail | AI watches and suggests, humans decide |

The big takeaway: **you built all of this by describing what you wanted
in plain English.** Claude Code wrote the code. Your skill is knowing
what to ask for, checking whether it's right, and improving it through
conversation.

That skill works for anything — not just stocks. You can build tools
for tracking sports stats, analyzing social media trends, monitoring
weather, or anything else that involves data. The pattern is always
the same:

1. Describe what you want to Claude Code
2. Claude builds the tools
3. Connect to Claude Desktop
4. Use AI with access to real data
5. Keep improving
