# Week 3: Designing a Multi-Service Investment System

By Week 3, you have seen two separate tools:

- market regime analysis
- SEC filing retrieval

Professional investment workflows usually need several tools working together. Zo is useful because it can host and coordinate those pieces in one environment.

## Separation of Concerns

Each service should have a narrow job.

| Service | Job |
| --- | --- |
| Regime server | market state, levels, exposure context |
| Filing RAG | primary-source document retrieval |
| Dataset | durable prices, fundamentals, or index history |
| Dashboard | human-readable current state |
| Agent | scheduled workflow and notification |

Do not make one giant AI prompt responsible for all of this.

## The Architecture Question

Before building, ask:

- What data must be exact?
- What source documents must be cited?
- What can be summarized?
- What should run on a schedule?
- What should require approval?
- What output should be private versus public?

Those questions matter more than framework choice.

## Zo Deployment Surfaces

Zo gives you several deployment surfaces:

- workspace files for durable source and notes
- services for long-running tools
- sites and pages for dashboards
- automations for scheduled workflows
- integrations for delivery channels

The course uses these as building blocks rather than treating AI as a single app.

