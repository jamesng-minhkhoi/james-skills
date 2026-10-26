# Spec templates and rules

Load for Spec-mode work. These templates produce specs that `design-uiux` and
the frontend engineering skills can execute mechanically; the downstream cost
of each omitted decision is noted inline.

## Job story (per requirement)

```
When <situation in the user's context: device, state of things, urgency>,
I want <capability in user language>,
so I can <outcome that resolves the situation>.
```

Acceptance criteria under each story, each as a checkable statement. A
checkable criterion: a designer can verify it against a rendered flow, or an
engineer can write a passing test from it. "Works well" and "feels fast" are
not checkable; the metric table exists exactly for those cases.

**Downstream cost omitted criteria hide:** permission states, empty and error
rendering, and what happens when two users act at once. List them even when
the answer is "match existing patterns" — vague calls become invented behavior.

## PRD skeleton

```
# PRD: <feature>
Status: <READY | READY_WITH_CONDITIONS | NOT_READY | UNKNOWN> — <why>

## Problem
<2–4 sentences with claim statuses inline, e.g. "30% of trial users never
invite anyone (verified, dashboard path, 2026-07)">

## Who and jobs
- <segment>: <job>, <frequency of occurrence>

## Requirements
<job stories + acceptance criteria; or scoped sections if PRD-style>

## Interface states described (not designed)
loading / empty / typical / dense / pending / success / error / retry /
offline-or-stale — whichever apply, one checkable line each.

## Non-goals
- <explicitly out of scope, and the one-line reason>

## Success metrics
| Metric | Definition | Target | Instrument | Owner |
|---|---|---|---|---|
| ... | event/property | value+deadline | where it is tracked | who answers for it |

## Open questions
| Question | Current thinking | Claim status | What resolves it |
```

## Verdict rules

- `READY`: every acceptance criterion checkable, all open questions have
  owners and non-default answers recorded, metrics have instruments and owners.
- `READY_WITH_CONDITIONS`: build can start where independent of the open
  questions; conditions name them and the sequence.
- `NOT_READY`: one or more core criteria are still discretionary. Say which
  sentence of the spec depends on the blocker.
- `UNKNOWN`: requested without enough context to even outline requirements.

## Claim statuses in specs

Inherited from [the ontology](../../_shared/ontology.md), not redefined: a spec
is full of claims about behavior, outcomes, and market. Mark the load-bearing
ones — the ones the readout later judges — with status and evidence path.
Unmarked healthy claims are `unverified`; that is allowed for minor ones but
not for metrics targets or any requirement sentence.
