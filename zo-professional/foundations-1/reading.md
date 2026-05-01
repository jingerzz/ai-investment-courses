# Foundations 1: Zo as an AI Operating Environment

## F1.1 What Changes When the AI Gets a Computer

A regular AI chat works like this: you type, the model writes back, the conversation ends. Whatever you and the AI discussed lives only in the chat history. If you log out and come back tomorrow, you are starting from scratch.

That is fine for a quick question. It is a poor fit for investment work, where you usually want a durable record, exact numbers, and the ability to keep working on something across days or weeks.

When you give the AI a computer, the shape of the work changes. You can ask the AI to:

- save a research note to a folder you can re-open later
- run a script that pulls today's prices and reports them exactly
- read a 10-K filing that lives on disk and quote a specific section
- post a chart to a hosted page anyone on your team can visit
- schedule a job that runs every Friday at 5 PM whether you are at your desk or not

None of these are possible from a chat-only AI app. They become possible the moment the AI has files, a terminal, and a place to host things. That is what Zo Computer provides.

> **You do not need to memorize this module.** The point of Foundations 1 is to install a mental model. The hands-on work in later weeks is what makes the model concrete.

## F1.2 The Four Layers

Zo is easier to think about if you split it into four layers. Every workflow you will build sits across all four.

| Layer | What It Holds | Investment Examples |
| --- | --- | --- |
| **Files** | Markdown notes, scripts, data, anything text or binary | Research memos, watchlists, strategy docs, filings on disk |
| **Tools** | Scripts, MCP servers, internal APIs that compute things | SPY/TLT signal calculator, SEC filing search, valuation script |
| **Surfaces** | Hosted pages, dashboards, public or private | Regime dashboard, research note, internal tool page |
| **Agents** | Scheduled or event-driven jobs | Post-close brief at 4:30 PM, filing monitor every morning |

The AI sits across all four. It can read files, call tools, edit code, publish pages, and (when you allow it) schedule future work.

A useful exercise: pick any investment task you do today and decide which layer each piece of the work belongs in. The answer is usually obvious once you ask.

For example, "evaluate a new long idea":

- **Files** — prior research notes, the company's recent filings, a watchlist
- **Tools** — a script that pulls fundamentals; a filing-search tool; a regime tool for context
- **Surfaces** — a one-page summary you can share with a colleague
- **Agents** — a scheduled job that re-checks the company every quarter and flags drift

Most workflows do not start with all four layers. They grow into them. The point of the layered model is to know what to add when.

## F1.3 Why This Matters in Finance

Investment work is rarely a single prompt. It is a chain of steps:

1. Pull data
2. Clean it
3. Compute the metric or signal you actually care about
4. Pull source documents (filings, transcripts, research)
5. Reason about the context
6. Produce an output (memo, recommendation, chart)
7. Review it
8. Decide
9. Archive the trail

If that whole chain lives only in a chat window, every step is fragile. The data may be stale, the math may be wrong, the citation may be invented, and the next time you want to repeat it you are doing the whole thing by hand again.

If the chain lives on a computer you control, each step is inspectable. You can rerun the script and check the output. You can open the filing and verify the quote. You can compare today's run to last week's. You can let an agent repeat the boring parts.

The chat-only version of an investment workflow is a demo. The computer-based version is a system.

## F1.4 The Guardrail Pattern

The most important pattern in the course is one short rule:

> **AI should explain and orchestrate. Code should compute. Sources should substantiate. Humans should decide.**

Each part is doing a different job, and confusing them is where investment AI projects fail.

Here is what each part means in practice:

**AI should explain and orchestrate.** The model is good at reading a tool's output, putting it into plain English, and choosing which tool to call next. That is genuine value. Use it for that.

**Code should compute.** Anything that has to be exact — a price, a moving average, a position size, a Sharpe ratio — should come from a script, not a model. Models hallucinate numbers. Scripts do not.

**Sources should substantiate.** Anything quoted from a filing or a research document should come from the document itself, not from the model's memory. The model can find the right section; the section is the source of truth.

**Humans should decide.** Capital allocation decisions belong to people. The AI's job is to surface what matters, not to act.

Here is a side-by-side example:

| Bad Pattern | Good Pattern |
| --- | --- |
| "What is SPY trading at?" → AI guesses from memory | "What is SPY trading at?" → AI calls a quote tool that returns today's price |
| "What does Apple's 10-K say about supply concentration?" → AI paraphrases from training | "What does Apple's 10-K say about supply concentration?" → AI retrieves the section, quotes it, cites the document and node |
| "Should I buy this?" → AI says "yes/no" | "Should I buy this?" → AI summarizes the levels, the regime, the recent filing tone, and the key risks; human decides |

If you can identify the bad pattern in any of your existing AI use, you have already learned the most important thing in this module.

## F1.5 What Good Looks Like

A useful AI investment workflow should pass each of these checks:

- **Grounded in real data.** Every number traces back to a source you can open.
- **Easy to re-run.** Running it tomorrow with the same inputs produces the same output.
- **Explicit about stale inputs.** If the data is from yesterday, the output says so.
- **Clear about sources.** Every claim about a filing has a citation.
- **Narrow enough to audit.** A reviewer can read the output and the inputs in under five minutes.
- **Designed for human approval.** Capital is never put at risk without an explicit human "go".
- **Carries context across sessions.** The AI knows what was decided last week without you re-explaining. (Foundations 3 covers the memory layer that enables this.)

You will be applying this checklist throughout the course. By Week 4, you should be able to look at any AI investment workflow — yours or someone else's — and say where it passes and where it fails.

## F1.6 Common Failure Modes

It helps to know the specific ways things go wrong, because they happen often enough to have names.

**The "AI knows everything" trap.** A user assumes the model has live data because it answers fluently. The model does not. It is reciting from training that ended months ago. Symptom: a confident-sounding answer with a wrong number.

**The blurred tool boundary.** The model is asked to "calculate" something. It produces a plausible number that was not actually calculated. Symptom: numbers that almost match a script's output but not quite.

**The phantom citation.** The model "quotes" a filing from memory. The wording is plausible but not in the filing. Symptom: a sentence with quote marks that does not appear in the source document.

**The silent stale read.** A tool runs against a stale data file and the output looks identical to a fresh run. Symptom: a regime call that contradicts what you can see on a chart.

**The runaway agent.** A scheduled job has a small bug, and it sends the wrong message every weekday at 4:30 PM for two weeks before anyone notices. Symptom: an alert that everyone learns to ignore.

The good news: every one of these has a known fix. The course walks through each fix in the relevant module.

## Key Takeaways

- **Zo gives the AI a computer.** Files, tools, hosted pages, scheduled jobs. The chat is just one of many surfaces.
- **Think in four layers.** Files, tools, surfaces, agents. Every workflow uses all four eventually.
- **Investment work is a chain.** The longer the chain, the more important it is that each link is inspectable.
- **The guardrail pattern is the whole course.** AI explains, code computes, sources substantiate, humans decide.
- **Good workflows are boring.** Reproducible, cited, narrow, auditable, human-approved. The boring version is the durable one.

## Zo Documentation

The four layers discussed in this module map directly to Zo's core features. For reference:

- [Introduction to Zo](https://docs.zocomputer.com/intro) — what Zo Computer is and how it works
- [Files](https://docs.zocomputer.com/files) — managing files on your Zo Computer
- [Tools](https://docs.zocomputer.com/tools) — how tools work and what's available
- [Sites](https://docs.zocomputer.com/sites) — hosting pages and dashboards
- [Automations](https://docs.zocomputer.com/automations) — scheduling jobs and event-driven workflows
