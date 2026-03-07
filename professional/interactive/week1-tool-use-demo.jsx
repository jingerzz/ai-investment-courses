import { useState, useEffect } from "react";

const STEPS = [
  {
    id: "question",
    label: "User Asks",
    icon: "💬",
    content: '"How is AAPL performing in my portfolio?"',
    detail: "You ask Claude in plain English. No special syntax needed.",
  },
  {
    id: "read",
    label: "AI Reads Tools",
    icon: "📖",
    content: "get_position_summary(ticker: str) → Position details including P&L, weight, risk",
    detail: "Claude reads the tool docstring to understand when and how to use it.",
  },
  {
    id: "decide",
    label: "AI Decides",
    icon: "🧠",
    content: 'I need position data for AAPL → call get_position_summary("AAPL")',
    detail: "Claude picks the right tool and fills in the parameters automatically.",
  },
  {
    id: "call",
    label: "Tool Executes",
    icon: "⚡",
    content: JSON.stringify(
      {
        ticker: "AAPL",
        shares: 150,
        avg_cost: 142.5,
        current_price: 178.32,
        unrealized_pnl: 5373.0,
        return_pct: 25.13,
        portfolio_weight_pct: 12.4,
        data_source: "live_feed",
        as_of: "2026-03-07T16:00:00Z",
      },
      null,
      2
    ),
    detail: "Python computes all numbers. The AI never does math — zero hallucination risk.",
  },
  {
    id: "synthesize",
    label: "AI Synthesizes",
    icon: "✨",
    content:
      "AAPL is your largest position at 12.4% of the portfolio. You're up $5,373 (+25.1%) on 150 shares with a cost basis of $142.50. Current price is $178.32 as of market close today (live data).",
    detail: "Claude interprets the structured data and explains it in natural language.",
  },
];

const BAD_APPROACH = {
  label: "Traditional: Dump Everything",
  flow: ["Dump 10,000 rows into prompt", "AI tries to find AAPL", "AI calculates P&L (might hallucinate)", "Generic response"],
  issues: ["Token waste", "Math errors", "No data freshness info", "Exposes all positions"],
};

const GOOD_APPROACH = {
  label: "Tool-Use: Structured Calls",
  flow: ["AI reads tool descriptions", "Calls get_position_summary('AAPL')", "Receives pre-computed JSON", "Interprets with context"],
  benefits: ["Only fetches what's needed", "Python does all math", "Includes data_source + timestamp", "Your data stays in your systems"],
};

export default function ToolUseDemo() {
  const [activeStep, setActiveStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [showComparison, setShowComparison] = useState(false);

  useEffect(() => {
    if (!isPlaying) return;
    if (activeStep >= STEPS.length - 1) {
      setIsPlaying(false);
      return;
    }
    const timer = setTimeout(() => setActiveStep((s) => s + 1), 2000);
    return () => clearTimeout(timer);
  }, [isPlaying, activeStep]);

  const play = () => {
    setActiveStep(0);
    setIsPlaying(true);
  };

  return (
    <div style={{ fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", background: "#0a0f1a", color: "#e2e8f0", minHeight: "100vh", padding: "2rem" }}>
      <div style={{ maxWidth: 900, margin: "0 auto" }}>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 700, marginBottom: "0.5rem" }}>Week 1: The Tool-Use Pattern</h1>
        <p style={{ color: "#94a3b8", marginBottom: "2rem" }}>How AI connects to your data through structured tools — not data dumps.</p>

        {/* Animated Flow */}
        <div style={{ background: "#111827", border: "1px solid #2a3a4e", borderRadius: 12, padding: "2rem", marginBottom: "2rem" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1.5rem" }}>
            <h2 style={{ fontSize: "1.1rem", fontWeight: 600 }}>Interactive Flow</h2>
            <button
              onClick={play}
              style={{
                background: "#3b82f6", color: "white", border: "none", borderRadius: 8,
                padding: "0.5rem 1.25rem", fontSize: "0.9rem", fontWeight: 600, cursor: "pointer",
              }}
            >
              {isPlaying ? "Playing..." : "▶ Play Animation"}
            </button>
          </div>

          {/* Steps */}
          <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
            {STEPS.map((step, i) => {
              const isActive = i === activeStep;
              const isPast = i < activeStep;
              return (
                <div
                  key={step.id}
                  onClick={() => { setIsPlaying(false); setActiveStep(i); }}
                  style={{
                    display: "flex", gap: "1rem", alignItems: "flex-start",
                    background: isActive ? "rgba(59,130,246,0.08)" : "transparent",
                    border: `1px solid ${isActive ? "#3b82f6" : "#2a3a4e"}`,
                    borderRadius: 10, padding: "1rem", cursor: "pointer",
                    opacity: isPast ? 0.5 : 1,
                    transition: "all 0.3s",
                  }}
                >
                  <div style={{
                    width: 40, height: 40, borderRadius: "50%",
                    background: isActive ? "#3b82f6" : isPast ? "#22c55e" : "#1a2332",
                    display: "flex", alignItems: "center", justifyContent: "center",
                    fontSize: "1.1rem", flexShrink: 0,
                    transition: "all 0.3s",
                  }}>
                    {isPast ? "✓" : step.icon}
                  </div>
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <div style={{ fontSize: "0.8rem", fontWeight: 600, color: "#3b82f6", marginBottom: "0.25rem" }}>
                      Step {i + 1}: {step.label}
                    </div>
                    <div style={{
                      background: "#0a0f1a", borderRadius: 6, padding: "0.75rem",
                      fontFamily: "monospace", fontSize: "0.85rem", lineHeight: 1.5,
                      whiteSpace: "pre-wrap", wordBreak: "break-word",
                      color: isActive ? "#e2e8f0" : "#64748b",
                      maxHeight: isActive ? 300 : 44, overflow: "hidden",
                      transition: "all 0.4s",
                    }}>
                      {step.content}
                    </div>
                    {isActive && (
                      <div style={{ fontSize: "0.85rem", color: "#94a3b8", marginTop: "0.5rem", fontStyle: "italic" }}>
                        {step.detail}
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Comparison Toggle */}
        <div style={{ background: "#111827", border: "1px solid #2a3a4e", borderRadius: 12, padding: "2rem" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1.5rem" }}>
            <h2 style={{ fontSize: "1.1rem", fontWeight: 600 }}>Why This Beats Data Dumps</h2>
            <button
              onClick={() => setShowComparison(!showComparison)}
              style={{
                background: "transparent", color: "#3b82f6", border: "1px solid #3b82f6",
                borderRadius: 8, padding: "0.5rem 1rem", fontSize: "0.85rem", cursor: "pointer",
              }}
            >
              {showComparison ? "Hide" : "Show"} Comparison
            </button>
          </div>

          {showComparison && (
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem" }}>
              {/* Bad */}
              <div style={{ background: "#1a2332", border: "1px solid rgba(239,68,68,0.3)", borderRadius: 10, padding: "1.25rem" }}>
                <div style={{ fontSize: "0.75rem", textTransform: "uppercase", letterSpacing: "0.1em", color: "#ef4444", fontWeight: 700, marginBottom: "1rem" }}>
                  {BAD_APPROACH.label}
                </div>
                {BAD_APPROACH.flow.map((step, i) => (
                  <div key={i} style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.5rem" }}>
                    <span style={{ color: "#ef4444", fontSize: "0.8rem" }}>✗</span>
                    <span style={{ fontSize: "0.85rem", color: "#94a3b8" }}>{step}</span>
                  </div>
                ))}
                <div style={{ borderTop: "1px solid #2a3a4e", marginTop: "0.75rem", paddingTop: "0.75rem" }}>
                  {BAD_APPROACH.issues.map((issue, i) => (
                    <span key={i} style={{
                      display: "inline-block", background: "rgba(239,68,68,0.1)", color: "#ef4444",
                      borderRadius: 12, padding: "0.2rem 0.6rem", fontSize: "0.75rem", margin: "0.15rem",
                    }}>
                      {issue}
                    </span>
                  ))}
                </div>
              </div>

              {/* Good */}
              <div style={{ background: "#1a2332", border: "1px solid rgba(34,197,94,0.3)", borderRadius: 10, padding: "1.25rem" }}>
                <div style={{ fontSize: "0.75rem", textTransform: "uppercase", letterSpacing: "0.1em", color: "#22c55e", fontWeight: 700, marginBottom: "1rem" }}>
                  {GOOD_APPROACH.label}
                </div>
                {GOOD_APPROACH.flow.map((step, i) => (
                  <div key={i} style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.5rem" }}>
                    <span style={{ color: "#22c55e", fontSize: "0.8rem" }}>✓</span>
                    <span style={{ fontSize: "0.85rem", color: "#94a3b8" }}>{step}</span>
                  </div>
                ))}
                <div style={{ borderTop: "1px solid #2a3a4e", marginTop: "0.75rem", paddingTop: "0.75rem" }}>
                  {GOOD_APPROACH.benefits.map((b, i) => (
                    <span key={i} style={{
                      display: "inline-block", background: "rgba(34,197,94,0.1)", color: "#22c55e",
                      borderRadius: 12, padding: "0.2rem 0.6rem", fontSize: "0.75rem", margin: "0.15rem",
                    }}>
                      {b}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Key Takeaway */}
        <div style={{
          marginTop: "2rem", background: "rgba(59,130,246,0.08)", border: "1px solid rgba(59,130,246,0.3)",
          borderRadius: 12, padding: "1.5rem", textAlign: "center",
        }}>
          <div style={{ fontSize: "1.1rem", fontWeight: 600, marginBottom: "0.5rem" }}>
            The Mental Model
          </div>
          <div style={{ color: "#94a3b8", fontSize: "0.95rem" }}>
            Think of AI as a new analyst who just joined your desk. They're smart — but they need access to your systems.
            MCP tools are the equivalent of giving them a login to your terminals.
          </div>
        </div>
      </div>
    </div>
  );
}
