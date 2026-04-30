# Server Context for the Zo-Centric Track

This track uses the updated MCP teaching servers already shipped in the professional course tree.

## Source of Truth

Use `origin/main` of `jingerzz/ai-investment-courses`.

Relevant sync commits:

- `8a86085` — PageIndex RAG course parity, drift detector, intentional divergence registry
- `b29c1d6` — Course vs production MCP server side-by-side

## Servers Used

| Server | Course Path | Production Relationship |
| --- | --- | --- |
| SPY/TLT strategy | `professional/servers/spy-tlt-course` | 14-tool teaching subset of the 37-tool production server |
| SEC filing RAG | `professional/servers/page-index-rag-course` | 14-tool course server, functionally aligned with production SEC-RAG |
| Single-stock strategy | Not shipped | Production-only; intentionally excluded from this course |

## What Changed for Students in the Sync Pass

- SEC RAG is now close to production parity.
- PageIndex RAG supports backend selection and environment-driven configuration.
- Course RAG includes pre-indexed BLK and HOOD filings.
- SPY/TLT course server keeps the core signal, level, pattern, backtest, and briefing flow.
- Drift and divergence docs explain what should not be ported from production.

## What Deliberately Did Not Change

- SPY/TLT course does not include futures, options, broker risk, or live account tooling.
- The course server remains monolithic for pedagogy.
- The single-stock strategy server is not shipped.
- RAG keeps richer teaching guidance even where production trims prompts for context efficiency.

## Where to Look Next Time

On `origin/main`, read:

- `docs/course_vs_production.md`
- `docs/intentional_divergence.md`
- `docs/drift-report.md`
- `professional/servers/spy-tlt-course`
- `professional/servers/page-index-rag-course`
