---
name: code2flow
description: Map frontend and mobile codebases (Next.js, Expo Router, React Router, TanStack Router, SwiftUI, Flutter, Jetpack Compose, Static HTML) into visual user-flow graphs, live screenshot canvases, PRD story manifests, and 11-heuristic UX gap reports.
---

# Code2Flow — Codebase-to-User-Flow Mapper & UX Gap Auditor (`code2flow`)

Statically and dynamically map any frontend or mobile repository into a verified user-flow topology (Mermaid `.mmd`, JSON `graph.json`, or offline HTML screenshot canvas), validate PRD user stories against real code transitions, and audit against 11 structural UX heuristics.

When NOT to use: visual design or taste (`design-uiux`), runtime UI review (`audit-uiux-web` / `audit-uiux-mobile`), or changing the app to satisfy the graph (`frontend-web-engineering` / `frontend-mobile-engineering`). This skill maps structure and reports gaps; it does not edit the target.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

---

## 1. Core Capabilities & Progressive Disclosure

Load only the reference file matching the current job:

| Task / Job | Reference to Load | CLI / Script |
| :--- | :--- | :--- |
| **Static Route Extraction, Mermaid Graph & 11-Heuristic Audit** | Section 2 & 3 below | `python3 skills/code2flow/scripts/code2flow_audit.py <repo>` |
| **Full Interactive Flow Canvas (`init -> run -> serve/export`)** | [canvas-and-prd-stories.md](references/canvas-and-prd-stories.md) | `npx design-os-code2flow run <repo>` |
| **PRD -> Story Manifest (`code2flow.stories.json`) & Drift Check** | [canvas-and-prd-stories.md](references/canvas-and-prd-stories.md) | `code2flow stories scaffold <repo> <prd.md>` |
| **Reachability, Shortest Paths & Evidence Queries** | [canvas-and-prd-stories.md](references/canvas-and-prd-stories.md) | `code2flow paths <repo> --from <A> --to <B>` |
| **Transition Confidence Tiers & Screenshot Capture Rules** | [confidence-and-capture.md](references/confidence-and-capture.md) | `high` / `medium` / `low` / `missing` |
| **Framework Adapter Rules (Next.js, React Router, Static HTML, Hover)** | [adapters.md](references/adapters.md) | Route & State Screen normalization |
| **`code2flow.config.json` & `code2flow.stories.json` Schema** | [config-reference.md](references/config-reference.md) | `serverUrl`, `routeExamples`, `login`, `stage` |

---

## 2. Fast Zero-Dependency Static Audit & Mermaid Flow Generation

For any Next.js (App or Pages Router), Expo Router, React Router, TanStack Router, SwiftUI, Flutter, Jetpack Compose, or Static HTML repository, run the bundled Python auditor first to extract the route graph, emit a Mermaid diagram, and check all 11 UX heuristics in milliseconds:

```bash
python3 skills/code2flow/scripts/code2flow_audit.py /path/to/repo \
  --json-out /tmp/code2flow-graph.json \
  --mermaid-out /tmp/code2flow-flows.mmd
```

Need a publication-grade editorial SVG/PNG of the extracted `.mmd` user flow? Hand `/tmp/code2flow-flows.mmd` directly to `diagram-design` (`import-mermaid.md`).

---

## 3. The 11 Structural UX & Flow Heuristics

Every `code2flow` audit evaluates the extracted route graph against 11 structural heuristics with `file:line` evidence:

| ID | Rule | Severity | What It Catches |
| :--- | :--- | :--- | :--- |
| **`H01_BROKEN_LINK`** | `broken-link` | `error` | Literal `href`, `to`, `router.push`, or `redirect` pointing to a route that does not exist (`missing:<path>`). |
| **`H02_ORPHAN_SCREEN`** | `orphan-screen` | `warn` | Route screen with zero inbound transitions and no entry in shared layout/shell navigation. |
| **`H03_DEAD_END_SCREEN`** | `dead-end` | `info` | Route screen with zero outbound links, redirects, or state-screen actions leading anywhere. |
| **`H04_UNGUARDED_AUTH_ROUTE`** | `unguarded-auth-route` | `warn` | Protected-looking route (`/dashboard`, `/admin`, `/settings`, `/billing`, `/account`) lacking middleware or session/auth guard. |
| **`H05_DESTRUCTIVE_NO_CONFIRM`** | `destructive-without-confirm` | `warn` | Destructive action (`delete`, `remove`, `revoke`, `destroy`) on a screen with no confirmation modal/dialog. |
| **`H06_FORM_NO_FEEDBACK`** | `form-without-feedback` | `info` | `<form>` or `useForm` handler without visible pending/disabled/error feedback state. |
| **`H07_DYNAMIC_NEEDS_SAMPLE`** | `needs-sample` | `info` | Dynamic route (`[slug]`, `[id]`) needing a concrete sample path in `routeExamples` for live screenshot capture. |
| **`H08_MISSING_LOADING_BOUNDARY`** | `missing-loading-state` | `info` | Repository lacks route loading boundaries (`loading.tsx`). |
| **`H09_MISSING_ERROR_BOUNDARY`** | `missing-error-boundary` | `warn` | Repository lacks route error boundaries (`error.tsx`). |
| **`H10_MISSING_NOT_FOUND`** | `missing-not-found` | `info` | Repository lacks a custom 404 / `not-found.tsx` boundary. |
| **`H11_DEEP_CLICK_DEPTH`** | `deep-click-depth` | `info` | Route requires `> 4` navigation hops from `/`, hurting discoverability. |

---

## 4. Live Screenshot Flow Canvas & PRD Drift Workflow

When the user wants a live interactive Flow Canvas with real Chrome screenshots, Present/Stage mode, or PRD story-lane validation ([canvas-and-prd-stories.md](references/canvas-and-prd-stories.md)):

1. **Initialize config:** `npx design-os-code2flow init <repo>` (writes `code2flow.config.json` and gitignores `.code2flow/`).
2. **Scan, capture & export:** `npx design-os-code2flow run <repo> [--url http://127.0.0.1:<port>]` -> outputs `.code2flow/graph.json`, `.code2flow/run-summary.json`, and offline `.code2flow/export/<repo>-flows.html`.
3. **Validate PRD stories:**
   - Run `npx design-os-code2flow stories scaffold <repo> <path/to/prd.md>`.
   - Draft `code2flow.stories.json` using **only** screen IDs from `.code2flow/graph.json` (never invent transitions or reorder PRD steps to hide drift).
   - Run `npx design-os-code2flow stories validate <repo>` to surface unknown screens and unimplemented PRD transitions.

---

## 5. Non-Negotiable Rules

- **Never edit target application code just to silence the parser or linter** — report every broken link, orphan screen, or parser counter (`needs-sample`, `login-redirect`, `unresolved-expression`) with `file:line` evidence.
- **Never leave a background dev server running** after `code2flow run` completes.
- **Never answer reachability or flow questions from memory** when `.code2flow/graph.json` or `code2flow_audit.py` output is available.

---

> Adapts the [DESIGN:OS](https://github.com/jangtrinh) engines by Jang Trinh under the PolyForm Shield 1.0.0 license (<https://polyformproject.org/licenses/shield/1.0.0>).
> Required Notice: Copyright (c) 2026 Jang Trinh (https://github.com/jangtrinh)
> See [NOTICE](../../NOTICE.md).
