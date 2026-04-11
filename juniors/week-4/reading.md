# Week 4: AI That Watches and Alerts You

## 4.1 From Questions to Monitoring

In Weeks 1-3, you built tools that Claude uses when *you* ask a
question. You ask "How is Apple doing?", Claude calls your tool, and
you get an answer. The AI waits for you.

This week, we flip it around. You'll build AI that **proactively
watches** your stocks and tells you when something important happens —
without you having to ask.

Think of it like a smoke detector. You don't check your smoke detector
every five minutes. It watches quietly, and when something's wrong,
it alerts you. Your stock monitor works the same way.

### The Progression

Here's how AI involvement grows:

```
Level 0 — Manual:    You check stocks yourself
Level 1 — Ask AI:    You ask Claude, Claude looks it up
Level 2 — AI watches: Claude monitors automatically, alerts you
Level 3 — AI suggests: Claude monitors AND recommends what to do
Level 4 — AI acts:    Claude makes decisions on its own (BAD idea!)
```

This week you'll build Level 2-3: AI that watches and suggests, but
**never acts on its own.** Level 4 is dangerous for investing and you
should never build it.

---

## 4.2 Why AI Should Never Trade By Itself

This is the most important lesson in the whole course. Here are three
reasons why AI should always ask a human before doing anything with
real money:

**Reason 1: AI makes confident mistakes.**

Remember the five failure modes from Foundations 1? They all apply here,
but with higher stakes. AI doesn't say "I'm not sure about this." When
it's wrong, it's wrong with the same confidence as when it's right. If
an AI monitoring system misreads a normal price dip as a crash and sells
everything, you've lost money on a mistake the AI was totally confident
about. A hallucinated reasoning chain --- like "Since Apple just lost a
major lawsuit..." (when no lawsuit happened) --- could trigger a sell
recommendation that sounds perfectly logical but is based on nothing real.

**Reason 2: AI can't understand context.**

Maybe Apple's stock dropped 5% because of a temporary news story that
doesn't actually matter. A human investor knows to wait it out. An
autonomous AI might panic-sell. Context, judgment, and experience are
things AI doesn't have.

**Reason 3: Building trust takes time.**

You wouldn't give a brand-new employee full control of your bank
account on day one. Same with AI. Start by having it alert you. If
the alerts are consistently good over weeks and months, you can
gradually give it more responsibility — but never full control.

---

## 4.3 The Monitor: How It Works

Your monitoring script follows a simple pattern:

```
1. CHECK    Look at each stock (price, volume, position size)
2. CLASSIFY Is this normal, noteworthy, or urgent?
3. LOG      Write down what was found (even if nothing happened)
4. ALERT    If something important, notify the user
```

### Classification Levels

Every finding gets classified:

| Level | Meaning | Example |
|-------|---------|---------|
| **SILENT** | Normal, just log it | Stock moved 0.5% — nothing unusual |
| **ALERT** | Worth knowing about | Stock moved 4% or volume is 2x normal |
| **URGENT** | Needs attention now | Stock crashed 8% or broke a limit |
| **BLOCKED** | Never automated | Actually buying or selling stocks |

**BLOCKED is permanent.** No matter how smart your AI gets, no matter
how much you trust it — buying and selling stocks should always require
a human decision. This isn't training wheels. This is a permanent rule.

---

## 4.4 The Audit Trail: Logging Everything

An **audit trail** is a complete record of everything the monitor does.
Every check, every alert, every "all clear" — it's all written down
with timestamps.

Why log everything, even boring routine checks?

1. **You can review what happened while you were away.** "What did the
   monitor see while I was at school?" The log tells you.

2. **You can spot patterns.** "Tesla has triggered alerts 3 times this
   week" is more useful than seeing each alert individually.

3. **You have proof.** If something goes wrong, the log shows exactly
   what the monitor saw and what it recommended.

4. **You can improve.** Looking back at old alerts helps you adjust
   thresholds. Too many false alarms? Make the threshold higher. Missing
   important moves? Make it lower.

Each log entry includes:
- **When** — timestamp
- **What** — which stock, which check
- **Result** — what was found
- **Classification** — SILENT, ALERT, or URGENT
- **Suggestion** — what you might want to do

---

## 4.5 Rules and Thresholds

Your monitor needs clear rules. Here are some examples:

```
"If a stock moves more than 3% in one day → ALERT"
"If a stock moves more than 5% in one day → URGENT"
"If one stock is more than 25% of your portfolio → ALERT"
"If trading volume is more than 2x normal → ALERT"
"If I want to actually buy or sell a stock → BLOCKED (always manual)"
```

These rules should be visible and adjustable. Don't bury them deep in
code where you can't find them. Put them at the top of your script
where you (or Claude Code) can easily change the numbers.

**Start loose, tighten later.** It's better to get too many alerts at
first (and dial back the ones that are noise) than to miss something
important because your thresholds were too strict.

---

## 4.6 Connecting It All Together

Here's the complete picture of what you've built over four weeks:

```
Week 1: Stock data tools
    ↓
Week 2: Daily report with safety checks
    ↓
Week 3: Multiple servers, organized by topic
    ↓
Week 4: Monitor that watches and alerts (THIS WEEK)
    ↓
Claude Desktop sees everything and connects it all
```

When you ask Claude Desktop "Any alerts?", it reads your monitor log.
When you ask "Give me the full picture", it combines the monitor
alerts with your stock data and daily report tools. The AI connects
everything into one coherent answer.

---

## Key Takeaways

1. **Monitoring flips the model** — AI watches proactively instead of
   waiting for your questions
2. **AI should NEVER trade by itself** — Level 4 autonomy is dangerous
   for investing. Always keep a human in the loop.
3. **Four classification levels** — SILENT (log only), ALERT (tell me),
   URGENT (tell me now), BLOCKED (never automate)
4. **Log everything** — the audit trail is a complete record of what
   the monitor saw and recommended
5. **Start loose** — set thresholds that catch too much, then tighten
   over time
6. **BLOCKED is permanent** — buying/selling stocks always requires a
   human decision, no matter how much you trust the AI
