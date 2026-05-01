# Week 4: Building a Controlled Investment Agent

## 4.1 Why "Agent" Is Both Powerful and Risky

By Week 4, you have seen tools (Week 1, Week 2) and you have seen workflow design (Week 3). This week is about the layer that makes the workflow run on its own: the **agent**.

An agent is just a scheduled AI workflow. It runs on a clock, not because you opened a chat. That changes its character entirely. A scheduled workflow can:

- Run when you are asleep, on a flight, or in a meeting
- Catch market closes, filing drops, and overnight news without your involvement
- Build the muscle memory that good investment work needs

It can also, when poorly specified, do real damage. A scheduled workflow can:

- Send a misleading message to your phone at 5 AM that you act on before you are fully awake
- Publish something publicly that has stale data
- Burn through API credits running a broken loop
- Quietly fail and leave you thinking the workflow is still working

The difference between a useful agent and a dangerous agent is not the model. It is the **specification**. This week is about writing one.

## 4.2 What an Agent Should Do (and Should Not)

Treat this as the starting point for every agent spec. Tighten it from here.

**An investment agent can:**

- Run on a schedule
- Refresh data using a deterministic tool
- Call the workflow's tools in a fixed sequence
- Compose a brief or update from the tool outputs
- Save a record of the run to your workspace
- Send the brief to a private channel (your Telegram, your email)
- Surface stale data and abort if it is too stale

**An investment agent should not:**

- Invent missing data ("revenue probably grew about 8%")
- Hide errors (a tool failed but the brief looks normal)
- Execute trades
- Change strategy rules without your approval
- Publish your portfolio details, positions, or P&L on a public surface by default
- Send messages to anyone other than you, by default

That last word — **default** — matters. You can override it for any specific case. But you should override it on purpose, not by accident.

## 4.3 The Agent Spec

The agent spec is the contract. Before you create the agent in Zo, you write the spec down in a markdown file, you read it back to yourself, and you ask the AI to stress-test it. Only then do you create the agent.

A complete spec has eight sections. Each has a purpose.

**1. Purpose** — One sentence: what decision does this agent's output support? (Pulled directly from your Week 3 design.)

**2. Schedule** — When does it run? What is the consequence of missing a run?

**3. Allowed Inputs** — What data sources is it allowed to read?

**4. Allowed Tools** — What scripts, MCP tools, or services is it allowed to call? Be explicit. "All tools" is not an answer.

**5. Required Output** — What does a finished run produce? A markdown file, a Telegram message, both? With what fields?

**6. Approval Required For** — What actions require you to approve before they happen? Default: any external message, any public publish, any trade.

**7. Audit Log** — What does each run write to the workspace, regardless of whether it sent a message?

**8. Stop Conditions** — When does the agent abort the run? Stale data, tool failure, missing input — name them all.

If a section is empty, the agent is not ready to run.

## 4.4 The Audit Trail Is Not Bureaucracy

A research analyst keeps notes. An auditor keeps work papers. A surgeon keeps an op note. The audit trail is the same idea applied to AI workflows.

For every run, the trail should answer:

- **When** did the agent run?
- **What** tools did it call, and in what order?
- **What** did each tool return?
- **What** changed since the previous run?
- **What** did the agent recommend or surface?
- **What** did the human (you) decide afterward?

This is not paranoia. It is what makes the workflow durable enough to trust with capital decisions. When you look back in six months and ask "was the agent right about that signal in May?", the audit trail is the only answer.

A simple convention: every run writes one markdown file under `Records/<agent-name>/YYYY-MM-DD.md` with all of the above. Even if the run is silent (nothing to send), the file gets written.

## 4.5 Giving Your Agent Memory

The audit trail captures what happened in a single run. Memory captures what is happening across runs. They are complementary, and a serious agent needs both.

If you completed Foundations 3, you already have a file-based memory system in your workspace: `USER.md`, `MEMORY.md`, the `memory/` folder, and the two Rules. A scheduled agent can — and should — read and write the same memory layer that interactive chats use. The shared layer is what turns a one-shot run into a thread.

**What memory adds to an agent.**

- **Continuity.** The agent that posted Friday's brief knows what Monday's brief said. It can lead with *"regime is unchanged from last week"* instead of restating the full color-day rationale every time.
- **Thesis tracking.** The agent that re-evaluates an open position can read the original thesis from a project memory entry and report against it, instead of re-deriving the thesis from current price action.
- **Drift detection.** The agent can read the prior daily note before producing the new one and flag when something has materially changed since the last run, instead of leaving that work to you.
- **Quieter briefs.** When nothing has changed since the last run, the agent can say so in one line. The signal-to-noise improvement is real after a few weeks.

**The pattern, in three rules.**

- **Read first.** Before calling tools, the agent reads `USER.md`, `MEMORY.md`, and the most recent daily note for its own scope (`memory/daily/<date>.md` or `memory/projects/<name>.md`).
- **Write last.** After the brief is produced and any external send is done, the agent writes a project entry update or a daily note describing the run in a few lines.
- **Ask before adding new types.** A scheduled agent should not invent new memory folders on its own. If a run reveals a gap in the memory schema, the agent flags it and you decide.

A useful concrete example: a Friday post-close brief agent. Its run sequence becomes *(1) read prior week's daily note → (2) refresh data via the regime tool → (3) compose a brief that explicitly compares to last Friday → (4) send the brief to your private Telegram → (5) write a new daily note capturing today's run and any thesis-level deltas.* The agent did not get smarter. It got context.

**Pitfalls to avoid.**

- **Letting an agent edit `USER.md`.** Profile drift is very hard to debug. Agents read `USER.md`; they do not change it.
- **Letting an agent run without writing.** A silent agent run that produces a brief but writes nothing to memory is invisible to next week's run. Always write — even one line — before you treat the run as complete.
- **Memory and audit logs duplicating each other.** The audit log is *what happened in this run* (every tool call, every output). Memory is *what we now believe about the world*. Same agent, two artifacts, two purposes.

If you need only the audit log, skip the memory layer for that agent. If you need cross-run continuity — and most investment agents do — wire both in from the start.

## 4.6 The Human Decision Loop

The full pattern, end to end, is this:

1. **Agent observes.** The clock fires. The agent wakes up.
2. **Tools compute.** The agent calls the workflow's tools in sequence. Code does the math.
3. **Sources substantiate.** Citations come from real tools and real documents, not from the model.
4. **AI summarizes.** The model turns the tool outputs into a short brief.
5. **Human decides.** You read the brief and decide what to do, if anything.
6. **System records the outcome.** The audit log captures the run; you (or a separate workflow) capture the decision.

That loop is the whole investment-management philosophy of this course. The AI does the work it is good at — navigating, summarizing, comparing. Code does the work that needs to be exact. You do the work that requires judgment and accountability. None of the three is interchangeable.

## 4.7 Failure Modes (Week 4 Edition)

These are the agent-specific bugs. Watch for them in your own builds.

**The runaway agent.** A bug in the loop logic causes the agent to fire every minute instead of once a day. Usually caught by an API bill. Fix: check the schedule with `zo agent list` before going to bed the first night.

**The silent failure.** A tool returns an error, the AI summarizes the error message as if it were data, and the brief reads normally. You act on garbage. Fix: stop conditions. If a tool returns a non-200, abort the run and write the error to the audit log instead of pretending.

**The stale brief.** Data was last refreshed three days ago. The brief says "today's regime is Blue." It is technically reading the file, but the file is old. Fix: every brief includes the data timestamp, prominently. Anything older than your tolerance window is an abort.

**Permission creep.** You add "and also publish to my public dashboard" to an agent that started as a private brief. Now your positions are on the open internet. Fix: re-run the approval policy from scratch any time you change the agent's surface.

**The mood-piece brief.** The brief reads like commentary instead of facts. "Markets felt nervous today." Fix: every brief is structured. Date, regime, key levels, what changed, recommended decision. No mood pieces.

**The forgotten audit log.** The agent runs, sends the brief, and writes nothing to disk. In six months you cannot reconstruct what happened. Fix: the audit log write happens *first*, before any external send. If the log fails, the send does not happen.

## 4.8 What "Done" Looks Like

You have an investment-grade agent when:

- The spec fits on one page
- Every tool the agent calls is named and exists
- The output format is fixed and reviewable in under 60 seconds
- Approval points are explicit, not implicit
- The audit log is written on every run, even silent ones
- Stop conditions are named — and tested at least once
- You can read a brief on your phone and act on it without going to your laptop to verify

If any of those is rough, the agent is not ready to run on a schedule yet. Run it manually a few times first.

## Key Takeaways

- **An agent is a scheduled workflow.** The schedule changes the risk profile completely.
- **The spec is the contract.** Eight sections: purpose, schedule, allowed inputs, allowed tools, required output, approval points, audit log, stop conditions.
- **Default to private and ask-for-approval.** Override on purpose, never by accident.
- **The audit trail is part of the workflow, not extra.** Every run writes to disk before sending anything externally.
- **Memory and audit are complementary.** The audit log captures *what happened*; memory captures *what we now believe*. A serious investment agent has both.
- **The loop is: agent observes, tools compute, sources substantiate, AI summarizes, human decides, system records.**
- **None of the three roles — code, AI, you — is interchangeable.** Each does what it is good at.
