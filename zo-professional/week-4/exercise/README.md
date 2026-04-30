# Exercise: Specify a Controlled Investment Agent

## Goal

Write the specification for a scheduled Zo agent that supports an investment decision without making the decision.

## Steps

1. Choose the architecture from Week 3.
2. Define the schedule.
3. Define the exact tools or scripts the agent may run.
4. Define the output format.
5. Define the delivery channel.
6. Define what requires human approval.
7. Define the audit log entry.

## Agent Spec Template

```markdown
# Agent Name

## Purpose

## Schedule

## Allowed Inputs

## Allowed Tools

## Required Output

## Approval Required For

## Audit Log

## Stop Conditions
```

## Prompt to Use

```text
Review this investment agent spec. Tighten the scope, identify unsafe permissions, and rewrite it so the agent observes and recommends but does not make capital-allocation decisions.
```

## Checkpoint

You are done when:

- the agent has one clear job
- the schedule is justified
- the output is short enough to review
- approval points are explicit
- failures are visible
- the agent cannot trade or change rules on its own

