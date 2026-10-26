# Flow Canvas, PRD Story Manifests & Path Query Playbook

This reference combines the three operational workflows of Code2Flow:
1. **Mapping a Codebase to a Flow Canvas (`map-codebase`)**
2. **Turning a PRD into a Validated Story Manifest (`stories-from-prd`)**
3. **Answering Reachability & Drift Questions from `.code2flow/graph.json` (`answer-flow-questions`)**

---

## 1. Workflow A — Map Codebase to Flow Canvas (`code2flow init` + `run`)

Everything runs locally with zero telemetry. When using the full Playwright screenshot canvas (`npx design-os-code2flow` or `code2flow`):

### Preconditions
1. Check if `code2flow` is installed (`code2flow --help` or run the zero-dependency static auditor `python3 skills/code2flow/scripts/code2flow_audit.py <repo>`).
2. Respect the target repo's fixed `localhost_port` contract if declared in `.project-agent.md`. Never silently pick another port if a server is already listening; pass `--url http://127.0.0.1:<port>` instead.

### Procedure
1. `code2flow init <repo>` — creates `code2flow.config.json` ([config-reference.md](config-reference.md)), adds `.code2flow/` to `.gitignore`.
2. Populate `routeExamples` in `code2flow.config.json` for dynamic routes (full paths like `/products/omniact`, never bare slugs) when `scan` flags `needs-sample`.
3. `code2flow run <repo>` (or `code2flow run <repo> --url http://127.0.0.1:<port>`) — runs `scan -> snapshot -> stories validate -> lint -> export` and stops any dev server it started.
4. Inspect exit codes:
   - `0`: Completed with zero lint errors.
   - `1`: Completed, but lint found a broken link (`broken-link`).
   - `2`: Did not run (port conflict, missing `serverUrl`, dev server failure, or invalid `code2flow.stories.json`).
5. Deliver `.code2flow/export/<repo>-flows.html` (offline interactive HTML canvas) or start `code2flow serve <repo>` on `http://127.0.0.1:4317`.

### Reporting Contract
```text
Status: DONE | DONE_WITH_CONCERNS
Screens: <routes> routes + <n> state screens · Edges: high/medium/low · Captured: x/y
Gaps: <needs-sample, login-gated, capture-failed>
Lint: <errors> errors (broken links), <warnings> warnings, <info> to review
Export: <path>
```

---

## 2. Workflow B — PRD to Validated Story Manifest (`code2flow.stories.json` v3)

Turns a Product Requirements Document (`prd.md`) into user-story lanes on the Flow Canvas and detects PRD-vs-code drift.

### Rules (Nothing Invented)
- Run `code2flow stories scaffold <repo> <prd.md>` to generate `<repo>/.code2flow/stories-prompt.md` containing the schema, all discovered screen IDs, and the PRD text.
- Use **only** screen IDs from the scanned graph. If the PRD names a screen that does not exist in code, include its expected route ID in `screens` so `code2flow stories validate <repo>` reports it as an `unknown screen` drift signal.
- One story = one user goal (`id` kebab-case, `title` verbatim from PRD, `source: "<prd-path>#<heading-slug>"`).
- Walk every `steps` chain (`{ "screen", "via", "caption", "note", "cue" }`) against `.code2flow/graph.json`:
  - `via` is the exact UI trigger label (`"Approve"`, `"Save changes"`), never prose.
  - If a PRD transition has no matching edge in `graph.json`, keep the step and add `"note": "asserted by PRD, not detected in code"` so drift is surfaced explicitly.
- Never delete stories silently when updating `code2flow.stories.json` — mark superseded stories `"archived": true`.
- Run `code2flow stories validate <repo>` and report all unknown screens, missing transitions, and unmapped PRD sections.

---

## 3. Workflow C — Answering Flow & Reachability Questions

Always answer from `.code2flow/graph.json` or `code2flow_audit.py` output with `file:line` evidence and transition confidence ([confidence-and-capture.md](confidence-and-capture.md)) — never from memory.

| Question | Command / Query | What to Report |
| :--- | :--- | :--- |
| **How do users get from A to B?** | `code2flow paths <repo> --from <A> --to <B> [--shell]` | Up to 5 shortest paths; each hop = trigger label + confidence (`high`/`medium`/`low`) + `file:line`. |
| **Which screens are unreachable or dead ends?** | `code2flow paths <repo> --orphans` / `--dead-ends` or `code2flow lint <repo> --json` | `orphan-screen` (no inbound edge and not in shell nav) and `dead-end` (no outbound action/link). |
| **Which links are broken?** | `code2flow lint <repo> --json` | `broken-link` (`severity: error`) — literal `href`/`to`/`push` that resolves to no route. |
| **Where does the PRD disagree with code?** | `code2flow stories validate <repo>` | `unknown screen` (PRD screen missing in code) and `no detected transition A -> B via "X"`. |
| **What did the parser see but not draw?** | `graph.json -> counters` | `needs-sample`, `unresolved-expression`, `login-redirect`, `capture-failed` ([adapters.md](adapters.md)). |
