# Prompts: Week 4

Use these prompts to specify and review a controlled Zo agent.

## Draft the Agent Spec

```text
Turn this Week 3 workflow into a scheduled Zo agent spec. Include purpose, schedule, allowed inputs, allowed tools, required output, approval requirements, audit log, and stop conditions.
```

```text
Rewrite this agent spec so the agent observes, computes, and recommends, but does not make capital-allocation decisions.
```

## Review Permissions

```text
Review this agent spec for unsafe permissions. Flag anything that could send external messages, publish publicly, alter services, change rules, or affect capital decisions without approval.
```

```text
Classify each possible action as silent, logged, ask-for-approval, or blocked. Explain the boundary in plain English.
```

## Test the Human Loop

```text
Simulate one run of this agent using mocked inputs. Show the output I would receive, the audit log entry, and the human decision I would need to make.
```

```text
Review the simulated output. Is it short enough to act on? Does it include sources, stale-data warnings, and a clear next decision?
```
