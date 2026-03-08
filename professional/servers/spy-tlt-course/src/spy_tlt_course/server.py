"""
MCP Server for SPY/TLT Color Strategy — Course Edition.

A standalone MCP server with 14 tools for learning MCP concepts.
No broker dependencies, no API keys — uses yfinance + bundled CSV data.

Run with:
    uv run spy-tlt-server          # starts on stdio (for Claude Desktop)
"""

from __future__ import annotations

import io
from contextlib import redirect_stdout
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional
from zoneinfo import ZoneInfo

from mcp.server.fastmcp import FastMCP

from spy_tlt_course.data import load_csv_bars, fetch_yfinance_bars, write_bars_csv
from spy_tlt_course.advisor import (
    build_rows,
    filter_rows_by_date,
    compute_strategy_returns,
    compute_trading_levels,
    compute_trade_plan,
    SIGNAL_PLAYBOOK,
    _find_pattern_matches,
    _forward_return,
)
from spy_tlt_course.spy_analysis import (
    load_data,
    analyze_extreme_moves,
    analyze_streaks,
    analyze_seasonal,
)

# ── Server configuration ─────────────────────────────────────────────────────

mcp = FastMCP(name="spy-tlt-course")

# Data paths — relative to this package
_DATA_DIR = Path(__file__).parent.parent.parent / "data"
SPY_CSV = _DATA_DIR / "SPY-history.csv"
TLT_CSV = _DATA_DIR / "TLT-history.csv"

# Cached state
_cached_rows: list[dict] | None = None
_cached_mtimes: tuple[float, float] = (0.0, 0.0)
_spy_stats_df = None


def _load_rows() -> list[dict]:
    """Load and process all strategy rows (cached by CSV mtime)."""
    global _cached_rows, _cached_mtimes
    mtimes = (
        SPY_CSV.stat().st_mtime if SPY_CSV.exists() else 0.0,
        TLT_CSV.stat().st_mtime if TLT_CSV.exists() else 0.0,
    )
    if _cached_rows is not None and mtimes == _cached_mtimes:
        return _cached_rows
    rows, _, _ = build_rows(spy_csv=SPY_CSV, tlt_csv=TLT_CSV, auto_fetch=False)
    _cached_rows = rows
    _cached_mtimes = mtimes
    return rows


def _invalidate_cache() -> None:
    global _cached_rows, _cached_mtimes
    _cached_rows = None
    _cached_mtimes = (0.0, 0.0)


def _get_spy_stats_df():
    global _spy_stats_df
    if _spy_stats_df is None:
        _spy_stats_df = load_data(str(SPY_CSV))
    return _spy_stats_df


class _SpyArgs:
    """Minimal args shim for spy_analysis functions."""
    def __init__(self, top: int = 10, threshold: float = 2.0):
        self.top = top
        self.threshold = threshold
        self.charts = False


def _capture(fn, *args, **kwargs) -> str:
    buf = io.StringIO()
    with redirect_stdout(buf):
        fn(*args, **kwargs)
    return buf.getvalue()


def _is_data_stale(data_date_str: str) -> tuple[bool, str]:
    """Check if strategy data is stale."""
    today = datetime.now(ZoneInfo("America/New_York")).date()
    try:
        data_date = datetime.strptime(data_date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return True, f"Cannot parse data date: {data_date_str!r}. Call refresh_data()."
    expected = today
    while expected.weekday() >= 5:
        expected -= timedelta(days=1)
    if data_date >= expected:
        return False, ""
    gap = (expected - data_date).days
    return True, (
        f"Data appears stale: latest row is {data_date_str} but expected "
        f"{expected.isoformat()} ({gap} day(s) behind). Call refresh_data()."
    )


# =============================================================================
# TOOL 1: STRATEGY GUIDE
# =============================================================================

@mcp.tool()
async def get_strategy_guide(topic: str = "all") -> dict:
    """Orientation guide for the SPY/TLT Color Strategy server.

    Call this first in every session. Returns an overview of all tools,
    recommended workflows, strategy concepts, and example scenarios.

    Args:
        topic: What to return. Options: all, tools, workflow, concepts, signals.
    """
    tool_catalog = {
        "strategy_core": [
            {"name": "get_strategy_guide", "purpose": "This tool. Call first to orient."},
            {"name": "get_current_signal", "purpose": "Today's signal, color, exposure, action."},
            {"name": "get_recent_history", "purpose": "Last N days of signals and actions."},
            {"name": "get_backtest_summary", "purpose": "Performance stats (CAGR, Sharpe, drawdown vs SPY B&H)."},
            {"name": "explain_signal", "purpose": "Detailed explanation of a specific signal."},
            {"name": "get_signal_list", "purpose": "All 9 signals organized by tier."},
            {"name": "get_trading_levels", "purpose": "SPY pivot points, SMAs, ATR, trade plan."},
            {"name": "analyze_pattern", "purpose": "Historical outcomes for a color sequence."},
            {"name": "refresh_data", "purpose": "Fetch latest data from Yahoo Finance. Call before every analysis."},
            {"name": "get_trade_briefing", "purpose": "Pre-formatted briefing with all numbers Python-inserted."},
        ],
        "spy_historical": [
            {"name": "spy_extreme_moves", "purpose": "Biggest gains/drops, return distribution."},
            {"name": "spy_streaks", "purpose": "Winning/losing streaks, what happens next."},
            {"name": "spy_seasonal", "purpose": "Day-of-week, monthly, yearly patterns."},
            {"name": "spy_summary", "purpose": "All three analyses combined."},
        ],
    }

    workflows = {
        "morning_briefing": [
            "1. refresh_data() — MANDATORY before any analysis",
            "2. get_trade_briefing() — complete briefing with signal, levels, plan",
            "3. Present the 'briefing' field directly — all numbers are pre-computed",
        ],
        "daily_signal_check": [
            "1. refresh_data()",
            "2. get_current_signal()",
            "3. If signal active → explain_signal(signal_name)",
        ],
        "historical_research": [
            "1. analyze_pattern(sequence='Blue,Red,Blue') — what happened historically",
            "2. spy_summary() — full SPY statistical analysis",
        ],
    }

    concepts = {
        "colors": {
            "Green": "SPY up, TLT up — risk-on, both equities and bonds rise",
            "Orange": "SPY up, TLT down — equity strength, bonds sold (complacency)",
            "Blue": "SPY down, TLT up — flight to safety (most actionable for this strategy)",
            "Red": "SPY down, TLT down — capitulation, no safe haven bid",
        },
        "signal_tiers": {
            "Tier 1": "Maximum conviction → 2.0x exposure (T1_BOTH_STRONG_BLUE, T1_STRONG_HIVOL_RED, T1_STRONG_RED_STREAK)",
            "Tier 2": "High conviction → 1.5x exposure (T2_STRONG_BLUE_NEGCORR, T2_WEAK_RED_EXHAUSTION, T2_GREEN_MOMENTUM, T2_SPY_DOWN_STREAK)",
            "Tier 3": "Moderate conviction → 1.25x exposure (T3_WEAK_BLUE_NEGCORR, T3_ORANGE_GRIND)",
        },
        "key_rules": [
            "Base position: always hold 1.0x SPY",
            "Max exposure: 2.0x, Min: 0.0x (danger state only)",
            "Danger state: 4+ consecutive Blue days (bull) or 3+ (bear) → exit to cash",
            "Greed trim: 5-day greed score >= 6.0 → close any active boost",
            "Pre-compute all numbers — AI interprets, Python calculates",
        ],
    }

    critical_rules = [
        "ALWAYS call refresh_data() before any signal or levels query.",
        "NEVER hallucinate price levels — only use tool output.",
        "When get_trade_briefing() returns a briefing field, present it verbatim.",
    ]

    result: dict[str, Any] = {"critical_rules": critical_rules}
    if topic in ("all", "tools"):
        result["tools"] = tool_catalog
    if topic in ("all", "workflow"):
        result["workflows"] = workflows
    if topic in ("all", "concepts"):
        result["concepts"] = concepts
    if topic in ("all", "signals"):
        result["signals"] = {
            name: {"title": info["title"], "trigger": info["trigger"]}
            for name, info in SIGNAL_PLAYBOOK.items()
        }
    return result


# =============================================================================
# TOOL 2: CURRENT SIGNAL
# =============================================================================

@mcp.tool()
async def get_current_signal() -> dict:
    """Get today's strategy signal, color classification, and recommended action.

    Returns the latest day's signal evaluation including color, signal name,
    tier, target exposure, and recommended action. Includes stale data
    warning if data needs refreshing.
    """
    try:
        rows = _load_rows()
    except Exception as e:
        return {"error": f"Failed to load strategy data: {e}"}

    if not rows:
        return {"error": "No strategy data available. Call refresh_data() first."}

    latest = rows[-1]
    stale, stale_msg = _is_data_stale(latest["date"])

    return {
        "date": latest["date"],
        "color": latest["color"],
        "signal": latest["signal"] or None,
        "tier": latest["tier"],
        "target_exposure": latest["target_exposure"],
        "action": latest["action"],
        "boost_action": latest["boost_action"],
        "boost_hold_days": latest["boost_hold_days"],
        "danger": latest["danger"],
        "greed_trim": latest["greed_trim"],
        "reason": latest["reason"],
        "signal_explainer": latest.get("signal_explainer") or None,
        "spy_close": latest["spy_close"],
        "spy_pct_change": round(latest["spy_pct_change"], 2),
        "tlt_close": latest["tlt_close"],
        "tlt_pct_change": round(latest["tlt_pct_change"], 2),
        "data_source": "yfinance + local CSV",
        "stale_data_warning": stale_msg if stale else None,
    }


# =============================================================================
# TOOL 3: RECENT HISTORY
# =============================================================================

@mcp.tool()
async def get_recent_history(days: int = 10) -> dict:
    """Get the last N trading days of strategy signals and actions.

    Args:
        days: Number of recent trading days to return (default 10, max 60).
    """
    try:
        rows = _load_rows()
    except Exception as e:
        return {"error": f"Failed to load data: {e}"}

    days = max(1, min(days, 60))
    recent = rows[-days:]

    return {
        "days_returned": len(recent),
        "history": [
            {
                "date": r["date"],
                "color": r["color"],
                "spy_close": r["spy_close"],
                "spy_pct_change": round(r["spy_pct_change"], 2),
                "tlt_close": r["tlt_close"],
                "tlt_pct_change": round(r["tlt_pct_change"], 2),
                "signal": r["signal"] or None,
                "tier": r["tier"],
                "target_exposure": r["target_exposure"],
                "action": r["action"],
            }
            for r in recent
        ],
        "data_source": "yfinance + local CSV",
    }


# =============================================================================
# TOOL 4: BACKTEST SUMMARY
# =============================================================================

@mcp.tool()
async def get_backtest_summary(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> dict:
    """Get strategy performance statistics vs SPY buy-and-hold.

    Returns CAGR, total return, max drawdown, and Sharpe ratio for both
    the strategy and SPY buy-and-hold over the specified period.

    Args:
        start_date: Optional start date (YYYY-MM-DD). Defaults to full history.
        end_date: Optional end date (YYYY-MM-DD). Defaults to latest data.
    """
    try:
        rows = _load_rows()
    except Exception as e:
        return {"error": f"Failed to load data: {e}"}

    start = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
    end = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
    filtered = filter_rows_by_date(rows, start=start, end=end)

    if len(filtered) < 10:
        return {"error": "Not enough data for meaningful backtest (need 10+ days)."}

    stats = compute_strategy_returns(filtered)
    stats["data_source"] = "yfinance + local CSV"
    stats["note"] = (
        "Backtest assumes fractional exposure compounding. "
        "No transaction costs, slippage, or margin interest included."
    )
    return stats


# =============================================================================
# TOOL 5: EXPLAIN SIGNAL
# =============================================================================

@mcp.tool()
async def explain_signal(signal_name: str) -> dict:
    """Get a detailed explanation of a specific strategy signal.

    Args:
        signal_name: Signal identifier (e.g., 'T1_BOTH_STRONG_BLUE').
                     Call get_signal_list() to see all available signals.
    """
    info = SIGNAL_PLAYBOOK.get(signal_name)
    if not info:
        return {
            "error": f"Unknown signal: {signal_name}",
            "available_signals": list(SIGNAL_PLAYBOOK.keys()),
        }
    return {
        "signal_name": signal_name,
        **info,
    }


# =============================================================================
# TOOL 6: SIGNAL LIST
# =============================================================================

@mcp.tool()
async def get_signal_list() -> dict:
    """List all 9 strategy signals organized by tier.

    Returns signal names, tiers, target exposures, and brief descriptions.
    """
    return {
        "tier_1_max_conviction": [
            {"name": "T1_BOTH_STRONG_BLUE", "exposure": "2.0x", "hold": "3 days",
             "trigger": "SPY down >1% AND TLT up >1%"},
            {"name": "T1_STRONG_HIVOL_RED", "exposure": "2.0x", "hold": "3 days",
             "trigger": "Red day, SPY down >1%, volume >1.5x average"},
            {"name": "T1_STRONG_RED_STREAK", "exposure": "2.0x", "hold": "1 day",
             "trigger": "3+ Red days with 2+ strong-down SPY days"},
        ],
        "tier_2_high_conviction": [
            {"name": "T2_STRONG_BLUE_NEGCORR", "exposure": "1.5x", "hold": "3 days",
             "trigger": "Strong Blue + SPY/TLT correlation < -0.3"},
            {"name": "T2_WEAK_RED_EXHAUSTION", "exposure": "1.5x", "hold": "1 day",
             "trigger": "3+ Red days, all with small moves (exhaustion)"},
            {"name": "T2_GREEN_MOMENTUM", "exposure": "1.5x (2.0x in bull trend)", "hold": "streak-based",
             "trigger": "3+ Green days continuing"},
            {"name": "T2_SPY_DOWN_STREAK", "exposure": "1.5x", "hold": "1 day",
             "trigger": "SPY down 4+ consecutive days"},
        ],
        "tier_3_moderate_conviction": [
            {"name": "T3_WEAK_BLUE_NEGCORR", "exposure": "1.25x", "hold": "3 days",
             "trigger": "Weak Blue + SPY/TLT correlation < -0.3"},
            {"name": "T3_ORANGE_GRIND", "exposure": "1.25x", "hold": "streak-based",
             "trigger": "3+ consecutive Orange days"},
        ],
        "note": "Signals are evaluated top-down in priority order. First match wins.",
    }


# =============================================================================
# TOOL 7: TRADING LEVELS
# =============================================================================

@mcp.tool()
async def get_trading_levels(days: int = 5) -> dict:
    """Get SPY pivot points, support/resistance, SMAs, ATR, and a trade plan.

    Computes standard floor-trader pivots from the most recent session's OHLC,
    plus 50d/200d SMAs and ATR(14). Includes a signal-calibrated trade plan
    when a boost signal is active.

    Args:
        days: Number of days of daily level history to include (default 5).
    """
    try:
        rows = _load_rows()
        spy_bars = load_csv_bars(SPY_CSV)
    except Exception as e:
        return {"error": f"Failed to load data: {e}"}

    levels = compute_trading_levels(spy_bars, history_days=days)
    if "error" in levels:
        return levels

    # Add trade plan based on current signal
    latest = rows[-1] if rows else {}
    plan = compute_trade_plan(
        signal_name=latest.get("signal") or None,
        tier=latest.get("tier"),
        target_exposure=latest.get("target_exposure", 1.0),
        danger=latest.get("danger", False),
        spy_levels=levels["spy"],
    )
    levels["trade_plan"] = plan
    levels["data_source"] = "yfinance + local CSV"

    stale, stale_msg = _is_data_stale(latest.get("date", ""))
    if stale:
        levels["stale_data_warning"] = stale_msg

    return levels


# =============================================================================
# TOOL 8: ANALYZE PATTERN
# =============================================================================

@mcp.tool()
async def analyze_pattern(
    sequence: str,
    horizons: str = "1,3,5",
) -> dict:
    """Analyze historical outcomes for a specific color sequence.

    Example: sequence='Blue,Red,Blue' finds all times this pattern occurred
    and shows what happened next (forward returns at various horizons).

    Args:
        sequence: Comma-separated colors (e.g., 'Blue,Red,Blue').
        horizons: Comma-separated forward return horizons in trading days (default '1,3,5').
    """
    try:
        rows = _load_rows()
    except Exception as e:
        return {"error": f"Failed to load data: {e}"}

    # Parse sequence
    colors = []
    for c in sequence.split(","):
        c = c.strip().capitalize()
        if c not in {"Green", "Orange", "Blue", "Red"}:
            return {"error": f"Invalid color '{c}'. Use: Green, Orange, Blue, Red"}
        colors.append(c)

    # Parse horizons
    try:
        horizon_list = sorted(set(int(h.strip()) for h in horizons.split(",")))
    except ValueError:
        return {"error": "Horizons must be comma-separated integers (e.g., '1,3,5')."}

    matches = _find_pattern_matches(rows, colors, None, None)

    # Compute forward stats
    forward_stats = {}
    for h in horizon_list:
        rets = [_forward_return(rows, idx, h) for idx in matches]
        valid = [r for r in rets if r is not None]
        if valid:
            up = sum(1 for r in valid if r > 0)
            avg = sum(valid) / len(valid)
            forward_stats[f"{h}d"] = {
                "observations": len(valid),
                "up_pct": round(up / len(valid) * 100, 1),
                "avg_return_pct": round(avg * 100, 2),
            }

    # Current window
    current = rows[-len(colors):] if len(rows) >= len(colors) else []
    current_colors = [r["color"] for r in current] if current else []
    matches_now = current_colors == colors

    return {
        "pattern": " -> ".join(colors),
        "total_matches": len(matches),
        "forward_stats": forward_stats,
        "current_window": {
            "colors": current_colors,
            "matches_now": matches_now,
            "dates": f"{current[0]['date']} -> {current[-1]['date']}" if current else None,
        },
        "recent_matches": [
            {
                "end_date": rows[idx]["date"],
                "next_1d_return": round(_forward_return(rows, idx, 1) * 100, 2)
                if _forward_return(rows, idx, 1) is not None else None,
            }
            for idx in matches[-10:]
        ],
        "data_source": "yfinance + local CSV",
    }


# =============================================================================
# TOOL 9: REFRESH DATA
# =============================================================================

@mcp.tool()
async def refresh_data() -> dict:
    """Fetch the latest SPY and TLT data from Yahoo Finance.

    CALL THIS BEFORE EVERY ANALYSIS. Updates the local CSV files with
    any new trading days since the last refresh.
    """
    try:
        rows, fetched_spy, fetched_tlt = build_rows(
            spy_csv=SPY_CSV, tlt_csv=TLT_CSV, auto_fetch=True,
        )
        _invalidate_cache()

        latest = rows[-1] if rows else {}
        return {
            "status": "ok",
            "new_spy_bars": fetched_spy,
            "new_tlt_bars": fetched_tlt,
            "latest_date": latest.get("date"),
            "latest_color": latest.get("color"),
            "latest_signal": latest.get("signal") or None,
            "total_trading_days": len(rows),
            "data_source": "yfinance",
        }
    except Exception as e:
        return {"error": f"Refresh failed: {e}"}


# =============================================================================
# TOOL 10: TRADE BRIEFING (pre-formatted template)
# =============================================================================

@mcp.tool()
async def get_trade_briefing() -> dict:
    """Get a complete pre-formatted morning/evening briefing.

    Returns a ready-to-display markdown briefing with all numbers
    pre-computed by Python. The AI should present the 'briefing' field
    verbatim — do not round, recalculate, or reformat any numbers.

    This is the primary tool for daily briefings.
    """
    try:
        rows = _load_rows()
        spy_bars = load_csv_bars(SPY_CSV)
    except Exception as e:
        return {"error": f"Failed to load data: {e}"}

    if not rows:
        return {"error": "No data available. Call refresh_data() first."}

    latest = rows[-1]
    levels = compute_trading_levels(spy_bars, history_days=1)
    spy_lvl = levels.get("spy", {})

    plan = compute_trade_plan(
        signal_name=latest.get("signal") or None,
        tier=latest.get("tier"),
        target_exposure=latest.get("target_exposure", 1.0),
        danger=latest.get("danger", False),
        spy_levels=spy_lvl,
    )

    # Determine regime
    sma50 = spy_lvl.get("sma50")
    sma200 = spy_lvl.get("sma200")
    spy_close = latest["spy_close"]
    if sma50 and sma200:
        if spy_close > sma50 and spy_close > sma200:
            regime = "Bull (above SMA50 and SMA200)"
        elif spy_close < sma200:
            regime = "Bear (below SMA200)"
        else:
            regime = "Mixed"
    else:
        regime = "Insufficient data for regime classification"

    # Stale check
    stale, stale_msg = _is_data_stale(latest["date"])

    # Build briefing
    signal_text = latest["signal"] or "None"
    tier_text = f"Tier {latest['tier']}" if latest["tier"] else "No active signal"

    lines = [
        f"## Trade Briefing — {latest['date']}",
        "",
    ]
    if stale:
        lines.append(f"**WARNING:** {stale_msg}")
        lines.append("")

    lines.extend([
        f"**Signal:** {signal_text} ({tier_text})",
        f"**Target Exposure:** {latest['target_exposure']:.2f}x",
        f"**Action:** {latest['action']}",
        f"**Color:** {latest['color']} (SPY {latest['spy_pct_change']:+.2f}%, TLT {latest['tlt_pct_change']:+.2f}%)",
        f"**Regime:** {regime}",
        "",
        "### Key SPY Levels",
        f"| Level | Price |",
        f"|-------|-------|",
        f"| R3 | {spy_lvl.get('r3', 'N/A')} |",
        f"| R2 | {spy_lvl.get('r2', 'N/A')} |",
        f"| R1 | {spy_lvl.get('r1', 'N/A')} |",
        f"| **Pivot** | **{spy_lvl.get('pivot', 'N/A')}** |",
        f"| S1 | {spy_lvl.get('s1', 'N/A')} |",
        f"| S2 | {spy_lvl.get('s2', 'N/A')} |",
        f"| S3 | {spy_lvl.get('s3', 'N/A')} |",
        "",
        f"SMA50: {spy_lvl.get('sma50', 'N/A')} | SMA200: {spy_lvl.get('sma200', 'N/A')} | ATR(14): {spy_lvl.get('atr14', 'N/A')}",
        "",
    ])

    if plan["state"] == "ACTIVE":
        entry = plan["entry_zone"]
        stop = plan["stop"]
        t1 = plan["target_1"]
        lines.extend([
            f"### Trade Plan ({plan['trade_type']})",
            f"- **Entry zone:** {entry['low']} - {entry['high']}",
            f"- **Stop:** {stop['price']} ({stop['level_name']}) — {stop.get('risk_pts', 'N/A')} pts risk",
            f"- **Target 1:** {t1['price']} ({t1['level_name']}) — R:R {t1.get('rr', 'N/A')}",
            f"- **Target 2:** {plan['target_2']['price']} ({plan['target_2']['level_name']})",
        ])
    elif plan["state"] == "FLAT":
        lines.append(f"### Position: FLAT (Danger State)")
        lines.append(f"_{plan['note']}_")
    else:
        lines.append(f"### Position: BASE ({plan['exposure']:.1f}x)")
        lines.append(f"_{plan['note']}_")

    if latest.get("signal_explainer"):
        lines.extend(["", "### Signal Detail", latest["signal_explainer"]])

    if latest.get("reason"):
        lines.extend(["", f"**Reason:** {latest['reason']}"])

    briefing = "\n".join(lines)

    return {
        "briefing": briefing,
        "present_verbatim": True,
        "signal": latest["signal"] or None,
        "color": latest["color"],
        "regime": regime,
        "data_source": "yfinance + local CSV",
        "stale_data_warning": stale_msg if stale else None,
        "as_of": latest["date"],
    }


# =============================================================================
# TOOLS 11-14: SPY HISTORICAL ANALYSIS
# =============================================================================

@mcp.tool()
async def spy_extreme_moves(top: int = 10, threshold: float = 2.0) -> dict:
    """Analyze the biggest single-day SPY gains and drops in history.

    Returns distribution statistics, threshold frequency counts, and
    lists of the top N gains and drops.

    Args:
        top: Number of extreme moves to show (default 10).
        threshold: Percentage threshold for frequency counts (default 2.0).
    """
    try:
        df = _get_spy_stats_df()
        output = _capture(analyze_extreme_moves, df, _SpyArgs(top=top, threshold=threshold))
        return {"analysis": output, "data_source": "SPY-history.csv"}
    except Exception as e:
        return {"error": f"Analysis failed: {e}"}


@mcp.tool()
async def spy_streaks() -> dict:
    """Analyze SPY winning and losing streak patterns.

    Returns top streaks, streak length distribution, and 'what happens next'
    analysis showing average next-day returns after N consecutive up/down days.
    """
    try:
        df = _get_spy_stats_df()
        output = _capture(analyze_streaks, df, _SpyArgs())
        return {"analysis": output, "data_source": "SPY-history.csv"}
    except Exception as e:
        return {"error": f"Analysis failed: {e}"}


@mcp.tool()
async def spy_seasonal() -> dict:
    """Analyze SPY seasonal and calendar patterns.

    Returns average daily returns by day of week, by month, and annual
    summaries from 1993 to present.
    """
    try:
        df = _get_spy_stats_df()
        output = _capture(analyze_seasonal, df, _SpyArgs())
        return {"analysis": output, "data_source": "SPY-history.csv"}
    except Exception as e:
        return {"error": f"Analysis failed: {e}"}


@mcp.tool()
async def spy_summary(top: int = 10, threshold: float = 2.0) -> dict:
    """Run all three SPY analyses (extreme moves + streaks + seasonal) combined.

    Args:
        top: Number of extreme moves to show (default 10).
        threshold: Percentage threshold for frequency counts (default 2.0).
    """
    try:
        df = _get_spy_stats_df()
        args = _SpyArgs(top=top, threshold=threshold)
        output = (
            _capture(analyze_extreme_moves, df, args)
            + _capture(analyze_streaks, df, args)
            + _capture(analyze_seasonal, df, args)
        )
        return {"analysis": output, "data_source": "SPY-history.csv"}
    except Exception as e:
        return {"error": f"Analysis failed: {e}"}


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Run the MCP server on stdio transport."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
