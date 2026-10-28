# Choreography, HyperFrames, and Reference Recreation

Distilled from Jang Trinh's `ui-walkthrough-builder.mjs`, `hyperframes-engine.mjs`, `motion-core.js`, `motion-video-recreation-pipeline.md`, and `audit-cursor-click-hotspots.mjs`.

## 1. Decoupled Camera & Pointer Kinematics (Gate 8 Invariant)

When AI agents animate camera zoom/pan and cursor movement at the same time, the viewer gets motion sickness and the cursor drifts across moving targets. Enforce **strictly decoupled phases** for every UI walkthrough step (`scripts/ui-walkthrough-builder.mjs`):

```text
Phase 1: Camera Punch-In (0.5s)   -> Camera zooms/pans to target; pointer stays stationary.
Phase 2: Camera Settle Hold (0.2s)-> Camera locks completely still; viewer orients to the UI area.
Phase 3: Pointer Travel (0.5s)    -> Pointer travels from previous position to target while camera is still.
Phase 4: Click Action (0.3s)      -> Pointer presses + concentric click ripple expands.
Phase 5: Response & Hold (1.5s+)  -> UI state changes (sheet opens, row updates, callout appears).
```

Never overlap `cameraPunch` and `pointerTravel` intervals.

## 2. Cursor Tip & Click Ripple Concentricity (Gate 6 Invariant)

A synthetic cursor that misses a button or triggers a ripple 20px away from its tip immediately reads as fake:

1. **Canonical tip origin:** Place the macOS/pointer SVG arrow tip strictly at local coordinate `(0, 0)` of `#virtual-cursor`.
2. **Concentric ripple (`Δ <= 1.0px`):** At every click timestamp `evt.t` in `window.__CLICK_EVENTS`, the Euclidean distance between the cursor tip (`curRect.left`, `curRect.top`) and the ripple center (`ripRect.left + ripRect.width / 2`, `ripRect.top + ripRect.height / 2`) must be `<= 1.0px`.
3. **Target hit-box containment:** The pointer tip at `evt.t` must land strictly inside the target interactive element's `getBoundingClientRect()`.
4. **Zero press jitter:** Activating `.pressed` on the cursor scales around `transform-origin: 0 0` so the tip never shifts off `(0, 0)`.

Audit automatically with `node scripts/audit-cursor-click-hotspots.mjs`.

## 3. Pure-Time Physics Primitives (`kit/motion-core.js`)

Avoid rigid linear tweens and stateful physics loops that break when seeking out of order. Compute every spring and transition in closed form as a function of `t`:

- **Closed-form underdamped spring (`D.spring(dt, omega, zeta)`):**
  - Default UI card/element track: `omega = 22`, `zeta = 0.86` (snappy settle, subtle overshoot).
  - Weighted object / camera travel: `zeta = 0.65–0.80` (one counter-swing of `1.5°–5°`, settling under `1.5°` within `0.35s`).
- **Multi-keyframe spring superposition (`D.track(keys, t, omega, zeta)`):**
  - Treats `[[t0, v0], [t1, v1], ...]` as a sum of step responses starting at each `ti`, so a target can move multiple times smoothly without state carry.
- **Visibility window (`D.vis(t, tin, tout, fin, fout)` + `D.applyVis(el, v, lift)`):**
  - Combines smoothstep opacity with a subtle vertical lift (`translateY((1 - v) * lift)`) and short motion blur (`blur((1 - v) * 7px)`), hiding inactive elements with `display = 'none'` and restoring them with `display = ''` (never hard-code `display = 'block'`, which breaks `display: grid` cards — `R8`).

## 4. HyperFrames v2 Staging (`scripts/hyperframes-engine.mjs`)

Before spending time on high-gloss styling, stage the video as a finite, paused beat draft using atomic beat kinds (`text`, `logo`, `input`, `chat`, `window`, `phone`, `cards`, `list`, `chart`, `notify`, `shape`) and pure sampling presets (`scripts/hyperframes-motion-presets.mjs`):

- `sampleHyperFrameProgress(time, start, end)` — smoothstep `[0, 1]` over `[start, end]`.
- `sampleHyperFrameStagger(time, start, index, spacing, duration)` — deterministic staggered item entrances.
- `sampleHyperFrameCarry(time, enterStart, enterEnd, exitStart, exitEnd)` — enter-hold-exit envelope for carried elements.
- `sampleHyperFrameKeyframes(time, keys)` — piecewise smoothstep interpolation across `[t, v1, v2, ...]`.

## 5. Reference Video Recreation Contract

When the user supplies a reference promo video to analyze or recreate:

1. **Intake before code:** Inspect the reference with `ffprobe` (native resolution, frame rate, frame count, duration, audio streams) and extract source-indexed frames (`frame-%06d.png`) and PTS timestamps into git-ignored scratch storage. Never guess FPS or shot timing from memory.
2. **Scene & transition ledger:** Map every state `[start_frame, end_frame)` AND every boundary between states. Automatic cut detection (`scripts/detect-scene-cuts.mjs`) finds hard cuts only; inspect soft transitions manually at `0.1s` frame strips around each boundary and answer:
   - What leaves, what enters, and which object persists across the boundary?
   - Is the transition a mask/iris, camera rush, depth defocus, object carry, or hard cut? (Never replace a specific source transition with a generic uniform crossfade.)
3. **Separate engineering pass from visual acceptance:**
   - **Engineering pass:** `window.__seekToTime` determinism, anti-flop gates, and clean MP4 decode pass.
   - **Visual pass:** Side-by-side comparison of source frames and **decoded final MP4 frames** across scene interiors and boundary strips, plus continuous playback at `0.25×` and `1×`. Never claim a numeric similarity percentage (e.g., "99% identical"); report concrete matches, open gaps, and wait for James's visual acceptance.
