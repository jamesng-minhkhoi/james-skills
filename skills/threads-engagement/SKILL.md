---
name: threads-engagement
description: Research, draft, publish, measure, and improve authentic Threads posts and replies for any project or account. Use for topic discovery, ranked-feed analysis, natural project-native or indie-builder voice, community engagement, product promotion, launch conversations, listening experiments, performance reviews, and converting repeated feedback into evidence-backed content patterns.
---

# Threads Engagement

Use Threads as a conversation and learning surface. Make every engagement
useful without requiring a profile visit, and improve the workflow from
repeated evidence rather than copying a single high-performing post.

## Operating modes

Choose one mode before acting:

- **Draft:** research targets and produce copy, rationale, CTA options, and a
  preflight report. Do not publish.
- **Research and queue:** rank relevant conversations and prepare a small queue.
  Do not publish or engage.
- **Live execution:** publish, reply, like, repost, follow, or otherwise act
  only when the user explicitly authorizes the current account and batch.
- **Listening:** collect topic language, questions, objections, and ranking
  observations without posting.
- **Performance audit:** compare a like-for-like sample of strong, ordinary,
  and weak posts; separate attention, conversation, and conversion.
- **Learning maintenance:** review the learning ledger, promote only repeated
  patterns, and propose changes to this shared skill. Do not silently rewrite
  the shared skill during live engagement.

## Workflow

### 1. Build the account and project brief

Record the account, owner, audience, project or offer, active voice, objective,
primary metric, two guardrails, available proof, CTA destination, and safety or
brand constraints. Keep the skill project-agnostic: load project-specific
claims, voice, privacy, legal, health, or platform guidance only when the
workspace provides it.

Record whether the account is a founder, builder, product, community, or
personal account. If a voice reference exists, load it before writing. For
indie-builder work, use the mechanics in
[voice-adapters.md](references/voice-adapters.md); do not copy a creator's
phrases, persona, biography, or distinctive verbal tics.

If the request is live, verify the authenticated account before drafting. Do
not use credentials, cookies, tokens, hidden browser state, or an account that
the user did not place in scope.

### 2. Analyze the topic and ranked surface before targeting

For every topic or post considered, inspect the actual Threads surface:
search top versus recent, a profile, a post detail page, a reply sort, or the
home feed. Compare several visible results in the same topic and time window;
do not explain ranking from one post alone.

Capture:

- URL, platform, surface, visible position, timestamp, and post age;
- topic, audience job, first-line hook, and likely search-language match;
- visible likes, replies, reposts, quotes, views, and engagement velocity
  relative to age when comparable;
- reply depth, author relevance, audience fit, media or format, novelty,
  emotional trigger, question or participation prompt, and external timing;
- what is observed, what is inferred as a ranking hypothesis, and what remains
  unknown;
- topic fit, useful contribution, product distance, safety risk, and CTA fit.

Treat prominent placement as an observation, not proof of the Threads ranking
algorithm. Do not claim that a signal causes ranking unless authoritative
platform documentation or repeated comparable evidence supports it. A high-
ranking post is still a skip when the only possible contribution is a generic
compliment or an advertisement.

Use this target table before drafting:

| Target | Surface/rank evidence | Topic and audience job | Useful addition | Risk | Decision |
| --- | --- | --- | --- | --- | --- |
| URL/account | age, position, visible metrics | learn, compare, share, ask, discover | answer, example, tradeoff, question | low/med/high | reply/queue/skip/listen |

### 3. Select the smallest useful batch

Prefer a few distinct, recent, high-fit conversations over a volume quota.
Avoid replying to several posts with the same hook, CTA, or product claim.
Match the emotional temperature and language of the parent post. Do not use
unrelated viral content as an ad slot.

### 4. Choose a natural voice mode

Choose one dominant mode before drafting:

- **Quick observation:** spoken reaction or half-formed noticing → one precise
  consequence → optional artifact or question.
- **Build-in-public:** what shipped or changed → what surprised, broke, or was
  harder than expected → what is being tested next.
- **Builder education:** familiar tension → concrete artifact or example → one
  crisp point of view → low-friction invitation.
- **Project-native:** the account's actual vocabulary and audience language,
  with no creator adapter when imitation would be artificial.

Default Threads to the quick-observation mode. Use build-in-public when there
is real work to show. Do not turn every post into a lesson, launch, or CTA.

### 5. Draft for the parent conversation

Use one of these shapes:

- **Direct answer:** answer the question first, then add one detail or tradeoff.
- **Useful extension:** add a concrete example, process, or next step.
- **Respectful disagreement:** agree with the valid part and explain the limit.
- **Focused question:** ask one specific question that advances the thread.
- **Relevant product fit:** provide value first, then mention the product only
  when it naturally solves the described problem.
- **Original post:** recognizable situation or observation → concrete detail or
  proof → one point of view → optional low-friction question or CTA.

Keep the reply understandable if the reader never clicks the profile. Put the
useful contribution before any brand mention. Use a CTA only when it is
relevant, optional, and clear about the payoff. Avoid hard-sell repetition,
link-only replies, copied creator language, fake certainty, and manufactured
urgency.

Write from a real moment, decision, artifact, mistake, or observed detail.
Allow contractions, fragments, a small aside, or an unfinished thought when
they fit the account. Prefer one specific noun, behavior, time, number, or
tradeoff over a polished emotional summary. Let the image carry some context.

For Petio work, also load [Natural Petio Copy](../petio-marketing/references/natural-copy.md)
and apply its source-backed scene, participation, AI-smell, and remove-the-brand
gates. Use it as a rewrite aid, never as a phrase bank. For Buffer scheduling,
also follow Petio's [Visual and CTA contract](../petio-marketing/SKILL.md#visual-and-cta-contract);
the CTA is optional only when the brief explicitly marks the post
`conversation-only`.

Do not use a generic content-brief bridge such as “sharing a small peek,” “I
like the quiet parts,” or “the kind of detail that makes everything easier.”
Do not force a hook → three-paragraph explanation → brand CTA cadence. If the
copy would not sound plausible as a short voice note from this account, rewrite
it before preflight.

### 4c. Buffer native Topic targeting

When Buffer's Threads composer exposes a `Topic` field, treat it as a required
distribution field for discovery-oriented posts. A `Thread` is the post format;
it is not the same thing as a native Topic.

- Choose one relevant Topic from Buffer's visible autocomplete or topic control.
  Prefer the target audience's real interest (for example, pet care or
  multi-pet households) over a broad or unrelated trending suggestion.
- Record the exact Topic, source (`manual`, `suggested`, or `trending`), audience
  node, and fit rationale beside the draft. Never use a celebrity or unrelated
  trend as a reach shortcut.
- If the composer has no Topic control, record `native_topic: unavailable` and
  use a specific audience problem, reply surface, or conversation target as the
  fallback. Do not claim native Topic targeting happened.
- After saving an edit or schedule, reopen the item and verify the exact Topic,
  caption, media, channel, and scheduled time. A blank Topic is a targeting
  failure that must be reported or corrected before calling the post ready.

### 4b. Use a copywriter's humanization loop

Start with raw material, not a content prompt. Before drafting, name:

- the one reader or parent-post participant being addressed;
- the real scene, decision, mistake, behavior, or artifact;
- the friction, surprise, tradeoff, or unresolved question;
- the one point of view the account can honestly add;
- what the reader gets before any brand mention or CTA.

Draft two or three versions from that same material. Use these editing passes:

1. **Scene:** replace an abstract claim with an actor, active verb, and concrete
   object or action.
2. **Tension:** keep one real complication or point of uncertainty. Do not
   smooth every edge into positive marketing language.
3. **Point:** make one clear observation or belief do the work. Cut the second
   lesson, the throat-clearing, and the summary that merely repeats the point.
4. **Rhythm:** put the meaning early, keep one idea per paragraph, vary sentence
   length, and allow a fragment when it sounds natural aloud.
5. **Generosity:** make the reply useful even if the reader never visits the
   profile. A CTA is an optional next step, not the reason the post exists.

Run the portability test: if the draft could move to another account without
changing a noun, action, or opinion, it is too generic. Run the remove-brand
test: temporarily delete the brand and CTA. If the remaining observation is
not worth reading, return to the scene. When two drafts are equally accurate,
prefer the clearer, slightly less polished one with more lived detail.

Research basis: [Nielsen Norman Group](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/)
supports concise, scannable, objective writing over promotional "marketese";
[Buffer](https://buffer.com/resources/social-media-style-guide/) favors
relatable, genuine voice, empathy, and everyday words; [GOV.UK](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/tone-of-voice/right-tone/)
favors specific, conversational, active, human writing; [Google's people-first
guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
emphasizes first-hand experience and useful purpose. These are writing
principles, not claims about a Threads ranking formula.

### 4a. AI-tone banned lexicon and punctuation gate

This is a reusable rewrite gate, not a guarantee about any AI detector. Apply
it to the draft's own words only. Leave quoted parent text, proper nouns, brand
names, technical terms, identifiers, URLs, and user-requested exact copy
unchanged.

Use these mechanical rules:

- AI-TONE-01: rewrite generic AI/marketing vocabulary: delve, leverage,
  utilize, facilitate, seamless, robust, unlock, empower, elevate, game-changer,
  revolutionary, innovative, transformative, ecosystem, landscape, journey,
  navigate, foster, tapestry, paradigm, synergy, holistic, actionable,
  scalable, streamline, frictionless, cutting-edge, at the end of the day,
  in today's world, it's worth noting, here's the thing, excited to share,
  a testament to, small but mighty, sharing a small peek, the quiet parts,
  the little details, or makes everything easier. Use a plain verb or a
  specific detail instead.
- AI-TONE-02: ban em dashes (—) and en dashes (–) as sentence punctuation.
  Use a period, comma, colon, or parentheses. ASCII hyphens (-) are allowed
  only in legitimate compounds, identifiers, versions, URLs, or code, never
  as sentence separators.
- AI-TONE-03: rewrite generic bridges, slogan endings, "not X but Y"
  templates, empty rhetorical questions, and polished CTAs that could fit any
  project.
- AI-TONE-04: rewrite unnecessary three-part lists, mirrored clauses, and
  repeated parallel phrasing when they exist mainly for rhythm.
- AI-TONE-05: read the copy aloud once. If it sounds like a landing-page
  caption, rewrite from the concrete moment, decision, behavior, or artifact.
- AI-TONE-06: require one concrete anchor: a specific noun, action, time,
  number, tradeoff, or observed detail. Abstract warmth alone fails.

Mark AI-TONE: PASS only when all hard checks pass, the copy contains a
concrete anchor, and the voice-note test passes. Otherwise mark
AI-TONE: FAIL, identify the rule ID and exact offending phrase, and rewrite
before posting.

### 5. Run the preflight

Return `ready`, `needs evidence`, `needs rewrite`, or `do not post`.

Check that:

- the target analysis explains the visible ranking context and labels
  observation versus inference;
- the reply answers, extends, clarifies, or respectfully questions the parent;
- every number, capability, testimonial, result, and link is verified;
- the product mention and CTA are contextual and optional;
- the copy is original, human, and appropriate to the account;
- the first line sounds spoken rather than like a campaign headline;
- the draft contains a real scene, one tension, one point of view, and a clear
  reader payoff before any CTA;
- the draft passes the portability test and remove-brand test;
- the draft contains at least one concrete, account-specific observation or
  artifact and does not rely on abstract warmth;
- the draft passes the anti-AI-text check: no generic content-brief bridge,
  slogan-like conclusion, unnecessary three-part list, repetitive em-dash
  rhythm, “not X but Y” template, empty rhetorical question, or polished CTA
  that could fit any project;
- the selected voice mode is visible in the draft and is not an imitation of a
  named creator;
- health, safety, legal, financial, privacy, or other sensitive claims are
  bounded by the project's evidence and safety rules;
- the batch has no duplicate replies, engagement exchange, follow churn,
  indiscriminate follows, irrelevant hashtags, or spam-like distribution.

### 6. Execute and verify only when authorized

Use the available authenticated Threads/browser surface. Immediately verify
the visible account, exact text, parent post, CTA/link, and public permalink.
Record failed, partial, deleted, edited, rate-limited, challenged, or spam-
flagged states. Stop the batch if the account receives a warning or the target
conversation changes materially.

Never silently like, follow, repost, quote, DM, or publish beyond the action
the user authorized. Browser automation must use the installed browser-control
guidance and fresh DOM/state inspection before and after each action.

### 7. Record outcomes and improve

Before acting, record the ranking hypothesis and experiment cell. Afterward,
record the exact content, target, voice mode, CTA placement, human feedback, and
outcome in a project-local JSONL ledger. Use
`references/learning-ledger.md` for the schema and run:

```bash
python3 scripts/threads_learning.py validate --ledger <ledger.jsonl>
python3 scripts/threads_learning.py report --ledger <ledger.jsonl>
```

Capture a first stable snapshot after 24–72 hours and a later snapshot when
conversion needs more time. Separate:

- **Attention:** views, impressions, profile visits, detail expansions;
- **Conversation:** qualified replies, reposts with commentary, bookmarks,
  relevant follows;
- **Conversion:** clicks, signups, installs, activated users, sales.

Likes are context, not proof of quality, audience fit, or conversion. Compare
like with like: same format, topic, age window, account state, audience, CTA,
and distribution conditions.

## Iterative learning contract

Maintain learning in the project or campaign ledger, not in hidden model
memory. For every action, store the source, target analysis, hypothesis,
content cell, feedback, outcome, confidence, and next decision. Preserve
negative results and unknowns.

Use these evidence levels:

- **Observed:** directly visible in the Threads surface or analytics.
- **Attributed:** downstream event tied to a reliable link, event, or explicit
  user report.
- **Inferred:** plausible explanation that still needs testing.
- **Unknown:** not observed or not comparable.

Do not promote a pattern from one post. Treat a pattern as:

- **insufficient** with fewer than 3 comparable observations;
- **repeated-signal** with at least 3 observations and at least 2 positive
  outcomes, while retaining confounders;
- **promotion-candidate** only after a larger comparable sample, normally 8–12
  observations, with repeated positive outcomes and no obvious alternative
  explanation.

Promoting a pattern means adding it to a reviewed, project-agnostic guidance
section as a hypothesis with sample, dates, conditions, and limitations. Do
not encode “always,” guaranteed ranking tactics, or one project’s voice as a
universal rule. Shared-skill edits require an explicit maintenance action and
review; live engagement may produce a candidate update but must not mutate this
skill automatically.

## Resources

- Read [learning-ledger.md](references/learning-ledger.md) before recording or
  auditing engagement results.
- Run [threads_learning.py](scripts/threads_learning.py) for deterministic
  validation and descriptive pattern reporting. The script never publishes,
  edits, likes, follows, or contacts anyone.
