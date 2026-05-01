# Introduction: Your Investment AI Needs a Home

Most demonstrations of AI in investing happen inside a chat window. You type a question, the model writes a paragraph, you read it, the conversation ends.

That is fine for playing around. It is not enough for actual investment work.

Real investment workflows need a place to keep things: data files, research notes, scripts that crunch numbers, scheduled jobs that run after market close, a hosted dashboard a teammate can open, and a record of what was done and why. They also need a place where those pieces keep running after a conversation ends, with the same files and tools available the next time you log in.

That is the premise of this course. **Zo Computer is the home for your investment AI.**

If you are new to Zo, the simplest description is this: it is a personal cloud computer that you can talk to in plain English. You can also open files, run scripts, host pages, and schedule jobs on it. The AI lives inside that environment, so when you ask it to do something, it has files, tools, and services it can actually use — not just words it can generate.

## Why a Chat Window Is Not Enough

To see why the home matters, picture two analysts.

The first analyst is brilliant but lives in a soundproof room. You can pass notes under the door, and they pass thoughtful answers back. They know finance deeply and can reason about almost anything. But they cannot pull up a Bloomberg page, open a 10-K, run a backtest, or check yesterday's close. Whatever they tell you about a specific number or recent event, they are guessing — politely, but guessing.

The second analyst sits at a desk in your office. They have a laptop, market data, your firm's research folder, a terminal, a set of internal tools, and a printer. When you ask "what does the latest 10-K say about insider transactions?", they pull up the filing, find the section, and quote it back with a page reference. When you ask "where is SPY trading relative to its 200-day moving average?", they run a script that calculates it.

The first analyst is what you get from a plain chat. The second is what you get from an AI with a computer.

This course is about giving your AI the second job.

## What This Course Is Not

This course is not about asking a model to pick stocks, predict prices, or generate trades. Models are bad at all three of those things, and pretending otherwise is how investment AI projects fail.

It is about building a controlled system where an AI can:

- call code that returns exact, reproducible numbers
- read primary-source filings instead of guessing what they say
- explain the result in plain language a colleague can use
- run on a schedule, leaving an audit trail behind
- notify you when something matters enough to look at

The goal is not autonomy for its own sake. It is leverage with control. **AI proposes, code computes, sources substantiate, humans decide.** That sentence is the most important idea in the course. You will see it again.

## How the Course Is Structured

The course has seven modules. Three foundations modules build the mental model. Four weekly modules walk through real investment workflows.

| Module | What You Build | Pattern |
| --- | --- | --- |
| Foundations 1 | A mental model for Zo as the home | Files + tools + surfaces + scheduled jobs |
| Foundations 2 | A clean workspace setup | Folders, secrets, channels, hosting |
| Foundations 3 | Persistent context for investment AI | Memory files, USER.md, AGENTS.md, session continuity |
| Week 1 | A market-context tool | AI calls a script that classifies the day |
| Week 2 | A SEC filing reader | AI answers from indexed filings, with citations |
| Week 3 | A multi-piece workflow | Several small tools coordinating one job |
| Week 4 | A scheduled, controlled agent | Runs without you, leaves a record, asks before acting |

Every module follows the same five-step pattern:

1. **Learn the concept.** Read the short reading.
2. **Use it on Zo.** Run the exercise. The first time through, you should not have to write code.
3. **Inspect the output.** Read what the tool actually returned.
4. **Identify the guardrail.** What stops the AI from making something up here?
5. **Decide what a professional version would require.** What would need to change before you trust this with real capital?

Each module is roughly 30 minutes of reading and 30 minutes of hands-on. You can move faster or slower; the structure is here to help, not pressure you.

## Where This Course Fits

This is the **Zo-centric track** of the AI Investment Academy. There is also a Claude-centric track, which teaches the same patterns by writing code from scratch with Claude Desktop and Claude Code. The two tracks are siblings.

- Pick this track if you want to lean on a managed environment and learn to think in workflows, files, and services. You will still see code, but the focus is on architecture and judgment.
- Pick the Claude-centric track if you prefer to write the code yourself and want a deeper look at the internals.

Both tracks teach the same core philosophy. Many students do both.

## A Note on Jargon

You will see terms like *MCP*, *RAG*, *deterministic tool*, *regime*, and *audit trail* throughout the course. We define each of them on first use, and the glossary at the end has plain-English entries for everything. If a sentence reads like alphabet soup, the next paragraph almost always unpacks it. You are not missing anything; we are just trying to be precise.

## The Permanent Pattern

Every module reinforces one design pattern. It is worth memorizing now:

> **AI proposes. Code computes. Sources substantiate. Humans decide.**

Everything else — the folder structure, the tool design, the audit trail, the scheduled agent — is in service of that sentence. By the end of the course, you should be able to explain why each piece of the pattern is there, and what goes wrong when one of them is missing.

Let's get started.
