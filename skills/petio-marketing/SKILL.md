---
name: petio-marketing
description: Run Petio's evidence-led marketing loop across Buffer-managed social channels, creator/UGC outreach, and English search/content surfaces. Use when planning, drafting, scheduling, auditing, or improving Petio content; analyzing replies or conversion patterns; reading Buffer Insights; learning from post performance; or coordinating copywriting, Gmail outreach, X, Threads, and SEO adapters. Keep all work scoped to the Petio app, its verified capabilities, and its pet-health safety boundary.
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
| General hooks, clarity, persuasion, or variants | `$copywriting` when installed | Use for options and editing mechanics; re-run Petio proof, claims, voice, and audience gates afterward. No copywriting skill is currently present in this repo, so do not assume one exists. |
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

When improving an active channel, build a small pattern matrix for the
comparable window before choosing the next batch. Classify each post using the
same fields so that “what worked” is not reduced to a lucky creator or a high
view count:

- **topic/job:** the owner problem and intended action;
- **content mode:** day-in-the-life or routine, contextual product demo, owner
  story/question, direct explainer, checklist, trend/comedy, generic food,
  mukbang, or other entertainment-led format;
- **trust vehicle:** known creator, real owner/UGC, expert/source, Petio account,
  or no identifiable trust source;
- **product role:** natural tool in the story, demonstrated solution, explicit
  pitch, or absent;
- **audience node and channel:** one Petio audience node, native platform, and
  format;
- **CTA and intent strength:** none, conversation, profile visit, click, install,
  activation, or subscription intent.

Compare rates within comparable cohorts, not raw totals across platforms. Label
each pattern as:

- **attention-poor:** weak reach, views, starts, or completion;
- **conversation-poor:** attention arrived but replies, shares, saves, or
  qualified questions were weak;
- **intent-poor:** attention or engagement was acceptable but verified profile,
  click, install, activation, or subscription signals were weak;
- **unknown:** the downstream event is not available or the cohort is too small.

Do not call a post “converting” from views, likes, or comments alone. A pattern
that attracts attention without qualified intent is useful evidence of an
entertainment or curiosity mismatch, not a successful growth format.

Treat external observations as hypotheses to test for Petio, not rules to copy.
For example, contextual day-in-the-life content from a trusted creator may
outperform a direct product explainer, while generic food or comedy content may
earn views without product intent. Test the mechanism with Petio’s own audience,
proof, and safety constraints before promoting or demoting the pattern.

### Trend and virality loop: borrow the moment, keep Petio’s job

“Viral” is a research input, not a quality bar. Before drafting a timely post,
collect three signals:

- **Live trigger:** a current news item, seasonal moment, cultural conversation,
  platform-native format, or calendar event, with source and date recorded;
- **Audience behavior:** a repeated question, comment pattern, remixable format,
  creator mechanic, or Buffer pattern that explains why people may stop and
  respond;
- **Petio angle:** one specific owner job that Petio can support with verified
  proof, such as keeping a timeline, attaching a food scan to a pet profile, or
  sharing records with family.

Score each candidate before using it: relevance to a Petio audience (0–3),
conversation potential (0–3), verified proof fit (0–3), freshness (0–2),
safety (0–2), asset readiness (0–2), and a credible next step (0–2). Reject a
candidate with no safe frame, no proof, or no useful owner action even if it is
receiving attention elsewhere.

Use the trend as the wrapper, not as a reason to make a claim. A calendar event
can frame a saveable owner prompt; a current recall can frame “save the label and
lot details” without naming a product unsafe for a particular animal; a popular
format can carry a real routine or question. Do not force unrelated news into
Petio, imply that a trend proves Petio demand, or manufacture urgency. Create a
platform-native version for each channel, and keep the same experiment variable
visible across the variants.

Record the source URL, publication date, observation date, confidence, trend
wrapper, chosen Petio job, and why the idea is safe. Recheck fast-moving claims
before scheduling; mark social-platform observations as hypotheses unless
Buffer or a primary source confirms them.

### X topic distribution for a low-follower founder lane

For the explicitly reopened `@JamesNMK` lane, treat X Topics as a distribution
experiment when the composer exposes a Topic field. A small or low-follower
account cannot rely on an existing audience alone, so choose one native topic
that matches the intended audience's problem (for example, pet care, pet
parents, or indie product building) rather than choosing Petio as a brand
topic or attaching an unrelated trending name.

- Record the exact selected topic, topic source (`manual`, `suggested`, or
  `trending`), audience node, and relevance rationale beside the post.
- Use the trending-topic panel as research and discovery, not as permission to
  hijack a conversation. Reject a topic that does not give the target reader a
  useful reason to stop or reply.
- Keep the main post useful without the topic label. A Topic is a distribution
  aid, not proof that X will recommend the post or that the audience is a fit.
- Test Topic assigned versus no Topic as one variable at a time. Hold the hook,
  media role, CTA placement, and posting window as constant where possible.
- Use qualified replies or profile visits as the primary engagement signal;
  impressions and irrelevant replies/spam signals are guardrails. Follower
  growth, likes, and views alone do not establish that the topic worked.
- If the composer has no Topic control, record the equivalent problem cluster
  in the learning ledger and prioritize relevant replies; do not compensate by
  adding unrelated hashtags or repeating the link.

### Entertainment-to-traffic lane for personal accounts

When the brief explicitly targets the personal `@JamesNMK` or `@jamesk.zip` lane,
allow a measured entertainment cell. Use entertainment to earn attention
and a relevant owner bridge to earn traffic; do not treat virality as proof of
Petio demand.

- Start with owned, licensed, or permissioned funny pet media or a relatable
  owner moment. Record the source and rights status; never pull a viral image or
  video without permission.
- Keep Petio out of the opening frame and opening line. For a carousel, add a
  subtle Petio end card in the final frame only when it follows the joke or
  owner problem. For video, use a brief final frame/end card and do not make it
  a bait-and-switch. The end card may mention Petio, but every capability claim
  must be verified.
- For an `entertainment-to-traffic` cell, put the explicit download CTA in the
  first comment or self-reply when the channel supports it. Explain the bridge
  to the same owner job and use the verified `petiogo.com` destination. If the
  channel cannot place a comment, use the documented body-CTA fallback and
  record the limitation.
- Do not attach a Petio CTA to an unrelated meme. Mark it
  `entertainment-awareness` and omit the funnel when no honest Petio bridge
  exists. The main post must still stand alone if the reply is not seen.
- Label each cell `entertainment-awareness`, `entertainment-to-traffic`, or
  `product-proof`. Record the first-frame role, final-frame Petio mention, CTA
  location, asset rights/source, audience node, topic or thread target, and
  experiment cell.
- Start with entertainment in roughly 20–30% of personal-account originals as
  a test allocation. Change that allocation only after comparable stable
  results; it is not a virality formula.
- For traffic cells, choose one primary metric: qualified profile visits or
  link clicks. Use views/impressions as the attention guardrail and qualified
  replies plus irrelevant-reply/spam rate as conversation/trust guardrails.
  For awareness cells, attention is the primary metric, but do not call reach a
  growth win without target-audience signals. Treat installs as `unknown`
  unless a downstream attribution path exists.
- Use a directly relevant X Topic or a specific high-fit conversation when
  available, but never hijack an unrelated trend. In a thread, give each post
  one job: joke or observation, useful bridge, then CTA.
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

Every acquisition-oriented post needs both a visual reason to stop and a
measurable next step. The media should carry the same human situation as the
copy, not decorate a product pitch:

1. Choose one primary visual: a real pet/owner moment, a clearly licensed
   relevant image, or a simple visualized question/checklist.
2. Add one Petio proof visual when the channel and post format support it: a
   verified app screen, profile, scan, record, or reminder. Do not invent UGC,
   reviews, outcomes, or medical imagery.
3. Add alt text or a short media description, record the asset source/license,
   and check that the image remains legible in the platform preview.
4. Keep a media matrix and reuse ledger so the same screenshot is not blindly
   repeated across every post. On one channel, apply a seven-day minimum
   cooldown for the exact asset; prefer a 28-day cooldown before reusing the
   same screenshot across the wider campaign. Never use the same exact asset in
   both daily slots. A shorter reuse is allowed only for a materially changed
   screen or a proof-critical follow-up, and the reason must be recorded.
5. Prefer a fresh primary visual for each slot: owner/pet moment, licensed
   image, UGC with permission, or a new visualized checklist. The Petio screen
   is supporting proof, not the default hero image. Freshness is a hypothesis to
   test, not a promise of higher reach.

For any post whose job includes product discovery, installs, or app-store
clicks, treat the primary visual, Petio proof visual, and explicit download CTA
as required deliverables. If one is missing, return `needs rewrite` rather than
calling the post ready. For a conversation-only post, mark that objective
explicitly in the brief; otherwise use the acquisition default.

Put the download CTA in a first comment or self-reply when the authenticated
Buffer/channel capability supports it. On X and Threads, use the next thread
post for a useful follow-up plus the CTA; do not make the first post a store
link. On LinkedIn, inspect Buffer’s First Comment control. If it is unavailable
or upgrade-locked, use a concise CTA in the body and record the limitation
instead of pretending a comment was scheduled. Use only a verified destination
(currently the Petio App Store listing in the source map); never claim Android
availability or a completed install.

The CTA must say what to do and why it follows from the post, for example:
“If keeping that context in one place would help, download Petio for iPhone:
[verified App Store link].” Keep the useful answer before the CTA, avoid fake
urgency, and measure clicks or app-store actions separately from replies and
likes.

Before approving social copy, ask:

- Would this sound natural if spoken by one thoughtful pet owner to another?
- Is there a human situation, concrete observation, or visible action before the
  product explanation?
- Does Petio appear as evidence or a tool rather than the subject of a sales
  paragraph?
- Would the post still provide value if the reader never installed the app?
- Does the product mention belong in this channel and this conversation?

If the answer to the first three is no, rewrite the opening and reduce the
product explanation before continuing. This rule does not replace the proof or
health-safety gates; natural-sounding copy still needs verified claims.

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

Return one of `ready`, `needs evidence`, `needs rewrite`, or `do not post`.

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
- observation maturity: `early`, `directional`, `stable`, or
  `promotable pattern`;
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
3. pattern matrix: topics, content modes, trust vehicles, product roles, and
   cohort sizes;
4. trend signals and the selected wrapper, with source/date/confidence and
   safety/proof fit;
5. attention, conversation, and verified intent results, including patterns
   that are intent-poor despite high views;
6. primary metric, guardrails, confidence, and unknowns;
7. one selected hypothesis and why it is testable;
8. what to keep, change, stop, and measure next.

For a drafting request, return each platform version with:

- ready-state;
- audience and job;
- proof used;
- claims/safety ruling;
- native-content test: the human situation or observation, the product's small
  role, and why the mention belongs in that channel;
- hook selected plus two alternatives;
- trend wrapper and source/date/confidence;
- media direction, asset source/alt text, asset ID, last-used date, cooldown
  state, CTA destination/location, and comment or thread capability state;
- the metric or experiment cell it belongs to.

For a scheduling request, also return the exact Buffer channel, timezone,
scheduled date/time, verification state, and any capacity or account limits.

For a daily planning request, also return the two-slot matrix for every
channel, the content-scorecard result for each item, the media pair, the exact
CTA location, and the experiment variable held constant across the batch.

For a creator or UGC outreach request, also return:

- the evidence window and creator-source URLs used for selection;
- candidate counts by `eligible-iphone`, `android-blocked`, `paid-only`,
  `unknown-fit`, and `do-not-contact`;
- the personalization evidence and verified greeting for each selected
  creator;
- offer terms and links, with every unconfirmed term clearly marked;
- the reply classification, next action, follow-up date, and stop reason;
- deduplication evidence, including previously contacted and duplicate-excluded
  counts;
- delivery, reply, brief-request, install, activation, referral, and revenue
  metrics, with attention and engagement kept separate from conversion.

Never report an email as sent because it was drafted or because a composer
opened. Sending requires explicit current-task authorization, actual send
confirmation, and a Sent-folder reconciliation.
