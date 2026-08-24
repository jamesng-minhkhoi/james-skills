#!/usr/bin/env python3
"""Build a cautious Markdown report from an X content audit CSV or JSON file."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median
from typing import Any


METRIC_FIELDS = (
    "impressions",
    "likes",
    "replies",
    "reposts",
    "quotes",
    "bookmarks",
    "profile_visits",
    "link_clicks",
    "qualified_replies",
    "conversions",
)
CLASSIFICATIONS = {"winner", "ordinary", "weak", "distraction"}
FORMATS = {"original", "reply", "quote", "repost"}


def parse_number(value: Any) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    text = str(value).strip().replace(",", "")
    match = re.fullmatch(r"([-+]?\d*\.?\d+)\s*([KMBkmb]?)", text)
    if not match:
        return None
    number = float(match.group(1))
    multiplier = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}
    return number * multiplier[match.group(2).upper()]


def clean(value: Any) -> str:
    return " ".join(str(value or "").split())


def load_rows(path: str) -> list[dict[str, Any]]:
    if path == "-":
        raw = sys.stdin.read()
        return load_json_text(raw) if raw.lstrip().startswith(("[", "{")) else list(csv.DictReader(raw.splitlines()))
    source = Path(path)
    if not source.exists():
        raise SystemExit(f"Input does not exist: {source}")
    if source.suffix.lower() == ".json":
        return load_json_text(source.read_text(encoding="utf-8"))
    with source.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def load_json_text(raw: str) -> list[dict[str, Any]]:
    data = json.loads(raw)
    if isinstance(data, dict):
        data = data.get("posts", data.get("rows", data))
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise SystemExit("JSON input must be an array of objects or an object with posts/rows")
    return data


def enrich(row: dict[str, Any]) -> dict[str, Any]:
    result = {key: clean(value) for key, value in row.items()}
    for field in METRIC_FIELDS:
        result[field] = parse_number(row.get(field))
    impressions = result["impressions"]
    engagement_total = sum(result[field] or 0 for field in ("likes", "replies", "reposts", "quotes", "bookmarks"))
    qualified_total = sum(result[field] or 0 for field in ("qualified_replies", "link_clicks"))
    result["engagement_rate"] = safe_div(engagement_total, impressions)
    result["qualified_response_rate"] = safe_div(qualified_total, impressions)
    result["conversion_rate"] = safe_div(result["conversions"], result["link_clicks"])
    return result


def safe_div(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator


def pct(value: float | None) -> str:
    return "—" if value is None else f"{value * 100:.2f}%"


def compact(value: float | None) -> str:
    if value is None:
        return "—"
    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if abs(value) >= 1_000:
        return f"{value / 1_000:.1f}K"
    return f"{value:.0f}"


def excerpt(value: Any, limit: int = 88) -> str:
    text = clean(value).replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def group_rows(rows: list[dict[str, Any]], field: str, minimum: int) -> list[dict[str, Any]]:
    groups: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = row.get(field) or "unknown"
        groups[key].append(row)
    result = []
    for key, members in groups.items():
        if len(members) < minimum:
            continue
        engagement = [row["engagement_rate"] for row in members if row["engagement_rate"] is not None]
        qualified = [row["qualified_response_rate"] for row in members if row["qualified_response_rate"] is not None]
        result.append(
            {
                "key": key,
                "n": len(members),
                "engagement": median(engagement) if engagement else None,
                "qualified": median(qualified) if qualified else None,
            }
        )
    return sorted(result, key=lambda item: (item["qualified"] or -1, item["engagement"] or -1), reverse=True)


def table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return "_No comparable rows._"
    output = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    output.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(output)


def build_report(rows: list[dict[str, Any]], title: str, minimum: int) -> str:
    enriched = [enrich(row) for row in rows]
    classifications = Counter(row.get("classification") or "unknown" for row in enriched)
    formats = Counter(row.get("format") or "unknown" for row in enriched)
    confidence = Counter(row.get("source_confidence") or "unknown" for row in enriched)
    missing_impressions = sum(row["impressions"] is None for row in enriched)
    invalid_classification = sorted({row.get("classification", "") for row in enriched if row.get("classification") not in CLASSIFICATIONS})
    invalid_format = sorted({row.get("format", "") for row in enriched if row.get("format") not in FORMATS})

    scored = [row for row in enriched if row["engagement_rate"] is not None]
    qualified = [row for row in enriched if row["qualified_response_rate"] is not None]
    top_engagement = sorted(scored, key=lambda row: row["engagement_rate"], reverse=True)[:10]
    top_qualified = sorted(qualified, key=lambda row: row["qualified_response_rate"], reverse=True)[:10]

    warnings = []
    if missing_impressions:
        warnings.append(f"{missing_impressions} of {len(enriched)} rows lack impressions; their normalized rates are unavailable.")
    if invalid_classification:
        warnings.append("Unexpected classification values: " + ", ".join(invalid_classification))
    if invalid_format:
        warnings.append("Unexpected format values: " + ", ".join(invalid_format))
    if len(enriched) < 24:
        warnings.append("Sample is smaller than the recommended 30+ posts; do not call a pattern causal.")
    if not qualified:
        warnings.append("No qualified-response rates were calculable; attention is the only measurable layer in this input.")

    report = [
        f"# {title}",
        "",
        "Generated from a manually captured or exported sample. This report summarizes associations; it does not prove that a format caused performance.",
        "",
        "## Sample overview",
        "",
        table(
            ["Metric", "Value"],
            [
                ["Rows", str(len(enriched))],
                ["Classifications", ", ".join(f"{key}: {value}" for key, value in classifications.items()) or "—"],
                ["Formats", ", ".join(f"{key}: {value}" for key, value in formats.items()) or "—"],
                ["Source confidence", ", ".join(f"{key}: {value}" for key, value in confidence.items()) or "—"],
                ["Rows with impressions", f"{len(enriched) - missing_impressions}/{len(enriched)}"],
            ],
        ),
        "",
        "## Top by normalized engagement",
        "",
        table(
            ["Post", "Class", "Format", "Topic", "Engagement", "Text"],
            [
                [
                    excerpt(row.get("id"), 34),
                    row.get("classification", "unknown"),
                    row.get("format", "unknown"),
                    row.get("topic", "unknown"),
                    pct(row["engagement_rate"]),
                    excerpt(row.get("text")),
                ]
                for row in top_engagement
            ],
        ),
        "",
        "## Top by qualified response",
        "",
        table(
            ["Post", "Class", "Format", "Topic", "Qualified", "Conversions", "Text"],
            [
                [
                    excerpt(row.get("id"), 34),
                    row.get("classification", "unknown"),
                    row.get("format", "unknown"),
                    row.get("topic", "unknown"),
                    pct(row["qualified_response_rate"]),
                    compact(row["conversions"]),
                    excerpt(row.get("text")),
                ]
                for row in top_qualified
            ],
        ),
        "",
        "## Cluster comparison",
        "",
        "Median rates are shown because a single viral outlier can distort averages.",
        "",
    ]

    for field, heading in (("classification", "Classification"), ("format", "Format"), ("topic", "Topic"), ("media_type", "Media type"), ("media_role", "Media role"), ("hashtag_use", "Hashtag use")):
        report.extend(
            [
                f"### {heading}",
                "",
                table(
                    [heading, "N", "Median engagement", "Median qualified response"],
                    [[item["key"], str(item["n"]), pct(item["engagement"]), pct(item["qualified"])] for item in group_rows(enriched, field, minimum)],
                ),
                "",
            ]
        )

    report.extend(["## Warnings and interpretation boundaries", ""])
    if warnings:
        report.extend(f"- {warning}" for warning in warnings)
    else:
        report.append("- No structural warnings detected. Causal conclusions still require controlled follow-up tests.")
    report.extend(
        [
            "",
            "Do not declare a winning formula from this report alone. Use the clusters to propose one or two tests, changing one major variable at a time and measuring attention, qualified conversation, and conversion separately.",
            "",
        ]
    )
    return "\n".join(report)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a cautious Markdown report from an X content audit sample")
    parser.add_argument("--input", required=True, help="CSV/JSON path, or - for stdin")
    parser.add_argument("--output", help="Markdown output path; print to stdout when omitted")
    parser.add_argument("--title", default="X content audit", help="Report title")
    parser.add_argument("--min-group", type=int, default=2, help="Minimum rows for a cluster table")
    args = parser.parse_args()
    if args.min_group < 1:
        parser.error("--min-group must be at least 1")
    report = build_report(load_rows(args.input), args.title, args.min_group)
    if args.output:
        Path(args.output).write_text(report + "\n", encoding="utf-8")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
