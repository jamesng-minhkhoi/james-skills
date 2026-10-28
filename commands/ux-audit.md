---
description: Run an independent UI/UX or store submission audit without making code edits
---

Delegate to the `auditor` subagent or apply the relevant audit skill (`audit-uiux-web`, `audit-uiux-mobile`, `audit-mobile-store-submission`) to:
$ARGUMENTS

Audit rules:
1. Builder ≠ verifier: provide an independent review; do not edit code or apply fixes unless explicitly asked.
2. Structure findings with `F-*` IDs, severity (P0-P3), and evidence path or runtime proof.
3. Use the proof ladder (declared < rendered < interactive < connected < failure-tested < device < production).
4. Output verdicts with closed vocabulary: PASS | FAIL | BLOCKED | NOT_RUN.
