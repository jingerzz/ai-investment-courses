# Week 3: Designing a Multi-Tool Investment Workflow

## 3.1 Where the Course Has Taken You So Far

By Week 3, you have used two separate tools:

- **Week 1: a market regime tool** — what kind of day is the market having?
- **Week 2: a SEC filing tool** — what does this company actually say in its own filings?

Each one answered one question well. Real investment work usually needs several tools answering several questions, all in the same workflow. This week is about putting tools together — how to design a workflow on Zo that uses more than one of them, without turning into a pile of glue.

You will not build the full system this week. You will design it on paper. The build comes in Week 4.

## 3.2 The Mistake to Avoid

There is a tempting bad pattern that almost everyone tries first: **the giant prompt**.

It looks like this:

> "Hey Zo, every morning, look at the market, check my watchlist, read the latest filings on each name, summarize what changed, send me a brief, and tell me what to buy."

This sounds productive. It is also a recipe for a workflow that is impossible to debug, impossible to trust, and quietly hallucinates half its inputs.

The reason is that **one big prompt mixes the parts that need to be exact with the parts that should be flexible**. Prices need to be exact. Filing quotes need to be exact. Whether to add to a position needs to be your call. Letting one prompt own all of it means a small mistake at any layer poisons the whole brief.

The fix is to break the workflow into layers, each with one job, and let each layer be the right tool for its job — code where it should be code, AI where it should be AI, you where it should be you.

## 3.3 The Layers of a Real Workflow

Most professional-grade investment workflows look like this:

| Layer | Job | Example |
| --- | --- | --- |
| **Data** | Fetch and store raw facts | Prices, fundamentals, filing texts |
| **Tools / Services** | Compute structured answers from data | Regime classification, filing search |
| **Workflow / Agent** | Run the tools in a sequence on a schedule | "After close: refresh data, run regime, check watchlist filings" |
| **Surface** | Show the result to a human | Dashboard page, Telegram message, email brief |
| **Decision** | The human decides what to do | You |

You will hear different names for these layers — "ETL", "service layer", "orchestrator", "UI", "decision-maker." The names matter less than the **separation**. Each layer has one job. The boundaries between layers are where you write your guardrails.

Zo gives you a different deployment surface for each layer:

- **Data** lives in workspace files, datasets, and external sources (yfinance, EDGAR, etc.)
- **Tools / Services** are MCP servers (like the SPY/TLT and PageIndex servers from Weeks 1–2)
- **Workflow / Agent** is a scheduled Zo agent
- **Surface** is a Zo Space page, a Telegram message, or an email
- **Decision** is you, in chat or on your phone

You do not need to use all of them for every workflow. But you should know which layer you are working in at any given moment.

## 3.4 The Architecture Question

Before you build anything, sit down and answer six questions about the workflow you want. These are the questions that, if you skip them, will bite you later:

1. **What decision does this workflow support?** "I want to know whether to add to my SPY position tomorrow." Specific. A workflow with no decision is not a workflow; it is noise.
2. **What inputs must be exact?** Prices, dates, filing quotes, position sizes. Anything where a wrong number changes the decision. These get a tool, not a prompt.
3. **What can be summarized?** Market commentary, qualitative analysis, briefing language. These can be AI prose.
4. **What runs on a schedule, and what runs on demand?** A daily post-close brief is scheduled. An ad-hoc filing question is on-demand.
5. **What needs human approval?** Anything that sends a message externally, publishes publicly, places a trade, or changes a strategy rule. Default to "needs approval."
6. **Public or private?** Personal portfolio data is private. A market regime dashboard might be public. Decide before you build, not after.

These six questions are the spec. When you write your design doc this week, answering them is most of the work.

## 3.5 A Worked Example: Post-Close Market Brief

To make this concrete, here is what a real post-close market brief workflow looks like, using the layers above:

**Decision supported:** "Do I need to adjust my SPY/TLT exposure tomorrow morning?"

**Data layer:**
- yfinance for SPY, TLT, QQQ prices
- A workspace file with my current positions

**Tools layer:**
- The SPY/TLT regime server (Week 1) — `get_current_signal`, `refresh_data`
- A small custom tool that reads my positions file

**Workflow layer:**
- A Zo agent scheduled at 4:30 PM ET on weekdays
- It calls `refresh_data`, then `get_current_signal`, then the positions tool
- It composes a 5-line brief

**Surface layer:**
- A Telegram message to me
- A copy saved to `Records/post-close-briefs/YYYY-MM-DD.md`

**Decision layer:**
- I read the Telegram brief on my phone and decide whether to act

**Approval points:**
- The agent never trades
- The agent never publishes anywhere except my private channel and my workspace
- If `stale_data_warning` is non-null, the agent flags it and stops

That is six questions answered, five layers wired up, and a clear stopping point for the agent. When the AI is helping you design your own workflow, you should be able to fill in the same outline.

## 3.6 Failure Modes (Week 3 Edition)

These bite when you skip the design step and just start prompting.

**Scope creep.** "While we're at it, let me also have it score my watchlist and draft an outreach email." Now the workflow has three decisions, not one. Cut it back to one decision per workflow.

**Schedule overlap.** Two agents both run at 4:30 PM and both refresh data. They race and one fails silently. Fix: one agent owns each piece of shared state.

**Missing approval gate.** The agent sends a message externally without asking. Fix: anything that leaves Zo's walls is approval-required by default.

**Sneaky AI inputs.** A "tool" turns out to be a prompt that asks the AI to compute a number. The number is then used as if it were data. Fix: tools that compute numbers must be code, not prompts.

**No audit trail.** The agent ran, sent a brief, and there is no record of what it saw. Fix: every run writes a record to the workspace before sending anything externally.

## Key Takeaways

- **The giant prompt is a trap.** Break the workflow into layers, each with one job.
- **Five layers: data, tools, workflow, surface, decision.** Each maps to a Zo deployment surface.
- **Six design questions. Answer them on paper before you build.** Decision, exact inputs, summarizable inputs, schedule, approval, public-vs-private.
- **One workflow supports one decision.** If a second decision sneaks in, that is a second workflow.
- **The audit trail is part of the design, not an add-on.** Every run leaves a record.
