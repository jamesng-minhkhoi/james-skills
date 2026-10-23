# James Skills

Reusable Codex and Claude skills extracted from project work.

## Skills

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
- [`seo-aeo-content`](skills/seo-aeo-content/SKILL.md) — audit Petio search
  performance, improve existing articles, and write new evidence-led content
  with reusable daily and monthly workflows.
- [`petio-marketing`](skills/petio-marketing/SKILL.md) — plan, schedule, and
  iteratively improve Petio marketing content using Buffer evidence and
  platform-specific adapters.
- [`threads-engagement`](skills/threads-engagement/SKILL.md) — research, draft,
  publish, and measure authentic Threads posts and replies.
- [`x-engagement`](skills/x-engagement/SKILL.md) — research, draft, execute, and
  measure authentic X posts, replies, threads, and listening experiments.

## Agents and routing

[`ROUTING.md`](ROUTING.md) says which skill handles what and in what order
(design → build → audit; marketing never edits code). Skills still load on
their own from their descriptions; the routing guide covers the seams between
them.

[`agents/`](agents) holds Claude Code subagents, added only where a separate
context pays for itself:

- [`auditor`](agents/auditor.md) — independent, edit-free UI/UX and
  store-readiness audits with the three audit skills preloaded. It exists
  because a review is worth more when it is not done by whoever built the UI.

Add another agent when real work shows the need (for example, marketing runs
that flood the main session), not for symmetry.

Each skill is self-contained and can be copied or linked into a Codex or Claude
skills directory. Keep project-specific branding, routes, and business rules
in the source repository rather than hard-coding them into a reusable skill.

## Install

```sh
./install.sh            # symlink every skill into the agent skill directories
./install.sh --dry-run  # show what would change first
```

By default this links skills into `~/.claude/skills`, `~/.codex/skills`, and
`~/.agents/skills`, links agents into `~/.claude/agents`, and adds a marked
routing block to `~/.claude/CLAUDE.md` (a live `@import`) and
`~/.codex/AGENTS.md` (a copy, refreshed on each run). Pass directories as
arguments to link skills into specific targets only.
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
4. **Commit with the case name**, e.g. `fix: x-engagement fired for Petio posts
   (routing case petio-threads)`, so the log records why each rule exists.

Budgets: descriptions ≤ 80 words, `SKILL.md` ≤ 300 lines, `ROUTING.md` ≤ 40
lines. Skills already over budget are listed in
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
