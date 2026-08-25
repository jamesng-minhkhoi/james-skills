# Buffer learning loop

Use this reference when the task includes Buffer Insights, “what worked,”
iterative improvement, a content audit, or scheduling into an existing queue.

## Read-only performance pass

1. Open the authenticated Buffer workspace in the browser. Do not treat the
   ambient tab as authorization or as evidence of the correct account.
2. Identify the current organization, connected channel, owner, native
   platform, timezone, queue count, drafts, and sent history.
3. Open Insights for a comparable range: normally the last 7 days for an active
   experiment and 28 days for a direction decision. Record the exact range and
   whether the numbers are post-, channel-, or account-level.
4. Capture only visible metrics. Typical fields may include impressions, reach,
   views, likes, comments/replies, reposts/shares, profile visits, follows,
   clicks, saves, or completion/watch data. Buffer's available fields can vary;
   absent data is `unknown`.
5. Inspect enough winners and weak posts to compare like with like. Include
   format, media, first line/hook, audience, topic, CTA, posting time, and
   whether the post was organic, scheduled, or promoted.

Do not use one high-like post as a strategy. Do not compare raw counts across
platforms or accounts without normalization. Do not infer conversion from
impressions, or product value from engagement.

## Metric interpretation

| Layer | Useful signals | Question |
| --- | --- | --- |
| Attention | impressions, reach, views, video starts/completions | Did the opening and asset earn attention? |
| Conversation | replies, comments, shares/reposts, qualified questions | Did the idea make the right people respond? |
| Intent | profile visits, follows, clicks, app-store clicks, sign-up events | Did attention create a verified next step? |
| Guardrails | negative feedback, spam warnings, duplicate rate, audience mismatch | Did the tactic damage trust or account health? |

Use one primary metric and two guardrails per experiment. Label each conclusion:

- `confirmed` — directly visible in a comparable sample;
- `high-confidence inference` — a repeated pattern with plausible mechanism;
- `hypothesis` — useful next test, not yet established;
- `unknown/confounded` — missing data, mixed cohorts, or too-small sample.

## Learning record

Append a dated record to the Petio content repository, normally a new file under
`petio-content/plans/` or the existing `plans/EXECUTION-LOG.md` when the user
asks for durable logging:

```md
## YYYY-MM-DD — Buffer learning: [channel / experiment]

- window: [exact dates and timezone]
- account/channel: [verified identity]
- sample: [posts included and why they are comparable]
- hypothesis: [one sentence]
- primary metric: [metric, result, baseline if available]
- guardrails: [two metrics and results]
- confirmed: [what the data directly shows]
- inference: [mechanism, with confidence]
- unknowns: [missing or confounded evidence]
- keep: [specific element]
- change: [one variable for the next test]
- stop: [tactic to demote or avoid]
- next review: [date/range]
```

Do not edit the core proof ledger, health-safety file, or brand voice from one
Buffer result. Promote a recurring hook or format only after at least two
comparable observations, and keep the old rule if the evidence is mixed.

## Draft and duplicate check

Before scheduling:

- inspect the channel queue, drafts, and recent sent posts;
- search exact opening lines and near-duplicate angles;
- compare against the latest file in `petio-content/plans/`;
- mark intentional repeats with the experiment reason and changed variable;
- prefer a fresh angle when the same text or idea is already queued.

This check matters because Buffer can hold existing posts even when a new plan
looks empty locally.

## Scheduling write pass

Only perform this pass after the user authorizes scheduling the current batch.

1. Reconfirm channel identity, owner, timezone, posting date/time, queue
   capacity, and whether the action is schedule, draft, edit, delete, or publish.
2. Use the native Buffer composer. Never infer success from a toast alone.
3. After every save, verify the queue card contains the intended channel,
   exact copy, date, time, and scheduled state.
4. Schedule small batches. Stop at a Free-plan limit, duplicate, warning,
   challenge, rate limit, or ambiguous state.
5. Report scheduled, drafted, published, failed, and skipped counts separately.

Treat the following as distinct evidence levels:

- local draft created;
- Buffer draft saved;
- Buffer queue card verified;
- post visibly published;
- public post/permalink verified;
- performance data captured after a defined window.

## Review rhythm

- **Immediately:** verify queue state and record exact schedule metadata.
- **24–72 hours:** capture early attention and conversation signals; do not call
  a winner if the sample is incomplete.
- **7 days:** compare the experiment cohort with the prior comparable window.
- **28 days:** decide whether to promote, demote, or keep testing the pattern.

Keep the learning loop focused on Petio's job: useful clarity and qualified
product discovery. Do not optimize toward panic, medical certainty, or generic
engagement bait.
