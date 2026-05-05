# Exercise: Run the SPY/TLT Course Server on Zo

## Goal

By the end of this exercise, the AI in your Zo workspace will be able to answer "what kind of day did the market just have?" by calling a real tool — not by guessing from training memory. You will see the tool's raw output, then watch the AI explain it.

Time: about 20–30 minutes. Server install is handled by the prerequisites; this exercise focuses on the tool-use pattern itself.

## What You Will Use

- **The course repository** — [github.com/jingerzz/ai-investment-courses](https://github.com/jingerzz/ai-investment-courses), the GitHub repo that contains the SPY/TLT teaching server.
- **Zo terminal** — the shell where you will install and run the server.
- **Zo chat** — where you will ask questions and watch the AI call tools.

## Steps

### 1. Confirm your environment is ready

If you completed the [prerequisites](../../prerequisites.md), the SPY/TLT course server is already installed on your Zo and registered with your workspace. Confirm it in Zo chat:

```text
List the MCP servers registered in this workspace and the tools each
one exposes. I am specifically looking for the spy-tlt-course server
and its 14 tools (get_strategy_guide, get_current_signal, etc.).
```

If the server is missing or the tool count is wrong, ask:

```text
Use the course-setup skill to verify and repair my course setup.
```

That re-runs the bootstrap and prints the registration prompt at the end. Do not move on until the server is registered and the tool count is 14.

### 2. First contact: ask for the strategy guide

The reading mentioned that `get_strategy_guide` is the tool the AI should call first in any session. Try it:

```text
Call get_strategy_guide on the SPY/TLT server and summarize what
this strategy is, in plain English, in under 200 words.
```

The AI will call the tool, receive a structured object, and turn it into prose. Read the summary. If anything in it sounds vague or invented, push back — the source of truth is the tool's output.

### 3. Get today's signal

This is the centerpiece prompt for Week 1. Run it exactly:

```text
Call get_current_signal on the SPY/TLT server. Report the tool's
output verbatim first — every field, every number, including any
stale_data_warning. Then, in a separate paragraph, explain what
the result means.
```

A good response will:

- Quote the JSON or list the fields exactly as returned
- State the color (Green / Orange / Blue / Red) without hedging
- Pass through the `stale_data_warning` field, even if `null`
- Explain the regime in language a colleague could repeat

### 4. Refresh and re-run

The cached prices may be a day or two old. Force a refresh:

```text
Call refresh_data on the SPY/TLT server, then call get_current_signal
again. Compare the new output to the previous one — did the date,
prices, or signal change?
```

This is the moment where you confirm `refresh_data` actually does something. If the dates do not move, the server is not pulling fresh prices. Investigate before going further.

### 5. Stress-test against the failure modes

Pick at least two of these and run them. They are designed to surface the failure modes from the reading.

**The phantom price test.**

```text
What did SPY close at on the most recent trading day? Cite the tool
call and the field you got the number from.
```

If the AI gives you a number without naming a tool call, that is a phantom. Tell it to redo with a tool.

**The signal explanation test.**

```text
Take the signal name from the latest get_current_signal output and
call explain_signal on it. Show me the explanation the tool
returned.
```

If the AI explains the signal without calling `explain_signal`, it is using its training memory. Push it to use the tool.

**The professional standard test.**

```text
Using only the SPY/TLT course tools, answer all six of the
professional-standard questions from this week's reading: regime,
data sources, freshness, levels, invalidation, and human decision.
Cite the tool call for each answer.
```

This is the question you would ask a real analyst before trusting them with money. The AI should be able to answer all six with a tool call behind each one.

## Checkpoint

You are done when:

- The SPY/TLT course server is registered and the AI can call its tools
- You have seen `get_current_signal` output verbatim at least once
- You have run `refresh_data` and watched the data update
- You have caught the AI in at least one mistake and corrected it with a better prompt
- You can name the four color days and what each one means without looking

If any of these are still rough, repeat the relevant step before moving on. Week 2 builds on the same tool-use pattern.
