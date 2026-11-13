# Text focus-in (a line that is spoken or announced)

The reference feel for one short line arriving on screen as a single, sleek
motion: a mascot's speech bubble, an assistant's first line, an onboarding
caption, a success line. The whole line comes into focus at once, from soft
and blurred to sharp. It does not slide, and its words don't arrive one by one.

**Why this is the default.** It was chosen over two alternatives in a Petio
onboarding review (2026-11). Showing each word on its own beat (60 ms apart,
opacity only) was rejected as "not clean": each word popping in separately reads
choppy and gimmicky. A soft left-to-right wipe and a plain fade that follows the
bubble were the other options. The user's standing preference is
**modern, sleek, clean motion: one movement per element, never a stutter of
small ones.**

**Who does what.** design-uiux names this file in the option sheet and the
handoff (`07-text-focus-in.md` → "Values"). `animate` (web) or `animate-expo`
(Expo) owns the feel. `frontend-*-engineering` owns the text source, fonts,
fitting and accessibility.

## What it looks like (say this in the option sheet)

1. The container arrives first. A bubble grows out of its tail toward the
   speaker (about 86% → 100%, a smooth spring, no overshoot) while it fades in.
   The container is a surface, so it may move.
2. The line starts 60 ms later, as one block: blurred (8 px) and transparent.
3. Over 420 ms on an ease-out curve, the blur goes to 0 and the opacity to 1
   together. The text stays where it is.
4. It's done in about 0.5 s. Then the line is plain, sharp text again.

Motion job, in one sentence: *someone just said this.* That is personality and
continuity, not decoration.

## Values

| Token | Value |
| --- | --- |
| Text blur from | 8 px → 0 |
| Text opacity | 0 → 1, on the same curve as the blur |
| Text duration | 420 ms |
| Text delay after the container starts | 60 ms |
| Text easing | ease-out, `cubic-bezier(0.22, 1, 0.36, 1)` |
| Container grow | about 0.86 → 1 from the tail or anchor, smooth spring (damping ratio 1, ~450 ms) |
| Exit | a quiet fade, about 180 ms, ease-in-out. No blur on the way out |

## When to use it, and when not

| Situation | Use |
| --- | --- |
| One short line that is "said": a mascot bubble, an assistant greeting, a caption, a result line | **Text focus-in** (this file) |
| Several stacked lines entering a hero or an empty state | `transitions-dev` texts-reveal (`18`), or [kinetic hero](01-kinetic-hero.md) |
| A short label changing in place (Copy → Copied) | text-morph (`33`) or text-states-swap (`04`) |
| A number changing | [digit pop-in](06-digit-pop-in.md) |
| Body copy, list rows, anything read often | No focus-in. Fade, or nothing |
| Reduce Motion is on | Keep the blur and the fade, which don't move anything. Drop the container grow. The line still arrives in one piece |

Never stagger the words of a line that should read as one thought. If the
text has to feel as if it's being spoken, slow the focus down (up to about
520 ms). Don't split it.

## Build notes

- **Web.** `filter: blur()` and `opacity` on the text element, transitioned
  together. Pad any `overflow: hidden` ancestor so the blur halo isn't clipped.
- **Expo / React Native.** iOS can't blur a native `Text`: RN's `filter: blur`
  is Android-only, and a `BlurView` over the text frosts the background too.
  Draw the line in Skia instead: a `Paragraph` inside a `Group` whose `layer`
  paint holds a `<Blur mode="decal">`, with blur and opacity driven by one
  shared progress value. Then:
  - Load the fonts once per process and cache them, so a remount doesn't
    flash the fallback text.
  - Fit the text yourself, because Skia has no `adjustsFontSizeToFit`. Step
    the size down to the floor and ellipsize after that.
  - Scale by the system font scale.
  - Pad the canvas by about 3× the blur so the halo isn't clipped.
  - Give the wrapper an `accessibilityLabel` with the text, since a canvas is
    silent to screen readers.
  - Keep a plain `Text` fallback for the frame before the fonts load.
- Keep the same renderer for the line after it settles. Swapping from Skia to
  native text at the end shifts the glyphs by a pixel and reads as a jump.

## Failure modes

- Each word arrives on its own beat: choppy. This is the rejected version.
- The text slides or rises as it focuses. That breaks the rule that text only
  changes in place; only surfaces move.
- The blur halo is clipped into a hard box.
- The text is blurred again on exit, making two effects for one step back.
- The line is handed from a blurred layer to a sharp one, and the swap lands
  before the focus finishes, so the last frames cut.
- It runs on every list row or every repeated message. Use it only for lines
  that are said once.

---

Our own pattern, from the Petio onboarding motion review. Timings sit on the
transitions.dev motion-token scale (Jakub Antalik); no snippet is copied from
that library.
