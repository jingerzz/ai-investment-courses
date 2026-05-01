# Prompts: Week 1

These prompts go with the SPY/TLT exercise. Run them in Zo chat after the server is registered. A general-purpose model is fine; a coding-grade model is not required.

The prompts are grouped by what you are trying to do. Each one has a one-line note explaining what to expect from the AI's reply.

## First Contact

```text
Call get_strategy_guide on the SPY/TLT server. Summarize the strategy
in under 200 words for someone who has never seen it.
```

> The AI should call the tool first, then write its summary using the tool's content. If the summary contradicts the tool, push back.

```text
List every tool the SPY/TLT server exposes, with a one-sentence
description of what each one returns. Group them: orientation, live
state, reference data, analysis, data hygiene.
```

> A good answer matches the 14 tools from the reading and groups them the same way. If a name is missing or invented, the registration is off.

## Read Today's Signal

```text
Call get_current_signal on the SPY/TLT server. Show me the raw output
verbatim, then explain in plain English what it means.
```

> This is the workhorse prompt for the week. Watch for verbatim output. The AI should not paraphrase the JSON — it should quote it.

```text
Report today's regime in one sentence, with the tool field name you
read it from in parentheses. No hedging.
```

> Forces the AI to commit to a regime label. If it hedges, it has either ignored the tool or lost the answer.

## Verify Freshness

```text
Call refresh_data on the SPY/TLT server, then call get_current_signal
again. Tell me whether any field changed and which ones.
```

> If nothing changed, the data was already current — or `refresh_data` did not do its job. Either is worth knowing.

```text
Look at the stale_data_warning field on the latest get_current_signal
output. Quote it exactly. If it is null, say so.
```

> Trains the AI to surface the freshness field every time. You will use this in production prompts later.

## Probe the Boundaries

```text
What did SPY close at on the most recent trading day? Tell me which
tool call and which field you got the number from.
```

> The first half is a number; the second half is provenance. If the AI gives the number without provenance, it may be a phantom.

```text
Take the signal name from the latest get_current_signal call and pass
it to explain_signal. Show me the tool's explanation, then add your
own one-sentence summary at the end.
```

> Catches signal-meaning hallucinations. The AI should not explain a signal name from memory when there is a dedicated tool.

## Apply the Professional Standard

```text
Using only the SPY/TLT course tools, answer all six professional-
standard questions: regime, data sources, freshness, levels,
invalidation, and human decision. Cite a tool call for each.
```

> This is the audit prompt. Every claim needs a tool call. Save the response — you will reuse this prompt against your own server in later weeks.

```text
Pretend you are briefing a portfolio manager who has 60 seconds
before a meeting. Use the SPY/TLT server output to write the brief.
Lead with the regime, then the action, then the one risk that would
flip the call.
```

> Tests whether the AI can compress without losing fidelity. The brief should not invent numbers; it should compress real ones.

## A Note on Pushback

If the AI ever returns a number, signal, or level it did not get from a tool, treat it as a bug and tell it explicitly: *"That value is not in the tool output. Re-run with a tool call and quote the field."* Two or three rounds of this in your first session will train the rest of the week's behavior.
