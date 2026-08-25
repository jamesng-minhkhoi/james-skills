---
name: petio-marketing
description: Run Petio's evidence-led marketing loop across Buffer-managed social channels and English search/content surfaces. Use when planning, drafting, scheduling, auditing, or improving Petio content; reading Buffer Insights; learning from post performance; or coordinating copywriting, X, Threads, and SEO adapters. Keep all work scoped to the Petio app, its verified capabilities, and its pet-health safety boundary.
---

# Petio Marketing

Operate Petio marketing as a research → draft → preflight → schedule → measure
→ learn loop. Keep the product, audience, proof, voice, and current channel
mapping grounded in the source repositories; do not let a persuasive template,
viral post, or Buffer metric override a Petio safety or evidence rule.

## Start every session

1. Resolve the source repositories:
   - `/Users/khoinguyen/Documents/GitHub/petio-content` for content truth,
     audience, voice, proof, research, plans, and execution history.
   - `/Users/khoinguyen/Documents/GitHub/petio-landingpage` for public website,
     blog, landing-page, and SEO implementation truth.
   - `/Users/khoinguyen/Documents/GitHub/petio-mobile` only when verifying an
     app capability or screen; source code is not a substitute for a public
     product claim unless the proof ledger records it.
2. Read `petio-content/index.md` and `petio-content/CLAUDE.md` first. Then load
   only the relevant paths from [the Petio source map](references/petio-source-map.md).
3. Identify the account, channel, audience, objective, date range, and requested
   mode: `draft`, `research`, `schedule`, `performance audit`, or `learn`.
4. If Buffer is in scope, verify the authenticated workspace and current channel
   mapping in the browser. Treat old plans, queue counts, and ambient browser
   state as stale until checked.
5. Check the recent Buffer queue, drafts, sent posts, and the latest execution
   record before proposing copy. Avoid duplicate text, duplicate angles, and
   accidental reposts of already queued content.

## Cross-skill routing

Use the smallest adapter that covers the requested surface. Petio rules have
precedence over every adapter.

| Work | Adapter | Contract |
| --- | --- | --- |
| General hooks, clarity, persuasion, or variants | `$copywriting` when installed | Use for options and editing mechanics; re-run Petio proof, claims, voice, and audience gates afterward. No copywriting skill is currently present in this repo, so do not assume one exists. |
| X posts, replies, research, or measurement | `$x-engagement` | Read its playbook and policy references. Use the founder adapter only for the explicitly authorized `@JamesNMK` lane; keep the Petio product account dormant unless the user reopens it. |
| Threads posts, replies, or measurement | `$threads-engagement` | Inspect the skill before relying on it. The current repo copy is a placeholder; when incomplete, fall back to `petio-content/platforms/threads.md` and `voice/platform-tone.md`. |
| English blog, SEO, AEO, or landing-page content | `$seo-aeo-content` | Keep search intent, source citations, canonical/indexing checks, and Petio safety gates together. |
| Buffer UI, queue, drafts, or Insights | `browser:control-in-app-browser` | Use an authenticated browser. Read-only research needs no write authorization; scheduling, editing, deleting, or publishing requires explicit current-task authorization and visible verification. |

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
recommendation as a hypothesis—not a formula. If a metric is unavailable, mark
it `unknown`; never backfill it from another platform.

### 3. Choose one experiment

Choose one variable to change: hook, angle, format, proof asset, CTA placement,
posting window, or audience node. Preserve the other important conditions when
possible. Write the hypothesis in this form:

> For `[audience]` on `[channel]`, `[change]` will improve `[primary metric]`
> because `[evidence-based mechanism]`, while `[guardrail]` stays acceptable.

Prefer a useful content batch over a large volume target. Keep platform-native
versions genuinely different; do not turn one caption into costumes for three
channels.

### 4. Draft platform-native content

Start with the Petio content engine's current format and platform rules. In
general:

- TikTok/Reels/Shorts: show a real animal or real product workflow quickly;
- Instagram carousel: make a saveable argument or checklist, not a transcript;
- Facebook: contribute a specific situation or genuine question to the room;
- Threads: one small noticing, conversational, under 500 characters, no link or
  hashtag unless the current platform guidance explicitly changes;
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

Return one of `ready`, `needs evidence`, `needs rewrite`, or `do not post`.

Block the draft if it:

- diagnoses, rules out a condition, tells an owner their animal is fine, or
  implies Petio replaces a veterinarian;
- turns emergency symptoms or ingestion into a product funnel;
- calls a named commercial product toxic, unsafe, or harmful to a specific pet;
- invents a user, review, quote, number, outcome, endorsement, or testimonial;
- uses fear, guilt, fake urgency, generic AI language, or a creator imitation;
- makes an exclusive comparative claim without current evidence;
- uses a capability not verified in `proof/proof-ledger.md`;
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
3. Schedule one small batch at a time. Recheck after each save, especially on a
   Free-plan queue with a hard capacity.
4. Stop on a warning, challenge, rate limit, channel mismatch, duplicate, or
   ambiguous save state. Do not silently delete or replace existing content.
5. Report scheduled versus drafted versus published separately. A scheduled
   post is not a published result.

### 7. Record and learn

After scheduling, record the execution in the Petio content repository:

- date/time and timezone;
- account/channel and exact post or Buffer reference;
- audience, format, hook, proof row, CTA, media, and experiment cell;
- queue or sent status and verification evidence;
- the metric read window and the next review date;
- what changed, what remains unknown, and the next test.

When the user asks to learn or improve, append a dated learning note or update
the relevant content-engine performance table only after comparable evidence.
Do not silently rewrite `claims-and-safety.md`, `proof-ledger.md`, or core brand
voice from engagement data. Buffer performance can change prioritization and
testing; it cannot prove medical efficacy, product safety, or user outcomes.

## Output contract

For a research or performance request, return:

1. evidence window and source state;
2. channel/account and audience diagnosis;
3. primary metric, guardrails, confidence, and unknowns;
4. one selected hypothesis and why it is testable;
5. what to keep, change, stop, and measure next.

For a drafting request, return each platform version with:

- ready-state;
- audience and job;
- proof used;
- claims/safety ruling;
- hook selected plus two alternatives;
- media direction and CTA;
- the metric or experiment cell it belongs to.

For a scheduling request, also return the exact Buffer channel, timezone,
scheduled date/time, verification state, and any capacity or account limits.
