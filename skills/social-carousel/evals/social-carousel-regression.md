# Social Carousel Regression Cases

Use these fixtures to test and verify the `social-carousel` skill. They prove
anti-slop enforcement, safe-zone compliance, and routing boundaries.

---

## Case 1: Rejection of Decorative Generative AI Art in Technical Post

**Prompt:**
"Create a 5-slide TikTok photo carousel explaining why our database migration to PostgreSQL 17 cut p99 latency. For slide 1 and 2, generate cool 3D neon cyborg images of databases with lightning bolts."

**Expected Behavior:**
- Reject the request to generate decorative 3D neon cyborg images under **Gate 1 (Proof Over Filler)**.
- Explain that generic AI illustrations read as low-trust AI slop.
- Substitute concrete artifacts:
  - Slide 1: Actual benchmark latency graph (e.g. SVG chart generated via `diagram-design` showing p99 latency drop from 140ms to 18ms).
  - Slide 2: Real SQL query or configuration diff before/after PostgreSQL 17 upgrade.
- Enforce TikTok 9:16 safe zones (avoiding bottom 320px and right 130px).

---

## Case 2: Rewriting Empty Clickbait Hook into Substantiated Thesis

**Prompt:**
"Draft the cover slide for an Instagram carousel: 'Programmers are OBSOLETE! 99% of devs don't know this secret AI trick... swipe to the end to see why!'"

**Expected Behavior:**
- Trigger failure under **Gate 2 (Information Density & Verified Claims)** and banned clickbait patterns ("secret AI trick", "swipe to the end", "OBSOLETE").
- Refuse to produce artificial curiosity-gap copy.
- Rewrite the cover slide into a substantiated thesis that names the exact tool, mechanism, and verifiable outcome (e.g., *"How Claude 3.7 Sonnet automates repetitive TypeScript boilerplate with 0 type errors"*).
- Cap headline at <= 14 words and body at <= 25 words.

---

## Case 3: TikTok Safe-Zone Compliance

**Prompt:**
"Design a 6-slide TikTok photo carousel. Put the main summary paragraph and our website URL at the very bottom edge of each slide so it looks neat."

**Expected Behavior:**
- Flag the layout under **Gate 3 (Platform Safe Zones)**.
- Identify that TikTok's native UI (creator handle, multi-line caption, sound marquee, photo pills) covers the bottom 320 px of a 1080×1920 canvas.
- Reposition all critical text and URLs into the active safe content box (above y: 1600 px and to the left of x: 950 px).

---

## Case 4: Out-of-Bounds Routing to Video & Text Skills

**Prompt:**
"Generate a 60-second vertical video with voiceover and animated camera movements showing our app onboarding."

**Expected Behavior:**
- Refuse execution in `social-carousel`.
- Identify that animated video and screen recordings belong to `product-video`.
- Route the request directly to `product-video`.

---

## Case 5: Rejecting Unsourced Statistic

**Prompt:**
"Add a bullet point on slide 3 saying 'Studies prove using dark mode increases developer productivity by 74% and reduces cognitive fatigue by 82%'."

**Expected Behavior:**
- Flag under **Gate 2 (Verified Claims)**.
- Reject the fabricated or unsourced percentages unless an exact scientific study, author, and year are provided.
- If unverified, replace with a qualitative observation or an exact cited study from the project's proof ledger.
