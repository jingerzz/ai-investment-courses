"""
Daily trading advisor for the TLT/SPY Color Day strategy — Course Edition.

Standalone version with no trading-core dependencies.
"""

from __future__ import annotations

import csv
import math
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, TypedDict

from spy_tlt_course.data import (
    DailyBar,
    load_csv_bars,
    write_bars_csv,
    fetch_yfinance_bars,
    merge_auto_fetch,
    _format_change_pct,
)


class StrategyRow(TypedDict):
    date: str
    color: str
    spy_close: float
    spy_abs_change: float
    spy_pct_change: float
    tlt_close: float
    tlt_abs_change: float
    tlt_pct_change: float
    signal: str
    tier: int
    target_exposure: float
    action: str
    boost_action: str
    boost_hold_days: int
    danger: bool
    greed_trim: bool
    reason: str
    signal_detail: str
    signal_explainer: str


# ── Signal playbook ──────────────────────────────────────────────────────────

SIGNAL_PLAYBOOK = {
    "T1_BOTH_STRONG_BLUE": {
        "title": "Both-Strong Blue (Tier 1)",
        "trigger": "SPY down >1% and TLT up >1% on the same day.",
        "meaning": "Acute risk-off shock: equities are sold while long Treasuries are bought aggressively.",
        "sizing": "Maximum conviction — target 2.0x for 3 days.",
        "statistical_framing": "High-quality mean-reversion setup in the 2002-2026 backtest.",
        "risk": "If stress is persistent, rebounds can fail; leverage amplifies that drawdown.",
    },
    "T1_STRONG_HIVOL_RED": {
        "title": "Strong High-Volume Red (Tier 1)",
        "trigger": "Red day with SPY down >1% and SPY volume >1.5x its 20-day average.",
        "meaning": "Capitulation-style selling can exhaust sellers and produce sharp rebound pressure.",
        "sizing": "Tier 1: 2.0x target exposure for 3 days.",
        "statistical_framing": "Uses extreme downside + participation (volume) as a stronger reversal proxy.",
        "risk": "High volume can also confirm trend continuation in crash regimes.",
    },
    "T1_STRONG_RED_STREAK": {
        "title": "Strong Red Streak (Tier 1)",
        "trigger": "At least 3 Red days, with at least 2 strong down SPY days in that streak.",
        "meaning": "Clustered panic often leads to a short snapback window.",
        "sizing": "2.0x but only 1-day hold to target the immediate bounce.",
        "statistical_framing": "Short-horizon mean-reversion setup, not a trend call.",
        "risk": "In regime breaks, panic can persist beyond one day.",
    },
    "T2_STRONG_BLUE_NEGCORR": {
        "title": "Strong Blue + Negative Correlation (Tier 2)",
        "trigger": "Strong Blue day and 20-day SPY/TLT correlation < -0.3.",
        "meaning": "Flight-to-safety mechanics are functioning normally, supporting reversal logic.",
        "sizing": "High confidence but below Tier 1: 1.5x for 3 days.",
        "statistical_framing": "Cross-asset confirmation improves quality versus a standalone SPY drop.",
        "risk": "Correlation can destabilize quickly during macro shocks.",
    },
    "T2_WEAK_RED_EXHAUSTION": {
        "title": "Weak Red Exhaustion (Tier 2)",
        "trigger": "At least 3 Red days in a row, none with SPY drop >1%.",
        "meaning": "Persistent but shallow selling can indicate weakening downside impulse.",
        "sizing": "1.5x for 1 day, aiming to capture a near-term relief bounce.",
        "statistical_framing": "Weaker than capitulation signals, so hold and size are restrained.",
        "risk": "Shallow selling can still transition into stronger declines.",
    },
    "T2_GREEN_MOMENTUM": {
        "title": "Green Momentum (Tier 2)",
        "trigger": "At least 3 Green days in a row, latest day not strong.",
        "meaning": "Broad, orderly risk-on behavior may continue.",
        "sizing": "Base 1.5x; upgrades to 2.0x when SPY is above both 50d and 200d SMA.",
        "statistical_framing": "Continuation logic rather than panic-reversal logic.",
        "risk": "Momentum can reverse abruptly after extended runs.",
    },
    "T2_SPY_DOWN_STREAK": {
        "title": "SPY Down Streak (Tier 2)",
        "trigger": "SPY closes down 4 or more consecutive days.",
        "meaning": "Short-term downside streaks often mean-revert at least partially.",
        "sizing": "1.5x for 1 day only, focused on next-day bounce probability.",
        "statistical_framing": "Tactical setup with narrow holding horizon.",
        "risk": "Serial declines can continue during macro repricing events.",
    },
    "T3_WEAK_BLUE_NEGCORR": {
        "title": "Weak Blue + Negative Correlation (Tier 3)",
        "trigger": "Blue day, SPY decline <=1%, and 20-day correlation < -0.3.",
        "meaning": "Mild risk-off signal with supportive cross-asset structure.",
        "sizing": "Moderate confidence: 1.25x for 3 days.",
        "statistical_framing": "Lower edge than strong-signal variants; size is reduced accordingly.",
        "risk": "Noise and whipsaw risk are higher than Tier 1/2 setups.",
    },
    "T3_ORANGE_GRIND": {
        "title": "Orange Grind (Tier 3)",
        "trigger": "At least 3 consecutive Orange days (SPY up, TLT down).",
        "meaning": "Equity strength despite bond weakness can signal persistent risk appetite.",
        "sizing": "Moderate add: 1.25x while Orange streak persists.",
        "statistical_framing": "Lower-conviction continuation pattern.",
        "risk": "Rate-driven pressure can eventually weigh on equities as well.",
    },
}


# ── Helpers ──────────────────────────────────────────────────────────────────

def _describe_action(result: dict) -> str:
    target = float(result["target_exposure"])
    boost_action = result.get("boost_action", "NONE")
    if target <= 0.0:
        return "Exit SPY; hold cash (0.0x) next open"
    if math.isclose(target, 1.0, rel_tol=0.0, abs_tol=1e-9):
        if boost_action == "CLOSE":
            return "Close boost; return to 1.0x next open"
        return "Hold base SPY at 1.0x"
    if boost_action == "OPEN":
        return f"Add SPY to {target:.2f}x at next open"
    if boost_action == "HOLD":
        return f"Maintain SPY at {target:.2f}x"
    return f"Target SPY exposure: {target:.2f}x"


def _describe_signal(result: dict) -> str:
    signal = str(result.get("signal", "") or "")
    if not signal:
        return ""
    tier = int(result.get("tier", 0))
    boost_action = str(result.get("boost_action", "NONE"))
    hold_days = int(result.get("boost_hold_days", 0))
    hold_text = f"{hold_days}d" if hold_days > 0 else "streak-based"
    return f"Tier {tier} | {signal} | {boost_action} | {hold_text}"


def _build_signal_explainer(result: dict) -> str:
    signal = str(result.get("signal", "") or "")
    if not signal:
        return ""
    info = SIGNAL_PLAYBOOK.get(signal)
    if not info:
        return ""
    hold_days = int(result.get("boost_hold_days", 0))
    hold_text = f"{hold_days} trading day(s)" if hold_days > 0 else "until streak condition breaks"
    target = float(result.get("target_exposure", 1.0))
    lines = [
        f"{info['title']}",
        f"Trigger: {info['trigger']}",
        f"What it means: {info['meaning']}",
        f"Action confidence framing: {info['statistical_framing']}",
        f"Why {target:.2f}x / {hold_text}: {info['sizing']}",
        f"Risk check: {info['risk']}",
    ]
    return "\n".join(lines)


def join_market_data(
    spy_bars: Dict[date, DailyBar],
    tlt_bars: Dict[date, DailyBar],
) -> List[Tuple[date, DailyBar, DailyBar]]:
    common_dates = sorted(set(spy_bars).intersection(tlt_bars))
    return [(d, spy_bars[d], tlt_bars[d]) for d in common_dates]


def run_strategy_rows(
    joined: List[Tuple[date, DailyBar, DailyBar]],
) -> List[StrategyRow]:
    from spy_tlt_course.strategy import ColorStrategy

    strategy = ColorStrategy(use_breadth=False)
    rows: List[dict] = []
    prev_spy_close: Optional[float] = None
    prev_tlt_close: Optional[float] = None

    for day, spy, tlt in joined:
        result = strategy.evaluate(
            date=day.isoformat(),
            spy_open=spy.open,
            spy_close=spy.close,
            spy_volume=spy.volume,
            tlt_close=tlt.close,
        )

        if prev_spy_close is None:
            spy_abs = spy_pct = tlt_abs = tlt_pct = 0.0
        else:
            spy_abs = spy.close - prev_spy_close
            tlt_abs = tlt.close - prev_tlt_close
            spy_pct = (spy_abs / prev_spy_close) * 100.0 if prev_spy_close else 0.0
            tlt_pct = (tlt_abs / prev_tlt_close) * 100.0 if prev_tlt_close else 0.0

        prev_spy_close = spy.close
        prev_tlt_close = tlt.close

        rows.append({
            "date": day.isoformat(),
            "color": result["color"],
            "spy_close": spy.close,
            "spy_abs_change": spy_abs,
            "spy_pct_change": spy_pct,
            "tlt_close": tlt.close,
            "tlt_abs_change": tlt_abs,
            "tlt_pct_change": tlt_pct,
            "target_exposure": float(result["target_exposure"]),
            "action": _describe_action(result),
            "signal_detail": _describe_signal(result),
            "signal": result["signal"],
            "tier": int(result["tier"]),
            "boost_action": result["boost_action"],
            "boost_hold_days": int(result["boost_hold_days"]),
            "danger": bool(result["danger"]),
            "greed_trim": bool(result["greed_trim"]),
            "reason": result["reason"],
            "signal_explainer": _build_signal_explainer(result),
        })
    return rows


def filter_rows_by_date(
    rows: List[dict],
    start: Optional[date],
    end: Optional[date],
) -> List[dict]:
    out: List[dict] = []
    for row in rows:
        d = datetime.strptime(row["date"], "%Y-%m-%d").date()
        if start and d < start:
            continue
        if end and d > end:
            continue
        out.append(row)
    return out


def _forward_return(rows: List[dict], idx: int, horizon: int) -> Optional[float]:
    if idx + horizon >= len(rows):
        return None
    start = float(rows[idx]["spy_close"])
    end = float(rows[idx + horizon]["spy_close"])
    if start == 0:
        return None
    return (end / start) - 1.0


def _find_pattern_matches(
    rows: List[dict],
    sequence: List[str],
    require_last_signal: Optional[str],
    require_last_boost_action: Optional[str],
) -> List[int]:
    k = len(sequence)
    matches: List[int] = []
    for end_idx in range(k - 1, len(rows)):
        window = rows[end_idx - k + 1 : end_idx + 1]
        if [w["color"] for w in window] != sequence:
            continue
        last = rows[end_idx]
        if require_last_signal and str(last.get("signal", "")) != require_last_signal:
            continue
        if require_last_boost_action and str(last.get("boost_action", "")).upper() != require_last_boost_action:
            continue
        matches.append(end_idx)
    return matches


def compute_strategy_returns(rows: List[dict], start_value: float = 10000.0) -> dict:
    """Compute compounded P&L for strategy vs SPY buy-and-hold."""
    if len(rows) < 2:
        return {}

    equity = start_value
    bah = start_value
    peak_equity = equity
    peak_bah = bah
    max_dd = 0.0
    max_dd_bah = 0.0
    daily_strat_returns: List[float] = []

    for i in range(1, len(rows)):
        spy_ret = rows[i]["spy_pct_change"] / 100.0
        exposure = rows[i - 1]["target_exposure"]
        strat_ret = exposure * spy_ret
        daily_strat_returns.append(strat_ret)

        equity *= 1.0 + strat_ret
        bah *= 1.0 + spy_ret

        if equity > peak_equity:
            peak_equity = equity
        dd = (equity - peak_equity) / peak_equity
        if dd < max_dd:
            max_dd = dd

        if bah > peak_bah:
            peak_bah = bah
        dd_bah = (bah - peak_bah) / peak_bah
        if dd_bah < max_dd_bah:
            max_dd_bah = dd_bah

    start_dt = datetime.strptime(rows[0]["date"], "%Y-%m-%d").date()
    end_dt = datetime.strptime(rows[-1]["date"], "%Y-%m-%d").date()
    years = (end_dt - start_dt).days / 365.25

    total_ret = (equity / start_value) - 1.0
    total_ret_bah = (bah / start_value) - 1.0
    cagr = (equity / start_value) ** (1.0 / years) - 1.0 if years > 0 else 0.0
    cagr_bah = (bah / start_value) ** (1.0 / years) - 1.0 if years > 0 else 0.0

    n = len(daily_strat_returns)
    if n > 1:
        mean_r = sum(daily_strat_returns) / n
        variance = sum((r - mean_r) ** 2 for r in daily_strat_returns) / (n - 1)
        std_r = math.sqrt(variance)
        sharpe = (mean_r / std_r) * math.sqrt(252) if std_r > 0 else 0.0
    else:
        sharpe = 0.0

    return {
        "period": {
            "start": rows[0]["date"],
            "end": rows[-1]["date"],
            "trading_days": len(rows),
            "years": round(years, 2),
        },
        "starting_capital": start_value,
        "strategy": {
            "ending_value": round(equity, 2),
            "total_return_pct": round(total_ret * 100, 2),
            "cagr_pct": round(cagr * 100, 2),
            "max_drawdown_pct": round(max_dd * 100, 2),
            "sharpe_ratio": round(sharpe, 2),
        },
        "spy_buy_and_hold": {
            "ending_value": round(bah, 2),
            "total_return_pct": round(total_ret_bah * 100, 2),
            "cagr_pct": round(cagr_bah * 100, 2),
            "max_drawdown_pct": round(max_dd_bah * 100, 2),
        },
    }


def compute_trading_levels(spy_bars: Dict[date, DailyBar], history_days: int = 5) -> dict:
    """Compute SPY pivot points, SMAs, and ATR from historical OHLC data."""
    if len(spy_bars) < 2:
        return {"error": "Need at least 2 trading days to compute levels."}

    sorted_dates = sorted(spy_bars.keys())
    as_of_date = sorted_dates[-1]
    prev_bar = spy_bars[as_of_date]
    pdh, pdl, pdc, pdo = prev_bar.high, prev_bar.low, prev_bar.close, prev_bar.open

    # Standard floor-trader pivot formulas
    p = (pdh + pdl + pdc) / 3.0
    r1 = 2.0 * p - pdl
    r2 = p + (pdh - pdl)
    r3 = pdh + 2.0 * (p - pdl)
    s1 = 2.0 * p - pdh
    s2 = p - (pdh - pdl)
    s3 = pdl - 2.0 * (pdh - p)

    # SMAs
    closes = [spy_bars[d].close for d in sorted_dates]
    sma50 = sum(closes[-50:]) / 50 if len(closes) >= 50 else None
    sma200 = sum(closes[-200:]) / 200 if len(closes) >= 200 else None

    # ATR(14)
    atr14: Optional[float] = None
    if len(sorted_dates) >= 15:
        lookback = min(30, len(sorted_dates))
        atr_dates = sorted_dates[-lookback:]
        trs: List[float] = []
        for i in range(1, len(atr_dates)):
            curr = spy_bars[atr_dates[i]]
            prev = spy_bars[atr_dates[i - 1]]
            tr = max(
                curr.high - curr.low,
                abs(curr.high - prev.close),
                abs(curr.low - prev.close),
            )
            trs.append(tr)
        if len(trs) >= 14:
            atr = sum(trs[:14]) / 14.0
            for tr_val in trs[14:]:
                atr = (atr * 13.0 + tr_val) / 14.0
            atr14 = atr

    spy_levels = {
        "pdh": round(pdh, 2), "pdl": round(pdl, 2),
        "pdc": round(pdc, 2), "pdo": round(pdo, 2),
        "pivot": round(p, 2),
        "r1": round(r1, 2), "r2": round(r2, 2), "r3": round(r3, 2),
        "s1": round(s1, 2), "s2": round(s2, 2), "s3": round(s3, 2),
        "sma50": round(sma50, 2) if sma50 else None,
        "sma200": round(sma200, 2) if sma200 else None,
        "atr14": round(atr14, 2) if atr14 else None,
    }

    # Build daily history
    history_days = max(1, min(history_days, len(sorted_dates)))
    daily_levels: List[dict] = []
    for sess_date in sorted_dates[-history_days:]:
        bar = spy_bars[sess_date]
        bp = (bar.high + bar.low + bar.close) / 3.0
        daily_levels.append({
            "date": sess_date.isoformat(),
            "spy": {
                "pdh": round(bar.high, 2), "pdl": round(bar.low, 2),
                "pdc": round(bar.close, 2), "pdo": round(bar.open, 2),
                "pivot": round(bp, 2),
                "r1": round(2 * bp - bar.low, 2),
                "s1": round(2 * bp - bar.high, 2),
            },
        })

    return {
        "as_of_date": as_of_date.isoformat(),
        "levels_for_session": (as_of_date + timedelta(days=1)).isoformat(),
        "spy": spy_levels,
        "daily_levels": daily_levels,
        "notes": "Levels derived from SPY daily OHLC data via yfinance.",
    }


def compute_trade_plan(
    signal_name: Optional[str],
    tier: Optional[int],
    target_exposure: float,
    danger: bool,
    spy_levels: dict,
) -> dict:
    """Compute a signal-calibrated trade plan from SPY pivot levels."""
    if danger:
        return {
            "state": "FLAT",
            "signal": None,
            "exposure": 0.0,
            "note": "Danger state active — all exposure closed. No entries until danger clears.",
        }

    if not signal_name:
        return {
            "state": "BASE",
            "signal": None,
            "exposure": target_exposure,
            "note": f"No active boost signal. Hold {target_exposure:.1f}x base exposure.",
        }

    # Classify signal
    momentum_signals = {"T2_GREEN_MOMENTUM", "T3_ORANGE_GRIND"}
    trade_type = "momentum" if signal_name in momentum_signals else "mean_reversion"

    pivot = spy_levels.get("pivot")
    r1 = spy_levels.get("r1")
    r2 = spy_levels.get("r2")
    r3 = spy_levels.get("r3")
    s1 = spy_levels.get("s1")
    s2 = spy_levels.get("s2")
    s3 = spy_levels.get("s3")
    atr = spy_levels.get("atr14")

    def _r(v):
        return round(v, 2) if v is not None else None

    if trade_type == "mean_reversion":
        entry_low, entry_high = s1, pivot
        entry_mid = _r((s1 + pivot) / 2) if s1 and pivot else None
        stop_price = s3 if tier == 1 else s2
        stop_name = "S3" if tier == 1 else "S2"
        t1_price, t1_name = r1, "R1"
        t2_price, t2_name = r2, "R2"
    else:
        entry_low, entry_high = pivot, r1
        entry_mid = _r((pivot + r1) / 2) if pivot and r1 else None
        stop_price = s1 if tier in (1, 2) else pivot
        stop_name = "S1" if tier in (1, 2) else "Pivot"
        t1_price, t1_name = r2, "R2"
        t2_price, t2_name = r3, "R3"

    risk_pts = _r(entry_mid - stop_price) if entry_mid and stop_price else None
    rew_t1 = _r(t1_price - entry_mid) if t1_price and entry_mid else None
    rr_t1 = _r(rew_t1 / risk_pts) if rew_t1 and risk_pts else None

    return {
        "state": "ACTIVE",
        "signal": signal_name,
        "tier": tier,
        "trade_type": trade_type,
        "exposure": target_exposure,
        "entry_zone": {"low": _r(entry_low), "high": _r(entry_high), "mid": entry_mid},
        "stop": {"price": _r(stop_price), "level_name": stop_name, "risk_pts": risk_pts},
        "target_1": {"price": _r(t1_price), "level_name": t1_name, "reward_pts": rew_t1, "rr": rr_t1},
        "target_2": {"price": _r(t2_price), "level_name": t2_name},
        "atr14": atr,
    }


def build_rows(
    spy_csv: Path,
    tlt_csv: Path,
    auto_fetch: bool = False,
) -> Tuple[List[dict], int, int]:
    """Load CSV data, optionally fetch new bars, run strategy, return rows."""
    spy_bars = load_csv_bars(spy_csv)
    tlt_bars = load_csv_bars(tlt_csv)

    spy_bars, fetched_spy = merge_auto_fetch(spy_bars, "SPY", auto_fetch=auto_fetch)
    tlt_bars, fetched_tlt = merge_auto_fetch(tlt_bars, "TLT", auto_fetch=auto_fetch)

    if auto_fetch and fetched_spy > 0:
        write_bars_csv(spy_csv, spy_bars)
    if auto_fetch and fetched_tlt > 0:
        write_bars_csv(tlt_csv, tlt_bars)

    joined = join_market_data(spy_bars, tlt_bars)
    if len(joined) < 2:
        raise RuntimeError("Need at least 2 matching trading days between SPY and TLT.")
    rows = run_strategy_rows(joined)
    return rows, fetched_spy, fetched_tlt


def write_report_csv(rows: List[dict], output_path) -> None:
    """Write strategy rows to CSV."""
    fieldnames = [
        "date", "color", "spy_close", "spy_abs_change", "spy_pct_change",
        "tlt_close", "tlt_abs_change", "tlt_pct_change", "target_exposure",
        "action", "signal_detail", "signal", "tier", "boost_action",
        "boost_hold_days", "danger", "greed_trim", "reason", "signal_explainer",
    ]
    if hasattr(output_path, "write"):
        writer = csv.DictWriter(output_path, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fieldnames})
    else:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow({k: row.get(k) for k in fieldnames})
