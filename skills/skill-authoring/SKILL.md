---
name: skill-authoring
description: Write, rewrite, split, or prune a skill in this library. Use when adding a skill, fixing one that routes wrongly, loads too much, or lost its evidence. Not for product docs (→ product-discovery), code documentation (→ documentation), or read-only review (→ skill-reviewer).
---

# Skill Authoring

Own the library itself: turn a real failure into a rule, put the rule in the
smallest skill that can carry it, and prove the result with an eval case. The
artifact is a changed skill that a zero-context agent can follow, plus the
cases that justify it.

Shared vocabulary: [ontology](../_shared/ontology.md). The writing standard is
[authoring](../_shared/authoring.md); read it before the first edit.

## When NOT to use

- Writing a PRD, spec, or product doc → `product-discovery`.
- Documenting code or an API for humans → the `documentation` skill, when
  installed.
- Reviewing a skill you did not change, with no intent to edit → the
  `skill-reviewer` agent.
- Adding a product fact (voice, routes, names, prices) → the product repo, not
  this library.

## 1. Pick the job

Say which one before editing. They have different gates.

| Job | Trigger | Artifact |
| --- | --- | --- |
| **New** | No skill owns the request; a neighbour is being stretched | A new `SKILL.md`, eval case, routing case |
| **Rewrite** | The skill fires for the wrong request, or a step cannot be followed | Same file, one instruction where there were two |
| **Split** | `SKILL.md` passes 300 lines and the excess is depth | A shorter router plus `references/` |
| **Prune** | A rule no longer earns its context | A deletion, with the eval still passing |

If the request is "make it better", ask for the failing request. A rewrite with
no failure is a preference, and preferences do not enter this library.

## 2. Find the owner and the boundary

Check [`ROUTING.md`](../../ROUTING.md) and the descriptions of the nearest
three skills. Write one sentence:

> `<request>` routes to `<skill>` because `<it owns the artifact>`, not
> `<neighbour>`, which owns `<different artifact>`.

If two skills could own it, the request is two jobs or the descriptions are
wrong. Fix the boundary before writing the body. Never add a skill that only
rewords a neighbour.

## 3. Write the description first

The description is the router. Write it to
[authoring](../_shared/authoring.md) § The description: job first, the
near-miss trigger phrases, then `Not for X (→ skill)`, inside the 80-word
budget.

Test it cold: show only the description to a fresh agent and ask which of three
real prompts it would take. If it takes the wrong one, rewrite the description
before the body.

## 4. Write the body to the frame

Follow [authoring](../_shared/authoring.md) § The frame. The non-negotiables:

- **Numbered workflow**, each step producing something inspectable.
- **Gates** with a known failing input. A gate that has never gone red has not
  been shown to work.
- **Failure modes** with the correction, not just the symptom.
- **Hand-over** that separates ran / proved / skipped, and marks unobserved as
  `NOT_RUN` or `UNKNOWN`.
- **No private vocabulary.** Link the ontology and use its terms.

Keep the main file under 300 lines. Move depth a step opens only sometimes into
`references/`, and name the condition in the step. A reference every run needs
belongs in the main file.

## 5. Add the cases

1. **Behavior case** — `evals/<skill>-regression.md`: a realistic prompt,
   expected behavior, and a `Must not have` list. Write the case that would
   have caught the failure from § 1.
2. **Routing case** — a line in
   [`evals/routing.txt`](../../evals/routing.txt) when the trigger or boundary
   changed: `id|expected|prompt`.
3. **Negative case** — one prompt that must route elsewhere or to `none`, so a
   greedy description fails loudly.

No case, no rule. If the failure cannot be stated as a prompt and an expected
behavior, it is not yet understood well enough to encode.

## 6. Run the gates

Run from the repository root:

```sh
scripts/lint-skills.sh
```

If the script is missing or not executable, record
`CHECKS: scripts/lint-skills.sh → not found`, mark the structural gate
`NOT_RUN`, and name the checks you therefore did not run. Never report a `PASS`
you did not earn.

The lint enforces structure, links, the 80-word description budget, the
ontology link, and the presence of an eval case. An imported skill that exceeds
a budget is pinned in `scripts/lint-baseline.txt`; that file is shrink-only, so
lower an entry when the skill shrinks and never raise one to make lint pass.
The lint cannot check whether the steps are followable.

Then hand the changed files and their cases to `skill-reviewer`. Its findings
are eval-case candidates, not style notes. A `P0` or `P1` blocks the change.

Run `scripts/eval-routing.sh` only when routing changed; it spends tokens.

## 7. Hand over

Return exactly:

```text
CHANGED: <files, one line each, with why>
JOB: new | rewrite | split | prune
FAILURE: <the request or eval case that motivated it>
BOUNDARY: <what this owns / what the neighbour owns>
CASES: <added or changed, with ids>
CHECKS: <command → exit code>
REVIEW: <skill-reviewer verdict, or NOT_RUN>
NOT_VERIFIED: <anything not run, read, or confirmed>
```

## Failure modes

| Symptom | Cause | Correction |
| --- | --- | --- |
| Skill fires for a neighbour's request | Description lists features instead of a job, or no `Not for` | Rewrite the description around the artifact; add the negative case |
| Agent skips a step | Step is advice, not an action | Make it produce a file, command, table, or verdict |
| Context is huge before work starts | Depth sits in `SKILL.md` | Split to `references/`, name the condition in the step |
| Two skills disagree | Rule duplicated instead of linked | Pick one owner; link from the other |
| Eval passes but the behavior is wrong | Case tests wording, not outcome | Rewrite the case around the artifact and its failing input |
| Imported skill loses its license | Footer or `NOTICE.md` missing | Restore the source, license, and required notice before commit |

## Changing this skill

Start from a real authoring failure — a skill that shipped and then routed
wrongly, loaded too much, or could not be followed cold. Add the case first,
then change the rule it points at. Keep this file a router for the standard,
not a second copy of it.
