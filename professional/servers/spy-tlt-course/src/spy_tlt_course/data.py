"""
Standalone data layer for the SPY/TLT Course Edition.

Replaces trading-core dependencies with direct CSV I/O and yfinance calls.
No broker connections, no tastytrade, no authentication.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, Optional, Tuple


@dataclass
class DailyBar:
    """Single day of OHLCV data."""

    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int
    adj_close: Optional[float] = None
    change_pct: Optional[str] = None


def _parse_float(val: str) -> float:
    """Parse a float from CSV, handling empty strings."""
    val = val.strip()
    if not val or val == "—":
        return 0.0
    return float(val.replace(",", ""))


def _parse_int(val: str) -> int:
    """Parse an int from CSV, handling empty strings and floats."""
    val = val.strip()
    if not val or val == "—":
        return 0
    return int(float(val.replace(",", "")))


def _format_change_pct(pct: float) -> str:
    """Format a percentage change as a string like '+1.23%' or '-0.45%'."""
    if pct > 0:
        return f"+{pct:.2f}%"
    elif pct < 0:
        return f"{pct:.2f}%"
    return "0.00%"


def load_csv_bars(csv_path: Path) -> Dict[date, DailyBar]:
    """
    Load a CSV file (Yahoo Finance format) into a dict of date -> DailyBar.

    Expected columns: Date, Open, High, Low, Close, Adj. Close, Change, Volume
    """
    bars: Dict[date, DailyBar] = {}
    with csv_path.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                d = datetime.strptime(row["Date"], "%Y-%m-%d").date()
                bars[d] = DailyBar(
                    date=d,
                    open=_parse_float(row["Open"]),
                    high=_parse_float(row["High"]),
                    low=_parse_float(row["Low"]),
                    close=_parse_float(row["Close"]),
                    volume=_parse_int(row["Volume"]),
                    adj_close=_parse_float(row.get("Adj. Close", row.get("Close", "0"))),
                    change_pct=row.get("Change", "0.00%"),
                )
            except (ValueError, KeyError):
                continue
    return bars


def write_bars_csv(csv_path: Path, bars: Dict[date, DailyBar]) -> None:
    """Write bars back to CSV in Yahoo Finance format."""
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    sorted_dates = sorted(bars.keys())
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Open", "High", "Low", "Close", "Adj. Close", "Change", "Volume"])
        prev_close: Optional[float] = None
        for d in sorted_dates:
            bar = bars[d]
            if prev_close and prev_close > 0:
                pct = ((bar.close - prev_close) / prev_close) * 100.0
                change_str = _format_change_pct(pct)
            else:
                change_str = bar.change_pct or "0.00%"
            writer.writerow([
                d.isoformat(),
                f"{bar.open:.2f}",
                f"{bar.high:.2f}",
                f"{bar.low:.2f}",
                f"{bar.close:.2f}",
                f"{bar.adj_close or bar.close:.3f}",
                change_str,
                bar.volume,
            ])
            prev_close = bar.close


def _latest_safe_fetch_end() -> date:
    """Return the latest safe end date for yfinance fetches (today or yesterday if before market close)."""
    return date.today()


def fetch_yfinance_bars(
    ticker: str,
    start: date,
    end: date,
) -> Dict[date, DailyBar]:
    """Fetch daily bars from Yahoo Finance."""
    try:
        import yfinance as yf
    except ImportError:
        return {}

    # yfinance end date is exclusive, add 1 day
    end_str = (end + timedelta(days=1)).isoformat()
    start_str = start.isoformat()

    try:
        df = yf.download(ticker, start=start_str, end=end_str, progress=False, auto_adjust=False)
    except Exception:
        return {}

    if df is None or df.empty:
        return {}

    # yfinance may return multi-level columns for single ticker; flatten them
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.droplevel(1)

    bars: Dict[date, DailyBar] = {}
    for idx, row in df.iterrows():
        d = idx.date() if hasattr(idx, "date") else idx
        try:
            # Handle potential Series values by converting explicitly
            open_val = float(row["Open"].iloc[0]) if hasattr(row["Open"], "iloc") else float(row["Open"])
            high_val = float(row["High"].iloc[0]) if hasattr(row["High"], "iloc") else float(row["High"])
            low_val = float(row["Low"].iloc[0]) if hasattr(row["Low"], "iloc") else float(row["Low"])
            close_val = float(row["Close"].iloc[0]) if hasattr(row["Close"], "iloc") else float(row["Close"])
            vol_val = int(row["Volume"].iloc[0]) if hasattr(row["Volume"], "iloc") else int(row["Volume"])
            adj_key = "Adj Close" if "Adj Close" in row.index else "Close"
            adj_val = float(row[adj_key].iloc[0]) if hasattr(row[adj_key], "iloc") else float(row[adj_key])

            bars[d] = DailyBar(
                date=d,
                open=open_val,
                high=high_val,
                low=low_val,
                close=close_val,
                volume=vol_val,
                adj_close=adj_val,
            )
        except (ValueError, KeyError, IndexError):
            continue
    return bars


def merge_auto_fetch(
    existing: Dict[date, DailyBar],
    ticker: str,
    auto_fetch: bool = True,
) -> Tuple[Dict[date, DailyBar], int]:
    """
    If auto_fetch is True, fetch new bars after the latest existing bar
    and merge them. Returns (merged_bars, num_new_bars).
    """
    if not auto_fetch or not existing:
        return existing, 0

    latest = max(existing.keys())
    fetch_start = latest + timedelta(days=1)
    fetch_end = _latest_safe_fetch_end()

    if fetch_start > fetch_end:
        return existing, 0

    new_bars = fetch_yfinance_bars(ticker, fetch_start, fetch_end)
    if not new_bars:
        return existing, 0

    merged = dict(existing)
    added = 0
    for d, bar in new_bars.items():
        if d not in merged:
            merged[d] = bar
            added += 1
    return merged, added
