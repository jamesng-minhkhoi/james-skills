# Platform Safe Zones and Dimensional Specifications

Mobile social feeds overlay permanent native user interface elements (account
headers, right-hand interaction icons, bottom captions, audio discs, and system
status bars) over carousel posts. Content placed outside platform safe zones
will be obscured or clipped.

---

## 1. Dimensional Presets

| Platform | Mode | Aspect Ratio | Dimensions (px) | Primary Inset Requirement |
|---|---|---|---|---|
| **TikTok** | Photo Mode | 9:16 | 1080 × 1920 | Strict safe zone (heavy bottom and right UI) |
| **Instagram** | Feed Carousel | 4:5 (Standard) | 1080 × 1350 | Vertical bounds; top/bottom feed icons |
| **Instagram** | Square (Legacy) | 1:1 | 1080 × 1080 | Uniform 60px margin |
| **LinkedIn** | Document Deck | 4:5 or 16:9 | 1080 × 1350 or 1920 × 1080 | Standard margin (80px); top page indicator |

---

## 2. TikTok Photo Mode (9:16 — 1080 × 1920 px)

TikTok renders high-density UI overlays over vertical photo posts:

- **Top Safe Margin:** 160 px (System status bar, back button, search icon).
- **Bottom Safe Margin:** 320 px (Account name, multi-line caption, sound marquee, photo indicator pills).
- **Right Safe Margin:** 130 px (Profile follow icon, like count, comment count, bookmark/save icon, share icon).
- **Left Safe Margin:** 60 px (Standard comfortable screen padding).
- **Active Safe Content Canvas:** 890 px width × 1440 px height, offset from (x: 60, y: 160).

**Strict Rule:** No headline, critical diagram label, code snippet, or CTA button may intersect the bottom 320 px or right 130 px of a 1080 × 1920 TikTok slide.

---

## 3. Instagram Feed Carousel (4:5 — 1080 × 1350 px)

Instagram 4:5 fills the feed viewport vertically without letterboxing:

- **Top Safe Margin:** 80 px (Account header bar, ellipsis menu).
- **Bottom Safe Margin:** 100 px (Pagination dots, bookmark icon, like/comment bar).
- **Horizontal Safe Margins:** 70 px left and right.
- **Active Safe Content Canvas:** 940 px width × 1170 px height.

---

## 4. Typography and Legibility Thresholds

All typography must be legible when viewed on a 6.1" smartphone display at arms
length:

- **Slide Headline:** 56–72 px (Bold, high-contrast; max 2 lines).
- **Sub-headline / Section Header:** 36–44 px (Semi-bold).
- **Body Copy / Explanations:** 28–34 px (Regular or Medium; minimum line height 1.4x).
- **Diagram Callouts / Code:** Minimum 24 px (Monospace or clear Sans-Serif).
- **Source Citation / Eyebrow:** 20–24 px (Muted, uppercase).
- **Contrast:** Minimum 4.5:1 against the background (WCAG AA). 7:1 preferred for technical code diffs.
