---
name: product-discovery
description: Frame product opportunities from evidence and turn them into buildable specs: problem briefs, PRDs and job stories with acceptance criteria, prioritization, success metrics, and post-launch readouts. Use when deciding what to build, writing or editing a spec, scoring a backlog, or judging a shipped feature. Also use for squishy user problems, should-we questions, and conflicting requests. For screen design, use design-uiux; for PRD-versus-code drift, use code2flow; never change product code here.
---

# Product Discovery

Own the decision layer that sits before design and code: deciding what to
build, and writing a spec a designer or engineer can execute without having to
re-interrogate anyone. A fluent PRD after a shallow reading of the problem is
the failure mode this skill exists to prevent.

## Non-negotiable gates

Shared vocabulary: [ontology](../_shared/ontology.md). Use its claim statuses,
verdicts, and maturity ladder verbatim.

1. **Evidence before claims.** Every statement about users, the market, or
   product behavior carries a claim status: `verified` (an evidence path you
   inspected), `attributed` (source and date, not independently checked),
   `inferred`, or `unverified` (new or unmarked). A decision is only as good as
   the worst status feeding it. Never turn "the loudest person thinks" into
   "customers want" — that is a status upgrade by laundering.
2. **Specs are executable downstream.** Every acceptance criterion must be
   checkable by whoever consumes it — a designer reviewing it against
   `design-uiux` flows, or an engineer writing tests under
   `frontend-web-engineering` / `frontend-mobile-engineering`. If the reader
   would have to invent behavior, the criterion is not written yet. State the
   required interface states (loading, empty, typical, dense, pending, success,
   error, retry, offline when relevant) without drawing them.
3. **Metrics declared before launch.** A spec names its success metrics, an
   instrumentation plan, a target, and an owner. The same numbers and targets
   are what the readout compares against. Relabeling metrics after launch to
   make the readout pass is a FAIL.
4. **Scope honesty.** Every spec carries explicit non-goals. Negative scope is
   where most scope arguments happen later; spend the sentence now.
5. **No verdict without an artifact.** Readouts and go/no-go calls cite the
   metric evidence they judged. Unobserved is `NOT_RUN` or `UNKNOWN`, never
   `PASS`. If the data is not in front of you, the deliverable is `UNKNOWN`,
   not an opinion with formatting.

Stay in scope: this skill never produces screens, flows, colors, or code.
Renders and drift checks route elsewhere (see Boundaries).

## Boundaries

- Screen, flow, and interaction design decisions → `design-uiux`. It is fine
  for a spec to *describe* flows in prose; it is not this skill's job to decide
  what they look like.
- "Does the built product match the PRD?" → `code2flow` (route-graph extraction
  and PRD-vs-code drift checks). Write the checkable spec, then hand it there.
- Any code change, even "just the copy edit" → the frontend engineering skills.
- Landing page or announcement launches → `seo-aeo-geo` builds; this skill
  supplies the spec and the metrics, not the page.

## Operating modes

Choose one mode before doing work and say which:

- **Decide.** The problem is not agreed on yet: what matters, for whom, and how
  badly. Producers: a problem brief with evidence-labeled claims, options, and
  a recommendation.
- **Spec.** The decision is made; write the PRD or job stories. Producer: a
  buildable spec with acceptance criteria, states, non-goals, and metrics.
- **Prioritize.** Rank competing candidates under a constraint (a quarter, a
  headcount, a budget). Producer: a scored ranking with evidence maturity per
  candidate, and the known/unknown split exposed.
- **Readout.** Something shipped; judge it against the metrics its spec
  promised. Producer: a verdict per metric with `NOT_RUN`/`UNKNOWN` marks, and
  an iterate / persevere / kill recommendation labeled by what would change it.

## Workflow

### 1. Establish what is actually being decided

Before any artifact, write three sentences:

- the decision to be made (or product decision being reviewed);
- who owns it and the deadline or constraint;
- the current best guess and its claim status.

If you cannot state the decision without circling it two or three times, the
request is a Decide run wearing a Spec costume. Say so, and reduce ambition in
the output accordingly — an artifact that prematurely settles an unsettled
decision causes more churn downstream than asking one clarifying question.

Ask for evidence you are missing rather than inventing it. Reasonable asks:
analytics dashboards or exported data, support tickets, interview notes,
competitor pages, the product repo (for what exists today). When evidence is
unavailable, keep the claim `unverified` and list what would verify it.

### 2. Decide mode

Produce a problem brief from [the discovery playbook](references/discovery-playbook.md):

- **Jobs.** What is the person trying to get done, phrased in their words.
- **Evidence table.** Each claim with status, evidence path or source, and
  maturity (`anecdote` / `repeated` / `candidate` / `promoted`). One anecdote
  does not found a feature; name the maturity honestly and say what repeated
  evidence would need to show.
- **Options.** At least the candidate, one cheaper or narrower variant, and
  do-nothing with its quantified cost based on carry.
- **Recommendation and reversibility.** Single strongest option, what would
  falsify it within the first week or two, and what the pilot material or
  mockup will need from `design-uiux`. Prefer reversible choices; irreversible
  or expensive options need more `verified` claims than cheap reversible ones.

### 3. Spec mode

Write the spec from [the summary](references/spec-templates.md). Keep repos' existing
style; do not invent structure where templates are already in the product repo.

Minimum contents:

- problem statement backed by the brief from Decide mode;
- users and jobs;
- requirements as job stories (When / I want / So I can) or scoped PRD sections
  with acceptance criteria explicitly spelled out so a test can be written
  against each;
- required interface states described in prose (including calculated edge
  cases such as long content, concurrent edits, or clock skew when relevant);
- non-goals;
- success metrics with targets, instrumentation, and owner;
- open questions with the claim status of the current thinking on each.

Acceptance criteria rules: independent of implementation, observable to a user
or a test, and false-by-exception — if a state is not listed, the reader may
assume it does not exist. Where a criterion depends on data or providers,
annotate the proof level you expect by launch from the ontology ladder
(`declared` through `production`); this is what the builders' gates will be
judged against.

End the spec with a deliverable verdict: `READY`,
`READY_WITH_CONDITIONS` (list the conditions), `NOT_READY` (what is blocking),
or `UNKNOWN`. Do not mark READY over unstated open questions — that is the
same laundering the first gate forbids.

### 4. Prioritize mode

Use [the scoring reference](references/prioritization-and-readout.md). Score with impact,
confidence, effort, and the evidence maturity of every input, then split the
result by what is known versus unknown rather than hiding unknowns inside
"confidence". Ranking without the split is how a house feature dies quietly
behind a well-written row for an anecdote.

Report: ranked table, per-row one-line rationale, the unknowns that most alter
the ranking if resolved, and the single cheapest way to resolve each.

### 5. Readout mode

Compare shipped results to the spec's declared metrics:

- one verdict per metric: met / missed / `UNKNOWN` (data absent or fresh-but-thin), citing the evidence source and date;
- confounds named in one line each rather than argued: seasonality,
  migrations, price changes, dependent launches;
- recommendation: iterate (change the approach, keep the bet), persevere (keep
  the bet, keep watching), or kill (retire the bet) — with the single signal
  that would flip the recommendation;
- if the spec named no metrics, say so: the readout is `NOT_RUN` for any
  metric absent from the spec, and the fix is going back to Spec mode, not
  grading a guess.

Readouts of shipped work check the built product; this skill reads metric
evidence only. Where you suspect the implementation, route to `code2flow` or
the audits rather than speculating here.

## Calibration

Against the shared ontology: metrics readouts get deliverable verdicts too, and
`READY_WITH_CONDITIONS` plus the conditions is worse for downstream work than
an honest `NOT_READY`. The spec's verdict is the artifact a designer or
engineer picks up next; make it the single most trustworthy sentence in the file.
