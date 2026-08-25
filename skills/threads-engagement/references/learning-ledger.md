# Threads learning ledger

Use a project-local JSON Lines file. One line represents one engagement action
or one measured snapshot. Keep the file append-only where practical so failed
experiments and negative feedback remain visible.

## Action record

Required fields:

```json
{
  "id": "2026-08-26-target-001",
  "record_type": "action",
  "timestamp": "2026-08-26T01:00:00+07:00",
  "platform": "threads",
  "account": "@example",
  "target_url": "https://www.threads.com/@person/post/abc",
  "surface": "search-top",
  "visible_position": 1,
  "target_age_hours": 3.5,
  "topic": "pet care routines",
  "audience_job": "compare solutions",
  "first_line": "The visible opening line",
  "visible_metrics": {"likes": 120, "replies": 18, "reposts": 4},
  "ranking_hypothesis": {
    "observed": ["recent", "high reply depth", "specific question"],
    "inferred": ["conversation velocity may be helping visibility"],
    "unknown": ["personalized ranking inputs"]
  },
  "ranking_confidence": "low",
  "target_fit": "high",
  "decision": "reply",
  "account_type": "founder-or-builder",
  "voice_adapter": "spoken-builder-observation",
  "content_shape": "useful-extension",
  "pattern_key": "specific-question-plus-concrete-detail",
  "cta": "profile-soft",
  "text_version": "The exact reply or post text",
  "primary_metric": "qualified_replies",
  "experiment_cell": "reply-useful-extension-soft-cta",
  "authorization": "user-authorized-live"
}
```

`record_type` may also be `snapshot` or `feedback`. Snapshots should retain
the same `id` and add `hours_after_publish`, `attention`, `conversation`, and
`conversion` objects. Feedback should add `source`, `text`, `sentiment`, and
`actionable_learning`. For voice feedback, use a stable label such as
`ai-sounding`, `too-polished`, `too-salesy`, `natural`, or `specific-detail`.

For every action, add an `outcome` object when results are available:

```json
{
  "outcome": {
    "assessment": "positive",
    "primary_value": 7,
    "attention": {"views": 900, "profile_visits": 32},
    "conversation": {"qualified_replies": 7, "relevant_follows": 4},
    "conversion": {"link_clicks": 9, "signups": 1},
    "feedback_summary": "Readers asked for the workflow, not the feature list.",
    "confounders": ["target author replied early"],
    "next_decision": "test the same shape without a CTA"
  }
}
```

Allowed `assessment` values are `positive`, `neutral`, `negative`, and
`unknown`. Do not convert missing metrics into zero. Do not compare a fresh
reply with an older original post, or paid distribution with organic results,
without labeling the comparison as confounded.

## Pattern promotion

Use `pattern_key` to describe a testable combination of topic, audience job,
content shape, proof, participation prompt, CTA placement, or target surface.
Keep it short and stable; do not use a project name in the key.

The analyzer reports:

- `insufficient`: fewer than 3 comparable action outcomes;
- `repeated-signal`: at least 3 observations and 2 positive assessments;
- `promotion-candidate`: at least 8 observations and 5 positive assessments,
  subject to human review of confounders and sample comparability.

These labels are descriptive gates, not causal proof. A maintainer may promote a
pattern into shared skill guidance only with the sample window, platforms,
conditions, limitations, and a follow-up test. Keep project-specific copy,
claims, audiences, and brand voice in the project ledger rather than the shared
skill.
