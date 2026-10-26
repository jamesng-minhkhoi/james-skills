# Discovery playbook

Load for Decide-mode work: establishing what the problem is before any
artifact is written. The unit of output below is a **problem brief** — the
one-page document every other mode consumes.

## Evidence sources, cheapest first

Find what already exists before asking anyone for anything:

1. The product repo — what exists today, what routes exist, recent commits.
   Answers "is this already built?" and prevents re-discovery of shipped work.
2. Support tickets, review text, community threads. Verbatim user language is
   Scout-grade evidence for jobs and pain phrasing; treat volume claims as
   `inferred` until counted.
3. Analytics or exported usage data. Instance-level counts are the cheapest
   `verified` evidence available; name the dashboard or export path.
4. Existing interviews and internal research. Use with source and date;
   research older than ~a year is `attributed`, not `verified`.
5. New evidence. Only commission what the missing evidence actually gates —
   usually one specific claim the ranking or spec hinges on.

## Interview rules (when new conversations are authorized)

- Past behavior over future claims: what they did last time, not what they
  would pay for. Hypotheticals are the cheapest way to manufacture `unverified`
  certainty.
- Never pitch the idea before asking. The first third is about their life and
  workflow; the idea appears only after their situation is on the table.
- Record claims as quotes with the conversation date, status `attributed`.
- Write one finding per sentence and mark it — do not let a synthesis paragraph
  blur individual claim statuses.

## Problem brief template

```
# Problem brief: <one-phrase name>
Decision: <what specifically gets decided>
Owner: <who> · Constraint: <deadline, budget, headcount>
Best current guess: <one sentence> — status: <claim status>

## Jobs
- <job in the user's words> — claim: <status>, evidence: <path/source>

## Evidence
| Claim | Status | Evidence | Maturity |
|---|---|---|---|
| ... | verified/attributed/inferred/unverified | path | anecdote/repeated/candidate/promoted |

## Options
1. Do nothing — cost of carry: <what the pain costs while unsolved, with basis>
2. Narrower fix: <what it leaves unsolved, what it costs>
3. Candidate: <the full proposal>

## Recommendation
- Option N — one-line why.
- Falsifier: what observed result in the first 1–2 weeks would disprove this.
- Pilot: the smallest observable version — what design-uiux should mock and
  what single metric indicates the pain is real at scale.
```

## Failure modes this section exists to prevent

- **Loud-priority laundering:** converting an executive's or a big account's
  opinion into customer evidence. Quotes get `attributed`; verdicts need at
  least `repeated` evidence.
- **Denominator-free urgency:** "10 customers complained" without the base
  rate reads as real until the denominator appears. Always state it or mark
  the claim `inferred`.
- **Agreeing by artifact:** producing a slick PRD to settle an unsettled
  problem. If two people in the room would phrase the problem differently,
  the output is a problem brief, not a spec.
- **Solving the example, not the pattern:** one vivid anecdote drives the
  frame while boring repeat data sits unused. Sort the evidence table by
  maturity before writing the recommendation.
