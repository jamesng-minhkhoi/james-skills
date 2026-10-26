# James Skills

Reusable Codex and Claude skills extracted from project work.

## Skills

- [`product-discovery`](skills/product-discovery/SKILL.md) — frame product
  opportunities from evidence, write buildable PRDs and job stories with
  acceptance criteria and success metrics, prioritize backlogs, and run
  post-launch readouts.
- [`design-uiux`](skills/design-uiux/SKILL.md) — design mobile screens, web
  apps, dashboards, and landing pages as options on the Design canvas, then
  plan the build.
- [`frontend-mobile-engineering`](skills/frontend-mobile-engineering/SKILL.md) —
  implement and verify Expo React Native mobile behavior.
- [`audit-uiux-mobile`](skills/audit-uiux-mobile/SKILL.md) — audit mobile
  journeys with evidence-backed visual and accessibility QA.
- [`audit-uiux-web`](skills/audit-uiux-web/SKILL.md) — audit responsive web
  journeys with browser, accessibility, visual-system, motion, and proof QA.
- [`frontend-web-engineering`](skills/frontend-web-engineering/SKILL.md) — build,
  test, and verify production-ready frontend web application changes.
- [`audit-mobile-store-submission`](skills/audit-mobile-store-submission/SKILL.md)
  — audit App Store and Google Play submission readiness, rejection risks, and
  external release gates.
- [`threads-engagement`](skills/threads-engagement/SKILL.md) — research, draft,
  publish, and measure authentic Threads posts and replies.
- [`x-engagement`](skills/x-engagement/SKILL.md) — research, draft, execute, and
  measure authentic X posts, replies, threads, and listening experiments.
- [`product-video`](skills/product-video/SKILL.md) — storyboard, choreograph,
  render, and verify deterministic 1080p 60fps product launch videos, UI
  walkthroughs, and 16:9 + 9:16 social reels.
- [`diagram-design`](skills/diagram-design/SKILL.md) — generate editorial
  HTML/SVG diagrams and data charts across 27 visual types, or redraw `.drawio`
  and Mermaid `.mmd` diagrams with PNG/SVG export and brand onboarding.
- [`seo-aeo-geo`](skills/seo-aeo-geo/SKILL.md) — audit, scaffold, and optimize
  web apps, landing pages, docs sites, and GitHub repositories for SEO, Answer
  Engines (AEO / JSON-LD), and Generative Engines (GEO / `llms.txt` / 12-section
  READMEs).
- [`code2flow`](skills/code2flow/SKILL.md) — map frontend and mobile codebases
  into visual user-flow graphs, live screenshot canvases, PRD story manifests,
  and 11-heuristic UX gap reports.
- [`blender-3d-studio`](skills/blender-3d-studio/SKILL.md) — build, reconstruct,
  verify, and render 3D assets, mechanical CAD parts, 3D-printable STL/GLB
  solids, and procedural Three.js models using headless Blender (`bpy`) and
  deterministic `AGENT_OK` production gates.
- [`knowledge-builder`](skills/knowledge-builder/SKILL.md) — compile research
  into verified knowledge packs: sources frozen with sha256, claims promoted
  only when their verbatim quote verifies against the frozen capture, documents
  citing claims, and a ledger-backed epistemic stopping gate. Drives the
  [design-os-knowledge-builder](https://github.com/jangtrinh/design-os-knowledge-builder)
  CLI (PolyForm Shield 1.0.0 — used per its license, not copied); the skill text
  here is original.
- [`cv-and-career-ops`](skills/cv-and-career-ops/SKILL.md) — engineer FAANG-grade
  CVs (Google XYZ formula, monochrome HTML/LaTeX templates, 2-page Playwright
  PDF export) and run an AI career command center (A–G job evaluation, ghost-job
  detection, cover letters, LinkedIn outreach, STAR+R interview prep, and
  offer-contract reading).
- 16 `offensive-*` skills — SQLi, XSS, SSRF, SSTI, XXE, IDOR, file upload, RCE,
  deserialization, race conditions, request smuggling, open redirect, parameter
  pollution, GraphQL, WAF bypass, and business logic — adapted from
  [Claude-Red](https://github.com/SnailSploit/Claude-Red) (MIT; see
  [`NOTICE.md`](NOTICE.md)). Authorized targets only: each file's footer and
  `ROUTING.md` gate the scope before the first probe.

## Agents and routing

[`ROUTING.md`](ROUTING.md) says which skill handles what and in what order
(decide → design → build → audit; marketing never edits code). Skills still load on
their own from their descriptions; the routing guide covers the seams between
them.

[`agents/`](agents) holds subagents, added only where a separate context pays
for itself. `agents/*.md` is written once, in the Claude Code dialect;
`install.sh` links it into `~/.claude/agents` directly and generates converted
configs for OpenCode (permission denials), Codex (read-only TOML sandbox), and
Gemini (a tools allowlist that omits write tools):

- [`auditor`](agents/auditor.md) — independent, edit-free UI/UX and
  store-readiness audits with the three audit skills preloaded. It exists
  because a review is worth more when it is not done by whoever built the UI.
- [`skill-reviewer`](agents/skill-reviewer.md) — a zero-context pre-ship read of
  a changed skill, its references, `ROUTING.md`, or an agent definition. It
  holds only the handed files, so it fails exactly where the author — who
  already knows what they meant — passes, and every finding must be convertible
  into an eval case.

Add another agent when real work shows the need (for example, marketing runs
that flood the main session), not for symmetry.

Each skill is self-contained and can be copied or linked into a Codex or Claude
skills directory. Keep project-specific branding, routes, and business rules
in the source repository rather than hard-coding them into a reusable skill.

## Shared vocabulary

[`skills/_shared/ontology.md`](skills/_shared/ontology.md) is the one definition
of proof levels, verdicts, severities, claim status, and finding IDs. Every
skill links to it; the six-line card in `ROUTING.md` is the part that loads in
every session. Two other shared references hold mechanics that were duplicated:
[`ai-tone.md`](skills/_shared/ai-tone.md) and
[`loading-and-memoization.md`](skills/_shared/loading-and-memoization.md).
[`fix-report.md`](skills/_shared/fix-report.md) is the audit-to-fix handoff,
keyed by finding ID.

`_shared/` is not a skill: it has no `SKILL.md`, so it never competes for
routing. `install.sh` links it beside the skills so `../_shared` resolves in
both this repo and the installed targets. `lint-skills.sh` fails a skill that
does not link the ontology or that uses a retired synonym.

## Install

```sh
./install.sh            # symlink every skill into the agent skill directories
./install.sh --dry-run  # show what would change first
```

By default this links skills into `~/.claude/skills`, `~/.codex/skills`,
`~/.agents/skills`, and `~/.gemini/skills` — those four cover Claude, Codex,
OpenCode (which also reads the Claude and `.agents` paths), and Gemini.
Subagents are installed per harness: linked into `~/.claude/agents`, generated
into `~/.config/opencode/agents`, `~/.codex/agents`, and `~/.gemini/agents`
with each harness's frontmatter and the agent's tool bans translated. It also
writes a marked routing block into `~/.claude/CLAUDE.md` (a live `@import`) and
copies it into `~/.codex/AGENTS.md`, `~/.config/opencode/AGENTS.md`, and
`~/.gemini/GEMINI.md` (all copies, refreshed on each run). Pass directories as
arguments to link skills into specific targets only. Generated agent files
carry a managed marker so re-running after a rename or removal prunes stale
copies; edits always go to the repo file, never the generated one.
Symlinks mean an edit here takes effect everywhere immediately — a copied skill
silently goes stale, and a stale copy of a renamed skill keeps competing with
its replacement at skill-selection time. Re-run after adding, renaming, or
removing a skill; the script replaces outdated entries and prunes links whose
target no longer exists.

## Changing a skill

Change skills from evidence, and keep what loads in every session small.

1. **Start from a failure.** A real request routed wrongly or a skill produced
   a bad result. Capture it first: a line in [`evals/routing.txt`](evals/routing.txt)
   for routing, or a case in the skill's own `evals/` file for behavior. No
   failing case, no new rule.
2. **Fix by rewriting, not appending.** Edit the section the failure points
   at so it still reads as one instruction. Detail a step needs only some of
   the time goes in `references/`, linked from the step that needs it.
3. **Check.**
   ```sh
   scripts/lint-skills.sh      # structure, links, and size budgets
   scripts/eval-routing.sh     # routing cases (headless Claude; costs tokens)
   ```
   For a behavioral rewrite, first hand the changed files to the
   `skill-reviewer` agent: a zero-context read whose findings are eval-case
   candidates. What a cold reader cannot follow does not ship.
4. **Commit with the case name**, e.g. `fix: x-engagement fired for Petio posts
   (routing case petio-threads)`, so the log records why each rule exists.

Budgets: descriptions ≤ 80 words, `SKILL.md` ≤ 300 lines, `ROUTING.md` ≤ 40
lines, and at least one behavior case in every skill's `evals/` directory.
Skills already over budget are listed in
[`scripts/lint-baseline.txt`](scripts/lint-baseline.txt) and may shrink but
not grow; lower the number when you trim.

**Prune every month or two.** Remove a section, run the checks and the skill's
eval cases; if nothing regresses, leave it removed. Rules written for weaker
models or one-off incidents become dead weight.

**Keep knowledge in the right place.** How to do the work → skill. Facts about
a product (voice, features, routes) → that product's repo. What worked lately
(post performance, reply patterns) → a dated learning ledger in the product
repo, promoted into a skill's references only once it holds across cycles.

Add an agent or split a skill the same way: when eval cases show the need.
