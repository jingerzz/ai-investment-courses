# Exercise: Build and Run a Controlled Investment Agent

## Goal

By the end of this exercise, you will have a real Zo agent that runs on a schedule, calls a real tool from Weeks 1 or 2, writes a brief, sends it to a private channel, and leaves an audit log behind — with a written spec you read and approved before it ever fired.

You are turning the design from Week 3 into a running agent. This is the build week.

Time: about 90 minutes. Most of it is testing.

## What You Will Use

- **Your design doc** from Week 3 (`Documents/workflows/<workflow-name>.md`)
- **The course servers** from Weeks 1–2 (already registered)
- **Zo's agent system** — scheduled AI workflows
- **Telegram or email** as a private surface (Telegram is recommended — it's faster)

## Steps

### 1. Open the spec template

Create the agent spec next to your Week 3 design:

```text
Create a markdown file at Documents/workflows/<my-workflow-name>-agent.md
with this template, and leave the sections blank for me to fill in:

# Agent: [name]

## Purpose
(Pulled from the Week 3 design — one sentence.)

## Schedule
(When does it run? What happens if it misses a run?)

## Allowed Inputs
(What data sources is it allowed to read?)

## Allowed Tools
(What scripts, MCP tools, or services is it allowed to call? Be
explicit. "All tools" is not an answer.)

## Required Output
(What does a finished run produce — markdown file, Telegram message,
both? With what fields?)

## Approval Required For
(Default: any external message, public publish, trade.)

## Audit Log
(What does each run write to the workspace, regardless of whether it
sent a message?)

## Stop Conditions
(When does the agent abort the run? Stale data, tool failure, missing
input — name them all.)
```

### 2. Fill in the spec from the Week 3 design

```text
Read my Week 3 design doc at Documents/workflows/<my-workflow-name>.md
and propose first-draft answers for each section of the agent spec.
For sections that are not directly addressed in the Week 3 doc (audit
log format, stop conditions, exact output template), ask me before
filling them in.
```

You will end up with a draft spec. Read it back to yourself. The most common mistake at this step is a "Required Output" section that is too vague — tighten it until you could screenshot the output and act on it from your phone.

### 3. Tighten the scope

```text
Review this draft agent spec [paste the markdown]. Tighten the scope.
Identify any unsafe permissions and rewrite the spec so the agent
observes, computes, and recommends — but does not make
capital-allocation decisions or send messages to anyone except me.
```

The AI should suggest tightenings. Apply them.

### 4. Stress-test against failure modes

```text
For each failure mode listed in this week's reading (runaway agent,
silent failure, stale brief, permission creep, mood-piece brief,
forgotten audit log), explain how this spec defends against it. If it
does not defend against one, propose a single-line fix and add it to
Stop Conditions or Required Output.
```

Fold the fixes back into the spec. The spec should now be tight enough that you would feel comfortable having it run while you sleep.

### 5. Simulate one run by hand

Before creating the actual agent, walk through one run manually, in chat:

```text
Pretend it is exactly the agent's scheduled time right now. Walk
through one run: call the tools in the order specified, show me each
tool output, compose the brief, and show me the audit log entry you
would write. Do NOT actually send the brief — just show me what would
be sent.
```

A good simulated run produces:

- The actual tool outputs, verbatim
- A brief that fits on one phone screen
- A complete audit log entry
- A clear "ready to send" signal

If the simulated run is rough, the live agent will be rougher. Fix the spec, repeat.

### 6. Create the agent

When the simulation looks right, create the agent for real:

```text
Create a Zo agent from this spec [paste the spec]. Use the schedule,
allowed tools, and output format exactly as written. Wire the brief
to my Telegram (or email) and the audit log to
Records/<agent-name>/YYYY-MM-DD.md. Confirm the agent ID and the next
scheduled run time.
```

Save the agent ID. You will need it to edit, pause, or delete the agent later.

### 7. Trigger one manual run

Do not wait for the schedule. Trigger a run now:

```text
Run the [agent name] agent manually right now. Show me the audit log
entry it wrote and the message that was sent.
```

Read the message. Read the log. Compare both to what you saw in the simulated run. They should match.

### 8. Test a stop condition

This is the step almost everyone skips. Test that the agent actually aborts when it should.

```text
Force a stop condition for the [agent name] agent — for example, point
its data input at a stale file, or break the path to one of its tools.
Run it manually and confirm: it does NOT send the brief, and it DOES
write an error entry to the audit log explaining why.
```

If the agent sends a brief anyway, your stop conditions are not actually stopping. Fix the spec and test again.

### 9. Restore and verify the schedule

```text
Restore the agent to its normal config. Confirm the schedule is set
correctly and the next scheduled run is when I expect. Show me the
agent's current settings: schedule, allowed tools, output, approval
policy, audit log path.
```

Do this *before* going to bed the first night the agent will run on schedule. A misconfigured schedule is the most common runaway-agent bug.

## Checkpoint

You are done when:

- The spec is one page and every section is filled in
- The spec passed the failure-mode review
- A simulated run produced a complete brief and audit log
- A real manual run sent the brief to your private channel and wrote the audit log
- A stop-condition test caused the agent to abort cleanly
- The schedule is set correctly and the next run time is what you expect
- You can name what the agent will and will not do, without looking at the spec

If any of those is rough, do not let the agent run on schedule yet. Pause it and iterate.

## After This Course

You now have one investment-grade agent running on Zo. Treat it as the template. The next workflow you want — earnings prep, watchlist scanner, filing change detector — gets the same treatment: design doc → agent spec → simulation → manual run → stop-condition test → schedule.

The course content stops here. The discipline does not.
