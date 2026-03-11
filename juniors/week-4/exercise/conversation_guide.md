# Week 4: Conversation Guide

How to talk to Claude when building your stock monitor.

---

## Designing Rules (Claude Desktop)

### Getting started

```
I want to build a stock monitoring system. My watchlist has:
RBLX, SNAP, SPOT, DUOL, CROX.

What should it watch for? Help me think of everything — not just
prices, but volume, big news moves, and anything else that matters.
```

### Setting thresholds

```
Help me set good thresholds for alerts:
- How big of a daily move should trigger an alert? 3%? 5%?
- What volume level is "unusual"? 2x average? 3x?

I'd rather get too many alerts at first and dial them back.
```

### Thinking about what's BLOCKED

```
I want to make sure my monitor NEVER does certain things automatically.
Help me list everything that should be BLOCKED (human-only):
- Buying or selling stocks
- What else should never be automated?
```

---

## Building with Claude Code

### Creating the monitor

```
Build monitor.py that checks my stocks (RBLX, SNAP, SPOT, DUOL, CROX)
and logs everything to monitor_log.json.

Check: daily price change and volume for each stock.
Classify: SILENT (normal), ALERT (noteworthy), URGENT (important).
Print: only alerts and urgent items.
Log: everything, including routine checks.

Use yfinance for data.
```

### Adding the audit trail

```
Make the log entries more detailed. Each entry should have:
timestamp, ticker, check_type, current_value, threshold,
classification, suggested_action, data_source.

Each run adds to the log — never overwrite.
Add --summary flag to show alerts from the past 7 days.
```

### Making it an MCP tool

```
Add a tool to my stock server called get_monitor_alerts that reads
the latest entries from monitor_log.json and returns any alerts.
If everything is fine, return {"status": "all_clear"}.
Include the classification and suggested action for each alert.
```

### Adding a daily summary

```
Add a tool called get_daily_digest that:
1. Reads all log entries from today
2. Summarizes: how many checks, how many alerts
3. Lists each alert with context
4. Returns as a pre-formatted section (present_verbatim=true)
```

---

## Testing in Claude Desktop

### Basic alert check

```
Any alerts on my stocks?
```

### Morning review with monitoring

```
Give me my morning report, including any monitoring alerts.
```

### Historical review

```
How many alerts have I had this week? Any patterns?
```

### Understanding the rules

```
If Snapchat drops 6% today, what would my monitor flag?
```

---

## Troubleshooting

### Monitor won't run

```
When I run "uv run python monitor.py" I get this error:
[paste error]
Can you fix it?
```

### Too many alerts

```
I'm getting too many alerts for small moves. Can you change the
threshold from 3% to 5% for the ALERT level?
```

### Alerts not showing in Claude Desktop

```
My get_monitor_alerts tool returns empty even though monitor_log.json
has entries. Can you check if it's reading the right file?
```

### Log file getting huge

```
monitor_log.json is getting really big. Can you add a --cleanup flag
that removes entries older than 30 days?
```

---

## Tips for Week 4

1. **Start loose.** Set thresholds that catch everything. You can always
   raise them later.

2. **Run it manually first.** Test the monitor a few times yourself
   before thinking about automation.

3. **Check the log.** After each run, look at the log entries. Do the
   classifications make sense?

4. **BLOCKED is forever.** Never remove the BLOCKED level for buying
   and selling. This is a permanent design principle.

5. **Connect to Claude Desktop last.** Get the monitor working on its
   own first, then add the MCP tool.
