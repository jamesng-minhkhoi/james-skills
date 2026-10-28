# Authoring a skill

The house standard for writing, rewriting, splitting, or pruning a skill in
this library. `scripts/lint-skills.sh` enforces the mechanical parts; this file
explains the judgment the lint cannot check.

A skill is a contract between the author today and an agent tomorrow. That
agent has no memory of why a line exists, cannot ask, and will read a vague
clause literally. Write for that reader.

## The frame

Every `SKILL.md` follows the same order. Omit a section only when it would be
empty.

1. **Frontmatter** — `name` matches the folder; `description` ≤ 80 words.
2. **What this owns** — one or two sentences: the job, and the artifact it
   produces.
3. **When to use / when NOT** — both sides. Name the neighbouring skill that
   owns the excluded case.
4. **Shared vocabulary** — link [`ontology.md`](ontology.md). Never redefine a
   gate, verdict, severity, proof rung, or claim status privately.
5. **Workflow** — numbered steps. Each step produces something a reader can
   inspect, run, or cite. Not "consider", "ensure", "be careful".
6. **Gates** — what must be true before the work is called done, each with a
   known failing input.
7. **Failure modes** — the ways this skill goes wrong and the correction. A
   skill with no failure modes gives the next reader nothing to diagnose.
8. **Hand-over** — the exact block to return: what ran, what it proved, what
   was skipped, what is `NOT_VERIFIED`.
9. **Changing this skill** — start from an eval case, not a preference.

## The description

The description is the router. It is the only text every session pays for, so
it carries the trigger and the boundary.

- Start with the job, in the words a person would type.
- Include the near-miss phrases that should land here.
- End with `Not for X (→ skill)` when a neighbouring skill could be mistaken
  for this one.
- No marketing adjectives, no list of every feature, no restating the workflow.
- ≤ 80 words, at most three sentences: the job, the trigger phrases, the
  boundary. If it needs more, the skill probably owns two jobs.

## Progressive disclosure

Load only what the current job needs.

- `SKILL.md` holds the decision and the steps. `references/` holds detail a
  step opens only sometimes, and the step names the condition.
- A reference that every run needs belongs in the main file, not in a link the
  reader may skip.
- Do not duplicate a rule across files. One owner, linked from the others.
- Split when a section is opened by fewer than half the runs, or when the file
  passes 300 lines and the excess is depth rather than steps.
- A router skill routes; it does not also execute.

## Constraint language

- **State both sides.** Say what is allowed and what is not. A rule that only
  forbids leaves the safe path to guesswork.
- **Every prohibition carries its mechanism.** "Do not cache the token because
  a stale token survives sign-out" beats "do not cache the token".
- **CAPS only for load-bearing words.** NEVER, MUST, and NOT earn attention
  only when most sentences do not use them.
- **Repeat a core constraint at its point of use.** A reader arriving
  mid-file never saw the preamble.
- **No hardcoded counts.** "The six checks" rots; name the checks or let lint
  count them.

## Evidence and provenance

- Every externally checkable claim names its source, date, and status. A claim
  without all three is `unverified` per the ontology.
- A fact adapted from another project's skill keeps a footer naming the source
  and license, and the license text goes in [`NOTICE.md`](../../NOTICE.md).
- Product facts (voice, routes, names, prices) belong in the product repo, not
  in a reusable skill. This library holds method.
- A command the skill tells the agent to run must exist, or the skill must say
  what to do when it is absent and mark the gate `NOT_RUN`.

## Evals

Every skill has at least one behavior case in its own `evals/` directory;
routing cases live in the repository-level [`evals/routing.txt`](../../evals/routing.txt).

A behavior case is a realistic prompt plus expected behavior and a "must not
have" list. It is not a unit test and does not need code. Write the case that
would have caught the failure that motivated the change. If you cannot state
the failing input, you are not ready to write the rule.

## The rewrite test

Before keeping a rewrite, hand the changed files to `skill-reviewer` with the
eval cases. A cold reader who cannot follow the file from the file alone has
found a defect the author cannot see.

## Checklist

- [ ] `name` matches the folder; description ≤ 80 words, with a trigger and a
      `Not for X (→ skill)` boundary.
- [ ] The job and the artifact are stated in the first two sentences.
- [ ] Every step produces an inspectable result.
- [ ] Gates have known failing inputs.
- [ ] Failure modes name the correction.
- [ ] The hand-over block separates ran / proved / skipped.
- [ ] Ontology linked, no private synonyms.
- [ ] At least one eval case; routing case added when the trigger changed.
- [ ] Links resolve; `scripts/lint-skills.sh` passes.
- [ ] Adapted material attributed in the footer and `NOTICE.md`.
