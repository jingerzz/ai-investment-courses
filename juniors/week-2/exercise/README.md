# Week 2 Exercise: Build a Daily Stock Report with Safety Checks

## What You'll Build

You'll add new tools to your Week 1 server and create a daily stock
report. When you're done, you'll be able to ask Claude Desktop:

- "Give me my morning report"
- "What should I be paying attention to today?"

...and get an accurate, well-organized report with real data and safety
checks that keep the AI honest.

## Time: 30 minutes

## What You Need

- Your working server from Week 1
- Claude Code and Claude Desktop

---

## Step 1: Open Your Project in Claude Code (1 min)

```bash
cd ~/ai-stock-tools
claude
```

## Step 2: Add Market Context Tools (8 min)

Your Week 1 server knows about individual stocks. Now add tools that
show the bigger picture. Tell Claude Code:

```
I want to add new tools to my server.py for a daily report.
Please add:

1. get_market_overview - Shows how the major market indices are doing
   today (SPY for the S&P 500, QQQ for Nasdaq). Include daily change %
   and a simple label: "good day" if SPY is up, "rough day" if SPY is
   down more than 1%, "meh" otherwise.

2. get_sector_check - Shows how different parts of the economy are
   doing today (Technology via XLK, Energy via XLE, Healthcare via XLV,
   Finance via XLF, Consumer via XLY). Sort from best to worst. Flag
   any sector that's up or down more than 1.5%.

3. get_watchlist_movers - Returns my watchlist stocks sorted by today's
   performance. For each stock, include which sector it's in, whether
   it's doing better or worse than its sector, and a "notable" field if
   something unusual is happening (big move or high volume).

Pre-compute everything. The AI should never need to do math.
Every tool returns a dict with data_source and as_of fields.
```

Test each new tool:
```
Can you run the MCP inspector so I can test these new tools?
```

## Step 3: Add the Pre-Formatted Report Tool (7 min)

This is the big guardrail: a tool where the code builds part of the
report with exact numbers, so the AI can't accidentally change them.

```
Add a tool called get_report_formatted that:

1. Calls the other tools internally to gather data
2. Builds a pre-formatted markdown section with exact numbers:
   - A table of each stock with price and daily change %
   - The market status (good day / rough day / meh)
   - Any notable movers or unusual activity
3. Returns this formatted markdown in a field called "formatted_section"
4. Also returns a field called "present_verbatim" set to true
5. Also returns a field called "ai_notes" with a plain English summary
   of the interesting stuff the AI should talk about

The formatted section has exact numbers that the AI should present
as-is. The ai_notes give the AI permission to add commentary — but
it should never change the numbers in the formatted section.
```

## Step 4: Update the Guide Tool (3 min)

```
Update the get_strategy_guide tool to include all the new tools. Add a
recommended flow for a daily report:

1. get_market_overview - see how the overall market is doing
2. get_sector_check - see which industries are up and down
3. get_watchlist_movers - how my stocks are doing in context
4. get_report_formatted - get the pre-built summary

Also add these rules:
- "When get_report_formatted returns present_verbatim=true, present
  the formatted_section exactly as returned. Do not round or change
  any numbers in it."
- "Never calculate averages or totals from raw numbers. Always use
  pre-computed values from tool returns."
```

## Step 5: Test the Report in Claude Desktop (6 min)

Restart Claude Desktop if needed, then try:

```
Give me my morning report.
```

Check the output:
- Does it include the pre-formatted section with exact numbers?
- Does it connect the dots? (e.g., "Snapchat is down but so is its
  whole sector, so it's not just a SNAP problem")
- Does it mention the overall market status?

Try this tricky prompt:
```
What's my average return across all my stocks today?
```

If the AI tries to calculate the average by adding up individual
returns (which would be wrong), that's a guardrail gap. Tell Claude Code:

```
The AI is trying to calculate the average return by adding up individual
stock returns, which is wrong. Can you add a "watchlist_avg_return_pct"
field to get_watchlist_movers that correctly computes the average?
That way the AI uses the pre-computed number instead of doing bad math.
```

## Step 6: Add a Stale Data Warning (5 min)

```
Add stale data handling to all tools. If the stock market is closed
(weekend, holiday, or after 4 PM ET), every tool should include a field
called "stale_data_warning" with a message like "Market closed. Prices
are from the most recent trading day." If the market is open, set this
field to null.

Also update the guide tool: add a rule that says "If any tool returns a
stale_data_warning, mention it at the start of your response so the
user knows the data isn't live."
```

Test by running the report outside market hours (evening or weekend).

---

## What You Learned

- The **pre-formatted section** pattern: code builds tables with exact
  numbers, the AI presents them as-is
- The **stale data warning** pattern: tools tell the AI when data is old
- The **no-compute rule**: the AI should never do math — everything is
  pre-calculated
- How to **cross-reference** data (connecting stock moves to sector
  trends)
- How to **find and fix guardrail gaps** (AI doing math it shouldn't)

## If You Get Stuck

- "The new tool is crashing" — Paste the error to Claude Code
- "The report looks weird in Claude Desktop" — Ask Claude Code to
  adjust the formatting of the `formatted_section`
- "The AI is ignoring my pre-formatted section" — Make sure the guide
  tool mentions the `present_verbatim` rule
