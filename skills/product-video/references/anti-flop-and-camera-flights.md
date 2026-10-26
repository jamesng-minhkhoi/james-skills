# Visual Craft, Anti-Flop Gates, and AI Camera Flights

Distilled from Jang Trịnh's `skills/product-designer/SKILL.md`, `scripts/anti-flop-gate.py`, `skills/es-tutorial-video/look.md`, `knowledge/scroll-cinema-direction.md`, and `knowledge/gflow-hand.md`.

## 1. The 6 Visual Craft Hardrules for Video Scenes

Every HTML/SVG/CSS video scene must pass these rules before rendering:

1. **Zero Raw Emojis & Pseudo-Icons (Gate 1):**
   - Unicode emojis (`🚀`, `🌐`, `⚙️`, `💬`, `✨`) and text pseudo-arrows (`←`, `→`, `↻`, `▾`, `▷`) are strictly banned inside video stages, buttons, and badges.
   - Use official **Phosphor** (`@phosphor-icons/core`) or **Lucide** (`lucide-react`) inline SVG vectors with explicit `viewBox`, or the product's own shipped SVG icon set.
   - Pull third-party brand logos from **SVGL** (`https://svgl.app/`) with intact coordinates and `viewBox` — never hand-type approximate brand paths.
2. **Multi-Layer Tactile Depth or System Tokens (Gate 3):**
   - Follow the target product's design tokens first (per [slop and consistency](../../design-uiux/references/slop-and-consistency.md)).
   - When rendering elevated UI cards on a video stage, use layered ambient + directional depth (`0 1px 2px rgba(0,0,0,0.04), 0 8px 18px -6px rgba(0,0,0,0.08), 0 30px 50px -18px rgba(0,0,0,0.14)`) and `1px` translucent borders (`rgba(255,255,255,0.08)` in dark mode, `rgba(17,17,17,0.10)` in light mode), never flat harsh single-layer black drop shadows or `2px` opaque borders.
3. **Typography & Antialiased Smoothing (Gate 2):**
   - Always set `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;` on the stage body.
   - Display headlines (`>= 48px`) use tight negative tracking (`-0.02em` to `-0.04em`); metadata tags and timecodes use monospace (`Geist Mono` or `JetBrains Mono`).
   - Captions never overlap in time (`R6`: each caption window exits before the next enters).
4. **Aspect Ratio & Canvas Buffer Integrity (Gate 4):**
   - Any `<canvas>` or WebGL/Three.js surface inside a video scene must match its pixel buffer (`canvas.width`, `canvas.height`) to its CSS display bounds (`clientWidth`, `clientHeight`) so circular/3D elements never stretch across `16:9` and `9:16`.
   - Include `@media (prefers-reduced-motion: reduce)` fallbacks when shipping interactive web player deliverables.
5. **No Coordinate Hallucinations or Home Paths (Gate 5 & R2):**
   - Zero `NaN`, `Infinity`, or `undefined` values in SVG paths or inline styles.
   - Zero `/Users/<username>` strings in terminal cards, code excerpts, or image EXIF metadata (`mogrify -strip`).
6. **One Camera Across Build/Product Wipes (R12):**
   - When wiping between before/after states, themes, or 3D wireframe → final render passes (`R.wipe`), lock the exact same camera/viewport geometry across every layer so the subject never jumps during the sweep.

## 2. Automated Machine + Eye Checks (`validate.mjs` & `look.mjs`)

For projects built with the `product-video` kit (`node build.mjs ...`):

1. **Mechanical Validator (`node validate.mjs <project-dir>`):**
   - Checks `contract-intact`, `config-schema`, `timeline-eval`, `timeline-authored`, `evidence-shape`, `assets-exist`, `script-authored`, `script-clips`, `captions-overlap`, `display-block`, `no-home-path`, `gitignore-music`, and `beat-names`. Must exit `0`.
2. **Visual Sheet & Machine Probe (`node look.mjs <project-dir>`):**
   - Renders every chapter twice per aspect (`16:9` and `9:16` at `0.75` bar for the chapter card and midpoint for settled content) plus shard seam frame pairs into a single contact sheet (`out/look/look-sheet.png`).
   - Automatically verifies:
     - `L1 fonts`: required fonts (`Geist`, `Geist Mono`) loaded before capture.
     - `L2 edge`: no settled element (`opacity >= 0.9`) sticks outside stage bounds.
     - `L3 portrait`: in `9:16`, no settled content extends below `y = 1600` into the caption zone.
     - `L4 caption`: visible caption stays `>= 24px` inside stage edges.
     - `L5 requests`: zero page errors, failed network requests, or broken images.
3. **7 Mandatory Human/Agent Eye-Checks on `look-sheet.png`:**
   - **(1) Captions readable:** one pair at a time, sufficient contrast over every card.
   - **(2) No unmeasured clipping:** no text clipped by `overflow:hidden` or cut diacritics.
   - **(3) Wipes aligned:** phase wipes keep identical angle, scale, and position.
   - **(4) Card fan on stage:** fanned/grid cards stay ordered and inside the frame in both `16:9` and `9:16`.
   - **(5) Portrait slots:** top/bottom/mid slots in `9:16` look balanced and clear of the bottom caption.
   - **(6) Honest limits visible:** when documenting a build or product proof, limits are stated verbatim.
   - **(7) Seam frames continuous:** frames on either side of shard seams match with zero flash or jump.

If Chrome or ImageMagick `montage` is unavailable (`look.mjs` exits `2`), never claim a visual check — mark visual verification `NOT_RUN` (`unverified`) at the top of the hand-over.

## 3. AI Video Chaining & Scroll-Cinema (`scroll-cinema-direction` & `gflow`)

When a product video or launch page requires pre-rendered 3D/AI camera flights (e.g., Google Veo / Imagen i2v chains or scroll-scrubbed hero films):

1. **Architecture A (Continuous Forward Take — Default):**
   - The camera glides forward from scene to scene. Each leg is generated from the **actual extracted final frame** of the previous leg (`ffmpeg -sseof -0.04 -i leg_N.mp4 -frames:v 1 seed_N+1.png`), never from an assumed prompt or end-frame target.
   - Do not aim a forward leg at a wide establishing end-frame (which forces the model to pull backward and creates a rewind stutter at the seam).
2. **Seam Physics (Position + Velocity Continuity):**
   - **Across a seam:** the camera must never reverse direction. Every leg ends by settling into a slow, steady forward drift, and the next leg begins by continuing that same drift.
   - **Inside a leg:** mid-clip orbits, crane-ups, and lateral tracking around the product are encouraged as long as the entry and exit drifts match.
3. **Verify-Then-Spend Credit Rule:**
   - Every AI video/voice generation call spends real credits. Never auto-retry failed generation calls in a loop, and never chain leg `N+1` until leg `N`'s MP4 is downloaded, verified non-empty on disk, and its final frame is extracted.
   - Lock visual identity first: approve one anchor hero still before branching multi-scene variants.
