---
name: viral-distribution
description: Plan and operate organic short-form distribution campaigns on TikTok, Instagram Reels, and YouTube Shorts across three legitimate engines — clipping, UGC, and slideshow syndication. Covers engine selection, CPM/milestone contracts, creator briefs, and fraud scrubbing before payouts. Refuses phone farms, account fleets, and platform detection evasion. Do not use for text-only social (x-engagement, threads-engagement), raw video rendering (product-video), or web SEO (seo-aeo-geo).
---

# Viral Distribution

Scale organic short-form video and photo carousel distribution on TikTok,
Instagram Reels, and YouTube Shorts through disciplined campaign engineering.
Organic virality is an operational and algorithmic game, not random luck.

Ground campaigns in three legitimate, non-interchangeable distribution
mechanisms:

1. **Clipping Campaigns:** Crowdsourced cut-downs via Discord/Whop pools
   operating on pure performance CPM ($0.25–$2.00+). High speed, low
   operational friction, low control.
2. **UGC Programs:** Face-driven authentic videos filmed by real creators for
   brand accounts operating on Base Fee + CPM ($25 base + $1 CPM). Maximum
   trust, high conversion, high operational intensity.
3. **Slideshow Syndication Programs:** Multi-slide photo carousels (6–10
   slides) distributed across native creator accounts via milestone-tiered
   bounties ($100 @ 100k, $350 @ 1M). Ultra-low production cost, high save
   rates, zero base-fee downside. For carousel design/scripting, route to `social-carousel`.

**Out of scope, always:** phone farms / account fleets, running or
coordinating multiple accounts on dedicated hardware, engineering creative to
evade platform duplicate or automation detection, and synthetic AI-avatar slop
(faceless or generated talking heads mass-pitching products). These violate
platform terms of service or destroy consumer trust. If asked for them, refuse
and name the legitimate alternative (real independent creators, distinct
source moments, or paid ads).

Load [distribution engines](references/distribution-engines.md) for detailed
mechanics, slideshow anatomy, and industry fit. Load [payout and fraud rubric](references/payout-and-fraud-rubric.md)
before calculating budgets, releasing payouts, or auditing invoices.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder,
verdicts, and finding IDs.

---

## Operating Modes

Pick one mode before executing:

- **1. Engine Selection & Diagnostic:** Evaluate product type, trust
  requirements, creative reuse velocity, and available budget to select the
  right engine (Clipping vs. UGC vs. Slideshow Syndication).
- **2. Campaign Structuring & Economics:** Design the payout contract (Base
  fee, CPM, milestone hurdles, pool caps), recruitment brief, and compliance rules
  using `scripts/campaign_calculator.py`.
- **3. Performance Audit & Fraud Scrubbing:** Audit view claims before
  milestone payouts, detecting SMM panel bot injection, Tier-3 geo dilution,
  and engagement/save ratio anomalies.

---

## Two Owner Gates (Never Skip)

### Gate 1 — Campaign Brief & Payout Contract (Before Recruiting or Spending)
- Present the selected engine, target audience, creator/clipper brief, CPM
  rate card or milestone tier, base fees, budget cap, and escrow rules.
- **Stop and wait for James's approval.** Never launch an open clipping
  bounty, sign UGC creator agreements, or distribute slideshow decks while
  Gate 1 is unapproved (`null`).

### Gate 2 — Pre-Payout Verification (Before Paying)
- Verify view logs against the [fraud rubric](references/payout-and-fraud-rubric.md)
  (geo-distribution >= 70% Tier 1, likes-to-views >= 4%, comments >= 0.05%,
  carousel saves >= 1.5%). Reject bot-injected links.
- Never release milestone payments without explicit approval in the current
  conversation.

---

## Core Workflow

### 1. Select the Engine by Product & Industry Fit

Do not use cookie-cutter strategies. Match product realities to the right
distribution engine:

| Product Category | Primary Engine | Secondary / Amplification | Why |
|---|---|---|---|
| **Utility Mobile Apps & Micro-SaaS** | **Slideshow Syndication** | **UGC** | Checklists and diagnostic cards drive massive bookmark/save rates and qualify download intent at zero filming cost. |
| **Consumer Apps (B2C High-Trust)** | **UGC** | **Clipping** | Needs high personal trust and rapid problem-solution script testing with real creators. |
| **Film, TV & Entertainment** | **Clipping** | **Micro-UGC** | High-production source material; clippers cut narrative moments for pure CPM reach. |
| **Music & Indie Artists** | **Clipping** | **Micro-UGC** | Clips build trending sound volume; cheap UGC attaches real faces to tracks. |
| **E-Commerce / DTC** | **UGC** | **Clipping** | Physical product demonstrations convert on visual proof and authentic testing. |
| **B2B SaaS / High ACV** | **UGC (Founder/Operator)** | **Remotion Reels (`product-video`)** | Requires high authority and strict product accuracy. Open clipping damages reputation. |

### 2. Model Campaign Economics

Run `scripts/campaign_calculator.py` to calculate financial models:
```bash
# Compare all three engines for 1M views:
python3 skills/viral-distribution/scripts/campaign_calculator.py compare --views 1000000

# Model pure clipping campaign with fraud reserves:
python3 skills/viral-distribution/scripts/campaign_calculator.py clipping --views 500000 --cpm 1.50

# Model UGC creator campaign with base + performance CPM:
python3 skills/viral-distribution/scripts/campaign_calculator.py ugc --views 500000 --base 30.0 --cpm 1.00

# Model Slideshow Syndication milestone campaign ($100 @ 100k, $350 @ 1M):
python3 skills/viral-distribution/scripts/campaign_calculator.py slideshow --views 1000000 --payout-100k 100 --payout-1m 350
```

### 3. Scale Winning Creative the Legitimate Way

When a hook, script angle, or slide format wins, spread it across *independent creators*:
- **UGC:** pass the winning script to creators so each records their own authentic take.
- **Clipping:** let clippers cut different moments from the same source footage in their own style.
- **Slideshows:** syndicate the winning checklist/diagnostic format across independent creator Discord networks, varying cover hook titles, palette styling, and trending audio pairings.

What never happens: re-rendering the same MP4 or image sequence with pixel-hash tricks
to repost it from many brand accounts — that is duplicate-content evasion, it is out of
scope, and the remedy is more creators or paid ads, not evasion.

For code-rendered layouts and Remotion templates, hand off layout specifications to
`product-video`.

### 4. Audit Performance & Scrub Fraud Before Payout

Before releasing escrow funds to clippers, creators, or syndicators:
1. **Scrub Geo Dilution:** Verify >=70% views originate from Tier-1 target
   countries (US, UK, CA, AU, NZ, Western Europe). Apply Tier-3 penalty
   discounts on unmanaged submissions.
2. **Audit Engagement Ratios:** Flag videos where likes-to-views < 4% or
   comments-to-views < 0.05% as bot injections. For slideshows, require
   saves-to-views >= 1.5%.
3. **Verify Referral Sources:** Require screen recordings of creator
   analytics confirming traffic originated from the algorithmic For You /
   Recommended feed rather than external direct URLs.

---

## Out-of-Scope Boundaries

- **Phone farms, account fleets, multi-account hardware coordination, or
  duplicate/automation detection evasion:** Refuse. Violates platform ToS.
  Offer more creators, more distinct source moments, or paid ads instead.
- **Text-only social posting or replies on X:** Route to `x-engagement`.
- **Text-only social posting or replies on Threads:** Route to
  `threads-engagement`.
- **Deterministic 60fps MP4 video rendering, Remotion code, or FFmpeg
  pipelines:** Route to `product-video`.
- **Website SEO, Schema markup, or Answer Engine citations:** Route to
  `seo-aeo-geo`.
- **Product specifications, PRDs, or feature prioritization:** Route to
  `product-discovery`.
