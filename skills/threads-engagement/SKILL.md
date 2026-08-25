---
name: threads-engagement
description: Research, draft, publish, measure, and improve authentic Threads posts and replies for any project or account. Use for topic discovery, ranked-feed analysis, community engagement, product promotion, launch conversations, listening experiments, performance reviews, and converting repeated feedback into evidence-backed content patterns.
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

### 4. Draft for the parent conversation

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

### 5. Run the preflight

Return `ready`, `needs evidence`, `needs rewrite`, or `do not post`.

Check that:

- the target analysis explains the visible ranking context and labels
  observation versus inference;
- the reply answers, extends, clarifies, or respectfully questions the parent;
- every number, capability, testimonial, result, and link is verified;
- the product mention and CTA are contextual and optional;
- the copy is original, human, and appropriate to the account;
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
record the exact content, target, CTA placement, and outcome in a project-local
JSONL ledger. Use `references/learning-ledger.md` for the schema and run:

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
