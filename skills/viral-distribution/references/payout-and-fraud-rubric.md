# Payout & Fraud Rubric: Rate Cards, Verification & Payout Gates

This reference governs financial payout calculations and view-fraud
scrubbing for clipping campaigns, UGC programs, and slideshow syndication.

Account warming, anti-ban ladders, proxy setups, and fleet device protocols
were removed: they belonged to phone-farm/account-fleet operations, which are
out of scope for this skill (platform ToS violations — see SKILL.md).

---

## 1. Industry Standard CPM Rate Cards (Clipping & Performance UGC)

When setting up pay-per-view incentives, use the following benchmark CPMs (Cost Per 1,000 Verified Views):

| Industry / Niche | Benchmark CPM | Pricing Structure | Rationale |
|---|---|---|---|
| **Live Streaming & Creator Clips** | $0.25 – $0.50 | Pure CPM (milestone caps) | High volume of source footage, broad entertainment audience, lower direct conversion intent. |
| **Music & Sound Promotion** | $0.50 – $1.00 | Pure CPM or $10 base + $0.50 CPM | Aiming for sound page saves and trending audio usage. |
| **Film, TV & Entertainment** | $1.00 – $2.00 | Pure CPM ($1k–$5k pool caps) | Narrative clips, higher production value, studio distribution standards. |
| **Gaming & Mobile Games** | $1.00 – $2.50 | Pure CPM or base + install bounty | Focus on high retention gameplay moments and download links. |
| **Consumer Apps (B2C)** | $1.50 – $3.00 | $20–$50 Base + $1.00–$2.00 CPM | Needs personal utility demonstration and problem-solution hooks. |
| **E-Commerce & DTC Physical** | $3.00 – $5.00+ | $30–$80 Base + $2.00–$4.00 CPM | Direct physical product demonstration, higher customer lifetime value. |
| **B2B SaaS & High ACV** | $5.00 – $10.00+ | $50–$150 Base + $5.00 CPM | Very narrow audience; requires strict geo and professional persona targeting. |

---

## 2. Slideshow Milestone Tier Structure (TikTok & IG Carousels)

Unlike flat CPM video models, photo carousels thrive on **performance milestone hurdles**. Flop posts (<100k views) incur $0 payout risk for the brand.

| Milestone Level | Verified Views | Payout Amount | Effective CPM | Operational Purpose |
|---|---|---|---|---|
| **Hurdle Tier** | 0 – 99,999 | **$0.00** | $0.00 | Protects brand budget from algorithmic test flops. |
| **Milestone 1** | 100,000 – 499,999 | **$100.00** | $1.00 – $0.20 | Rewards initial viral breakout; creator covers basic costs. |
| **Milestone 2** | 1,000,000 – 1,999,999 | **$350.00** | $0.35 – $0.18 | High-volume scaling payout. |
| **Milestone 3 (Cap)** | 2,000,000+ | **$500.00** | $0.25 | Hard cap per single post to prevent runaway budget spend. |
| **Loyalty Bonus** | Hit Posts | **+$25 to $50** | — | Surprise unannounced bonus paid immediately to secure daily posting consistency. |

---

## 3. Fraud & Bot Scrubbing Checklist

On unmanaged clipping platforms (e.g. open Whop communities), Discord syndication networks, or unverified creator pools, view-fraud via cheap SMM (Social Media Marketing) bot panels is widespread. Before approving any milestone payout, verify:

### Gate Check A: Geo-Distribution Audit
- **Rule:** Minimum 70% of views must originate from target commercial tier (Tier 1: US, UK, CA, AU, NZ, Western Europe).
- **Red Flag:** High view count (>100k) with over 60% originating from non-target or click-farm geographies (e.g. Bangladesh, Vietnam, India, Pakistan) on a US-targeted product.
- **Action:** If geo-threshold fails, disqualify view batch or apply Tier-3 adjustment formula (`Valid_Views = Tier_1_Views + (Tier_3_Views * 0.1)`).

### Gate Check B: Engagement Ratio Discrepancies
Compare views against organic interaction baselines:
- **Organic Likes-to-Views Ratio:** Typical healthy short-form range is 4% to 12%. If views are 250,000 but likes are under 500 (0.2%), the traffic is artificial bot-scraped.
- **Comment-to-View Ratio:** Should exceed 0.05% (50 comments per 100k views). If a 100k-view video has 2 comments (both bot emojis), reject payout.
- **Save & Share Ratios (Crucial for Slideshows):**
  - For standard video: saves should be >=0.5%.
  - For **photo slideshows / carousels**: saves are the primary algorithmic driver and should fall between **1.5% and 5.0%** (1,500 to 5,000 saves per 100k views). High views with under 50 saves on a carousel is conclusive proof of SMM panel injection.

### Gate Check C: Sudden Velocity Spikes
- **Organic Curve:** Exponential build-up (slow climb over 2–6 hours as initial test buckets expand, peak at 12–36 hours).
- **Bot Injection Curve:** 0 views for 20 hours, sudden vertical jump to 80,000 views within 15 minutes, followed by flatline.
- **Action:** Request platform analytics screen recording (TikTok Studio / Meta Insights) showing retention graph and referral source (FYP vs. Direct/Unknown). Reject external direct URLs without FYP delivery.
