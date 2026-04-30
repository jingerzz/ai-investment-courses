# Week 1: Market Regime Tools on Zo

The first investment workflow is a market-regime tool based on the SPY/TLT strategy pattern.

The teaching server lives at:

`professional/servers/spy-tlt-course`

It is a teaching subset of the production SPY/TLT system. The production system has more tools, live service deployment, and broader futures/risk context. The course version keeps the core pattern small enough to inspect.

## What the Server Teaches

The server shows how an AI assistant should use deterministic tools for market state.

Instead of asking a model to guess the market regime, the AI calls a tool that:

- loads SPY and TLT price history
- computes trend and risk context
- classifies the current color day
- returns levels and evidence
- exposes the result through a small tool interface

The AI can then explain the signal, but it does not invent the signal.

## Why SPY/TLT

SPY and TLT are simple enough for teaching and expressive enough to show a real concept:

- equity risk appetite
- duration demand
- cross-asset confirmation
- regime change
- exposure discipline

The exact trading strategy is less important than the architecture.

## The Professional Standard

A market-regime tool should answer:

- What is the current regime?
- What data was used?
- How fresh is the data?
- Which levels matter?
- What would invalidate the signal?
- What should the human decide?

If an AI answer skips those questions, it is not yet investment-grade.
