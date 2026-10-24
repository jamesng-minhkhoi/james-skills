# Ontology

The shared vocabulary for every skill in this library. Load it before emitting a
proof level, verdict, finding, or claim. Skills may add domain terms; they may
not rename these.

## Entities

- **Skill** — owns one job; has a description, references, and evals.
- **Request → Route → Run** — a request routes to one skill, which runs.
- **Artifact** — the thing judged: route, build, post, article, submission.
- **Claim** — any statement about the product or the world.
- **Evidence** — a path, command output, screenshot, portal state, or source.
- **Finding** — a defect with an ID, severity, evidence, and owner.
- **Gate** — a check with a binary result.
- **Verdict** — the gate or deliverable result.
- **Receipt** — what ran, when, on which artifact, with what result.

## Invariants

1. One term per concept; no synonyms in any skill.
2. A claim without an evidence path is `inferred`, never `verified`.
3. Unobserved is `NOT_RUN` or `UNKNOWN`, never `PASS`.
4. A finding keeps its ID from audit to fix to re-audit.
5. Builder ≠ verifier for any audit.
6. Every gate has a known failing input.
7. No verdict without the artifact or build it applies to.
8. New or unmarked claims start `unverified`; trust is only ever lowered.

## Proof ladder

`declared < rendered < interactive < connected < failure-tested < device < production`

- **declared:** source, config, or prose says it.
- **rendered:** a screenshot or static render shows it.
- **interactive:** a real interaction was performed locally.
- **connected:** real data, provider, or auth was in the path.
- **failure-tested:** error, denial, offline, or recovery was observed.
- **device:** observed on a physical target device or store install.
- **production:** observed in the deployed production environment.

Never promote a rung by inference. Name the highest rung reached.

## Closed vocabularies

| Axis | Values |
| --- | --- |
| gate | `PASS` `FAIL` `BLOCKED` `NOT_RUN` |
| deliverable | `READY` `READY_WITH_CONDITIONS` `NOT_READY` `UNKNOWN` |
| severity | `P0` `P1` `P2` `P3` |
| freshness | `CURRENT` `STALE` `MISSING` |
| claim | `verified` `attributed` `inferred` `unverified` |
| maturity | `anecdote` `repeated` `candidate` `promoted` |

## Mapping

- Strong → PASS · Concern → FAIL (P2) · Critical → FAIL (P0/P1) · Unknown → NOT_RUN · N/A → not applicable
- needs evidence → BLOCKED · needs rewrite → FAIL · do not post → FAIL (hard)
- early → anecdote · directional → repeated · stable → candidate · promotable → promoted
- insufficient → anecdote · repeated-signal → repeated · promotion-candidate → candidate

## Findings

`F-<skill>-<n>`: `F-web-03`, `F-mobile-01`, `F-store-02`. IDs are stable across
handoffs; a re-audit closes, reopens, or adds, and never renumbers.

## Gates vs checks

A check reports; a gate blocks. Only gates get verdicts. A gate that has never
gone red has not been shown to work, so every gate needs a failing fixture.

## Claim rule

Every externally checkable claim carries a source, a date, and a status. If any
of the three is missing, the claim is `unverified`.
