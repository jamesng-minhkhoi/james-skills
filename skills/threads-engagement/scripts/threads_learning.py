#!/usr/bin/env python3
"""Validate and summarize a project-local Threads engagement JSONL ledger.

This script is descriptive only. It never accesses Threads or publishes
anything. It intentionally avoids causal claims and requires repeated records
before labeling a pattern as worth maintaining.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


REQUIRED_ACTION_FIELDS = {
    "id",
    "record_type",
    "timestamp",
    "platform",
    "account",
    "target_url",
    "topic",
    "ranking_hypothesis",
    "content_shape",
    "pattern_key",
}
VALID_ASSESSMENTS = {"positive", "neutral", "negative", "unknown"}


def read_records(path: str) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    stream: Iterable[str]

    if path == "-":
        stream = sys.stdin
    else:
        try:
            stream = Path(path).open(encoding="utf-8")
        except OSError as exc:
            return [], [f"cannot open {path}: {exc}"]

    try:
        for line_number, raw in enumerate(stream, start=1):
            if not raw.strip():
                continue
            try:
                value = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON ({exc.msg})")
                continue
            if not isinstance(value, dict):
                errors.append(f"line {line_number}: record must be an object")
                continue
            records.append(value)
    finally:
        if path != "-" and hasattr(stream, "close"):
            stream.close()  # type: ignore[union-attr]
    return records, errors


def validate_records(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    for index, record in enumerate(records, start=1):
        prefix = f"record {index}"
        missing = sorted(REQUIRED_ACTION_FIELDS - record.keys())
        if missing and record.get("record_type", "action") == "action":
            errors.append(f"{prefix}: missing required fields: {', '.join(missing)}")
        record_id = record.get("id")
        if record_id in seen_ids:
            errors.append(f"{prefix}: duplicate id {record_id!r}")
        if isinstance(record_id, str):
            seen_ids.add(record_id)
        if record.get("record_type", "action") == "action":
            hypothesis = record.get("ranking_hypothesis")
            if not isinstance(hypothesis, dict):
                errors.append(f"{prefix}: ranking_hypothesis must be an object")
        outcome = record.get("outcome")
        if outcome is not None:
            if not isinstance(outcome, dict):
                errors.append(f"{prefix}: outcome must be an object")
            elif outcome.get("assessment") not in VALID_ASSESSMENTS:
                errors.append(
                    f"{prefix}: outcome.assessment must be one of "
                    f"{', '.join(sorted(VALID_ASSESSMENTS))}"
                )
    return errors


def pattern_status(count: int, positive: int) -> str:
    if count >= 8 and positive >= 5:
        return "promotion-candidate"
    if count >= 3 and positive >= 2:
        return "repeated-signal"
    return "insufficient"


def report(records: list[dict[str, Any]]) -> str:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("record_type", "action") != "action":
            continue
        groups[str(record.get("pattern_key", "unclassified"))].append(record)

    lines = ["# Threads learning report", "", "Descriptive only; not causal proof.", ""]
    if not groups:
        return "\n".join(lines + ["No action records found."])

    for key in sorted(groups):
        items = groups[key]
        assessments = [
            item.get("outcome", {}).get("assessment")
            for item in items
            if isinstance(item.get("outcome"), dict)
        ]
        positive = assessments.count("positive")
        observed = len(assessments)
        values = [
            item.get("outcome", {}).get("primary_value")
            for item in items
            if isinstance(item.get("outcome"), dict)
            and isinstance(item.get("outcome", {}).get("primary_value"), (int, float))
        ]
        status = pattern_status(observed, positive)
        lines.extend(
            [
                f"## `{key}`",
                f"- Actions: {len(items)}; measured outcomes: {observed}; positive: {positive}",
                f"- Status: **{status}**",
                f"- Primary-value median: {statistics.median(values):g}" if values else "- Primary-value median: unknown",
                "- Caveat: inspect topic, age, audience, distribution, CTA, and confounders before promoting.",
                "",
            ]
        )
    lines.extend(
        [
            "## Maintenance rule",
            "Promote only repeated, comparable signals after human review. Keep project-specific voice and claims out of shared guidance.",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "report"):
        sub = subparsers.add_parser(command)
        sub.add_argument("--ledger", required=True, help="JSONL path, or - for stdin")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    records, parse_errors = read_records(args.ledger)
    validation_errors = validate_records(records)
    errors = parse_errors + validation_errors
    if args.command == "validate":
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print(f"Valid: {len(records)} record(s)")
        return 0

    if errors:
        for error in errors:
            print(f"WARNING: {error}", file=sys.stderr)
    print(report(records))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
