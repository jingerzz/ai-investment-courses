#!/usr/bin/env python3
"""
SPY Pattern Analysis Tool
Analyzes ~33 years of SPY daily OHLCV data for extreme moves, streaks, and seasonal patterns.

Usage:
  python spy_analysis.py [--charts] [--top N] [--threshold X] [--section all|extreme|streaks|seasonal]
"""

import argparse
import sys
from pathlib import Path

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")

    # Parse Change column: "+1.23%" or "-0.56%" or "0.00%" -> float
    df["change_pct"] = (
        df["Change"].str.replace("%", "", regex=False)
                    .str.replace("+", "", regex=False)
                    .astype(float)
    )

    # Derive daily return from Adj. Close (more reliable)
    df["daily_return"] = df["Adj. Close"].pct_change() * 100  # percent

    df.sort_index(inplace=True)
    return df


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SEP = "=" * 70

def header(title: str):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)


def fmt_date(dt) -> str:
    return pd.Timestamp(dt).strftime("%Y-%m-%d")


def print_table(rows, col_headers, col_widths):
    """Simple fixed-width table printer."""
    fmt = "  ".join(f"{{:<{w}}}" for w in col_widths)
    print(fmt.format(*col_headers))
    print("  ".join("-" * w for w in col_widths))
    for row in rows:
        print(fmt.format(*[str(v) for v in row]))


# ---------------------------------------------------------------------------
# Module 1: Extreme daily moves
# ---------------------------------------------------------------------------

def analyze_extreme_moves(df: pd.DataFrame, args):
    header("EXTREME DAILY MOVES")

    ret = df["daily_return"].dropna()

    # --- Distribution summary ---
    print("\nReturn Distribution Summary:")
    stats = {
        "Count":    f"{len(ret):,}",
        "Mean":     f"{ret.mean():.4f}%",
        "Std Dev":  f"{ret.std():.4f}%",
        "Skewness": f"{ret.skew():.4f}",
        "Kurtosis": f"{ret.kurt():.4f}",
        "Min":      f"{ret.min():.4f}%",
        "Max":      f"{ret.max():.4f}%",
    }
    for k, v in stats.items():
        print(f"  {k:<12}: {v}")

    # --- Threshold counts ---
    thresholds = sorted({1.0, 2.0, 3.0, 5.0, float(args.threshold)})
    print("\nDays Beyond Threshold:")
    col_w = [10, 12, 10, 12, 10]
    print_table(
        [],
        ["Threshold", "Up Days", "Up %", "Down Days", "Down %"],
        col_w,
    )
    total = len(ret)
    for t in thresholds:
        up   = (ret >  t).sum()
        down = (ret < -t).sum()
        print_table(
            [(f"±{t:.1f}%", up, f"{up/total*100:.2f}%", down, f"{down/total*100:.2f}%")],
            ["", "", "", "", ""],
            col_w,
        )

    # --- Top N gains ---
    n = args.top
    print(f"\nTop {n} Single-Day GAINS:")
    top_gains = ret.nlargest(n)
    rows = []
    for date, val in top_gains.items():
        close = df.loc[date, "Adj. Close"]
        rows.append((fmt_date(date), f"+{val:.4f}%", f"${close:.2f}"))
    print_table(rows, ["Date", "Return", "Adj Close"], [14, 12, 12])

    # --- Top N drops ---
    print(f"\nTop {n} Single-Day DROPS:")
    top_drops = ret.nsmallest(n)
    rows = []
    for date, val in top_drops.items():
        close = df.loc[date, "Adj. Close"]
        rows.append((fmt_date(date), f"{val:.4f}%", f"${close:.2f}"))
    print_table(rows, ["Date", "Return", "Adj Close"], [14, 12, 12])

    if args.charts:
        _chart_return_histogram(ret, thresholds)


def _chart_return_histogram(ret: pd.Series, thresholds: list):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.hist(ret, bins=200, color="steelblue", edgecolor="none", alpha=0.8)

    colors = ["orange", "red", "darkred", "maroon"]
    for t, c in zip(thresholds, colors):
        ax.axvline( t, color=c, linestyle="--", linewidth=1, label=f"+{t}%")
        ax.axvline(-t, color=c, linestyle="--", linewidth=1, label=f"-{t}%")

    ax.set_xlabel("Daily Return (%)")
    ax.set_ylabel("Frequency")
    ax.set_title("SPY Daily Return Distribution")
    ax.legend(fontsize=8, ncol=2)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# Module 2: Streak patterns
# ---------------------------------------------------------------------------

def _compute_streaks(ret: pd.Series):
    """Return a list of (start_date, end_date, direction, length, total_return_pct)."""
    directions = np.sign(ret.values)  # +1 up, -1 down, 0 flat (treat as down)
    dates = ret.index

    streaks = []
    i = 0
    n = len(directions)
    while i < n:
        d = directions[i]
        if d == 0:
            d = -1  # flat treated as not-up
        j = i + 1
        while j < n and (np.sign(ret.values[j]) if ret.values[j] != 0 else -1) == d:
            j += 1
        length = j - i
        # total return over streak using log approximation
        total_ret = ret.iloc[i:j].sum()
        streaks.append({
            "start": dates[i],
            "end":   dates[j - 1],
            "dir":   "up" if d == 1 else "down",
            "length": length,
            "total_return": total_ret,
        })
        i = j
    return streaks


def analyze_streaks(df: pd.DataFrame, args):
    header("STREAK PATTERNS")

    ret = df["daily_return"].dropna()
    streaks = _compute_streaks(ret)
    streak_df = pd.DataFrame(streaks)

    up_streaks   = streak_df[streak_df["dir"] == "up"]
    down_streaks = streak_df[streak_df["dir"] == "down"]

    # --- Longest streaks ---
    for label, sdf in [("UP", up_streaks), ("DOWN", down_streaks)]:
        print(f"\nTop 10 Longest {label} Streaks:")
        top = sdf.nlargest(10, "length")
        rows = [
            (fmt_date(r.start), fmt_date(r.end), r.length,
             f"{r.total_return:+.2f}%")
            for _, r in top.iterrows()
        ]
        print_table(rows, ["Start", "End", "Days", "Total Return"], [14, 14, 6, 14])

    # --- Streak length distribution ---
    print("\nStreak Length Distribution:")
    max_len = streak_df["length"].max()
    col_w = [8, 10, 10, 12, 12]
    print_table([], ["Length", "# Up", "# Down", "Avg Up Ret", "Avg Dn Ret"], col_w)
    for length in range(1, min(max_len + 1, 21)):
        u = up_streaks[up_streaks["length"] == length]
        d = down_streaks[down_streaks["length"] == length]
        avg_u = f"{u['total_return'].mean():+.2f}%" if len(u) else "  —"
        avg_d = f"{d['total_return'].mean():+.2f}%" if len(d) else "  —"
        print_table(
            [(length, len(u), len(d), avg_u, avg_d)],
            ["", "", "", "", ""],
            col_w,
        )

    # --- "What happens next" table ---
    print("\n'What Happens Next' — Average Next-Day Return After N Consecutive Days:")
    col_w = [10, 16, 12, 16, 12]
    print_table([], ["N Days", "After N Up", "N Up Obs", "After N Down", "N Dn Obs"], col_w)

    for n in range(1, 11):
        # Find all positions where the last n days were all up/down
        ret_arr = ret.values
        next_up_rets = []
        next_dn_rets = []
        for i in range(n, len(ret_arr) - 1):
            window = ret_arr[i - n:i]
            nxt = ret_arr[i]
            if all(w > 0 for w in window):
                next_up_rets.append(nxt)
            if all(w < 0 for w in window):
                next_dn_rets.append(nxt)
        au = f"{np.mean(next_up_rets):+.4f}%" if next_up_rets else "  —"
        ad = f"{np.mean(next_dn_rets):+.4f}%" if next_dn_rets else "  —"
        print_table(
            [(n, au, len(next_up_rets), ad, len(next_dn_rets))],
            ["", "", "", "", ""],
            col_w,
        )

    if args.charts:
        _chart_streak_distribution(up_streaks, down_streaks)


def _chart_streak_distribution(up_streaks: pd.DataFrame, down_streaks: pd.DataFrame):
    import matplotlib.pyplot as plt

    max_len = max(up_streaks["length"].max(), down_streaks["length"].max())
    lengths = list(range(1, min(max_len + 1, 21)))

    up_counts   = [len(up_streaks[up_streaks["length"] == l])   for l in lengths]
    down_counts = [len(down_streaks[down_streaks["length"] == l]) for l in lengths]

    x = np.arange(len(lengths))
    w = 0.35

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(x - w/2, up_counts,   w, label="Up Streaks",   color="green",  alpha=0.8)
    ax.bar(x + w/2, down_counts, w, label="Down Streaks", color="red",    alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([str(l) for l in lengths])
    ax.set_xlabel("Streak Length (days)")
    ax.set_ylabel("Frequency")
    ax.set_title("SPY Streak Length Distribution")
    ax.legend()
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# Module 3: Seasonal / calendar patterns
# ---------------------------------------------------------------------------

def analyze_seasonal(df: pd.DataFrame, args):
    header("SEASONAL / CALENDAR PATTERNS")

    ret = df["daily_return"].dropna().copy()
    idx = ret.index

    # --- Day of week ---
    dow_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    dow_map   = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
    dow_series = pd.Series(idx.dayofweek, index=idx).map(dow_map)
    dow_stats = ret.groupby(dow_series).agg(["mean", "std", "count"])
    dow_stats = dow_stats.reindex(dow_names)

    print("\nAverage Daily Return by Day of Week:")
    print_table([], ["Day", "Mean Return", "Std Dev", "Obs"], [12, 14, 12, 8])
    for day, row in dow_stats.iterrows():
        print_table(
            [(day, f"{row['mean']:+.4f}%", f"{row['std']:.4f}%", int(row['count']))],
            ["", "", "", ""],
            [12, 14, 12, 8],
        )

    # --- Month ---
    month_names = ["Jan","Feb","Mar","Apr","May","Jun",
                   "Jul","Aug","Sep","Oct","Nov","Dec"]
    month_series = pd.Series(idx.month, index=idx).map(
        {i+1: m for i, m in enumerate(month_names)}
    )
    month_stats = ret.groupby(month_series).agg(["mean", "std", "count"])
    month_stats = month_stats.reindex(month_names)

    print("\nAverage Daily Return by Month:")
    print_table([], ["Month", "Mean Return", "Std Dev", "Obs"], [8, 14, 12, 8])
    for month, row in month_stats.iterrows():
        print_table(
            [(month, f"{row['mean']:+.4f}%", f"{row['std']:.4f}%", int(row['count']))],
            ["", "", "", ""],
            [8, 14, 12, 8],
        )

    # Best / worst month
    best_m  = month_stats["mean"].idxmax()
    worst_m = month_stats["mean"].idxmin()
    print(f"\n  Best month historically:  {best_m}  ({month_stats.loc[best_m,  'mean']:+.4f}%/day avg)")
    print(f"  Worst month historically: {worst_m} ({month_stats.loc[worst_m, 'mean']:+.4f}%/day avg)")

    # --- Year ---
    year_series = pd.Series(idx.year, index=idx)
    year_stats = ret.groupby(year_series).agg(["sum", "mean", "count"])
    year_stats.columns = ["total_return", "mean_daily", "trading_days"]

    print("\nAnnual Summary (sum of daily returns — approximate):")
    print_table([], ["Year", "Total Return", "Mean Daily", "Trading Days"], [6, 14, 14, 14])
    for year, row in year_stats.iterrows():
        print_table(
            [(year, f"{row['total_return']:+.2f}%",
              f"{row['mean_daily']:+.4f}%", int(row['trading_days']))],
            ["", "", "", ""],
            [6, 14, 14, 14],
        )

    if args.charts:
        _chart_seasonal(dow_stats, month_stats, dow_names, month_names)


def _chart_seasonal(dow_stats, month_stats, dow_names, month_names):
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # DoW
    ax = axes[0]
    means = dow_stats["mean"].values
    colors = ["green" if v >= 0 else "red" for v in means]
    ax.bar(dow_names, means, color=colors, alpha=0.8)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Day of Week")
    ax.set_ylabel("Avg Daily Return (%)")
    ax.set_title("SPY: Avg Return by Day of Week")
    ax.tick_params(axis="x", rotation=15)

    # Monthly
    ax = axes[1]
    means = month_stats["mean"].values
    colors = ["green" if v >= 0 else "red" for v in means]
    ax.bar(month_names, means, color=colors, alpha=0.8)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Month")
    ax.set_ylabel("Avg Daily Return (%)")
    ax.set_title("SPY: Avg Return by Month")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# CLI & main
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="SPY Pattern Analysis Tool — extreme moves, streaks, seasonal patterns."
    )
    parser.add_argument(
        "--charts", action="store_true",
        help="Show matplotlib charts for each section."
    )
    parser.add_argument(
        "--top", type=int, default=10, metavar="N",
        help="Number of extreme moves to display (default: 10)."
    )
    parser.add_argument(
        "--threshold", type=float, default=2.0, metavar="X",
        help="% threshold for extreme move counts (default: 2.0)."
    )
    parser.add_argument(
        "--section", choices=["all", "extreme", "streaks", "seasonal"],
        default="all",
        help="Which analysis section to run (default: all)."
    )
    parser.add_argument(
        "--file", default="SPY-history.csv",  # resolved at runtime via DATA_DIR
        help="Path to SPY CSV data file."
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"\nLoading data from: {args.file}")
    try:
        df = load_data(args.file)
    except FileNotFoundError:
        print(f"ERROR: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(df):,} trading days  "
          f"({fmt_date(df.index[0])} → {fmt_date(df.index[-1])})")

    section = args.section
    if section in ("all", "extreme"):
        analyze_extreme_moves(df, args)

    if section in ("all", "streaks"):
        analyze_streaks(df, args)

    if section in ("all", "seasonal"):
        analyze_seasonal(df, args)

    print(f"\n{SEP}")
    print("  Analysis complete.")
    print(SEP + "\n")


if __name__ == "__main__":
    main()
