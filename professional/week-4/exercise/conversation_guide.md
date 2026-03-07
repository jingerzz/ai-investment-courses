# Week 4: Conversation Guide

How to talk to Claude when building monitoring and agent workflows.

---

## Designing Rules (Claude Desktop)

### Getting started with monitoring design

```
I want to build a portfolio monitoring agent. My portfolio has these
stocks: [list them].

What should it monitor? Help me think of everything — not just prices,
but risk metrics, volume, concentration, and anything else that matters
for an equity portfolio.
```

### Defining thresholds

```
Help me set reasonable thresholds for alerts:
- What daily price move should trigger an alert? 3%? 5%?
- How close to a risk limit should I be warned? 80% of limit? 90%?
- What volume multiple is "unusual"? 2x average? 3x?

I'd rather get too many alerts at first and dial them back than miss
something important.
```

### Thinking about approval levels

```
I want to categorize every possible action into these levels:
- SILENT: happens automatically, just logged
- ALERT: I'm notified and decide what to do
- URGENT: I'm notified immediately
- BLOCKED: never automated, always requires my manual action

Help me classify these actions:
- Routine data check
- Small price move (< 3%)
- Large price move (> 5%)
- Approaching a concentration limit
- Breaching a concentration limit
- Placing a trade to rebalance
- Changing a risk limit
```

---

## Building with Claude Code

### Creating the monitor script

```
Build a monitoring script called monitor.py that checks my portfolio
and logs everything to monitor_log.json.

Check:
- Price and daily change for each stock
- Position concentration vs 20% single-stock limit
- Sector concentration vs 35% sector limit
- Unusual volume (> 2x 10-day average)

Classify findings as alert/warning/info. Print only alerts and warnings.
Log everything.

My portfolio: [list stocks and approximate share counts]
```

### Adding the audit trail

```
The monitor_log.json needs more detail. For each finding, log:
- timestamp
- check_type (what was checked)
- ticker (which stock)
- current_value (what the current metric is)
- threshold (what the limit is)
- classification (alert/warning/info)
- suggested_action (what I should consider doing)
- data_source

Also add a --summary flag that shows alerts from the past 7 days.
```

### Making it an MCP tool

```
Add a tool to my portfolio_server.py called get_monitor_alerts that
reads the latest entries from monitor_log.json and returns any alerts
or warnings. If everything is fine, return {"status": "all_clear"}.

Include the approval level and suggested action for each alert.
```

### Adding a daily digest

```
Add a tool called get_daily_digest that:
1. Reads all monitor_log.json entries from today
2. Summarizes: how many checks ran, how many alerts, how many warnings
3. Lists each alert with context
4. Includes a "trend" field: is today more or less alert-heavy than
   the past 5 days?

Return this as a pre-formatted markdown section (present_verbatim=true)
so the AI shows exact numbers.
```

---

## Testing in Claude Desktop

### Basic alert check

```
Are there any alerts on my portfolio?
```

### Morning review with monitoring

```
Give me my morning briefing, including any monitoring alerts from
overnight.
```

### Historical review

```
How many alerts have I had this week? Any patterns?
```

### Testing the boundary

```
If NVDA drops 6% today, what would the monitor flag?
(Claude should explain the alert levels that would trigger)
```

---

## Troubleshooting

### Monitor script won't run

```
When I run "uv run python monitor.py" I get this error:
[paste error]
Can you fix it?
```

### Log file growing too large

```
monitor_log.json is getting very large. Can you add a --cleanup flag
that removes entries older than 30 days?
```

### Too many alerts

```
I'm getting too many "info" level entries in my alerts. Can you filter
the get_monitor_alerts tool to only return "alert" and "warning" level
findings? Keep logging everything, but only surface the important stuff.
```

### Alerts not showing in Claude Desktop

```
My get_monitor_alerts tool returns empty even though monitor_log.json
has entries. Can you check if it's reading the right file path?
```

---

## Tips for Week 4

1. **Start conservative.** Set all thresholds loose (3% moves, 80% of
   limits). You can always tighten them later.

2. **Run the monitor manually first.** Before automating, run it yourself
   a few times to verify the output makes sense.

3. **Check the audit log.** After each run, look at monitor_log.json
   (ask Claude Code to show you the latest entries). Verify the
   classifications make sense.

4. **The BLOCKED level is non-negotiable.** Never remove it for trading
   or limit changes. This is a permanent design principle, not training
   wheels.

5. **Connect it to Claude Desktop last.** Get the monitor working
   standalone first, then add the MCP tool. This way you debug one
   thing at a time.
