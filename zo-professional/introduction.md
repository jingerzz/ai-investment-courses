# Introduction: Your Investment AI Needs a Home

Most AI investing demos happen inside a chat window. That is useful for experimentation, but it is not enough for investment management.

An investment workflow needs files, datasets, services, secrets, scheduled jobs, source control, hosted dashboards, and an audit trail. It also needs a place where those pieces can keep running after the conversation ends.

That is the premise of this course: Zo Computer is the home for your investment AI.

## What Makes This Different

This course is not about asking a model for stock picks. It is about building controlled systems where AI can:

- call tools that return exact market data
- read primary-source filings instead of guessing
- explain model output in plain language
- run on a schedule
- notify you when something matters
- leave enough traceability that you can inspect what happened later

The goal is not autonomy for its own sake. The goal is leverage with control.

## The Course Pattern

Every module follows the same pattern:

1. Learn a concept.
2. Use it in Zo.
3. Inspect the output.
4. Identify the guardrail.
5. Decide what a professional version would require.

The teaching servers are intentionally smaller than the production systems they are based on. That is a feature. Students should be able to understand the architecture before they scale it.

## What You Will Build

You will work through four practical investment workflows:

- a SPY/TLT regime workflow for market exposure context
- a SEC filing RAG workflow for primary-source company research
- a multi-service architecture for investment research operations
- a scheduled agent workflow with approval and audit controls

You will also learn how to think about the boundaries between chat, files, services, dashboards, and automations.

## What You Will Not Do

You will not hand trading authority to an AI model.

You will not treat model output as a source of truth.

You will not build a toy chatbot and call it an investment platform.

The permanent design pattern is: AI proposes, tools compute, sources substantiate, humans decide.

