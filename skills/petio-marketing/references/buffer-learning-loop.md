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

- `confirmed`: directly visible in a comparable sample;
- `high-confidence inference`: a repeated pattern with plausible mechanism;
- `hypothesis`: useful next test, not yet established;
- `unknown/confounded`: missing data, mixed cohorts, or too-small sample.

## Evidence maturity gate

Record the age of every post when reading Buffer. Classify posts as `early`
when they are less than 24 hours old, `directional` at 24–72 hours, and
`stable` after 72 hours or when the platform has stopped materially updating
the visible metrics. Do not call an early zero a creative failure. A stable
zero with very low reach is usually `attention-poor`; a stable post with
attention but no response is `conversation-poor`; a stable post with verified
attention but no downstream action is `intent-poor`.

Require at least three comparable stable posts before promoting or demoting a
content mode. Keep the conclusion as a `hypothesis` when creator, topic,
timing, media, account state, or distribution is confounded. Never compare
Buffer engagement rates or raw counts across different platforms as if their
denominators were identical.

## Content-pattern audit

For a direction decision or an improvement request, classify the comparable
posts before selecting a winner. Use a small matrix with one row per post and
consistent labels for:

| Field | Examples |
| --- | --- |
| Topic/job | food or ingredient check, symptom preparation, records, reminders, useful conversation |
| Content mode | day-in-the-life/routine, contextual demo, owner story/question, explainer, checklist, trend/comedy, generic food, mukbang |
| Trust vehicle | known creator, real owner/UGC, expert/source, Petio account, none |
| Product role | natural tool in the story, demonstrated solution, explicit pitch, absent |
| Audience/channel | one audience node, native platform, format |
| CTA/intent | none, conversation, profile visit, click, install, activation, subscription |

Compare normalized rates within the same channel, audience, and format where
possible. Report three different failure modes:

- `attention-poor`: the opening or asset did not earn reach, views, starts, or
  completion;
- `conversation-poor`: people saw it but did not reply, share, save, or ask a
  qualified question;
- `intent-poor`: attention or engagement was acceptable but verified downstream
  actions were weak.

If installs, activation, or subscription data is not connected to the post,
mark conversion `unknown`. Never infer conversion from likes or views. A
high-view, low-intent pattern should be recorded as entertainment or curiosity
that does not yet prove product demand.

## Entertainment-to-traffic audit

For personal-account experiments, keep three content modes separate:

- `entertainment-awareness`: funny or relatable pet media with no product path;
- `entertainment-to-traffic`: the same attention mechanic plus a credible Petio
  bridge, subtle final-frame mention, and useful first-comment/self-reply CTA;
- `product-proof`: a direct Petio workflow or owner-job demonstration.

Record the asset rights/source, first-frame role, final-frame Petio mention,
CTA wording and location, verified destination, X Topic or thread target,
audience node, bridge sentence, and experiment cell. Reject a CTA when the meme
has no honest connection to a Petio-supported owner job. A high-view post with
no target-audience signal is attention-only, not evidence that the traffic
bridge worked.

For `entertainment-to-traffic`, select one primary metric (`qualified_profile_visits`
or `link_clicks`), use impressions/views as the attention guardrail, and use
qualified replies plus irrelevant-reply or spam rate as trust guardrails. For
`entertainment-awareness`, use impressions/views as the primary metric and do
not infer intent. Compare pure entertainment, bridged entertainment, and proof
only within the same channel and audience when possible; require at least three
comparable stable posts before changing the allocation.

## X topic and visual-freshness experiments

For `@JamesNMK`, a low-follower account may need native topic distribution and
relevant conversations to earn initial attention. Treat this as a hypothesis,
not a ranking fact. Capture the exact X Topic, whether it was manual, suggested,
or trending, the target audience node, and why the topic is relevant. Compare a
Topic-assigned cell with a no-Topic cell while holding the hook, media role,
CTA, and timing steady. Use qualified replies or profile visits as the primary
signal; impressions and irrelevant replies/spam signals are guardrails.

Do not use an unrelated trending topic, hashtag, or celebrity name as a reach
shortcut. If Buffer or X does not expose a Topic control, record the problem
cluster in the ledger and use relevant replies as the distribution surface.

Maintain an asset ledger with `asset_id`, role (`primary` or `Petio-proof`),
source/license, channels, last-used timestamp, and reuse reason. Apply a
seven-day minimum cooldown for the exact asset on the same channel and prefer
28 days before reusing the same screenshot across the campaign. Never repeat
the exact asset in both daily slots. A materially changed screen or proof-
critical follow-up may use a shorter cooldown only when the reason is logged.
Treat visual freshness as a separate test variable: do not claim new images
caused better engagement when topic, hook, format, timing, or audience also
changed. Text-first conversation posts can still be the stronger control.

External examples are hypotheses, not Petio rules. A useful test cell may be:

> For `[audience]` on `[channel]`, contextual routine content from a trusted
> voice will produce stronger `[verified intent metric]` than an explicit
> product explainer, while `[attention guardrail]` remains acceptable.

Do not promote or demote a content mode from one post. Require at least two
comparable observations, and keep the conclusion at `hypothesis` when the
sample is small or confounded by creator, topic, timing, or paid distribution.

## Trend and virality research

For a timely batch, capture the trigger before writing:

| Signal | What to record | Petio decision |
| --- | --- | --- |
| Live trigger | topic, source URL, publication date, observation date | Is it current and relevant to one audience node? |
| Audience behavior | repeated question, native format, creator mechanic, Buffer pattern | What would make the right owner stop or reply? |
| Petio angle | one owner job and proof row | Can Petio appear as a useful tool without making a medical claim? |

Score relevance, conversation potential, proof fit, freshness, safety, asset
readiness, and next-step clarity. Use a trend as a wrapper around a useful
owner action, never as evidence that Petio is popular or that a health claim is
true. Recheck fast-moving news immediately before scheduling. Record whether
the signal is `confirmed`, a `high-confidence inference`, or a `hypothesis`.

## Visual and CTA audit

For each scheduled post, verify the visual and conversion path separately from
the caption:

- primary visual, optional Petio proof visual, media count, preview legibility,
  alt text/description, and asset source/license;
- CTA wording, verified destination, and location: body, first comment, or
  self-reply/thread;
- whether Buffer visibly supports that comment/thread action for the channel;
- attention and intent metrics separately, including clicks or app-store
  actions when available.

For acquisition or install-oriented posts, missing media or a missing explicit
download CTA is a readiness failure, not an optional detail. For a deliberately
conversation-only post, record that objective and why a CTA was omitted.

If First Comment is unavailable or upgrade-locked, use the documented body CTA
fallback and record the capability limitation. Never report a CTA as a comment
when it was only placed in the post body.

## Learning record

Append a dated record to the Petio content repository, normally a new file under
`petio-content/plans/` or the existing `plans/EXECUTION-LOG.md` when the user
asks for durable logging:

```md
## YYYY-MM-DD: Buffer learning: [channel / experiment]

- window: [exact dates and timezone]
- account/channel: [verified identity]
- sample: [posts included and why they are comparable]
- pattern labels: [topic/job; content mode; trust vehicle; product role; audience/channel]
- trend wrapper: [trigger, source/date, confidence, safety/proof fit]
- visual: [primary asset; Petio proof asset; source/license; alt text]
- CTA: [wording; destination; location; capability state; result]
- entertainment bridge: [mode; first-frame role; final-frame Petio mention;
  bridge sentence; asset rights/source; topic/thread target]
- hypothesis: [one sentence]
- primary metric: [metric, result, baseline if available]
- guardrails: [two metrics and results]
- attention/conversation/intent: [what each layer shows; mark unavailable conversion unknown]
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
