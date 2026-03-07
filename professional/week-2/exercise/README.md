# Week 2 Exercise: Build a Morning Briefing with Guardrails

## What You'll Build

You'll expand your Week 1 server with new tools and create a morning briefing
workflow. When you're done, you'll be able to ask Claude Desktop:

- "Give me my morning briefing"
- "What should I be paying attention to today?"

...and get a structured, cross-referenced analysis using real data — with
guardrails that prevent the AI from making things up.

## Time: 30 minutes

## What You Need

- Your working MCP server from Week 1
- Claude Code and Claude Desktop

---

## Step 1: Open Your Project in Claude Code (1 min)

```bash
cd ~/ai-finance-tools
claude
```

## Step 2: Add Market Context Tools (8 min)

Your Week 1 server knows about individual stocks. Now add tools that provide
broader market context. Tell Claude Code:

```
I want to add new tools to my server.py to support a morning briefing.
Please add:

1. get_market_overview - Returns how the major indices are doing today
   (SPY, QQQ, DIA, IWM). Include daily change %, whether each is above
   or below its 50-day moving average, and a simple regime label:
   "risk-on" if SPY is up and above 50-day SMA, "risk-off" if SPY is
   down and below 50-day SMA, "mixed" otherwise.

2. get_sector_heatmap - Returns performance of the 11 S&P sectors today
   (use the sector ETFs: XLK, XLF, XLE, XLV, etc). Sort from best to
   worst. Flag any sector up or down more than 1.5%.

3. get_watchlist_movers - Returns my watchlist stocks sorted by today's
   performance. For each stock, include daily return %, whether it's
   outperforming or underperforming its sector, and a "notable" field
   if anything unusual is happening (big move, unusual volume).

Pre-compute everything. The AI should never need to do math.
Every tool returns a dict with data_source and as_of fields.
```

Test each new tool in the MCP inspector:
```
Can you run the MCP inspector so I can test these new tools?
```

## Step 3: Add a Pre-Formatted Briefing Tool (7 min)

This is the key guardrail concept: Python builds part of the briefing with
exact numbers, so the AI can't accidentally change them.

```
Add a tool called get_briefing_formatted that:

1. Calls the other tools internally to gather data
2. Builds a pre-formatted markdown section with exact numbers:
   - Portfolio summary table (each stock, price, daily change %)
   - Market regime status
   - Any notable movers or unusual activity
3. Returns this formatted markdown in a field called "formatted_section"
4. Also returns a field called "present_verbatim" set to true
5. Also returns a field called "ai_interpretation_notes" with a plain
   English summary of the key points the AI should elaborate on

The idea is: the formatted section has exact numbers that the AI presents
as-is. The interpretation notes give the AI permission to add context and
cross-reference — but it should never restate the numbers in different
words where it might round or miscalculate.
```

## Step 4: Update the Guide Tool (3 min)

```
Update the get_strategy_guide tool to include all the new tools. Add a
recommended flow for a morning briefing:

1. get_market_overview - understand the macro environment
2. get_sector_heatmap - see where money is flowing
3. get_watchlist_movers - how my stocks are doing in context
4. get_briefing_formatted - get the pre-built summary section

Also add a rule in the guide: "When get_briefing_formatted returns
present_verbatim=true, present the formatted_section exactly as returned.
Do not reformat, round, or recalculate any numbers in it."
```

## Step 5: Test the Briefing in Claude Desktop (6 min)

Restart Claude Desktop if needed (after any config changes), then try:

```
Give me my morning briefing.
```

Check the output:
- Does it include the pre-formatted section with exact numbers?
- Does it cross-reference data? (e.g., "XOM is your worst performer,
  and Energy is today's weakest sector — that's consistent")
- Does it mention the market regime and connect it to your stocks?

Try intentionally tricky prompts:
```
What's my portfolio's total return today?
```

If the AI calculates a total by adding up individual returns (which is
wrong — you can't just add percentages), that's a guardrail gap. Tell
Claude Code:

```
The AI is trying to calculate total portfolio return by adding up
individual stock returns, which is wrong. Can you add a
"watchlist_avg_daily_return" field to get_watchlist_movers that
correctly computes the average daily return? That way the AI uses
the pre-computed number instead of doing bad math.
```

## Step 6: Add a Stale Data Warning (5 min)

```
Add stale data handling to all tools. If the market is closed (weekend,
holiday, or after hours), every tool should include a field called
"stale_data_warning" with a message like "Market closed. Prices are from
the most recent trading session (2026-03-15)." If the market is open,
set this field to null.

Also update the guide tool: add a rule that says "If any tool returns a
stale_data_warning, display it prominently at the top of your response."
```

Test this by running the briefing outside market hours.

---

## What You Learned

- How to add tools to an existing MCP server by describing them to Claude Code
- The **pre-formatted template** pattern: Python builds sections with exact
  numbers, the AI presents them verbatim
- The **stale data warning** pattern: tools tell the AI when data isn't fresh
- How to **cross-reference** data across tools (market regime + sector + stock)
- How to **iterate** when you find a guardrail gap (AI doing bad math)

## If You Get Stuck

- "The new tool is crashing" → Paste the error to Claude Code
- "The briefing looks weird in Claude Desktop" → Ask Claude Code to adjust
  the formatting of the `formatted_section`
- "The AI is ignoring my pre-formatted section" → Make sure the guide tool
  mentions the `present_verbatim` rule
