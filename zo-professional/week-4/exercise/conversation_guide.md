# Prompts: Week 4

These prompts go with the agent build exercise. Run them in Zo chat after your Week 3 design doc is done.

The prompts are grouped by phase: drafting the spec, stress-testing it, simulating the run, building the agent, and testing it. Do them in order — skipping the simulation step is how agents end up sending broken briefs at 4:30 AM.

## Draft the Spec

```text
Read my Week 3 design doc at Documents/workflows/<my-workflow-name>.md
and propose first-draft answers for each section of the agent spec
template. For sections the Week 3 doc does not cover (audit log
format, stop conditions, exact output template), ask me before
filling them in.
```

> The AI should ask clarifying questions on the parts the Week 3 doc was vague about. If it doesn't ask and just fills everything in, push back: *"You filled in stop conditions without asking. What did you assume?"*

```text
Show me the proposed Required Output as a literal example — what would
one Telegram message look like? Use realistic placeholder values, not
TBDs.
```

> Forces the AI to commit to a concrete output. Vague output specs ("a brief about the market") become bad briefs.

## Tighten the Scope

```text
Review this draft agent spec [paste markdown]. Tighten the scope.
Identify any unsafe permissions and rewrite the spec so the agent
observes, computes, and recommends — but does not make
capital-allocation decisions or send messages to anyone except me.
```

> The AI should propose specific tightenings: removing tools, adding stop conditions, changing approval defaults. Apply them.

```text
For each Allowed Tool, show me a one-line justification for why the
agent needs it. Drop any tool whose justification is weak.
```

> Tool list should be minimal. If the AI added something "in case it's useful," drop it.

## Stress-Test Against Failure Modes

```text
For each failure mode in this week's reading (runaway agent, silent
failure, stale brief, permission creep, mood-piece brief, forgotten
audit log), explain how this spec defends against it. If it does not
defend against one, propose a single-line fix and add it to Stop
Conditions or Required Output.
```

> Treat this as a checklist. Every failure mode either has a defense or gets a fix added now.

```text
Classify every action this agent could take as one of: SILENT,
LOGGED, ASK, or BLOCKED. Justify each non-BLOCKED action in one
sentence.
```

> Same approval-policy classification from Week 3, applied to the actual agent. Every SILENT action needs a real defense.

## Simulate One Run

```text
Pretend it is exactly the agent's scheduled time right now. Walk
through one run: call the tools in the order specified, show me each
tool output, compose the brief, and show me the audit log entry you
would write. Do NOT actually send anything — just show me what would
be sent.
```

> The most important prompt of the week. Read the simulated brief carefully — that is what you will get on your phone every day.

```text
The simulated brief was [too long / too vague / missing X]. Rewrite
the Required Output section of the spec to fix it, and re-simulate.
```

> Iterate. The simulation is cheap; the live agent is not.

```text
Now simulate a run on a day where one of the stop conditions is
triggered (stale data, tool failure, missing input). Show me what the
agent does — what it writes to the audit log, what (if anything) it
sends.
```

> Confirms the abort path works on paper. If the simulated abort still sends a brief, the stop conditions are wrong.

## Create the Agent

```text
Create a Zo agent from this spec [paste final spec]. Use the schedule,
allowed tools, and output format exactly as written. Wire the brief
to my Telegram (or email) and the audit log to
Records/<agent-name>/YYYY-MM-DD.md. Confirm the agent ID and the next
scheduled run time.
```

> Save the agent ID. You will use it to edit, pause, or delete the agent later.

## Test the Live Agent

```text
Run the [agent name] agent manually right now. Show me the audit log
entry it wrote and the message that was sent.
```

> Live test on a real run. Compare what you got to what the simulation produced.

```text
Force a stop condition for the [agent name] agent. Run it manually
and confirm: no brief was sent, and the audit log explains why.
```

> The other most important prompt of the week. If the agent ignores stop conditions, you cannot run it on schedule.

```text
Restore the agent to its normal config. Show me its current settings:
schedule, allowed tools, output, approval policy, audit log path. And
the next scheduled run time.
```

> Last check before letting it run on its own. Do this before going to bed the first night.

## After the First Live Run

```text
Read the audit log entries for the agent's last [N] scheduled runs.
For each one, summarize: did it send a brief, did it abort, were there
any errors. Anything I should change in the spec.
```

> Use this every few days for the first week. Most agent bugs surface in the first 5–10 runs, then the agent stabilizes.

```text
Compare the last [N] briefs side by side. Are they consistently
useful, or are they becoming repetitive / empty / noisy? Suggest one
change to the Required Output that would make them more decision-
ready.
```

> Briefs that you stop reading are worse than briefs that don't get sent. Tune the output until you actually act on it.

## A Note on Pushback

If the AI ever proposes "we can skip the simulation, the spec looks fine," push back: *"No simulation, no schedule. Walk through one run end-to-end first."* The cost of one extra simulation is minutes; the cost of one bad scheduled run can be a day of cleanup.
