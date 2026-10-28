# Anti-Slop Rubric for Social Carousels

High-performing, trusted social carousels (TikTok photo mode, Instagram 4:5,
LinkedIn document decks) deliver immediate, dense utility. This rubric defines
the seven failure modes of generative AI slop and their high-craft replacements.

---

## The 7 Sins of AI Carousel Slop

| AI Slop Symptom | Why It Fails | High-Craft Replacement |
|---|---|---|
| **1. Decorative AI Art** | Floating 3D neon shapes, glowing brains, generic cybernetic robots, or Midjourney stock humans add zero informational signal. | **Concrete Artifacts:** Real UI screenshots, side-by-side code diffs, quantitative charts from `diagram-design`, or authentic photography. |
| **2. Curiosity-Gap Clickbait** | Slide 1 says *"99% of developers do this wrong... wait till slide 7!"* Viewer feels deceived when the payoff is trivial. | **Substantiated Thesis:** State the exact problem, mechanism, and payoff on slide 1 (e.g., *"Why React 19 Actions replace useEffect for form state"*). |
| **3. Wall-of-Text AI Bullet Lists** | Unedited ChatGPT prose copy-pasted into slide text blocks. Unreadable on mobile; looks lazy. | **Single-Idea Architecture:** One primary headline, one visual artifact, and max 3 supporting bullet points (<= 25 words total per slide). |
| **4. Fabricated / Uncited Metrics** | *"Studies show productivity drops 47%"* with no source, author, date, or study name. Destroys trust. | **Verified Attribution:** Every statistic or quote cites the exact source, author, and year (e.g., *GitHub Octoverse 2025* or project proof ledger). |
| **5. Artificial Cliffhangers** | Withholding the answer across 4 fluff slides just to force swipe counts. | **Front-Loaded Value:** Give the answer or core finding immediately on slide 2; use subsequent slides to unpack nuances, edge cases, and proofs. |
| **6. Safe-Zone Blindness** | Text placed at the extreme edges or lower third is covered by TikTok icons (like, comment, share) or caption overlays. | **Platform Safe Insets:** Keep all text and key graphics strictly within safe margins (150px top, 280px bottom, 120px right on 9:16). |
| **7. Engagement Pod Begging** | Slide 8 says *"Comment 'INFO' for the PDF!"* or *"Save this post right now!"* without delivering legitimate reference value. | **Merit-Based CTA:** Offer a contextual next step (e.g., repository link, companion tutorial, or a genuine technical debate question). |

---

## Content-Type Architecture

Match the carousel format to the nature of the proof:

1. **The Technical Teardown / Code Diff:**
   - Slide 1: Problem + outcome.
   - Slide 2: The naive / legacy approach (red diff or screenshot).
   - Slide 3: The breakdown of why it breaks (failure mechanism).
   - Slide 4: The modern / fixed approach (green diff or screenshot).
   - Slide 5: Benchmark or trade-off analysis.
   - Slide 6: Actionable takeaway.

2. **The Product / Design Forensic:**
   - Slide 1: The product UX friction or before state.
   - Slides 2–4: Step-by-step forensic analysis with highlighted callouts on actual UI.
   - Slide 5: The redesign or architectural pattern.
   - Slide 6: Measurable impact or implementation detail.

3. **The Data / Architecture Explainer:**
   - Slide 1: System tension or performance bottleneck.
   - Slide 2: High-level topology diagram (clean SVG from `diagram-design`).
   - Slides 3–4: In-depth zoom on the specific protocol or component.
   - Slide 5: Latency/throughput comparison table.
   - Slide 6: Summary rule of thumb.
