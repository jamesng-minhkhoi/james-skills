---
name: petio-marketing
description: Run Petio's evidence-led marketing loop across Buffer-managed social channels, creator/UGC outreach, and English search/content surfaces. Use when planning, drafting, scheduling, auditing, or improving Petio content; analyzing replies or conversion patterns; reading Buffer Insights; learning from post performance; or coordinating copywriting, Gmail outreach, X, Threads, and SEO adapters. Keep all work scoped to the Petio app, its verified capabilities, and its pet-health safety boundary.
---

# Petio Marketing

Operate Petio marketing as a research → draft → preflight → schedule → measure
→ learn loop. Keep the product, audience, proof, voice, and current channel
mapping grounded in the source repositories; do not let a persuasive template,
viral post, or Buffer metric override a Petio safety or evidence rule.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

## Start every session

1. Resolve the source repositories:
   - `/Users/khoinguyen/Documents/GitHub/petio-content` for content truth,
     audience, voice, proof, research, plans, and execution history.
   - `/Users/khoinguyen/Documents/GitHub/petio-landingpage` for public website,
     blog, landing-page, and SEO implementation truth.
   - `/Users/khoinguyen/Documents/GitHub/petio-mobile` only when verifying an
     app capability or screen; source code is not a substitute for a public
     product claim unless the proof ledger records it.
2. Read `petio-content/index.md` and `petio-content/CLAUDE.md` first. Then load only the relevant paths from [the Petio source map](references/petio-source-map.md); for AI-smell or viral-native work, also load [Natural Petio Copy](references/natural-copy.md).
3. Identify the account, channel, audience, objective, date range, and requested
   mode: `draft`, `research`, `schedule`, `performance audit`, or `learn`.
4. If Buffer is in scope, verify the authenticated workspace and current channel
   mapping in the browser. Treat old plans, queue counts, and ambient browser
   state as stale until checked.
5. Check the recent Buffer queue, drafts, sent posts, and the latest execution
   record before proposing copy. Avoid duplicate text, duplicate angles, and
   accidental reposts of already queued content.
6. When the brief asks for a daily cadence, build a two-slot matrix per channel
   before drafting. Use [the content scorecard](references/content-scorecard.md)
   to keep the slots distinct and to track media, CTA, and experiment state.
7. When creator outreach, UGC email, or creator-reply analysis is in scope, read
   [the UGC outreach workflow](references/ugc-outreach.md). Treat its eligibility,
   identity, offer, deduplication, and send checks as release gates.

## Cross-skill routing

Use the smallest adapter that covers the requested surface. Petio rules have
precedence over every adapter.

| Work | Adapter | Contract |
| --- | --- | --- |
| X posts, replies, research, or measurement | `$x-engagement` | Read its playbook and policy references. Use the founder adapter only for the explicitly authorized `@JamesNMK` lane; keep the Petio product account dormant unless the user reopens it. |
| Threads posts, replies, or measurement | `$threads-engagement` | Read its current workflow and learning-ledger guidance. If the adapter is unavailable or incomplete, fall back to `petio-content/platforms/threads.md` and `voice/platform-tone.md`. |
| English blog, SEO, AEO, or landing-page content | `$seo-aeo-content` | Keep search intent, source citations, canonical/indexing checks, and Petio safety gates together. |
| Buffer UI, queue, drafts, or Insights | `browser:control-in-app-browser` | Use an authenticated browser. Read-only research needs no write authorization; scheduling, editing, deleting, or publishing requires explicit current-task authorization and visible verification. |
| Creator discovery, Gmail outreach, UGC replies, or creator conversion analysis | [UGC outreach workflow](references/ugc-outreach.md) plus `browser:control-in-app-browser` for Gmail | Use public, relevant creator signals; deduplicate against all Gmail history; personalize from verified evidence; send only after the exact recipient, name, terms, links, and body pass preflight. |

Do not blend recognizable creator voices. Select one adapter, name it in the
brief, and use its mechanics rather than copying its wording.

## Core workflow

### 1. Build the evidence brief

Record:

- one audience node: `new-pet-parents`, `senior-pet-owners`, or
  `multi-pet-households`;
- one job: useful conversation, qualified discovery, installs, activation,
  subscription intent, or learning;
- one primary metric and two guardrails;
- the platform/account and its native format;
- the product capability or external source being used as proof;
- the current Buffer baseline and the hypothesis being tested;
- unknowns, missing assets, and any health/safety sensitivity.

If the request does not identify an audience or job, choose the narrowest
reasonable one and state the assumption. Do not write for “pet owners” in
general.

### 2. Learn from Buffer before writing when performance is relevant

Follow [the Buffer learning loop](references/buffer-learning-loop.md) when the
user asks to improve, when a prior batch exists, or when scheduling new content
into an active channel. Capture the comparable window, not just the top post.

Separate:

- attention: impressions/reach and views;
- conversation: replies, comments, reposts/shares, and qualified questions;
- intent: profile visits, follows, link clicks, app-store clicks, or other
  verified downstream events;
- guardrails: negative feedback, spam/risk signals, duplicate rate, health-claim
  concerns, and audience mismatch.

Normalize by channel, account, format, audience, media, hook, CTA placement,
and comparable time window. Treat a single winner, raw likes, or a Buffer
recommendation as a hypothesis, not a formula. If a metric is unavailable, mark
it `unknown`; never backfill it from another platform.

### 2a. Audit content patterns, not only individual posts

When improving an active channel, classify posts into comparable cohorts before
choosing the next batch. The fields, labels, and cohort rules are in
[the Buffer learning loop](references/buffer-learning-loop.md#audit-content-patterns-not-only-individual-posts).

### Trend and virality loop: borrow the moment, keep Petio's job

Treat "viral" as research input, not a quality bar. Score relevance, conversation
potential, proof fit, freshness, safety, asset readiness, and next step before
using a moment. Method and scoring: [trend and virality](references/trend-and-virality.md).

### Channel lanes and distribution

X Topic choice, Topic diversity across a batch, and the entertainment-to-traffic
lane are channel mechanics. Use [channel lanes](references/channel-lanes.md) when
the brief targets discovery on a personal or low-follower account; the adapter
skill still owns the drafting workflow.

### 3. Choose one experiment

Choose one variable to change: hook, angle, format, proof asset, CTA placement,
posting window, or audience node. Preserve the other important conditions when
possible. Write the hypothesis in this form:

> For `[audience]` on `[channel]`, `[change]` will improve `[primary metric]`
> because `[evidence-based mechanism]`, while `[guardrail]` stays acceptable.

Prefer a useful content batch over a large volume target. Keep platform-native
versions genuinely different; do not turn one caption into costumes for three
channels.

### 3a. Build the daily two-slot matrix

When the requested cadence is two posts per channel per day, create two
different jobs for each channel:

- **Slot A: attention/conversation:** a specific owner moment, tension,
  question, or verified timely wrapper;
- **Slot B: useful discovery/intent:** a checklist, workflow proof, or
  contextual product demonstration.

Do not fill both slots with product explanations or near-duplicate health
observations. Across a seven-day batch, use the default mix in
[the content scorecard](references/content-scorecard.md), then change the mix
only when a stable, comparable Buffer pattern supports it. Keep a content card
for each slot with its audience, job, hook, content mode, proof, primary visual,
Petio proof visual, CTA location, and primary metric.

### Native-content rule: make the product part of the moment, not the announcement

The best-performing social content should not feel like an advertisement or an
informational robot explaining a product. Start with a real owner moment,
observation, question, opinion, small story, or visible behavior. Let Petio
appear as a useful object inside that moment, the way a person would naturally
show or mention something they use. Do not make the product description the
opening scene.

Use this sequence for social posts and replies:

1. **Earn attention with the human situation.** Open on what the owner noticed,
   felt, tried, or wants to know, not “Petio is an AI pet-health app that…”
2. **Show or answer before explaining.** Demonstrate the scan, record, reminder,
   or Peti interaction in context; or answer the person’s question fully before
   mentioning Petio.
3. **Keep the product role small and specific.** One relevant capability is
   enough. Avoid feature tours, benefit stacks, corporate claims, and generic
   AI explanations.
4. **Leave the audience with a useful thought or next step.** The post should
   still be worth seeing if the product name is removed. A CTA is optional and
   should not interrupt the usefulness of the post.

For replies, the order is **person → useful answer → optional Petio context**.
Never use a reply as a disguised pitch, and do not force the app into a
conversation where it is not the natural next step.

### Visual and CTA contract

Every acquisition-oriented post needs a visual reason to stop and a measurable
next step: one relevant primary visual, one verified Petio proof visual as the
final item, alt text, a rights/source record, and an explicit CTA with a verified
destination. A non-direct acquisition post with fewer than two relevant media
items, or without a verified CTA, is `FAIL`. Cooldowns, media matrix,
and per-channel fallbacks: [visual and CTA](references/visual-and-cta.md).

### 4. Draft platform-native content

Start with the Petio content engine's current format and platform rules. In
general:

- TikTok/Reels/Shorts: open on a real animal, owner moment, or visible problem;
  let the product workflow appear naturally without a feature-list voiceover;
- Instagram carousel: make a saveable argument or checklist, not a transcript or
  product brochure; use Petio as the example or proof inside the argument;
- Facebook: contribute a specific situation or genuine question to the room;
  answer as a member first and mention Petio only when it genuinely helps;
- Threads: one small noticing, conversational, under 500 characters, no link or
  hashtag unless the current platform guidance explicitly changes; do not turn a
  noticing into a product announcement;
- X: use only an authorized lane, one concrete observation, and the applicable
  `$x-engagement` adapter;
- LinkedIn: use a clear product or operating insight without pretending Petio
  has traction, authority, or outcomes that are not proven;
- blog/SEO: answer the search question directly, cite authoritative sources,
  and use Petio as a workflow example rather than medical evidence.

Draft three hooks when the topic is important, choose one, and retain the two
alternatives for learning. Keep the audience, proof row, claims pattern, hook
type, CTA, and media direction beside each draft.

### 5. Run the Petio preflight

Return `PASS`, `BLOCKED` (needs evidence), `FAIL` (needs rewrite), or
`FAIL — do not post`.

Block the draft if it:

- diagnoses, rules out a condition, tells an owner their animal is fine, or
  implies Petio replaces a veterinarian;
- turns emergency symptoms or ingestion into a product funnel;
- calls a named commercial product toxic, unsafe, or harmful to a specific pet;
- invents a user, review, quote, number, outcome, endorsement, or testimonial;
- uses fear, guilt, fake urgency, generic AI language, or a creator imitation;
- opens with a product description, feature inventory, or sales pitch when a
  human situation or useful answer should come first;
- reads like a scripted advertisement, product tour, or informational robot
  instead of a person speaking naturally in that channel;
- mentions Petio in a reply before answering the person or contributing
  something useful;
- makes an exclusive comparative claim without current evidence;
- uses a capability not verified in `proof/proof-ledger.md`;
- has an acquisition objective but no relevant primary visual, verified Petio
  proof visual, or explicit download CTA with a verified destination and
  supported location;
- duplicates an existing Buffer queue/draft/sent post without a documented test
  reason.

For health topics, reframe verdict → preparation: notice, track, flag for review,
write it down, and bring a clearer question to a veterinarian. Emergency-care
guidance comes first and Petio stays out of the pitch.

### 6. Schedule through Buffer only when authorized

When the user authorizes scheduling:

1. Verify channel identity, timezone, queue capacity, target date/time, and
   account before opening the composer.
2. Use Buffer's native composer. Do not claim that a draft is scheduled because
   a form opened or a button returned; verify the saved queue card with account,
   exact text, date, and time.
3. Verify media count, media preview, alt text where available, and the CTA
   location. A thread or first-comment control is a separate deliverable from
   the main post; verify it explicitly. If a channel capability is unavailable,
   use the documented fallback and report it.
4. Schedule one small batch at a time. Recheck after each save, especially on a
   Free-plan queue with a hard capacity.
5. Stop on a warning, challenge, rate limit, channel mismatch, duplicate, or
   ambiguous save state. Do not silently delete or replace existing content.
6. Report scheduled versus drafted versus published separately. A scheduled
   post is not a published result.

### 7. Record and learn

After scheduling, record the execution in the Petio content repository:

- date/time and timezone;
- account/channel and exact post or Buffer reference;
- audience, topic/job, content mode, trust vehicle, product role, format, hook,
  proof row, trend signal/source/date/confidence, CTA location, media/asset
  source, and experiment cell;
- queue or sent status and verification evidence;
- the metric read window and the next review date;
- post age: `early`, `directional`, or `stable`;
- pattern maturity: `anecdote`, `repeated`, `candidate`, or `promoted`;
- what changed, what remains unknown, and the next test.

When the user asks to learn or improve, append a dated learning note or update
the relevant content-engine performance table only after comparable evidence.
Do not silently rewrite `claims-and-safety.md`, `proof-ledger.md`, or core brand
voice from engagement data. Buffer performance can change prioritization and
testing; it cannot prove medical efficacy, product safety, or user outcomes.

## Output contract

Return the evidence window and source state, the account/channel and audience
diagnosis, and the selected hypothesis with its primary metric, guardrails,
confidence, and unknowns.

For a drafting request, return each platform version with: ready-state; audience
and job; proof used; claims/safety ruling; the native-content test (human
situation, product's small role, why the mention belongs); hook plus two
alternatives; trend wrapper with source/date/confidence; media direction, asset
source/alt text, cooldown state, and CTA destination/location; AI-TONE result;
and the experiment cell.

For scheduling, add the exact Buffer channel, timezone, scheduled time,
verification state, and capacity limits. For UGC outreach, add the evidence
window, candidate counts by status, personalization evidence, offer terms with
unconfirmed items marked, reply classification, dedup evidence, experiment cell,
and delivery-to-revenue metrics.

Never report an email as sent from a draft or an open composer. Sending requires
current-task authorization, confirmation, and Sent-folder reconciliation.
