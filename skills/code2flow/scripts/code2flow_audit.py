#!/usr/bin/env python3
"""
code2flow_audit.py — Zero-dependency AST/Static Route-Graph Extractor & 11-Heuristic UX Gap Auditor.

Scans Next.js (App & Pages Router), Expo Router, React Router, TanStack Router, SwiftUI,
Flutter, Jetpack Compose, or Static HTML repositories to:
  1. Discover all Route Screens, State Screens (modals/tabs/drawers), and Navigation Edges.
  2. Emit a Mermaid user-flow diagram (.mmd / Markdown) and machine-readable graph.json.
  3. Audit the route graph against 11 structural UX & flow heuristics (broken links, orphans,
     dead ends, missing loading/error/404 boundaries, unguarded auth routes, destructive actions
     without confirmation, forms without error/pending feedback, deep click depth, and unlabeled
     dynamic routes).

Usage:
  python3 skills/code2flow/scripts/code2flow_audit.py <repo-path> [--json-out graph.json] [--mermaid-out flows.mmd]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import deque
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

IGNORE_DIRS = {
    ".git",
    "node_modules",
    ".next",
    "dist",
    "build",
    "out",
    ".expo",
    ".turbo",
    ".code2flow",
    "coverage",
    "__pycache__",
    ".venv",
    "venv",
    "Pods",
    "DerivedData",
}

PAGE_FILENAMES = {
    "page.tsx",
    "page.ts",
    "page.jsx",
    "page.js",
}

LOADING_FILENAMES = {"loading.tsx", "loading.ts", "loading.jsx", "loading.js"}
ERROR_FILENAMES = {"error.tsx", "error.ts", "error.jsx", "error.js"}
NOT_FOUND_FILENAMES = {"not-found.tsx", "not-found.ts", "not-found.jsx", "not-found.js", "+not-found.tsx"}

LINK_PATTERNS = [
    re.compile(r"""(?:href|to)\s*=\s*["'](/[^"'#\s?]*(?:\?[^"'\s]*)?)["']"""),
    re.compile(r"""router\.(?:push|replace|navigate)\(\s*["'](/[^"'#\s?]*(?:\?[^"'\s]*)?)["']"""),
    re.compile(r"""redirect\(\s*["'](/[^"'#\s?]*(?:\?[^"'\s]*)?)["']"""),
    re.compile(r"""navigate\(\s*["'](/[^"'#\s?]*(?:\?[^"'\s]*)?)["']"""),
]

STATE_MODAL_RE = re.compile(r"\b(Dialog|Sheet|Drawer|AlertDialog|Modal|BottomSheet)\b")
STATE_TAB_RE = re.compile(r"""\?(?:tab|modal|drawer|step)=([A-Za-z0-9_-]+)""")
DESTRUCTIVE_RE = re.compile(r"\b(delete|remove|destroy|revoke|cancelSubscription|wipe)\b", re.IGNORECASE)
CONFIRM_RE = re.compile(r"\b(AlertDialog|confirm|ConfirmDialog|Modal|Dialog|onConfirm|confirmation)\b")
FORM_RE = re.compile(r"<form\b|useForm\(|onSubmit=", re.IGNORECASE)
FORM_FEEDBACK_RE = re.compile(r"\b(isPending|isSubmitting|loading|disabled|error|errors|toast|aria-invalid)\b")
AUTH_PATH_RE = re.compile(r"^/(dashboard|admin|settings|account|billing|profile|workspace|app)(/|$)", re.IGNORECASE)
AUTH_GUARD_RE = re.compile(
    r"\b(useAuth|getServerSession|auth\(|currentUser|requireAuth|ProtectedRoute|middleware|redirect\(|session)\b"
)


def normalize_route_segment(seg: str) -> str:
    if seg.startswith("(") and seg.endswith(")"):
        return ""
    if seg.startswith("@"):
        return ""
    return seg


def file_to_route_id(app_root: Path, file_path: Path, mode: str) -> str:
    rel = file_path.relative_to(app_root)
    parts = list(rel.parts)
    if mode in ("nextjs-app", "expo-router"):
        parts = parts[:-1] if parts[-1] in PAGE_FILENAMES or parts[-1].startswith("index.") else parts
        if parts and parts[-1].endswith((".tsx", ".ts", ".jsx", ".js")):
            stem = Path(parts[-1]).stem
            if stem == "index":
                parts = parts[:-1]
            else:
                parts[-1] = stem
    elif mode == "pages-router":
        stem = Path(parts[-1]).stem
        if stem == "index":
            parts = parts[:-1]
        else:
            parts[-1] = stem
    clean = [normalize_route_segment(p) for p in parts]
    clean = [p for p in clean if p]
    return "/" + "/".join(clean) if clean else "/"


def route_matches(pattern_route: str, target_path: str) -> bool:
    base_target = target_path.split("?")[0].split("#")[0].rstrip("/") or "/"
    if pattern_route == base_target:
        return True
    p_segs = [s for s in pattern_route.strip("/").split("/") if s]
    t_segs = [s for s in base_target.strip("/").split("/") if s]
    if any(s.startswith("[...") for s in p_segs):
        prefix_len = next(i for i, s in enumerate(p_segs) if s.startswith("[..."))
        return len(t_segs) >= prefix_len and all(
            ps == ts or (ps.startswith("[") and ps.endswith("]"))
            for ps, ts in zip(p_segs[:prefix_len], t_segs[:prefix_len])
        )
    if len(p_segs) != len(t_segs):
        return False
    return all(ps == ts or (ps.startswith("[") and ps.endswith("]")) for ps, ts in zip(p_segs, t_segs))


def detect_framework(repo: Path) -> Tuple[str, Path]:
    for cand in (repo / "src" / "app", repo / "app"):
        if cand.is_dir():
            pages = list(cand.rglob("page.tsx")) + list(cand.rglob("page.jsx")) + list(cand.rglob("page.js"))
            if pages:
                return "nextjs-app", cand
            expo_files = [p for p in cand.rglob("*.tsx") if not p.name.startswith("_")]
            if expo_files and (repo / "app.json").is_file():
                return "expo-router", cand
    for cand in (repo / "src" / "pages", repo / "pages"):
        if cand.is_dir():
            return "pages-router", cand
    return "generic", repo


def scan_repository(repo: Path) -> Dict[str, Any]:
    framework, app_root = detect_framework(repo)
    screens: List[Dict[str, Any]] = []
    edges: List[Dict[str, Any]] = []
    has_loading = False
    has_error = False
    has_not_found = False
    has_middleware_auth = (repo / "middleware.ts").is_file() or (repo / "src" / "middleware.ts").is_file()

    source_files: List[Path] = []
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            p = Path(root) / f
            if f in LOADING_FILENAMES:
                has_loading = True
            if f in ERROR_FILENAMES:
                has_error = True
            if f in NOT_FOUND_FILENAMES or f.startswith("404."):
                has_not_found = True
            if p.suffix in {".tsx", ".ts", ".jsx", ".js", ".swift", ".dart", ".kt", ".html"}:
                source_files.append(p)

    route_files: Dict[str, Path] = {}
    for p in source_files:
        rel_str = str(p.relative_to(repo))
        if any(seg.startswith("_") or seg == "api" for seg in p.parts):
            continue
        if framework == "nextjs-app" and p.name in PAGE_FILENAMES and app_root in p.parents:
            rid = file_to_route_id(app_root, p, framework)
            route_files[rid] = p
        elif framework in ("expo-router", "pages-router") and app_root in p.parents and p.suffix in {".tsx", ".jsx", ".js"}:
            if p.stem not in {"_layout", "_app", "_document", "+html", "+not-found"}:
                rid = file_to_route_id(app_root, p, framework)
                route_files[rid] = p
        elif framework == "generic" and p.suffix == ".html":
            rid = "/" if p.name == "index.html" else "/" + str(p.relative_to(repo).with_suffix("")).replace("/index", "")
            route_files[rid] = p

    # Fallback for React Router / TanStack / SwiftUI / Flutter / Compose when route_files is empty
    if not route_files:
        route_decl_re = re.compile(r"""path\s*:\s*["'](/[^"']*)["']|<Route[^>]+path=["'](/[^"']*)["']""")
        for p in source_files:
            try:
                txt = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            for m in route_decl_re.finditer(txt):
                rid = m.group(1) or m.group(2)
                if rid:
                    route_files.setdefault(rid, p)

    for rid, fpath in sorted(route_files.items()):
        txt = fpath.read_text(encoding="utf-8", errors="ignore")
        rel_file = str(fpath.relative_to(repo))
        modals = sorted(set(STATE_MODAL_RE.findall(txt)))
        tabs = sorted(set(STATE_TAB_RE.findall(txt)))
        has_destructive = bool(DESTRUCTIVE_RE.search(txt))
        has_confirm = bool(CONFIRM_RE.search(txt))
        has_form = bool(FORM_RE.search(txt))
        has_form_feedback = bool(FORM_FEEDBACK_RE.search(txt))
        has_auth_guard = has_middleware_auth or bool(AUTH_GUARD_RE.search(txt))

        screens.append(
            {
                "id": rid,
                "kind": "route",
                "file": rel_file,
                "stateScreens": [f"{rid}#{m.lower()}" for m in modals] + [f"{rid}?tab={t}" for t in tabs],
                "hasDestructive": has_destructive,
                "hasConfirm": has_confirm,
                "hasForm": has_form,
                "hasFormFeedback": has_form_feedback,
                "hasAuthGuard": has_auth_guard,
            }
        )

        for lineno, line in enumerate(txt.splitlines(), start=1):
            for pat in LINK_PATTERNS:
                for m in pat.finditer(line):
                    raw_target = m.group(1)
                    base_target = raw_target.split("?")[0].split("#")[0].rstrip("/") or "/"
                    matched = [r for r in route_files if route_matches(r, base_target)]
                    target_id = matched[0] if matched else f"missing:{base_target}"
                    edges.append(
                        {
                            "source": rid,
                            "target": target_id,
                            "rawTarget": raw_target,
                            "confidence": "high",
                            "evidence": f"{rel_file}:{lineno}",
                        }
                    )

    # Also collect shell navigation from layout/nav components
    shell_targets: Set[str] = set()
    for p in source_files:
        if any(k in p.name.lower() for k in ("layout", "nav", "sidebar", "header", "tabbar")):
            txt = p.read_text(encoding="utf-8", errors="ignore")
            for pat in LINK_PATTERNS:
                for m in pat.finditer(txt):
                    base_target = m.group(1).split("?")[0].split("#")[0].rstrip("/") or "/"
                    for r in route_files:
                        if route_matches(r, base_target):
                            shell_targets.add(r)

    findings = run_11_heuristics(
        screens=screens,
        edges=edges,
        shell_targets=shell_targets,
        has_loading=has_loading,
        has_error=has_error,
        has_not_found=has_not_found,
    )

    return {
        "framework": framework,
        "repo": str(repo),
        "screens": screens,
        "edges": edges,
        "shellTargets": sorted(shell_targets),
        "findings": findings,
    }


def run_11_heuristics(
    screens: List[Dict[str, Any]],
    edges: List[Dict[str, Any]],
    shell_targets: Set[str],
    has_loading: bool,
    has_error: bool,
    has_not_found: bool,
) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []
    inbound: Dict[str, int] = {s["id"]: 0 for s in screens}
    outbound: Dict[str, int] = {s["id"]: 0 for s in screens}

    for e in edges:
        src, tgt = e["source"], e["target"]
        if src != tgt:
            outbound[src] = outbound.get(src, 0) + 1
        if tgt in inbound and src != tgt:
            inbound[tgt] = inbound.get(tgt, 0) + 1
        # H1: broken-link
        if tgt.startswith("missing:"):
            findings.append(
                {
                    "id": "H01_BROKEN_LINK",
                    "severity": "error",
                    "screen": src,
                    "message": f"Navigation target '{e['rawTarget']}' resolves to no route ({e['evidence']})",
                }
            )

    for s in screens:
        rid = s["id"]
        is_entry = rid == "/" or bool(re.search(r"login|signin|welcome|auth|onboarding", rid, re.I))
        # H2: orphan-screen
        if inbound.get(rid, 0) == 0 and rid not in shell_targets and not is_entry:
            findings.append(
                {
                    "id": "H02_ORPHAN_SCREEN",
                    "severity": "warn",
                    "screen": rid,
                    "message": f"No inbound transition or shell nav reaches '{rid}' ({s['file']})",
                }
            )
        # H3: dead-end
        if outbound.get(rid, 0) == 0 and not s["stateScreens"] and len(screens) > 1:
            findings.append(
                {
                    "id": "H03_DEAD_END_SCREEN",
                    "severity": "info",
                    "screen": rid,
                    "message": f"No outbound link, redirect, or modal leaves '{rid}' ({s['file']})",
                }
            )
        # H4: unguarded-auth-route
        if AUTH_PATH_RE.search(rid) and not s["hasAuthGuard"]:
            findings.append(
                {
                    "id": "H04_UNGUARDED_AUTH_ROUTE",
                    "severity": "warn",
                    "screen": rid,
                    "message": f"Protected-looking route '{rid}' has no detected session/auth guard or middleware ({s['file']})",
                }
            )
        # H5: destructive-without-confirm
        if s["hasDestructive"] and not s["hasConfirm"]:
            findings.append(
                {
                    "id": "H05_DESTRUCTIVE_NO_CONFIRM",
                    "severity": "warn",
                    "screen": rid,
                    "message": f"Destructive action keyword detected without confirmation dialog/modal ({s['file']})",
                }
            )
        # H6: form-without-feedback
        if s["hasForm"] and not s["hasFormFeedback"]:
            findings.append(
                {
                    "id": "H06_FORM_NO_FEEDBACK",
                    "severity": "info",
                    "screen": rid,
                    "message": f"Form detected without visible pending/disabled/error feedback state ({s['file']})",
                }
            )
        # H7: unlabeled-dynamic-route
        if "[" in rid and "]" in rid:
            findings.append(
                {
                    "id": "H07_DYNAMIC_NEEDS_SAMPLE",
                    "severity": "info",
                    "screen": rid,
                    "message": f"Dynamic route '{rid}' requires a concrete sample URL in routeExamples for live capture",
                }
            )

    # H8: missing-loading-state
    if screens and not has_loading:
        findings.append(
            {
                "id": "H08_MISSING_LOADING_BOUNDARY",
                "severity": "info",
                "screen": "/",
                "message": "No route loading boundary (loading.tsx) detected in repository",
            }
        )
    # H9: missing-error-boundary
    if screens and not has_error:
        findings.append(
            {
                "id": "H09_MISSING_ERROR_BOUNDARY",
                "severity": "warn",
                "screen": "/",
                "message": "No route error boundary (error.tsx) detected in repository",
            }
        )
    # H10: missing-not-found
    if screens and not has_not_found:
        findings.append(
            {
                "id": "H10_MISSING_NOT_FOUND",
                "severity": "info",
                "screen": "/",
                "message": "No custom 404 / not-found route (not-found.tsx) detected in repository",
            }
        )

    # H11: deep-click-depth (> 4 hops from "/")
    if any(s["id"] == "/" for s in screens):
        dist: Dict[str, int] = {"/": 0}
        q: deque[str] = deque(["/"])
        adj: Dict[str, List[str]] = {}
        for e in edges:
            adj.setdefault(e["source"], []).append(e["target"])
        for t in shell_targets:
            adj.setdefault("/", []).append(t)
        while q:
            cur = q.popleft()
            for nxt in adj.get(cur, []):
                if nxt not in dist and not nxt.startswith("missing:"):
                    dist[nxt] = dist[cur] + 1
                    q.append(nxt)
        for rid, d in sorted(dist.items()):
            if d > 4:
                findings.append(
                    {
                        "id": "H11_DEEP_CLICK_DEPTH",
                        "severity": "info",
                        "screen": rid,
                        "message": f"Route '{rid}' is {d} hops from '/' (exceeds 4-click depth budget)",
                    }
                )

    return findings


def to_mermaid(report: Dict[str, Any]) -> str:
    lines = ["flowchart LR"]
    node_ids: Dict[str, str] = {}
    for idx, s in enumerate(report["screens"], start=1):
        nid = f"S{idx}"
        node_ids[s["id"]] = nid
        lines.append(f'  {nid}["{s["id"]}"]')
    seen_edges: Set[Tuple[str, str]] = set()
    missing_idx = 1
    for e in report["edges"]:
        src_id = node_ids.get(e["source"])
        if not src_id:
            continue
        if e["target"].startswith("missing:"):
            mid = f"M{missing_idx}"
            missing_idx += 1
            lines.append(f'  {mid}["{e["target"]}"]:::missing')
            lines.append(f"  {src_id} -.-> {mid}")
        else:
            tgt_id = node_ids.get(e["target"])
            if tgt_id and (src_id, tgt_id) not in seen_edges:
                seen_edges.add((src_id, tgt_id))
                lines.append(f"  {src_id} --> {tgt_id}")
    lines.append("  classDef missing stroke:#dc2626,stroke-dasharray: 4 3;")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path, help="Path to target frontend/mobile repository")
    parser.add_argument("--json-out", type=Path, default=None, help="Write JSON report to path")
    parser.add_argument("--mermaid-out", type=Path, default=None, help="Write Mermaid .mmd flow graph to path")
    args = parser.parse_args()

    repo = args.repo.resolve()
    if not repo.is_dir():
        print(f"error: repository directory not found: {repo}", file=sys.stderr)
        return 2

    report = scan_repository(repo)
    mmd = to_mermaid(report)

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.mermaid_out:
        args.mermaid_out.parent.mkdir(parents=True, exist_ok=True)
        args.mermaid_out.write_text(mmd, encoding="utf-8")

    errors = sum(1 for f in report["findings"] if f["severity"] == "error")
    warns = sum(1 for f in report["findings"] if f["severity"] == "warn")
    infos = sum(1 for f in report["findings"] if f["severity"] == "info")

    print(
        f"Code2Flow Audit ({report['framework']}) — {len(report['screens'])} route screens, "
        f"{len(report['edges'])} edges, {errors} errors, {warns} warnings, {infos} info"
    )
    for f in report["findings"]:
        print(f"  [{f['severity'].upper()}] {f['id']} ({f['screen']}): {f['message']}")
    print("\n--- Mermaid User-Flow Graph ---")
    print(mmd)
    return 1 if errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
