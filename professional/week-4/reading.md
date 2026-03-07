# Week 4: Autonomous Agents — AI That Acts, With Guardrails

## 4.1 The Agent Loop

In Weeks 1-3, you built tools that AI uses when a human asks a question. The
AI is reactive — it waits for you, calls tools, and responds. This week, we
go further: AI that *proactively* monitors, reasons, and proposes actions.

### From Tool-Use to Autonomy

The progression:

```
Level 0 — Dashboard:      Human reads data, makes decisions
Level 1 — Tool-assisted:  Human asks AI, AI calls tools, human decides
Level 2 — Proactive:      AI monitors signals, proposes actions, human approves
Level 3 — Semi-autonomous: AI executes routine actions, escalates unusual ones
Level 4 — Autonomous:     AI executes independently (NOT recommended for finance)
```

Most investment firms should aim for **Level 2-3**. Level 4 is inappropriate for
regulated environments and high-stakes financial decisions.

### The Agent Loop

An autonomous agent follows a continuous loop:

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  1. GATHER    Call MCP tools for current state   │
│       ↓                                         │
│  2. REASON    AI synthesizes across tool results │
│       ↓                                         │
│  3. PROPOSE   Generate action with reasoning     │
│       ↓                                         │
│  4. APPROVE   Human reviews and approves/rejects │
│       ↓                                         │
│  5. EXECUTE   Send order to broker (if approved) │
│       ↓                                         │
│  6. LOG       Record everything to audit trail   │
│       ↓                                         │
│  (wait for next check interval, then repeat)    │
│                                                 │
└─────────────────────────────────────────────────┘
```

Each step has a clear boundary:

- **Gather:** The agent is an MCP *client* — it connects to your signal,
  risk, and research servers the same way a human analyst would.
- **Reason:** The AI synthesizes tool results. "Blue regime + ES near S1 +
  risk is below limits → this is a buying opportunity."
- **Propose:** The agent formats a specific proposal: "Buy 2 MES contracts
  at 5385, stop at 5340, target 5420. Risk: $225."
- **Approve:** A human (via Telegram, Slack, email, or dashboard) reviews
  and approves or rejects. The agent does NOT proceed without approval.
- **Execute:** Only after approval, the agent calls the broker API.
- **Log:** Every step — the tool results, the AI reasoning, the proposal,
  the approval/rejection, and the fill — is recorded.

### Separation of Concerns

A critical architectural decision: **signal servers are read-only, execution
is write-only.**

```
Signal Server (read-only):
  - get_current_signal()    → returns data
  - get_trade_plan()        → returns levels
  - get_risk_report()       → returns exposure
  - NEVER places orders

Execution Layer (write-only):
  - submit_order()          → sends to broker
  - get_fill_status()       → checks execution
  - cancel_order()          → cancels pending
  - NEVER computes signals
```

Why separate? If the signal server has a bug, it returns bad data — but it
can't place orders. The blast radius of any single component failure is limited.

---

## 4.2 Human-in-the-Loop Controls

### Why Full Autonomy Is Wrong for Finance

Three reasons to always keep a human in the loop:

1. **Regulatory:** Most jurisdictions require human oversight of algorithmic
   trading decisions. A fully autonomous AI trading system may violate
   regulations (MiFID II, SEC Rule 15c3-5, etc.).

2. **Risk:** AI can be confidently wrong. A hallucinated signal or
   misinterpreted data point could lead to a catastrophic trade. Human
   review catches "this doesn't feel right" moments.

3. **Trust:** Building trust with AI is incremental. Starting with full
   autonomy means the first mistake destroys confidence. Starting with
   approve-everything and gradually expanding autonomy builds trust.

### Approval Workflows

The approval mechanism should match your team's communication patterns:

**Telegram/Slack integration:**

```
Bot: 🔔 Trade Proposal
     Signal: T2_STRONG_BLUE (Tier 2)
     Action: BUY 2 MES @ 5385
     Stop: 5340 (45 pts, $225 risk)
     Target: 5420 (35 pts, $175 reward)
     R:R = 1:0.78
     Account risk: 0.45%

     [✅ Approve]  [❌ Reject]  [📝 Modify]
```

The proposal includes everything the PM needs to decide:
- What the signal is and why
- Exact order details with pre-computed risk
- Risk as a percentage of account
- One-tap approve/reject

**Key details:**
- Proposals expire after a configurable window (e.g., 15 minutes)
- Rejected proposals are logged with optional rejection reason
- Modified proposals (PM changes size or price) go through the same logging

### Escalation Patterns

Not all proposals are equal. Configure different approval requirements:

```python
APPROVAL_RULES = {
    # Routine: auto-notify, auto-approve after 5 min if no rejection
    "close_existing_position": ApprovalLevel.NOTIFY,

    # Standard: requires explicit approval
    "open_new_position": ApprovalLevel.APPROVE,

    # Elevated: requires approval + confirmation
    "increase_position_size": ApprovalLevel.CONFIRM,

    # Blocked: agent cannot propose this
    "override_risk_limit": ApprovalLevel.BLOCKED,
}
```

Start conservative (everything requires APPROVE) and gradually move routine
actions to NOTIFY as trust builds.

### Configurable Autonomy Levels

Define a progression from "day one" to "month six":

```
Day 1:    Everything requires explicit approval
Week 2:   Data refresh and signal checks run automatically
Month 1:  Position closes auto-approved (with notification)
Month 3:  Small positions (< 0.5% risk) auto-approved
Month 6:  Standard positions auto-approved; only large/unusual escalated
```

Each level should be explicitly documented, reviewed, and approved by
stakeholders before activation.

---

## 4.3 Audit Trails and Compliance

### What Gets Logged

Every agent action produces a log entry:

```python
@dataclass
class AgentLogEntry:
    timestamp: datetime
    event_type: str          # "signal_check", "proposal", "approval", "execution", "error"
    signal_data: dict        # Raw tool returns that informed the decision
    ai_reasoning: str        # The AI's full reasoning text
    proposed_action: dict    # Exact order details
    approval_status: str     # "pending", "approved", "rejected", "expired"
    approved_by: str         # Who approved (username)
    execution_result: dict   # Fill details from broker
    notes: str               # Human-added notes or rejection reason
```

This creates a complete chain: *what the AI saw → what it reasoned → what it
proposed → who approved → what happened*. This chain is essential for:

- **Post-trade review:** "Why did the agent propose this trade?"
- **Compliance audit:** "Show me all trades approved by PM_Smith last month"
- **Model improvement:** "The agent proposed 15 Blue-regime trades; 12 were
  profitable — the signal is working"

### Journal Pattern

Store the audit trail in a structured format (SQLite is simple and effective):

```sql
CREATE TABLE trade_journal (
    id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL,
    event_type TEXT NOT NULL,
    signal_name TEXT,
    signal_tier INTEGER,
    regime TEXT,
    proposed_ticker TEXT,
    proposed_side TEXT,
    proposed_quantity INTEGER,
    proposed_price REAL,
    stop_price REAL,
    target_price REAL,
    dollar_risk REAL,
    account_risk_pct REAL,
    ai_reasoning TEXT,
    approval_status TEXT DEFAULT 'pending',
    approved_by TEXT,
    approval_timestamp TEXT,
    fill_price REAL,
    fill_quantity INTEGER,
    fill_timestamp TEXT,
    pnl REAL,
    notes TEXT
);
```

Every query an analyst or compliance officer might ask is answerable from
this table.

---

## 4.4 Testing and Monitoring

### Testing Agent Systems

Agent systems need tests that go beyond unit tests:

**Scenario tests:** Simulate a complete agent loop with mocked data:

```python
async def test_blue_regime_proposes_long():
    """Agent should propose a long trade in Blue regime near support."""
    # Mock tools to return Blue regime + ES near S1
    mock_signal = {"color": "Blue", "signal": "T2_STRONG_BLUE", "exposure": 1.5}
    mock_levels = {"pivot": 5420, "s1": 5385, "current": 5390}
    mock_risk = {"status": "OK", "available_risk_pct": 2.0}

    proposal = await agent.reason(mock_signal, mock_levels, mock_risk)

    assert proposal is not None
    assert proposal["side"] == "BUY"
    assert proposal["stop"] < proposal["entry"]
    assert proposal["dollar_risk"] > 0

async def test_danger_state_no_proposal():
    """Agent should NOT propose trades during danger state."""
    mock_signal = {"color": "Blue", "danger_state": True, "exposure": 0.0}

    proposal = await agent.reason(mock_signal, {}, {})

    assert proposal is None  # No trade proposed
```

**Edge case tests:**

```python
async def test_stale_data_blocks_proposal():
    """Agent should not propose trades on stale data."""
    mock_signal = {
        "color": "Blue",
        "signal": "T2_STRONG_BLUE",
        "stale_data_warning": "Data is 4 hours old",
    }
    proposal = await agent.reason(mock_signal, {}, {})
    assert proposal is None  # Stale data = no action

async def test_broker_unavailable_logs_error():
    """If broker is down, agent logs error and does not retry."""
    mock_broker = MockBroker(available=False)
    result = await agent.execute(proposal, broker=mock_broker)
    assert result["status"] == "error"
    assert "broker unavailable" in result["error"].lower()
```

### Monitoring in Production

Key metrics to track:

```
Agent uptime:           Is the loop running?
Signal check frequency: Are checks happening on schedule?
Proposal rate:          How many proposals per day? (sudden spike = investigate)
Approval latency:       How long between proposal and approval?
Rejection rate:         High rejections = agent may be miscalibrated
Fill rate:              Are approved orders actually filling?
P&L tracking:           Is the agent's signal quality improving or degrading?
```

### The Iteration Advantage

Unlike ML models, MCP-based agents have a fast iteration cycle:

```
Traditional ML:
  New signal idea → collect data → train model → validate → deploy → months

MCP tool approach:
  New signal idea → write tool → add tests → deploy → AI has access → hours
```

No retraining, no fine-tuning, no validation set. You add a new tool, the AI
can immediately call it. This means you can experiment with new signals, risk
checks, or data sources at the speed of software development, not ML pipelines.

---

## Key Takeaways

1. **Level 2-3 autonomy** is appropriate for finance — AI proposes, humans approve
2. **Signal servers are read-only**, execution is write-only — limit blast radius
3. **Start conservative** — everything requires approval on day one
4. **Log everything** — tool results, AI reasoning, proposals, approvals, fills
5. **Approval UX matters** — one-tap approve/reject with all context included
6. **Escalation tiers** — routine actions can graduate to auto-approval over time
7. **Test the full loop** — scenario tests with mocked tools, not just unit tests
8. **Iterate fast** — new tools = new capabilities, no retraining needed
