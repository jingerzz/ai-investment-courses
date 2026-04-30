# Week 4: Agents, Controls, and the Human Decision Loop

Scheduled AI workflows are powerful because they keep running when you are not in the chat.

They are also risky when the task is vague.

The right pattern is a controlled agent: narrow scope, clear inputs, explicit output, audit trail, and human decision authority.

## What an Agent Should Do

An investment agent can:

- run after market close
- check whether new filings appeared
- update a dataset
- generate a dashboard snapshot
- send a short alert
- record what it did

An investment agent should not:

- invent missing data
- hide errors
- execute trades
- change strategy rules without approval
- publish personal portfolio details by default

## Audit Trail

An audit trail should answer:

- When did the agent run?
- What tools did it call?
- What data did it use?
- What changed since last run?
- What did it recommend?
- What did the human decide?

This is not bureaucracy. It is how you make AI workflows durable enough for capital allocation.

## The Human Decision Loop

The final pattern is:

1. Agent observes.
2. Tools compute.
3. Sources substantiate.
4. AI summarizes.
5. Human decides.
6. System records the outcome.

That loop is the course's core investment-management philosophy.

