#!/usr/bin/env python3
"""
Drift detector: compare course MCP servers vs. the upstream platform packages.

Walks shared file trees between:
    professional/servers/spy-tlt-course/src/spy_tlt_course/
    professional/servers/page-index-rag-course/src/pageindex_rag/

and the corresponding platform packages in /Users/jxie/AI-trading-platform/:
    packages/spy-tlt-strat/src/spy_tlt_strat/
    packages/sec-rag/src/pageindex_rag/

Categorises each file as:
    IDENTICAL       — bit-identical, no work needed
    MINOR    (1-30) — small diff, scan for bug fixes worth porting
    MAJOR     (>30) — large diff, decide whether to port or mark intentional
    COURSE-ONLY     — file exists in course but not platform
    PLATFORM-ONLY   — file exists in platform but not course

Outputs a markdown report to stdout (or --out FILE).

Usage:
    uv run python scripts/check_drift.py
    uv run python scripts/check_drift.py --out docs/drift-report.md
    uv run python scripts/check_drift.py --platform /custom/path/AI-trading-platform
"""
from __future__ import annotations

import argparse
import difflib
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PLATFORM = Path.home() / "AI-trading-platform"

# (label, course_root, platform_root) — course_root and platform_root point at
# the package's top-level Python directory; relative paths under them are the
# comparison key.
PAIRS = [
    (
        "spy-tlt-course ↔ spy-tlt-strat",
        Path("professional/servers/spy-tlt-course/src/spy_tlt_course"),
        Path("packages/spy-tlt-strat/src/spy_tlt_strat"),
    ),
    (
        "page-index-rag-course ↔ sec-rag",
        Path("professional/servers/page-index-rag-course/src/pageindex_rag"),
        Path("packages/sec-rag/src/pageindex_rag"),
    ),
]

IGNORE_DIRS = {"__pycache__", ".pytest_cache"}
IGNORE_SUFFIXES = {".pyc", ".pyo"}


@dataclass
class FileDiff:
    rel_path: str
    status: str  # IDENTICAL | MINOR | MAJOR | COURSE-ONLY | PLATFORM-ONLY
    diff_lines: int  # 0 if identical or single-side
    course_lines: int
    platform_lines: int


def walk_py(root: Path) -> set[str]:
    if not root.exists():
        return set()
    out: set[str] = set()
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in IGNORE_DIRS for part in p.parts):
            continue
        if p.suffix in IGNORE_SUFFIXES:
            continue
        out.add(str(p.relative_to(root)))
    return out


def line_count(p: Path) -> int:
    try:
        return sum(1 for _ in p.open("rb"))
    except OSError:
        return 0


def diff_size(a: Path, b: Path) -> int:
    """Number of changed lines (additions + deletions) between a and b."""
    a_lines = a.read_text(errors="replace").splitlines()
    b_lines = b.read_text(errors="replace").splitlines()
    diff = difflib.unified_diff(a_lines, b_lines, n=0)
    changed = 0
    for line in diff:
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
            changed += 1
    return changed


def categorize(course_dir: Path, platform_dir: Path) -> list[FileDiff]:
    course_files = walk_py(course_dir)
    platform_files = walk_py(platform_dir)

    results: list[FileDiff] = []
    for rel in sorted(course_files | platform_files):
        c = course_dir / rel
        p = platform_dir / rel
        in_course = rel in course_files
        in_platform = rel in platform_files

        if in_course and not in_platform:
            results.append(FileDiff(rel, "COURSE-ONLY", 0, line_count(c), 0))
            continue
        if in_platform and not in_course:
            results.append(FileDiff(rel, "PLATFORM-ONLY", 0, 0, line_count(p)))
            continue

        # Both sides exist
        c_bytes = c.read_bytes()
        p_bytes = p.read_bytes()
        if c_bytes == p_bytes:
            results.append(
                FileDiff(rel, "IDENTICAL", 0, line_count(c), line_count(p))
            )
            continue

        d = diff_size(c, p)
        status = "MINOR" if d <= 30 else "MAJOR"
        results.append(FileDiff(rel, status, d, line_count(c), line_count(p)))
    return results


def render_section(label: str, course_dir: Path, platform_dir: Path,
                   results: list[FileDiff]) -> str:
    by_status: dict[str, list[FileDiff]] = {}
    for r in results:
        by_status.setdefault(r.status, []).append(r)

    counts = {s: len(by_status.get(s, [])) for s in
              ("IDENTICAL", "MINOR", "MAJOR", "COURSE-ONLY", "PLATFORM-ONLY")}

    lines: list[str] = []
    lines.append(f"## {label}")
    lines.append("")
    lines.append(f"- Course path: `{course_dir}`")
    lines.append(f"- Platform path: `{platform_dir}`")
    lines.append("")
    lines.append(
        f"**Summary:** {counts['IDENTICAL']} identical · "
        f"{counts['MINOR']} minor · {counts['MAJOR']} major · "
        f"{counts['COURSE-ONLY']} course-only · "
        f"{counts['PLATFORM-ONLY']} platform-only"
    )
    lines.append("")

    for status in ("MAJOR", "MINOR", "PLATFORM-ONLY", "COURSE-ONLY", "IDENTICAL"):
        bucket = by_status.get(status, [])
        if not bucket:
            continue
        lines.append(f"### {status} ({len(bucket)})")
        lines.append("")
        if status in ("MAJOR", "MINOR"):
            lines.append("| File | Diff lines | Course LOC | Platform LOC |")
            lines.append("|------|-----------:|-----------:|-------------:|")
            for r in sorted(bucket, key=lambda x: -x.diff_lines):
                lines.append(
                    f"| `{r.rel_path}` | {r.diff_lines} | "
                    f"{r.course_lines} | {r.platform_lines} |"
                )
        elif status == "PLATFORM-ONLY":
            lines.append("| File | Platform LOC |")
            lines.append("|------|-------------:|")
            for r in sorted(bucket, key=lambda x: -x.platform_lines):
                lines.append(f"| `{r.rel_path}` | {r.platform_lines} |")
        elif status == "COURSE-ONLY":
            lines.append("| File | Course LOC |")
            lines.append("|------|-----------:|")
            for r in sorted(bucket, key=lambda x: -x.course_lines):
                lines.append(f"| `{r.rel_path}` | {r.course_lines} |")
        else:  # IDENTICAL
            for r in bucket:
                lines.append(f"- `{r.rel_path}`")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--platform", type=Path, default=DEFAULT_PLATFORM,
                    help=f"Path to AI-trading-platform repo (default: {DEFAULT_PLATFORM})")
    ap.add_argument("--out", type=Path, default=None,
                    help="Write report to FILE instead of stdout")
    args = ap.parse_args()

    if not args.platform.exists():
        print(f"ERROR: platform path not found: {args.platform}", file=sys.stderr)
        return 2

    out_lines: list[str] = []
    out_lines.append("# Course ↔ Platform Drift Report")
    out_lines.append("")
    out_lines.append(f"Generated by `scripts/check_drift.py`.")
    out_lines.append(f"Platform repo: `{args.platform}`")
    out_lines.append("")
    out_lines.append(
        "Status legend: **IDENTICAL** = no work · **MINOR** (≤30 line diff) = "
        "scan for fixes · **MAJOR** (>30) = decide port vs. intentional · "
        "**COURSE-ONLY** / **PLATFORM-ONLY** = file exists on one side only."
    )
    out_lines.append("")
    out_lines.append(
        "See `docs/intentional_divergence.md` for files where divergence is "
        "by design (don't merge)."
    )
    out_lines.append("")

    for label, course_rel, platform_rel in PAIRS:
        course_dir = REPO_ROOT / course_rel
        platform_dir = args.platform / platform_rel
        if not course_dir.exists():
            out_lines.append(f"## {label}\n\nERROR: course path missing: `{course_dir}`\n")
            continue
        if not platform_dir.exists():
            out_lines.append(f"## {label}\n\nERROR: platform path missing: `{platform_dir}`\n")
            continue
        results = categorize(course_dir, platform_dir)
        out_lines.append(render_section(label, course_rel, platform_rel, results))
        out_lines.append("")

    report = "\n".join(out_lines)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report)
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
