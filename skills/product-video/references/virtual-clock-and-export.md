# Virtual Clock, 60fps Export, and Multi-Aspect Safe Zones

Distilled from Jang Trịnh's `design-os-svg-animation` virtual-clock architecture (`virtual-clock.mjs`, `viewport.mjs`, `render-tutorial.mjs`, `export-60fps-video.mjs`, and `mix-voiceover.mjs`).

## 1. Why a Virtual Quantized Clock

Web animations driven by wall-clock `requestAnimationFrame` or `performance.now()` drop frames under CPU load and cannot be captured deterministically. Every video scene in this skill is a **pure function of time `t` in seconds**:

\[
t_k = \frac{k}{\text{FPS}}, \quad k \in \{0, 1, 2, \dots, N\}
\]

At 60 fps, integer frame `60` equals `1.000000s` (`frameToTime(60, { numerator: 60, denominator: 1 }) === 1.0`).

### Required Window Bindings

Every deliverable HTML page must expose:

```javascript
// Pure seek hook: seeking A -> B -> A must paint the exact same pixels at A.
window.seek = window.__seekToTime = function(timeSeconds) {
  // Compute spring/keyframe tracks, camera transforms, cursor position, and visibility from timeSeconds alone.
};

// Async readiness barrier before headless screenshot capture:
window.__framesReady = async function() {
  await document.fonts.ready; // Prevents missing lazy-loaded glyphs (e.g. Vietnamese diacritics)
  await Promise.all(
    [...document.images]
      .filter((im) => im.src && im.offsetParent !== null && getComputedStyle(im).visibility === 'visible')
      .map((im) => (im.complete && im.naturalWidth ? null : im.decode().catch(() => {})))
  );
};
```

In live browser preview (when `?render=1` or `?clean=true` is absent), a `requestAnimationFrame` loop may call `window.seek((performance.now() - t0) / 1000)`. During headless capture, the RAF loop stays off and Puppeteer steps `window.seek(t)` directly.

## 2. Multi-Aspect Viewports & Safe Zones

Never letterbox a 16:9 video into 9:16 with black bars. Author scenes that adapt spatially across aspect ratios (`scripts/viewport.mjs` and `kit/tutorial-portrait-layout.js`):

| Aspect | Resolution | Target Surfaces | Safe Zone Bounds (`[left, top, right, bottom]`) | Safe-Zone Rule |
| --- | --- | --- | --- | --- |
| `16:9` (`landscape`) | `1920 × 1080` | YouTube, X, Product Hunt, Web Hero | `[96, 54, 1824, 1026]` (`1728 × 972`, 90% inner) | 5% margin on all sides |
| `9:16` (`portrait`) | `1080 × 1920` | TikTok, Reels, Shorts, Stories | `[108, 230, 972, 1574]` (`864 × 1344`, 80% × 70%) | Exclude top 12% (`y < 230`, status/search bar) and bottom 18% (`y > 1574`, platform captions, audio marquee, like/share buttons) |
| `1:1` (`square`) | `1080 × 1080` | LinkedIn, X, Instagram Feed | `[81, 81, 999, 999]` (`918 × 918`, 85% inner) | 7.5% margin on all sides |

### Automatic 16:9 → 9:16 Reflow (`kit/tutorial-portrait-layout.js`)

When using the bundled `kit/` engine, author rects on the `1920 × 1080` stage. Passing `?aspect=portrait` switches the stage to `1080 × 1920`, enlarges typography by 15–20%, and maps landscape columns into vertical slots:
- **Left column (`cx < 1100`):** maps to `TOP = [48, 150, 984, 720]`
- **Right column (`cx >= 1100`):** maps to `BOT = [48, 900, 984, 680]`
- **Full-width (`w > 1400`):** maps to `MID = [48, 400, 984, 760]`
- **Custom portrait override:** attach `p: [x, y, w, h]` (or portrait keyframes `p: [[t, x, y, w, h], ...]`) on any element spec in the timeline when a stacked layout needs custom framing.
- **Hard limit (`L3`):** In `9:16`, no settled content card may extend below `y = 1600` (where the bottom caption zone sits).

## 3. Subframe Motion Blur & 60fps FFmpeg Pipe

Sharp 60fps vector/UI renders can look brittle during fast camera punches or card entries unless shutter motion blur is applied. The bundled renderer (`kit/render-tutorial.mjs` and `scripts/export-60fps-video.mjs`) pipes JPEG screenshots directly from Puppeteer into FFmpeg over `stdin` (`image2pipe`, zero temporary disk frames):

1. **Subframe sampling (`sub = 3` or `4`):** For each output frame at 60 fps, capture `sub` subframes across the shutter interval (`t = (i + 0.5) / (fps * sub)`), then blend them in FFmpeg with `tmix=frames=4:weights='1 1 1 1',fps=60`.
2. **Broadcast encoding parameters:**
   - Video: `-c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 -movflags +faststart`
   - Audio (when voiced/music): `-c:a aac -b:a 256k -shortest`
   - Silent social upload fallback (when no audio track is used): include a silent stereo 44.1 kHz AAC track (`-f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100`) so Instagram, Facebook, and X ingesters never reject the container.
3. **Parallel shard rendering:** Because `window.seek(t)` is pure, a long video can be split into `N` shards (`node build.mjs render <project> --full --shards 3`), rendered in parallel Chrome instances, and concatenated losslessly (`-f concat -c:v copy`) via `kit/join-shards.mjs`.

## 4. Audio Grid, Sidechain Ducking, and Voiceover Rules

1. **Measure the beat grid, never guess BPM (`R5`):** Measure the music file's actual tempo and first downbeat (`db0`) with `numpy` (comb filter + downbeat phase) and record how it was measured in `grid.measuredBy` inside `tutorial.config.json`. One 4/4 bar is `240 / bpm` seconds (`bar(n) = db0 + n * (240 / bpm)`). Place chapter cuts on integer downbeats.
2. **Voice placement and clearance (`R4`):**
   - Each chapter voice clip enters at `chapter.t0 + 0.5s` (`LEAD = 0.5`).
   - Each clip must finish at least `0.3s` (`GAP = 0.3`) before `chapter.t1`. If a clip overruns, widen that chapter using integer-bar `WARP` knots in the timeline rather than speeding up the voice.
3. **Sidechain ducking and loudness normalization (`kit/voiceover/mix-voiceover.mjs`):**
   - Music bed is ducked under the voiceover bus via `sidechaincompress=threshold=0.02:ratio=8:attack=40:release=700`.
   - Combined master is normalized to broadcast social loudness via `loudnorm=I=-16:TP=-1.5:LRA=11` (`-16 LUFS`, `-1.5 dBFS` true peak).
4. **License & Git hygiene (`R2`, `R3`):**
   - Never commit raw licensed music files (`audio/`) or mixed `.wav` masters (`out/*.wav`); ensure `.gitignore` excludes them.
   - Strip `/Users/<name>` paths from every evidence excerpt and run `mogrify -strip` on rendered stills so personal machine paths never leak into screen cards or image metadata.

## 5. Post-Render Media Integrity Verification

After the final code change, re-render the MP4 and run these three checks before reporting `rendered` proof:

```bash
# 1. Decode stream to null and fail on any container/frame error
ffmpeg -v error -i "$OUTPUT_VIDEO" -f null -

# 2. Inspect stream dimensions, codec, frame count, and duration
ffprobe -v error -show_entries format=duration -show_entries stream=codec_name,codec_type,width,height,r_frame_rate,nb_frames -of json "$OUTPUT_VIDEO"

# 3. Verify integrated loudness (-16 LUFS target) when audio is present
ffmpeg -nostats -i "$OUTPUT_VIDEO" -filter_complex ebur128 -f null - 2>&1 | tail -n 15
```
