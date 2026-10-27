# Payout & Fraud Rubric: Rate Cards, Verification & Payout Gates

This reference governs financial payout calculations and view-fraud
scrubbing for clipping campaigns and UGC programs.

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

## 2. Fraud & Bot Scrubbing Checklist

On unmanaged clipping platforms (e.g. open Whop communities) or unverified UGC networks, view-fraud via cheap SMM (Social Media Marketing) bot panels is widespread. Before approving any milestone payout, verify:

### Gate Check A: Geo-Distribution Audit
- **Rule:** Minimum 70% of views must originate from target commercial tier (Tier 1: US, UK, CA, AU, NZ, Western Europe).
- **Red Flag:** High view count (>100k) with over 60% originating from non-target or click-farm geographies (e.g. Bangladesh, Vietnam, India, Pakistan) on a US-targeted product.
- **Action:** If geo-threshold fails, disqualify view batch or apply Tier-3 adjustment formula (`Valid_Views = Tier_1_Views + (Tier_3_Views * 0.1)`).

### Gate Check B: Engagement Ratio Discrepancies
Compare views against organic interaction baselines:
- **Organic Likes-to-Views Ratio:** Typical healthy short-form range is 4% to 12%. If views are 250,000 but likes are under 500 (0.2%), the traffic is artificial bot-scraped.
- **Comment-to-View Ratio:** Should exceed 0.05% (50 comments per 100k views). If a 100k-view video has 2 comments (both bot emojis), reject payout.
- **Save & Share Ratios:** TikTok and IG algorithm recommendations heavily weight saves and shares. High views with near-zero saves indicates external SMM panel injection.

### Gate Check C: Sudden Velocity Spikes
- **Organic Curve:** Exponential build-up (slow climb over 2–6 hours as initial test buckets expand, peak at 12–36 hours).
- **Bot Injection Curve:** 0 views for 20 hours, sudden vertical jump to 80,000 views within 15 minutes, followed by flatline.
- **Action:** Request platform analytics screen recording (TikTok Studio / Meta Insights) showing retention graph and referral source (FYP vs. Direct/Unknown).
