---
name: product-video
description: Create deterministic 1080p 60fps product launch videos, UI walkthroughs, social reels (9:16 TikTok/Reels/Shorts and 16:9 YouTube/X), reference-video recreations, and AI camera flights. Use when the user asks to make, storyboard, animate, recreate, or export a promo video, product demo, tutorial video, animated SVG showcase, or scroll-cinema film for products or social media.
---

# Product Video

Build studio-grade product and social videos as **deterministic code** (`HTML/CSS/SVG/Canvas` driven by a quantized virtual clock `window.seek(t)` / `window.__seekToTime(t)`, rendered frame-by-frame via Headless Chrome + FFmpeg at 1080p 60fps with subframe `tmix` motion blur and `-16 LUFS` sidechain-ducked audio).

Distilled from Jang Trịnh's `design-os-svg-animation` and `design-os` video engines.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

## Modes & Bundled Tooling

Pick the lightest mode that fits the request:

| Mode | Best for | Bundled runtime & scripts in this skill |
| --- | --- | --- |
| **1. Social Reel & Explainer (`16:9` + `9:16`)** | Product launches, build tutorials, feature reels with music beat sync, captions, and optional voiceover | `build.mjs`, `validate.mjs`, `look.mjs`, `kit/` (`render-tutorial.mjs`, `motion-core.js`, `tutorial-scene.js`, `tutorial-elements.js`, `tutorial-portrait-layout.js`, `voiceover/mix-voiceover.mjs`), `templates/` |
| **2. Interactive UI Walkthrough** | SaaS/app screen demos with camera punch-ins, cursor travel, concentric click ripples, and `StudioPlayer` controls | `scripts/ui-walkthrough-builder.mjs`, `scripts/StudioPlayer.mjs`, `scripts/virtual-clock.mjs`, `scripts/viewport.mjs`, `scripts/audit-cursor-click-hotspots.mjs`, `scripts/export-60fps-video.mjs` |
| **3. Reference Video Recreation** | Recreating an Apple/Linear/Stripe-caliber reference video frame-for-frame | `scripts/hyperframes-engine.mjs`, `scripts/hyperframes-motion-presets.mjs`, `scripts/detect-scene-cuts.mjs`, `scripts/extract-audio-waveform.mjs` |
| **4. AI Camera Flight / Scroll-Cinema** | Veo/Imagen frame-locked camera flythroughs or scroll-scrubbed 3D product showcases | [anti-flop and camera flights](references/anti-flop-and-camera-flights.md) |

## Two Owner Gates (Never Skip)

1. **Gate 1 — Storyboard, Beat Map & Script (before spending credits or full encode):**
   - Present the chapter/scene storyboard, target aspects (`16:9`, `9:16`, `1:1`), duration, real product evidence/screens to show, and caption/voice script.
   - **Stop and wait for James's approval.** Never call a paid voiceover API, spend AI video generation credits, or run a multi-minute `--full` encode while `approvals.storyboard` or `approvals.script` is unapproved (`null`). Beat sheets (`--beats`) and paused browser drafts are encouraged before Gate 1 closes.
2. **Gate 2 — Encoded Proof & Visual Review (before publish, schedule, or merge):**
   - Hand over the rendered MP4 path(s), the visual contact sheet (`look-sheet.png` or `beat-sheet-*.jpg`), and the exact verification command outputs.
   - Never publish to social channels, schedule in Buffer, or commit large binaries without explicit approval in the current conversation.

## Core Workflow

### 1. Ground in the Product & Intake Evidence

1. **Read the product first:** Load the target repository's design tokens, real components, copy, and proof/safety rules before scripting. Rebuild or capture real product UI; never invent fake components or placeholder metrics (`R1`).
2. **If recreating a reference video:** Run `ffprobe` and extract indexed frames (`frame-%06d.png`) and PTS timestamps into git-ignored scratch storage before writing scene code. Map every state `[start_frame, end_frame)` and boundary transition in a scene ledger. Full contract: [choreography and recreation](references/choreography-and-recreation.md).
3. **Strip personal paths (`R2`):** Never allow `/Users/<username>` in terminal cards, code excerpts, or image metadata (`mogrify -strip`).

### 2. Stage the Timeline & Choreography

Load [virtual clock and export](references/virtual-clock-and-export.md) and [choreography and recreation](references/choreography-and-recreation.md) for implementation details. Follow these invariants:

- **Pure virtual clock:** Every visual state (DOM, SVG, Canvas, cursor, ripples, particles) must be a pure function of time `t` via `window.seek(t)` / `window.__seekToTime(t)`. Seeking `A → B → A` must paint the exact same frame at `A`.
- **Await readiness before capture:** Expose `window.__framesReady()` awaiting `document.fonts.ready` and visible `img.decode()` so lazy glyph subsets (such as Vietnamese diacritics) and assets never drop during capture (`R11`).
- **Decoupled camera & pointer kinematics (Gate 8):** In UI walkthroughs, camera and cursor never move simultaneously:
  `Camera Punch (0.5s) → Camera Settle Hold (0.2s) → Pointer Travel (0.5s) → Concentric Click (0.3s) → UI Response Hold`.
- **Cursor concentricity (Gate 6):** Pointer arrow tip is strictly at `(0, 0)`, lands inside the target's bounding box, and aligns with the click ripple center within `Δ <= 1.0px`.
- **Closed-form springs (`kit/motion-core.js`):** Use `D.spring(dt, omega, zeta)` and `D.track(keys, t)` (`zeta = 0.65–0.86`) rather than stateful frame-to-frame physics loops. Show elements with `style.display = ''` and hide with `style.display = 'none'` (never hard-code `display: block`, which breaks `display: grid` — `R8`).
- **Multi-aspect safe zones (Gate 7):** Never letterbox `16:9` into `9:16`. Use spatial reflow (`?aspect=portrait` in `kit/tutorial-portrait-layout.js` or `scripts/viewport.mjs`):
  - `16:9` (`1920×1080`): safe zone `[96, 54, 1824, 1026]`.
  - `9:16` (`1080×1920`): safe zone `[108, 230, 972, 1574]` (excludes top 12% status/search bar and bottom 18% Reels/TikTok caption & action buttons; no settled content card below `y = 1600`).
  - `1:1` (`1080×1080`): safe zone `[81, 81, 999, 999]`.
- **Anti-Flop visual craft:** Zero raw Unicode emojis or text pseudo-arrows (`→`, `▾`). Use official Phosphor/Lucide vectors or the product's icon set, and pull brand marks from SVGL (`https://svgl.app/`). Full rules: [anti-flop and camera flights](references/anti-flop-and-camera-flights.md).

### 3. Render Beat Sheets, Mix Audio, and Encode 60fps MP4

#### A. Using the Multi-Aspect Social / Tutorial Kit (`build.mjs`)
```bash
# 1. Scaffold a new video project into promo/<slug>-tutorial/
node skills/product-video/build.mjs scaffold <source-dir> <slug> --into <output-parent-dir>

# 2. Render pre-flight beat sheets (1 frame per bar in 16:9 and 9:16) for Gate 1 review
node skills/product-video/build.mjs render <project-dir> --beats

# 3. After Gate 1 approval recorded in tutorial.config.json:
#    Mix voiceover + music bed (sidechain ducked, normalized to -16 LUFS)
node skills/product-video/build.mjs mix <project-dir>

# 4. Render 1080p 60fps MP4s (4x subframe tmix shutter blur, parallel shards)
node skills/product-video/build.mjs render <project-dir> --full --shards 3
```

#### B. Using Standalone `StudioPlayer` / Walkthrough Exporter
- Compile walkthrough steps with `UIWalkthroughBuilder` (`scripts/ui-walkthrough-builder.mjs`) and `renderPlayerHTML` (`scripts/StudioPlayer.mjs`).
- Pipe 60fps frames from Headless Chrome (`?clean=true&autoplay=false`) into FFmpeg (`libx264`, `crf 16`, `yuv420p`, `bt709`, `+faststart`, `tmix` subframe blur) using the pattern in `scripts/export-60fps-video.mjs`.

### 4. Verify Before Hand-Over

Run every applicable check after the **last** edit (stale proofs must be cleared first):

1. **Kit project validation:**
   ```bash
   node skills/product-video/validate.mjs <project-dir>
   node skills/product-video/look.mjs <project-dir>
   ```
   Then inspect `out/look/look-sheet.png` against the 7 eye-checks in [anti-flop and camera flights](references/anti-flop-and-camera-flights.md).
2. **Walkthrough hotspot & anti-flop audit:**
   ```bash
   node skills/product-video/scripts/audit-cursor-click-hotspots.mjs
   ```
3. **Encoded MP4 integrity & loudness check:**
   ```bash
   ffmpeg -v error -i <output.mp4> -f null -
   ffprobe -v error -show_entries format=duration -show_entries stream=codec_name,width,height,r_frame_rate,nb_frames -of json <output.mp4>
   ```

If `ffmpeg`, `ffprobe`, ImageMagick `montage`, or Chrome is not installed in the current environment, mark the affected gates `NOT_RUN` (`unverified`) — never claim `PASS` from source code alone.

## Hand-Over Contract

Reply with these four items in exact order (`R13`):

1. **NOT_RUN / Unverified first:** Name any check not run (e.g., no headless Chrome, no `ffmpeg`/`montage`, voice clips not yet generated, `9:16` sheet not visually inspected).
2. **Deliverable & proof paths:** Storyboard, HTML player, beat sheets, `look-sheet.png`, and encoded `16:9` / `9:16` MP4 paths.
3. **Verified gates & receipts:** Each command run (`validate.mjs`, `look.mjs` L1–L5, `audit-cursor-click-hotspots.mjs`, `ffmpeg -v error`, `ebur128`), its exit code, and the highest proof rung reached (`declared`, `rendered`, `interactive`).
4. **Open owner gate:** State whether waiting on **Gate 1 (Storyboard & Script Approval)** or **Gate 2 (Listen/Watch & Publish Approval)**.
