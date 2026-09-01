# Petio content scorecard

Use this lightweight scorecard before approving a Petio social post. It is a
rewrite aid, not a substitute for source, proof, claims, or platform checks.

## Score each draft

Give each criterion 0, 1, or 2 points:

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Human hook | product-first or abstract | recognizable but generic | specific moment, tension, or observation |
| Participation | no reason to respond | broad question | easy, concrete prompt or useful disagreement |
| Utility | opinion only | vague takeaway | checklist, example, decision aid, or next step |
| Petio role | forced pitch | several features | one verified capability used as proof or tool |
| Visual stop | no relevant media | decorative or repeated asset | primary situation plus legible Petio proof when acquisition is the job |
| CTA path | absent or unverified | generic link | explicit download action, verified destination, correct comment/self-reply or body fallback |
| Native voice | campaign copy | acceptable adaptation | sounds natural for this account and platform |
| Freshness | duplicate angle | minor variation | distinct hook, audience moment, or verified timely wrapper |

Run the claims and safety gates separately. A missing source, unsafe claim,
invented proof, or unsupported capability is a block regardless of score.

Before scoring, run the freshness and distribution gates:

- record each asset ID, role, source/license, last-used date, and channel;
- do not reuse the exact asset on the same channel inside seven days, and prefer
  28 days before reusing the same screenshot across the campaign;
- do not use one screenshot as both the primary visual and the proof visual, or
  repeat it in both daily slots;
- for `@JamesNMK` X posts, record the exact native Topic and audience rationale
  when the composer supports Topics; a suggested or trending Topic must still
  be directly relevant and safe;
- if the post is intentionally conversation-only, a fresh text-first post can
  pass without an app screenshot, but mark that cell explicitly instead of
  silently omitting a required acquisition asset.

For entertainment cells, run the separate bridge gate:

- `entertainment-awareness` has an intentional no-CTA decision and does not
  pretend to be an acquisition post;
- `entertainment-to-traffic` uses owned, licensed, or permissioned media, keeps
  the opening native, places a subtle verified Petio mention in the final
  frame/end card, and puts a useful download CTA in the first comment or
  self-reply when supported;
- the CTA names the honest Petio owner-job connection and uses the verified
  destination; otherwise omit it and downgrade the cell to awareness;
- record the asset rights/source, final-frame mention, CTA location, audience
  node, topic/thread target, and primary traffic metric;
- viral reach without profile visits, clicks, or target-audience signals is
  recorded as attention, not as conversion or product-market evidence.

- **13–16:** `ready` if the platform and evidence checks pass.
- **9–12:** `needs rewrite`; improve the lowest-scoring two criteria.
- **0–8:** `do not post`; replace the hook and content mode.

For a post whose job includes product discovery, installs, or app-store clicks,
the visual and CTA rows cannot score 0. The default package is:

1. a primary lifestyle, owner, or problem visual;
2. one verified Petio screen or workflow visual when the format supports it;
3. an explicit “Download Petio on iPhone” CTA in a verified first comment or
   self-reply, with the documented body fallback when the channel cannot place
   a comment.

Do not force that package onto a conversation-only post. Label the post
`conversation-only` in the brief and explain why a CTA would damage the
conversation. If the brief does not specify an objective, treat a Buffer
campaign post as acquisition-oriented and require the package above.

## Daily two-slot matrix

When the user asks for two posts per channel per day, create two distinct cells
for each channel rather than duplicating one idea:

| Slot | Default job | Content shape | Success signal |
| --- | --- | --- | --- |
| A | attention and conversation | owner moment, tension, question, or timely wrapper | qualified replies, shares, reach/views |
| B | useful discovery and intent | checklist, workflow proof, or contextual demo | profile visits, clicks, app-store actions |

Across a seven-day batch, start with roughly 40% owner moments, 30% timely
utility, 20% product proof, and 10% founder/building-in-public. Adjust only after
the comparable Buffer readout supports a change. A verified live trigger may
replace Slot A; it must still pass the trend and Petio-safety checks.

Keep the hook, product role, visual pair, CTA location, primary metric, and
experiment cell beside every scheduled item. Never count a planned caption as
complete until its media and CTA deliverables are explicitly marked ready.

For X topic experiments, add `topic`, `topic_source`, `topic_fit`, and
`topic_cell` (`assigned` or `none`) to the content card. For visual experiments,
add `asset_id`, `asset_role`, `last_used_at`, `cooldown_state`, and
`reuse_reason`.

## Post-publication maturity

Record the observation age with every Buffer readout:

- `early`: less than 24 hours; do not call the post weak or strong;
- `directional`: 24–72 hours; use for triage only;
- `stable`: at least 72 hours, or the platform has stopped materially updating
  the visible metrics;
- `promotable pattern`: at least three comparable stable posts, with repeated
  positive results and no obvious timing, creator, topic, or distribution
  confounder.

Use platform-normalized rates within the same channel. Keep raw counts for
context, and label app installs or activation as `unknown` unless a reliable
downstream event is connected to the post.
