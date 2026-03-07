import { useState } from "react";

const RAG_APPROACHES = {
  cloud: {
    label: "Cloud RAG",
    icon: "☁️",
    color: "#3b82f6",
    tagline: "Send documents to cloud AI for processing",
    pros: ["Best reasoning quality", "No local hardware requirements", "Easiest setup"],
    cons: ["Data leaves your machine", "API costs per query", "Not suitable for proprietary docs"],
    flow: [
      { step: "Upload", desc: "10-K filing → cloud API", icon: "📤", detail: "Document sent to provider" },
      { step: "Chunk", desc: "Split into ~500 token pieces", icon: "✂️", detail: "Blind splitting, no structure awareness" },
      { step: "Embed", desc: "Cloud embedding model → vectors", icon: "🔢", detail: "Stored in cloud vector DB" },
      { step: "Query", desc: "Question → cloud embedding → similarity search", icon: "🔍", detail: "Returns top-k similar chunks" },
      { step: "Answer", desc: "Cloud LLM synthesizes from chunks", icon: "🧠", detail: "Claude / GPT-4 quality reasoning" },
    ],
    bestFor: "Public SEC filings, market data analysis, complex multi-step research",
  },
  local: {
    label: "Local RAG",
    icon: "💻",
    color: "#22c55e",
    tagline: "Run everything on your own machine with Ollama",
    pros: ["Data never leaves your machine", "No API costs", "Regulatory compliance"],
    cons: ["Requires decent hardware", "Lower reasoning quality", "Slower processing"],
    flow: [
      { step: "Load", desc: "10-K filing stays on your machine", icon: "📁", detail: "Nothing uploaded anywhere" },
      { step: "Chunk", desc: "Split into ~500 token pieces", icon: "✂️", detail: "Same blind splitting approach" },
      { step: "Embed", desc: "Ollama nomic-embed-text → vectors", icon: "🔢", detail: "Stored in local file" },
      { step: "Query", desc: "Question → local embedding → cosine similarity", icon: "🔍", detail: "All computation on-device" },
      { step: "Answer", desc: "Ollama text model synthesizes", icon: "🧠", detail: "qwen3.5 — good but not cloud-tier" },
    ],
    bestFor: "Proprietary research notes, client reports, compliance docs, high-volume search",
  },
  structure: {
    label: "Structure-First RAG",
    icon: "🏗️",
    color: "#a78bfa",
    tagline: "Preserve document hierarchy — citations you can trust",
    pros: ["Citation-grade answers", "Section-aware search", "98.7% accuracy on FinanceBench"],
    cons: ["More complex indexing", "Requires document parsing", "Best with structured docs"],
    flow: [
      { step: "Parse", desc: "10-K → Item 1, 1A, 7, 8...", icon: "📑", detail: "Preserve section hierarchy" },
      { step: "Summarize", desc: "AI summarizes each section node", icon: "📝", detail: "Summaries for navigation only" },
      { step: "Index", desc: "Build tree of sections + summaries", icon: "🌳", detail: "Hierarchy, not flat chunks" },
      { step: "Navigate", desc: "AI reads summaries → finds right section", icon: "🧭", detail: "Like a table of contents" },
      { step: "Read Raw", desc: "Get FULL TEXT of target section", icon: "📄", detail: "Answers from raw text, not summaries" },
    ],
    bestFor: "SEC filings, legal docs, any document where section identity matters for citations",
  },
};

const RAM_TIERS = [
  {
    ram: "8 GB",
    model: "qwen3.5:0.8b",
    disk: "~1 GB",
    modelRam: "~1 GB",
    quality: "Good",
    qualityColor: "#f59e0b",
    qualityWidth: "40%",
    notes: "Basic Q&A and summaries. Pair with Claude for complex reasoning.",
  },
  {
    ram: "16 GB",
    model: "qwen3.5:4b",
    disk: "~3.4 GB",
    modelRam: "~3-4 GB",
    quality: "Great",
    qualityColor: "#22c55e",
    qualityWidth: "70%",
    notes: "Strong reasoning, accurate citations. Recommended for most users.",
    recommended: true,
  },
  {
    ram: "32+ GB",
    model: "qwen3.5:9b",
    disk: "~7 GB",
    modelRam: "~6-7 GB",
    quality: "Excellent",
    qualityColor: "#3b82f6",
    qualityWidth: "95%",
    notes: "Near cloud-quality for local use. Can run 4B + 9B side by side.",
  },
];

const HYBRID_PATTERN = [
  { layer: "Search & Retrieval", tool: "Local Ollama", reason: "Data stays private, no API cost", color: "#22c55e" },
  { layer: "Complex Reasoning", tool: "Cloud Claude", reason: "Best synthesis quality", color: "#3b82f6" },
  { layer: "Document Structure", tool: "Structure-First", reason: "Citation-grade accuracy", color: "#a78bfa" },
];

export default function RAGComparison() {
  const [activeApproach, setActiveApproach] = useState("cloud");
  const [activeTab, setActiveTab] = useState("compare");
  const [hoveredStep, setHoveredStep] = useState(null);
  const [selectedRam, setSelectedRam] = useState(1);

  const approach = RAG_APPROACHES[activeApproach];

  return (
    <div style={{ fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", background: "#0a0f1a", color: "#e2e8f0", minHeight: "100vh", padding: "2rem" }}>
      <div style={{ maxWidth: 960, margin: "0 auto" }}>
        <h1 style={{ fontSize: "1.75rem", fontWeight: 700, marginBottom: "0.5rem" }}>Bonus: RAG Approaches Compared</h1>
        <p style={{ color: "#94a3b8", marginBottom: "2rem" }}>Three ways to give AI access to your documents — each with different privacy, cost, and quality trade-offs.</p>

        {/* Tabs */}
        <div style={{ display: "flex", gap: 0, marginBottom: "2rem", borderBottom: "1px solid #2a3a4e" }}>
          {[["compare", "Compare Approaches"], ["ram", "RAM Calculator"], ["hybrid", "Hybrid Pattern"]].map(([id, label]) => (
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

        {/* COMPARE TAB */}
        {activeTab === "compare" && (
          <div>
            {/* Approach selector */}
            <div style={{ display: "flex", gap: "0.75rem", marginBottom: "2rem" }}>
              {Object.entries(RAG_APPROACHES).map(([key, val]) => (
                <div
                  key={key}
                  onClick={() => setActiveApproach(key)}
                  style={{
                    flex: 1, padding: "1.25rem", borderRadius: 14, cursor: "pointer",
                    background: activeApproach === key ? `${val.color}15` : "#111827",
                    border: `2px solid ${activeApproach === key ? val.color : "#2a3a4e"}`,
                    transition: "all 0.3s",
                    boxShadow: activeApproach === key ? `0 0 20px ${val.color}20` : "none",
                  }}
                >
                  <div style={{ fontSize: "1.5rem", marginBottom: "0.25rem" }}>{val.icon}</div>
                  <div style={{ fontWeight: 700, fontSize: "0.95rem", marginBottom: "0.25rem" }}>{val.label}</div>
                  <div style={{ fontSize: "0.78rem", color: "#94a3b8" }}>{val.tagline}</div>
                </div>
              ))}
            </div>

            {/* Flow diagram */}
            <div style={{ background: "#111827", borderRadius: 14, padding: "1.5rem", border: `1px solid ${approach.color}40`, marginBottom: "1.5rem" }}>
              <div style={{ fontSize: "0.75rem", fontWeight: 700, color: approach.color, textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: "1rem" }}>
                How {approach.label} processes a 10-K filing
              </div>
              <div style={{ display: "flex", alignItems: "flex-start", gap: "0.5rem", overflowX: "auto" }}>
                {approach.flow.map((step, i) => (
                  <div key={i} style={{ display: "flex", alignItems: "center" }}>
                    <div
                      onMouseEnter={() => setHoveredStep(i)}
                      onMouseLeave={() => setHoveredStep(null)}
                      style={{
                        minWidth: 130, padding: "1rem", borderRadius: 12, textAlign: "center",
                        background: hoveredStep === i ? `${approach.color}20` : "#0a0f1a",
                        border: `1px solid ${hoveredStep === i ? approach.color : "#2a3a4e"}`,
                        transition: "all 0.2s", cursor: "default",
                      }}
                    >
                      <div style={{ fontSize: "1.3rem", marginBottom: "0.35rem" }}>{step.icon}</div>
                      <div style={{ fontWeight: 700, fontSize: "0.82rem", marginBottom: "0.25rem" }}>{step.step}</div>
                      <div style={{ fontSize: "0.72rem", color: "#94a3b8", marginBottom: hoveredStep === i ? "0.5rem" : 0 }}>{step.desc}</div>
                      {hoveredStep === i && (
                        <div style={{ fontSize: "0.72rem", color: approach.color, fontStyle: "italic" }}>{step.detail}</div>
                      )}
                    </div>
                    {i < approach.flow.length - 1 && (
                      <div style={{ color: approach.color, fontSize: "1.2rem", margin: "0 0.15rem", flexShrink: 0 }}>→</div>
                    )}
                  </div>
                ))}
              </div>
            </div>

            {/* Pros / Cons / Best For */}
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", marginBottom: "1.5rem" }}>
              <div style={{ background: "#111827", borderRadius: 12, padding: "1.25rem", border: "1px solid #2a3a4e" }}>
                <div style={{ fontWeight: 700, color: "#22c55e", fontSize: "0.82rem", marginBottom: "0.75rem" }}>STRENGTHS</div>
                {approach.pros.map((p, i) => (
                  <div key={i} style={{ fontSize: "0.88rem", color: "#94a3b8", marginBottom: "0.4rem", display: "flex", gap: "0.5rem" }}>
                    <span style={{ color: "#22c55e" }}>✓</span> {p}
                  </div>
                ))}
              </div>
              <div style={{ background: "#111827", borderRadius: 12, padding: "1.25rem", border: "1px solid #2a3a4e" }}>
                <div style={{ fontWeight: 700, color: "#ef4444", fontSize: "0.82rem", marginBottom: "0.75rem" }}>TRADE-OFFS</div>
                {approach.cons.map((c, i) => (
                  <div key={i} style={{ fontSize: "0.88rem", color: "#94a3b8", marginBottom: "0.4rem", display: "flex", gap: "0.5rem" }}>
                    <span style={{ color: "#ef4444" }}>✗</span> {c}
                  </div>
                ))}
              </div>
            </div>

            <div style={{
              background: `${approach.color}08`, border: `1px solid ${approach.color}30`,
              borderRadius: 10, padding: "1rem", fontSize: "0.9rem",
            }}>
              <strong style={{ color: approach.color }}>Best for:</strong>{" "}
              <span style={{ color: "#94a3b8" }}>{approach.bestFor}</span>
            </div>
          </div>
        )}

        {/* RAM CALCULATOR TAB */}
        {activeTab === "ram" && (
          <div>
            <p style={{ color: "#94a3b8", marginBottom: "1.5rem" }}>
              Pick your machine's RAM to see which local model fits. All setups use <code style={{ color: "#a78bfa", background: "#1a2332", padding: "0.15rem 0.4rem", borderRadius: 4, fontSize: "0.85rem" }}>nomic-embed-text</code> (~300MB) for embeddings.
            </p>

            {/* RAM selector */}
            <div style={{ display: "flex", gap: "0.75rem", marginBottom: "2rem" }}>
              {RAM_TIERS.map((tier, i) => (
                <div
                  key={i}
                  onClick={() => setSelectedRam(i)}
                  style={{
                    flex: 1, padding: "1.25rem", borderRadius: 14, cursor: "pointer", textAlign: "center",
                    background: selectedRam === i ? "#1a2332" : "#111827",
                    border: `2px solid ${selectedRam === i ? tier.qualityColor : "#2a3a4e"}`,
                    transition: "all 0.3s", position: "relative",
                  }}
                >
                  {tier.recommended && (
                    <div style={{
                      position: "absolute", top: -10, left: "50%", transform: "translateX(-50%)",
                      background: "#22c55e", color: "#0a0f1a", fontSize: "0.65rem", fontWeight: 700,
                      padding: "0.15rem 0.5rem", borderRadius: 8,
                    }}>RECOMMENDED</div>
                  )}
                  <div style={{ fontSize: "1.5rem", fontWeight: 700, color: tier.qualityColor }}>{tier.ram}</div>
                  <div style={{ fontSize: "0.78rem", color: "#94a3b8", marginTop: "0.25rem" }}>RAM</div>
                </div>
              ))}
            </div>

            {/* Selected tier detail */}
            {(() => {
              const tier = RAM_TIERS[selectedRam];
              return (
                <div style={{ background: "#111827", borderRadius: 14, padding: "1.75rem", border: `1px solid ${tier.qualityColor}40` }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1.5rem" }}>
                    <div>
                      <div style={{ fontSize: "0.75rem", fontWeight: 700, color: tier.qualityColor, textTransform: "uppercase", letterSpacing: "0.1em" }}>
                        Your Setup
                      </div>
                      <div style={{ fontSize: "1.3rem", fontWeight: 700, marginTop: "0.25rem" }}>{tier.ram} Machine</div>
                    </div>
                    <div style={{
                      background: `${tier.qualityColor}20`, color: tier.qualityColor,
                      padding: "0.35rem 1rem", borderRadius: 10, fontWeight: 700, fontSize: "0.85rem",
                    }}>
                      {tier.quality}
                    </div>
                  </div>

                  {/* Model card */}
                  <div style={{
                    background: "#0a0f1a", borderRadius: 12, padding: "1.25rem", marginBottom: "1.25rem",
                    border: "1px solid #2a3a4e",
                  }}>
                    <div style={{ fontFamily: "monospace", fontSize: "1.1rem", fontWeight: 700, color: "#e2e8f0", marginBottom: "0.75rem" }}>
                      {tier.model}
                    </div>
                    <div style={{ display: "flex", gap: "2rem" }}>
                      <div>
                        <div style={{ fontSize: "0.72rem", color: "#64748b", textTransform: "uppercase" }}>Disk</div>
                        <div style={{ fontSize: "0.95rem", fontWeight: 600 }}>{tier.disk}</div>
                      </div>
                      <div>
                        <div style={{ fontSize: "0.72rem", color: "#64748b", textTransform: "uppercase" }}>RAM Usage</div>
                        <div style={{ fontSize: "0.95rem", fontWeight: 600 }}>{tier.modelRam}</div>
                      </div>
                      <div>
                        <div style={{ fontSize: "0.72rem", color: "#64748b", textTransform: "uppercase" }}>Embedding Model</div>
                        <div style={{ fontSize: "0.95rem", fontWeight: 600 }}>nomic-embed-text (~300MB)</div>
                      </div>
                    </div>
                  </div>

                  {/* Quality bar */}
                  <div style={{ marginBottom: "1rem" }}>
                    <div style={{ fontSize: "0.78rem", color: "#64748b", marginBottom: "0.35rem" }}>Answer Quality</div>
                    <div style={{ height: 8, background: "#0a0f1a", borderRadius: 4, overflow: "hidden" }}>
                      <div style={{ height: "100%", width: tier.qualityWidth, background: tier.qualityColor, borderRadius: 4, transition: "width 0.5s" }} />
                    </div>
                  </div>

                  <p style={{ color: "#94a3b8", fontSize: "0.9rem" }}>{tier.notes}</p>

                  {/* RAM breakdown visual */}
                  <div style={{ marginTop: "1.25rem" }}>
                    <div style={{ fontSize: "0.78rem", color: "#64748b", marginBottom: "0.5rem" }}>RAM Allocation</div>
                    <div style={{ display: "flex", height: 32, borderRadius: 8, overflow: "hidden", gap: 2 }}>
                      <div style={{ flex: parseInt(tier.modelRam), background: tier.qualityColor, display: "flex", alignItems: "center", justifyContent: "center", fontSize: "0.7rem", fontWeight: 600, minWidth: 60 }}>
                        Model
                      </div>
                      <div style={{ flex: 1, background: "#a78bfa40", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "0.7rem", fontWeight: 600, minWidth: 50 }}>
                        Embed
                      </div>
                      <div style={{ flex: parseInt(tier.ram) - parseInt(tier.modelRam) - 1, background: "#64748b40", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "0.7rem", fontWeight: 600 }}>
                        OS + Apps
                      </div>
                    </div>
                  </div>
                </div>
              );
            })()}
          </div>
        )}

        {/* HYBRID PATTERN TAB */}
        {activeTab === "hybrid" && (
          <div>
            <p style={{ color: "#94a3b8", marginBottom: "1.5rem" }}>
              The production pattern: use each approach where it's strongest. Local for privacy, cloud for reasoning, structure-first for accuracy.
            </p>

            <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem", marginBottom: "2rem" }}>
              {HYBRID_PATTERN.map((layer, i) => (
                <div key={i} style={{
                  background: "#111827", border: `1px solid ${layer.color}40`, borderRadius: 14,
                  padding: "1.25rem", display: "flex", alignItems: "center", gap: "1.25rem",
                }}>
                  <div style={{
                    background: `${layer.color}15`, color: layer.color,
                    padding: "0.5rem 1rem", borderRadius: 10, fontWeight: 700,
                    fontSize: "0.82rem", minWidth: 140, textAlign: "center",
                  }}>
                    {layer.tool}
                  </div>
                  <div style={{ flex: 1 }}>
                    <div style={{ fontWeight: 700, fontSize: "0.95rem" }}>{layer.layer}</div>
                    <div style={{ color: "#94a3b8", fontSize: "0.85rem" }}>{layer.reason}</div>
                  </div>
                </div>
              ))}
            </div>

            {/* Hybrid flow diagram */}
            <div style={{
              background: "#111827", borderRadius: 14, padding: "1.75rem",
              border: "1px solid #2a3a4e",
            }}>
              <div style={{ fontSize: "0.85rem", fontWeight: 700, color: "#e2e8f0", marginBottom: "1.25rem" }}>
                Example: "What are Apple's main risk factors?"
              </div>

              {[
                { step: "1", label: "Parse 10-K", desc: "Structure-first indexing preserves Item 1A section", color: "#a78bfa", icon: "🏗️" },
                { step: "2", label: "Embed locally", desc: "Ollama creates searchable vectors — data stays private", color: "#22c55e", icon: "💻" },
                { step: "3", label: "Search locally", desc: "Find Item 1A: Risk Factors via semantic match", color: "#22c55e", icon: "🔍" },
                { step: "4", label: "Read full section", desc: "Get raw text of Risk Factors (not just a summary)", color: "#a78bfa", icon: "📄" },
                { step: "5", label: "Claude reasons", desc: "Cloud AI synthesizes a cited answer from the raw text", color: "#3b82f6", icon: "🧠" },
              ].map((item, i) => (
                <div key={i} style={{ display: "flex", alignItems: "center", gap: "1rem", marginBottom: i < 4 ? "0.75rem" : 0 }}>
                  <div style={{
                    width: 36, height: 36, borderRadius: "50%",
                    background: `${item.color}20`, border: `1px solid ${item.color}`,
                    display: "flex", alignItems: "center", justifyContent: "center",
                    fontSize: "0.95rem", flexShrink: 0,
                  }}>
                    {item.icon}
                  </div>
                  <div style={{ flex: 1 }}>
                    <span style={{ fontWeight: 700, fontSize: "0.88rem" }}>{item.label}</span>
                    <span style={{ color: "#64748b", margin: "0 0.5rem" }}>—</span>
                    <span style={{ color: "#94a3b8", fontSize: "0.88rem" }}>{item.desc}</span>
                  </div>
                </div>
              ))}

              <div style={{
                marginTop: "1.25rem", padding: "1rem", background: "#0a0f1a",
                borderRadius: 10, fontSize: "0.85rem", color: "#94a3b8",
                borderLeft: `3px solid #3b82f6`,
              }}>
                <strong style={{ color: "#e2e8f0" }}>Result:</strong> "According to Item 1A (Risk Factors) of Apple's 10-K filing, the company identifies supply chain concentration, regulatory changes in key markets, and foreign exchange volatility as primary risk factors..."
                <div style={{ fontSize: "0.75rem", color: "#64748b", marginTop: "0.5rem" }}>
                  ↑ Citation-grade answer • Private data stayed local • Cloud AI did the reasoning
                </div>
              </div>
            </div>

            {/* Key insight */}
            <div style={{
              background: "rgba(167,139,250,0.08)", border: "1px solid rgba(167,139,250,0.2)",
              borderRadius: 10, padding: "1rem", marginTop: "1.5rem", fontSize: "0.9rem",
            }}>
              <strong style={{ color: "#a78bfa" }}>The sweet spot:</strong>{" "}
              <span style={{ color: "#94a3b8" }}>
                Use local models for document search and retrieval, cloud models for complex reasoning. Your MCP server uses Ollama to find the right passages, then Claude Desktop interprets them. Privacy where it matters, quality where it counts.
              </span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
