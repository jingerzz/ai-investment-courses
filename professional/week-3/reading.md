# Week 3: Architecture — From Prototype to Production System

## 3.1 Multi-Server Architecture

In Weeks 1-2, you built a single MCP server with a few tools. In production,
you'll have multiple domains — each with its own data sources, update cadence,
and access requirements. The question is: one big server or several small ones?

### Why Separate Servers

Consider a real investment platform with these domains:

- **Market signals** — regime detection, technical indicators, trade plans
- **Risk management** — position limits, sector exposure, drawdown monitoring
- **Research / RAG** — SEC filing analysis, earnings transcript Q&A
- **Execution** — order management, fill tracking, trade journal

Putting everything in one server creates problems:

```
Monolithic server:
  ✗ Deploy risk fix → accidentally break signal computation
  ✗ Research intern needs filing access → gets trade execution tools too
  ✗ Signal server needs real-time data → research server only needs daily
  ✗ One crash takes down everything
```

Separate servers solve these:

```
Multi-server:
  ✓ Deploy independently — risk fix doesn't touch signals
  ✓ Permission per server — research gets RAG only
  ✓ Scale independently — signal server gets more resources
  ✓ Fault isolation — research crash doesn't affect trading
```

### The Shared Library Pattern

Separate servers doesn't mean duplicated code. Extract common functionality
into a shared library:

```
shared-library (trading-core):
  ├── brokers/          # Data provider clients (tastytrade, yfinance)
  ├── data/             # CSV I/O, bar merging, staleness detection
  ├── risk/             # Position sizing formulas
  ├── auth/             # OAuth provider, user management
  └── transport.py      # MCP server configuration (stdio vs HTTP)

signal-server:
  └── Uses: brokers, data, transport
      Adds: regime classification, signal tiers, trade plans

risk-server:
  └── Uses: brokers, data, risk, transport
      Adds: limit checking, sector analysis, drawdown monitoring

research-server:
  └── Uses: data, transport
      Adds: RAG indexing, document search, citation generation
```

Each server depends on the shared library for infrastructure, then adds its
domain-specific logic. When you fix a bug in the data layer, all servers
benefit. When you add a new signal type, only the signal server changes.

### Data Sharing

Multiple servers often need the same market data. Two approaches:

**Shared storage (simpler):** Servers read/write to a common data directory.
CSV files or a shared database. Works well when servers run on the same machine
or share a volume.

**Event-driven (scalable):** A data service fetches and publishes market data.
Servers subscribe to what they need. More complex but avoids conflicts.

For most investment teams, shared storage is sufficient. The key is **append-only
data** — servers add new bars, never modify existing ones (except for partial
bar updates where newer data has significantly more volume).

---

## 3.2 Data Provider Strategy

Your AI tools are only as good as the data feeding them. A production system
needs a deliberate data provider strategy.

### Primary / Fallback Hierarchy

Designate one provider as primary and one (or more) as fallback:

```python
async def get_daily_bars(ticker: str) -> dict:
    try:
        bars = await primary_provider.fetch(ticker)  # Real-time, full-featured
        return {"bars": bars, "data_source": "primary"}
    except DataUnavailableError:
        bars = await fallback_provider.fetch(ticker)  # Delayed, limited
        return {
            "bars": bars,
            "data_source": "fallback",
            "stale_data_warning": "Using delayed data — primary feed unavailable",
        }
```

The `data_source` field is critical. When the AI sees `"data_source": "fallback"`,
it can tell the user "Note: this analysis uses delayed data because the live feed
is down." Without this, stale data looks identical to fresh data.

### Staleness Detection

Market data goes stale in predictable ways:

- **After-hours fetch:** Last bar is from market close, not "now"
- **Partial session bar:** Futures bar captured mid-session has low volume
- **Weekend/holiday:** Friday's data on a Monday morning

Build staleness detection into your data layer:

```python
def is_stale(bar: DailyBar) -> bool:
    """A bar is stale if it's from before the most recent close."""
    now = datetime.now(timezone.utc)
    market_close = get_last_market_close(now)
    return bar.date < market_close.date()

def is_partial(bar: DailyBar) -> bool:
    """A futures bar with very low volume was likely captured mid-session."""
    return bar.volume < 100_000
```

When staleness is detected, include it in the tool return. The AI then decides
how to qualify its analysis — "Based on Friday's close" vs. presenting it as
if it's real-time.

### Provider Abstraction

Don't leak provider details into your tools. Use an abstract interface:

```python
from typing import Protocol

class DataProvider(Protocol):
    async def get_quote(self, ticker: str) -> Quote: ...
    async def get_daily_bars(self, ticker: str, days: int) -> list[DailyBar]: ...
    async def get_options_chain(self, ticker: str, expiry: str) -> OptionsChain: ...

class TastytradeProvider:
    """Full-featured: real-time quotes, options, futures, intraday."""
    async def get_quote(self, ticker: str) -> Quote: ...

class YFinanceProvider:
    """Fallback: daily bars only. No real-time, no options Greeks."""
    async def get_quote(self, ticker: str) -> Quote: ...
```

Tools call the `DataProvider` interface, not a specific implementation. Swapping
providers means changing one configuration line, not rewriting tools.

---

## 3.3 Authentication, Deployment, and Cost

### OAuth 2.1 for MCP

When your MCP servers run in the cloud, they need authentication. MCP uses
OAuth 2.1 with dynamic client registration:

```
1. AI client discovers OAuth endpoint at your server URL
2. Client redirects user to your login page
3. User authenticates (username/password, SSO, etc.)
4. Server issues access token (short-lived) + refresh token (long-lived)
5. Client auto-refreshes tokens — no manual key management
```

This is better than API keys because:
- **Tokens expire** — a leaked token is time-limited damage
- **Per-user identity** — audit trail shows *who* accessed what
- **Standard protocol** — any OAuth-capable client works
- **No key rotation** — refresh tokens handle lifecycle automatically

### Cloud Deployment

MCP servers are stateless HTTP services — they fit naturally into modern cloud
platforms. Key considerations:

**Auto-suspend:** If your AI tools are used during market hours only, choose a
platform that suspends idle containers. This can reduce cost from $50/month to
$2-5/month.

**Persistent storage:** Auth databases and cached data need persistent volumes
that survive container restarts and deploys.

**Health endpoints:** Every server should expose `/health` that returns:

```json
{
  "status": "healthy",
  "data_provider": "connected",
  "last_data_update": "2026-03-15T16:05:00Z",
  "uptime_seconds": 3600
}
```

This enables monitoring and alerting when a server loses its data connection.

### Cost Reality

A common objection to AI tools: "How much does this cost?" The answer is
usually surprisingly low:

```
Cloud hosting (auto-suspend):    $2-5/month per server
LLM API calls (Claude):         $5-20/month typical usage
Data provider (tastytrade):      $0 (free with brokerage account)
Total for 4 MCP servers:         ~$30-50/month
```

Compare this to: Bloomberg terminal ($24K/year), FactSet ($12K+/year), or
hiring an additional analyst. AI tools are an order of magnitude cheaper for
capabilities that complement (not replace) professional terminals.

---

## 3.4 Testing AI Tool Systems

AI tools need testing at three levels:

### Unit Tests (per tool)

Test each tool in isolation with known inputs:

```python
async def test_position_detail_known_ticker():
    result = await get_position_detail("AAPL")
    assert "error" not in result
    assert result["ticker"] == "AAPL"
    assert isinstance(result["unrealized_pnl"], float)
    assert "data_source" in result
    assert "as_of" in result

async def test_position_detail_unknown_ticker():
    result = await get_position_detail("INVALID")
    assert "error" in result
    assert "No position found" in result["error"]
```

### Integration Tests (data pipeline)

Test that data flows correctly from provider to tool:

```python
async def test_data_refresh_updates_signal():
    # Refresh data from provider
    await refresh_data(["SPY", "TLT"])
    # Signal should reflect new data
    signal = await get_current_signal()
    assert signal["as_of"]  # Has a timestamp
    assert signal["data_source"] != "cached"  # Used fresh data
```

### Smoke Tests (server startup)

Verify that servers start without import errors:

```python
def test_server_imports():
    """Catch missing dependencies or broken imports early."""
    import signal_server.mcp_server.server  # Should not raise
    import risk_server.mcp_server.server
    import research_server.mcp_server.server
```

This catches a surprisingly common failure: you add a new dependency to one
package but forget to include it in the server's requirements.

---

## Key Takeaways

1. **Separate servers per domain** — independent deployment, permissions, and scaling
2. **Shared library for infrastructure** — don't duplicate broker/data/auth code
3. **Tag data provenance** — every tool return includes `data_source` and freshness
4. **Staleness detection** — build it into the data layer, not the tool layer
5. **Provider abstraction** — tools call interfaces, not implementations
6. **OAuth over API keys** — expiring tokens, per-user identity, standard protocol
7. **Auto-suspend hosting** — production AI tools can cost $30-50/month total
8. **Test at three levels** — unit (tools), integration (pipelines), smoke (imports)
