# Exercise: Design Your Investment System Architecture

## Goal

Design a Zo-native architecture for one investment workflow you actually want.

## Steps

1. Pick one workflow:
   - post-close market brief
   - company filing monitor
   - watchlist technical scanner
   - earnings prep dashboard
   - activist short report tracker
2. Write the decision the workflow supports.
3. Identify the exact data inputs.
4. Identify the source documents.
5. Decide which parts should be services, datasets, pages, and agents.
6. Mark the approval points.

## Architecture Template

```markdown
# Workflow

## Decision Supported

## Inputs

## Tools and Services

## Human Review Point

## Output

## Audit Trail

## Failure Modes
```

## Prompt to Use

```text
Review this Zo-native investment workflow architecture. Identify missing data sources, unsafe AI assumptions, unclear approval points, and the smallest version I should build first.
```

## Checkpoint

You are done when your architecture has:

- a specific decision
- exact inputs
- a narrow tool boundary
- a human approval point
- an output format
- at least three failure modes

