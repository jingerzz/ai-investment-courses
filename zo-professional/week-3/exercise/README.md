# Exercise: Design Your Own Investment Workflow

## Goal

By the end of this exercise, you will have a one-page design doc for a real investment workflow you actually want — not a hypothetical one. The doc will name the decision the workflow supports, the data it needs, the tools that compute the answers, the schedule, the human approval points, and the failure modes you already know about.

You will not build it this week. You will design it. The build comes in Week 4.

Time: about 60 minutes if you pick a workflow you have already been thinking about. Longer if you stop to look up tools.

## What You Will Use

- **A markdown file in your workspace** — `Documents/workflows/<workflow-name>.md` is a good place.
- **Zo chat** — to talk through the design and stress-test it.
- The two course servers from Weeks 1 and 2, as building blocks you can plug into the design.

## Steps

### 1. Pick one workflow

Choose ONE. Resist the urge to design two.

Good first choices:

- **Post-close market brief** — "Do I need to adjust exposure tomorrow?" (uses the SPY/TLT server)
- **Earnings prep monitor** — "What did this company say about [topic] in their last filing, before I listen to the call?" (uses the PageIndex server)
- **Watchlist regime check** — "Which of my watchlist names are setting up given today's market regime?" (uses both servers, plus a small positions file)
- **Activist short tracker** — "What new shorts have been published in the last 24 hours, and do any of them touch my book?"
- **Filing change detector** — "What changed in the most recent 10-K compared to the one before?"

Pick the one you'd actually use. The exercise is more useful when the workflow is real.

### 2. Open a fresh design doc

```text
Create a new markdown file at Documents/workflows/<my-workflow-name>.md
with this template, and leave the sections blank for me to fill in:

# Workflow: [name]

## Decision Supported

## Inputs (must be exact)

## Inputs (can be summarized)

## Tools / Services Used

## Schedule

## Approval Required For

## Surface (where the human sees the result)

## Audit Trail

## Failure Modes (at least three)

## Smallest Useful Version
```

You will fill it in with Zo's help in the next steps.

### 3. Define the decision

This is the most important step. If you can't write one specific decision in one sentence, the workflow isn't ready to design.

```text
I want to design a workflow that supports this decision: "[your one
sentence]." Push back if the decision is vague, multi-part, or implies
more than one workflow. Help me sharpen it.
```

A good sharpened decision looks like *"Should I add to my SPY position by 0.25x at tomorrow's open?"* or *"Is it worth me listening to the full earnings call tomorrow, or is the press release enough?"* — concrete, with a clear yes/no/how-much answer.

### 4. List the inputs, split by exactness

```text
For this workflow [paste decision], list every input the workflow
needs. For each input, mark it as either MUST BE EXACT (a number, a
date, a quoted filing passage) or CAN BE SUMMARIZED (commentary,
analysis, qualitative read).

The exact inputs need a tool. The summarizable inputs are where the AI
adds value.
```

Drop the result into your design doc.

### 5. Map inputs to tools

```text
For each MUST BE EXACT input above, name the specific tool or data
source that should produce it. If the SPY/TLT course server or the
PageIndex RAG course server can produce it, name the specific tool
call. If it needs a new tool, say so explicitly — we will not invent
tools that do not exist.
```

If the AI suggests a tool that doesn't exist on Zo yet, that is fine — note it as "to build." Just do not let the AI silently assume a tool exists.

### 6. Decide the schedule

```text
Should this workflow run on a schedule, on demand, or both? If on a
schedule, what is the natural time, and what is the consequence of
missing a run?
```

Most useful workflows are scheduled (daily post-close, daily pre-market, weekly Sunday review). On-demand workflows are usually research questions where you bring the question.

### 7. Lock down the approval points

```text
List every action this workflow could take. For each one, classify it
as one of: SILENT (no human review), LOGGED (writes to workspace,
no notification), ASK (sends a notification asking for approval), or
BLOCKED (the workflow is not allowed to do this at all).

Default external messages, public publishing, trades, and rule changes
to ASK or BLOCKED.
```

This becomes the agent's permission list when you build it in Week 4.

### 8. Pick the surface and the audit trail

```text
Where does the result land — Telegram, email, a Zo Space page,
a markdown file? And what record does every run leave in the
workspace, regardless of whether it sent anything?

A good audit trail answers: when did it run, what tools did it call,
what did it see, what did it recommend, what (if anything) did it
send.
```

The audit trail goes in your workspace, not the surface. Even if the agent doesn't notify you, every run writes a record.

### 9. Stress-test the design

```text
Review this draft workflow design [paste the markdown so far]. Identify
missing data sources, unsafe AI assumptions, unclear approval points,
and at least three failure modes I should design against now.
```

Add the failure modes the AI surfaces (plus any you already knew about) to the **Failure Modes** section of the doc.

### 10. Cut the scope to the smallest useful version

```text
This design is probably too big to build in a week. Cut it to the
smallest version that still supports the decision usefully. What gets
deferred to v2?
```

The smallest useful version is what you will build in Week 4. Defer everything else.

## Checkpoint

You are done when your design doc has:

- One clear decision in one sentence
- A list of exact inputs, each mapped to a specific tool
- A list of summarizable inputs (the AI's territory)
- A schedule, or "on-demand" with a reason
- An approval policy: silent, logged, ask, blocked — for every action
- A surface and an audit trail
- At least three named failure modes
- A "smallest useful version" you could build in a week

If any of those is hand-wavy, sit with the AI for another round. Vague designs become broken agents.

Save the doc. You will use it as the spec in Week 4.
