import { useState } from "react";

const STEPS = [
  {
    id: "gather",
    label: "GATHER",
    icon: "📡",
    color: "#3b82f6",
    title: "Call MCP tools for current state",
    detail: "The agent connects to your signal, risk, and research servers — the same ones you built in Weeks 1-3. It's an MCP client, just like Claude Desktop.",
    example: `get_current_signal() → Blue, T2_STRONG_BLUE, 1.5x
get_es_levels()      → pivot 5420, S1 5385, last 5398
get_risk_report()    → HEDGED, 0.85% risk used`,
  },
  {
    id: "reason",
    label: "REASON",
    icon: "🧠",
    color: "#a78bfa",
    title: "AI synthesizes across tool results",
    detail: "The AI cross-references all data points: regime signal + price vs. support + available risk capacity. This is the same synthesis from Week 2, but running autonomously.",
    example: `"Blue regime + ES near S1 (5385) + risk below limits
→ Mean-reversion buying opportunity aligned with signal.
   Bond hedge is working (TLT up in Blue regime).
   Available risk capacity: 1.15% of account."`,
  },
  {
    id: "propose",
    label: "PROPOSE",
    icon: "📋",
    color: "#f59e0b",
    title: "Generate action with reasoning",
    detail: "The agent formats a specific, fully-sized proposal. Every number is pre-computed by Python. The proposal includes everything the PM needs to make a decision in 10 seconds.",
    example: `🔔 Trade Proposal
   Signal: T2_STRONG_BLUE (Tier 2)
   Action: BUY 2 MES @ 5385
   Stop: 5340 (45 pts, $225 risk)
   Target: 5420 (35 pts, $175 reward)
   R:R = 1:0.78
   Account risk: 0.45%`,
  },
  {
    id: "approve",
    label: "APPROVE",
    icon: "✅",
    color: "#22c55e",
    title: "Human reviews and approves/rejects",
    detail: "The proposal arrives on Telegram/Slack with one-tap buttons. The agent does NOT proceed without explicit human approval. Proposals expire after 15 minutes.",
    example: `[✅ Approve]  [❌ Reject]  [📝 Modify]

PM taps ✅ Approve at 9:42 AM ET
→ Approval logged with timestamp and user ID`,
  },
  {
    id: "execute",
    label: "EXECUTE",
    icon: "⚡",
    color: "#ef4444",
    title: "Send order to broker (if approved)",
    detail: "Only after approval, the agent calls the execution server. Remember: signal servers are read-only, execution is write-only. The most dangerous capability is isolated.",
    example: `submit_order("MES", "BUY", 2, limit=5385)
→ Order ID: MES-20260307-001
→ Status: FILLED @ 5384.75 (2 contracts)`,
  },
  {
    id: "log",
    label: "LOG",
    icon: "📝",
    color: "#64748b",
    title: "Record everything to audit trail",
    detail: "Every step gets logged: what the AI saw, what it reasoned, what it proposed, who approved, and what happened. Your compliance team can audit any decision.",
    example: `INSERT INTO trade_journal:
  signal_name: T2_STRONG_BLUE
  ai_reasoning: "Blue regime + ES near S1..."
  proposed: BUY 2 MES @ 5385
  approved_by: PM_Smith
  fill_price: 5384.75
  dollar_risk: $225`,
  },
];

const AUTONOMY_LEVELS = [
  { day: "Day 1", rules: "Everything requires explicit approval", color: "#22c55e", width: "100%" },
  { day: "Week 2", rules: "Data refresh and signal checks run automatically", color: "#3b82f6", width: "85%" },
  { day: "Month 1", rules: "Position closes auto-approved (with notification)", color: "#a78bfa", width: "65%" },
  { day: "Month 3", rules: "Small positions (< 0.5% risk) auto-approved", color: "#f59e0b", width: "40%" },
  { day: "Month 6", rules: "Standard positions auto-approved; only large/unusual escalated", color: "#ef4444", width: "20%" },
];

const APPROVAL_RULES = [
  { action: "Close existing position", level: "NOTIFY", color: "#64748b", desc: "Auto-approve after 5 min if no rejection" },
  { action: "Open new position", level: "APPROVE", color: "#22c55e", desc: "Requires explicit approval" },
  { action: "Increase position size", level: "CONFIRM", color: "#f59e0b", desc: "Requires approval + confirmation" },
  { action: "Override risk limit", level: "BLOCKED", color: "#ef4444", desc: "Agent cannot propose this" },
];

export default function AgentLoop() {
  const [activeStep, setActiveStep] = useState(null);
  const [activeTab, setActiveTab] = useState("loop");

  return (
    <div style={{ fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", background: "#0a0f1a", color: "#e2e8f0", minHeight: "100vh", padding: "2rem" }}>
      <div style={{ maxWidth: 960, margin: "0 auto" }}>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 700, marginBottom: "0.5rem" }}>Week 4: Autonomous Agents</h1>
        <p style={{ color: "#94a3b8", marginBottom: "2rem" }}>AI that monitors, reasons, and proposes — with humans in control of every consequential decision.</p>

        {/* Tabs */}
        <div style={{ display: "flex", gap: 0, marginBottom: "2rem", borderBottom: "1px solid #2a3a4e" }}>
          {[["loop", "Agent Loop"], ["autonomy", "Autonomy Levels"], ["approval", "Approval Rules"]].map(([id, label]) => (
            <div
              key={id}
              onClick={() => setActiveTab(id)}
              style={{
                padding: "0.75rem 1.5rem", cursor: "pointer", fontSize: "0.9rem", fontWeight: 500,
                color: activeTab === id ? "#3b82f6" : "#94a3b8",
                borderBottom: `2px solid ${activeTab === id ? "#3b82f6" : "transparent"}`,
                transition: "all 0.2s",
              }}
            >{label}</div>
          ))}
        </div>

        {/* AGENT LOOP TAB */}
        {activeTab === "loop" && (
          <div>
            {/* Circular visual */}
            <div style={{ display: "flex", flexWrap: "wrap", gap: "0.5rem", justifyContent: "center", marginBottom: "2rem" }}>
              {STEPS.map((step, i) => (
                <div key={step.id} style={{ display: "flex", alignItems: "center" }}>
                  <div
                    onClick={() => setActiveStep(activeStep === i ? null : i)}
                    style={{
                      width: 100, height: 100, borderRadius: "50%",
                      background: activeStep === i ? step.color : "#1a2332",
                      border: `2px solid ${activeStep === i ? step.color : "#2a3a4e"}`,
                      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",
                      cursor: "pointer", transition: "all 0.3s",
                      boxShadow: activeStep === i ? `0 0 20px ${step.color}40` : "none",
                    }}
                  >
                    <div style={{ fontSize: "1.3rem" }}>{step.icon}</div>
                    <div style={{ fontSize: "0.7rem", fontWeight: 700, marginTop: "0.15rem" }}>{step.label}</div>
                  </div>
                  {i < STEPS.length - 1 && (
                    <div style={{ color: "#2a3a4e", fontSize: "1.2rem", margin: "0 0.25rem" }}>→</div>
                  )}
                </div>
              ))}
              <div style={{ display: "flex", alignItems: "center" }}>
                <div style={{ color: "#2a3a4e", fontSize: "1rem" }}>↩ repeat</div>
              </div>
            </div>

            {/* Detail panel */}
            {activeStep !== null && (
              <div style={{
                background: "#111827", border: `1px solid ${STEPS[activeStep].color}`,
                borderRadius: 14, padding: "1.75rem", transition: "all 0.3s",
              }}>
                <div style={{ fontSize: "0.75rem", fontWeight: 700, color: STEPS[activeStep].color, textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: "0.5rem" }}>
                  Step {activeStep + 1}: {STEPS[activeStep].label}
                </div>
                <h3 style={{ fontSize: "1.15rem", marginBottom: "0.75rem" }}>{STEPS[activeStep].title}</h3>
                <p style={{ color: "#94a3b8", fontSize: "0.95rem", marginBottom: "1rem" }}>{STEPS[activeStep].detail}</p>
                <pre style={{
                  background: "#0a0f1a", borderRadius: 8, padding: "1rem",
                  fontSize: "0.82rem", lineHeight: 1.6, whiteSpace: "pre-wrap", color: "#94a3b8",
                }}>
                  {STEPS[activeStep].example}
                </pre>
              </div>
            )}

            {!activeStep && activeStep !== 0 && (
              <div style={{ textAlign: "center", color: "#64748b", padding: "2rem", fontSize: "0.95rem" }}>
                Click any step in the loop above to explore it
              </div>
            )}
          </div>
        )}

        {/* AUTONOMY LEVELS TAB */}
        {activeTab === "autonomy" && (
          <div>
            <p style={{ color: "#94a3b8", marginBottom: "1.5rem" }}>
              Start conservative. Expand autonomy as trust builds. Each level is explicitly documented and approved by stakeholders.
            </p>
            <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
              {AUTONOMY_LEVELS.map((level, i) => (
                <div key={i} style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
                  <div style={{ width: 80, fontWeight: 600, fontSize: "0.85rem", color: level.color, flexShrink: 0 }}>
                    {level.day}
                  </div>
                  <div style={{ flex: 1 }}>
                    <div style={{
                      height: 36, background: `${level.color}20`, borderRadius: 8, position: "relative",
                      border: `1px solid ${level.color}40`, display: "flex", alignItems: "center",
                      paddingLeft: "0.75rem",
                    }}>
                      <div style={{
                        position: "absolute", top: 0, left: 0, bottom: 0, width: level.width,
                        background: `${level.color}15`, borderRadius: 8,
                      }} />
                      <span style={{ position: "relative", fontSize: "0.82rem", color: "#e2e8f0" }}>
                        {level.rules}
                      </span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
            <div style={{ display: "flex", justifyContent: "space-between", marginTop: "1rem", padding: "0 0 0 96px" }}>
              <span style={{ fontSize: "0.75rem", color: "#64748b" }}>← More human oversight</span>
              <span style={{ fontSize: "0.75rem", color: "#64748b" }}>More AI autonomy →</span>
            </div>

            <div style={{
              background: "rgba(239,68,68,0.08)", border: "1px solid rgba(239,68,68,0.2)",
              borderRadius: 10, padding: "1rem", marginTop: "2rem", fontSize: "0.9rem",
            }}>
              <strong style={{ color: "#ef4444" }}>Level 4 (Full Autonomy) is NOT recommended for finance.</strong> Most jurisdictions require human oversight of algorithmic trading decisions. MiFID II, SEC Rule 15c3-5, and similar regulations mandate human involvement in consequential financial decisions.
            </div>
          </div>
        )}

        {/* APPROVAL RULES TAB */}
        {activeTab === "approval" && (
          <div>
            <p style={{ color: "#94a3b8", marginBottom: "1.5rem" }}>
              Not all proposals are equal. Configure different approval requirements based on the action's risk level.
            </p>
            <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
              {APPROVAL_RULES.map((rule, i) => (
                <div key={i} style={{
                  background: "#111827", border: "1px solid #2a3a4e", borderRadius: 12,
                  padding: "1.25rem", display: "flex", alignItems: "center", gap: "1rem",
                }}>
                  <div style={{
                    background: `${rule.color}20`, color: rule.color,
                    padding: "0.3rem 0.75rem", borderRadius: 8, fontWeight: 700,
                    fontSize: "0.78rem", minWidth: 80, textAlign: "center",
                  }}>
                    {rule.level}
                  </div>
                  <div style={{ flex: 1 }}>
                    <div style={{ fontWeight: 600, fontSize: "0.95rem" }}>{rule.action}</div>
                    <div style={{ color: "#94a3b8", fontSize: "0.85rem" }}>{rule.desc}</div>
                  </div>
                </div>
              ))}
            </div>

            {/* Mock Telegram UI */}
            <div style={{ marginTop: "2rem" }}>
              <div style={{ fontSize: "0.85rem", color: "#94a3b8", marginBottom: "0.75rem" }}>What the PM sees on Telegram:</div>
              <div style={{
                background: "#1a2332", border: "1px solid #2a3a4e", borderRadius: 16,
                padding: "1.5rem", maxWidth: 400,
              }}>
                <div style={{ fontSize: "0.9rem", marginBottom: "0.75rem" }}>
                  <span style={{ fontSize: "1.1rem" }}>🔔</span> <strong>Trade Proposal</strong>
                </div>
                <div style={{ fontSize: "0.85rem", color: "#94a3b8", lineHeight: 1.7 }}>
                  <div><strong style={{ color: "#e2e8f0" }}>Signal:</strong> T2_STRONG_BLUE (Tier 2)</div>
                  <div><strong style={{ color: "#e2e8f0" }}>Action:</strong> BUY 2 MES @ 5385</div>
                  <div><strong style={{ color: "#e2e8f0" }}>Stop:</strong> 5340 (45 pts, $225 risk)</div>
                  <div><strong style={{ color: "#e2e8f0" }}>Target:</strong> 5420 (35 pts, $175 reward)</div>
                  <div><strong style={{ color: "#e2e8f0" }}>R:R:</strong> 1:0.78</div>
                  <div><strong style={{ color: "#e2e8f0" }}>Account risk:</strong> 0.45%</div>
                </div>
                <div style={{ display: "flex", gap: "0.5rem", marginTop: "1rem" }}>
                  {[["✅ Approve", "#22c55e"], ["❌ Reject", "#ef4444"], ["📝 Modify", "#f59e0b"]].map(([label, color]) => (
                    <button key={label} style={{
                      background: `${color}20`, color, border: `1px solid ${color}40`,
                      borderRadius: 8, padding: "0.5rem 0.75rem", fontSize: "0.82rem",
                      fontWeight: 600, cursor: "pointer", flex: 1,
                    }}>{label}</button>
                  ))}
                </div>
                <div style={{ fontSize: "0.7rem", color: "#64748b", marginTop: "0.75rem", textAlign: "center" }}>
                  Expires in 15 minutes
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
