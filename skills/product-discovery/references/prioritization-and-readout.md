# Prioritization and readout

Load for Prioritize and Readout modes.

## Prioritize: scoring

Score each candidate as Impact / Confidence / Effort (RICE-idiomatic), then
annotate every input with the evidence maturity it rests on
(`anecdote` / `repeated` / `candidate` / `promoted` per
[the ontology](../../_shared/ontology.md)).

```
| # | Candidate | Impact (basis) | Confidence (maturity) | Effort | Score |
|---|---|---|---|---|---|
```

Rules the scores enforce:

- **Maturity caps confidence.** An `anecdote`-backed candidate cannot score
  higher confidence than one with `repeated` evidence, whatever its backer's
  seniority. Say which inputs would move if the evidence matured, instead of
  silently letting anecdotes ride.
- **Effort is a range until a builder estimates it.** Use S/M/L until an
  engineer or designer has priced it; do not present day-counts as verified.
- **Effort-aware ordering:** pair a big-impact/high-effort candidate with
  whatever cheap `repeated`-evidence work unblocks or de-risks it, and say so —
  a ranked list that ignores sequencing quietly wastes the quarter.
- **State the disqualifiers once,** not per row: anything excluded outright
  (policy, strategy, non-goals of the period) in a one-line "excluded without
  scoring" strip.

Assign each row a status: `in` (this period), `waiting` (next, listed
direction), `watch` (needs one thing to be true), or `excluded` (with reason).
The status is the deliverable; the number alone is not.

## Readout: judging a shipped feature

Only metrics declared in the spec are judged. If the spec named none, the
readout is `NOT_RUN` and the fix is back to Spec mode — guessing post-hoc
targets is how features get graded against whatever they happened to hit.

```
| Metric | Spec target | Observed | Evidence + date | Verdict |
|---|---|---|---|---|
| ... | ... | ... | ... | met / missed / UNKNOWN |
```

- `UNKNOWN` when the instrument is missing, the window is too short, or the
  data is unreadable — never filled with directionally plausible numbers.
  A verdict without cited evidence is a claim, and a readout's claims need the
  same statuses as everything else in this library.
- Confounds get one line each, no arguing: seasonality, migrations, dependent
  launches, price changes.
- **Recommendation,** one of:
  - **iterate** — the bet still looks sound but the first approach underperformed
    its targets on mechanism-level misses;
  - **persevere** — targets not yet reached and not yet disprovable within the
    window; name the single signal that would flip this;
  - **kill** — the bet itself is disproven on spec-target terms. Say what
    kept-artifact looks like so the decision is reviewable.

Close the readout with a one-line "what this refines in the next spec," so the
loop actually circulates rather than ending at the grade — and where the
behavior of the shipped feature is what looks off rather than its numbers,
push that question through `code2flow` or the audits, not through this table.
