# Prompts: Week 3

These prompts go with the workflow design exercise. Run them in Zo chat. A general-purpose model is fine.

The goal is to fill out the design doc one section at a time. Keep the doc open in another tab and paste each AI answer in as you go.

## Sharpen the Decision

```text
I want to design a workflow that supports this decision: "[your one
sentence]." Push back if the decision is vague, multi-part, or implies
more than one workflow. Help me sharpen it into a single concrete
yes/no/how-much question.
```

> A good push-back from the AI is "this implies two decisions, which one are you actually trying to support?" If the AI nods along to a vague decision, prompt it harder.

```text
Rewrite the decision so the answer would be one of: yes, no, a
specific dollar/share/percentage figure, or "not enough information."
No "maybe consider exploring."
```

> Forces the decision into a shape that can actually drive an action.

## Split the Inputs

```text
For this decision [paste decision], list every input the workflow
needs. For each input, mark it as either MUST BE EXACT (a number,
date, price, quoted filing passage) or CAN BE SUMMARIZED (commentary,
qualitative read, analysis).
```

> Two columns. If the AI puts a price in the "summarized" column, push back — prices are exact.

```text
For each MUST BE EXACT input, name the specific tool or data source
that should produce it. If a course server can produce it, name the
exact tool call. If no tool exists yet, say "TO BUILD" — do not
invent tools.
```

> The "TO BUILD" line is honest and useful. A workflow with three "TO BUILD" tools is a longer project than you may want.

## Pick the Schedule

```text
Should this workflow run on a schedule, on demand, or both? If
scheduled, what is the natural time, and what happens if it misses
a run?
```

> "Run after market close" is more concrete than "run daily." Tie the schedule to a real event.

```text
Are there other workflows already running on this Zo at the same
time slot that might race for the same data? If so, list them.
```

> Surfaces shared-state issues before they bite. The AI may need to ask you to list current agents.

## Lock Down Approvals

```text
List every action this workflow could take — refresh data, write a
file, send a message, post to a public surface, place a trade, change
a rule. For each one, classify it as one of: SILENT, LOGGED, ASK, or
BLOCKED.
```

> The classifications become the agent's permission list. Default external messages and public publishing to ASK; default trades and rule changes to BLOCKED.

```text
For every action you marked SILENT or LOGGED, justify why a human
would not need to see it before it happens. If the justification is
weak, upgrade the action to ASK.
```

> Forces the AI to defend each "no human needed" call. A weak defense usually means the action belongs in ASK.

## Surface and Audit

```text
Where does the result land — Telegram, email, a Zo Space page, or a
markdown file? Pick one primary surface and at most one mirror.
```

> One primary surface keeps things simple. Mirrors are fine, but they should not be where you read first.

```text
Design the audit trail entry for one run. It should answer: when did
it run, which tools did it call, what did it see, what did it
recommend, what (if anything) did it send. Show me a YAML or markdown
template I can paste in.
```

> The audit entry is the workflow's memory. Make it easy enough to write that the agent will actually do it on every run.

## Stress-Test

```text
Review this draft design [paste full doc]. Identify missing data
sources, unsafe AI assumptions, unclear approval points, and at least
three failure modes I should design against now.
```

> The AI will often surface failure modes you would have learned the hard way after the agent is running. Take this seriously.

```text
For each failure mode you listed, propose a single line of guardrail
the agent should have to prevent it.
```

> Turns vague risks into concrete agent behavior. Drop the guardrails into the design doc as a checklist.

## Cut Scope

```text
This design is probably too big to build in a week. Cut it to the
smallest version that still supports the decision usefully. What gets
deferred to v2?
```

> The smallest useful version is the Week 4 build. Defer everything else.

```text
Rewrite the design as a build sequence: data file first, computed tool
second, scheduled agent third, surface fourth. For each step, name
the deliverable I should be able to test in isolation before moving on.
```

> Sequencing the build prevents the "I built the whole thing and nothing works" failure mode. Each step should produce something you can sanity-check.

## A Note on Pushback

If the AI ever skips the "MUST BE EXACT vs CAN BE SUMMARIZED" split and starts generating tool ideas, stop it: *"We need to classify the inputs first. Anything that must be exact gets a tool. Don't propose tools until we've split the inputs."* Discipline at this stage saves a lot of debugging in Week 4.
