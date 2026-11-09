# Digit pop-in (a number the user just changed)

The reference feel for a value that changes on screen because of what the user
did. Source:
[transitions.dev · Number pop-in](https://transitions.dev/detail.html?t=number-pop-in).
When a request says "animate the number", "make the total feel alive", or
"the price/score/balance updates", this is the default proposal.

**Who does what.** design-uiux describes the feel in the option sheet and
cites this file and section in the handoff (`06-digit-pop-in.md` → "Build").
It never pastes the code into product files and never retypes the keyframes
into a plan. `frontend-web-engineering` copies the CSS and one driver from this
file exactly. For Expo, `animate-expo` builds the motion described under
"Mobile", and `frontend-mobile-engineering` keeps the data and state plumbing
(as in ROUTING.md). The keyframes are the same as `transitions-dev`'s
`02-number-pop-in.md`. This file adds `tabular-nums` and declares the tokens
on the group. Use the drivers here, never upstream's: they fix the ghost digit,
the snap on a shrinking value, and the first-render animation (see "Build: the
diff rule").

## What it looks like (say this in the option sheet)

When `65.78` becomes `65.91`:

1. `65.` does not move. Leading characters that both values share, and every
   separator (`.` `,` `$` `%` space), stay still.
2. Every digit from the first change onward leaves upward. The old `7` and
   `8` rise about half a line, shrink toward 70%, blur, and fade out in 155 ms.
3. The new digit starts 50 ms after its old digit. It rises from below at 70%
   scale, blurred, and reaches full opacity about 180 ms later.
4. It goes a little too far. It lifts slightly above the baseline and grows to
   about 103%, then pulls back and settles at 100%. That overshoot is what
   makes it feel like a spring and not a fade.
5. The digits trail each other. The last two characters start 40 ms and 80 ms
   after the rest, so the change ripples left to right into the last digit.
6. The whole thing ends at about 730 ms: 600 ms of motion, a 50 ms entry
   delay, and up to 80 ms of stagger. Then the number is plain text again.

Motion job, in one sentence: *this value just changed because of what you did,
and here is the part that changed.* That is cause and effect, not decoration.

## Which number motion (decide by who changes it, then by how often)

| Situation | Use |
| --- | --- |
| The user's action changes the value once: cart total after a quantity change, a price on a monthly/yearly toggle, a balance after a transfer, a stat after a filter change | **Digit pop-in** (this file) |
| The data changes the value, not the user: a live price, a polled dashboard tile, a ticker | `transitions-dev` **number-subtle-change** (`36-number-subtle-change.md`): a quiet in-place cross-fade that drifts up or down with the direction. Never a pop-in, and never a count-up from 0 on each poll |
| The value updates several times a second (upload percent, a stopwatch) | No motion. Swap the text |
| The change is an event the user should celebrate: points earned, a reward, a milestone | `transitions-dev` **spinning-counter** (`26-spinning-counter.md`), once per event |
| A number appears for the first time and its size is the story (a landing metric) | Count-up from a meaningful origin in [numbers and counters](03-numbers-and-counters.md) |
| A short label changes (`Copy` to `Copied`, `Pending` to `Paid`) | `transitions-dev` **text-morph** (`33-text-morph.md`) when the labels share letters at the start or end, or **text-states-swap** (`04-text-states-swap.md`) when they share nothing. Do not use this file for words |
| Reduced motion is on | The final value renders immediately, with no swap and no old digit |

The frequency rule in design-uiux SKILL.md still wins. A value the user
changes 100 times a day (a quantity stepper in a POS, say) gets the calm tuning
below, or no motion.

It is honest by construction. It only ever shows the real old value and the
real new value, never invented in-between numbers, so the
[truthfulness contract](03-numbers-and-counters.md#the-truthfulness-contract)
holds without extra work. Pass it the **formatted** string from the project's
formatter (`1,299.00`, `$4.99`, `38k`), never a raw number.

## Brainstorm checklist (run this before proposing)

For each value on the screen, answer these in the option sheet:

1. Does the user's action change this value on this screen? If not, use the
   table above. It is not a pop-in.
2. How often does the user see it change? Once per action is right.
   Constantly (100+ times a day) means the calm tuning, or nothing.
3. Which characters usually change? Usually the last digits. If the whole
   string changes every time, the stagger still works, but say so.
4. Does a second value change because of the same action (subtotal and
   total)? Give both the same pop-in and timing, or animate only the one the
   eye should land on. Simultaneously visible values never get two different
   number motions. A value may count up when it first appears and pop in on
   later changes. That is one value, at two different moments.
5. Where does the eye go next? The swap holds attention for about 0.7 s. Next
   to the button the user presses next is fine: a total above Checkout
   confirms the change, and then the eye moves on. Do not place it beside an
   error or a message the user must read at that moment.

## Build: CSS (engineering copies exactly)

The `--digit-*` values are the reference tuning. The site declares them
elsewhere; here they are declared on the group so the snippet works when
pasted. Distances are in `em` and the blur is a curve on the font size, so the
same values fit a 12 px label and a 72 px hero number.

```css
/* Number pop-in. Transition from transitions.dev (https://transitions.dev). */
.t-digit-group {
  --digit-dur: 600ms;            /* anticipation + spring */
  --digit-exit-dur: 155ms;
  --digit-enter-delay: 50ms;     /* new digit starts after the old one leaves */
  --digit-stagger: 40ms;         /* per data-stagger step */
  --digit-distance: 0.52em;
  --digit-exit-distance: 0.52em;
  --digit-blur: max(0.067em, 0.171em - 2.1px); /* 0.8px at 12px, 2px at 24px, 10.2px at 72px */
  --digit-lift: 0.125em;         /* how far it overshoots above the baseline */
  --digit-start-scale: 0.7;
  --digit-peak: 1.03;            /* overshoot scale */
  display: inline-flex;
  align-items: baseline;
  font-variant-numeric: tabular-nums; /* required: stops width jitter */
}
.t-digit-slot { position: relative; display: inline-block; }
.t-digit-old { position: absolute; inset: 0; text-align: center; pointer-events: none; }
.t-digit { display: inline-block; will-change: transform, opacity, filter; }
.t-digit-group.is-animating .t-digit {
  animation: t-digit-in var(--digit-dur) linear both;
  animation-delay: calc(var(--digit-stagger) * var(--digit-i, 0) + var(--digit-enter-delay));
}
.t-digit-group.is-animating .t-digit-old {
  animation: t-digit-out var(--digit-exit-dur) linear both;
  animation-delay: calc(var(--digit-stagger) * var(--digit-i, 0));
}
.t-digit-group.is-animating [data-stagger="1"] { --digit-i: 1; }
.t-digit-group.is-animating [data-stagger="2"] { --digit-i: 2; }
/* Digits that did not change (the leading ones the old and new number
   share) stay still; only the digits that changed swap. */
.t-digit-group.is-animating .t-digit[data-same] { animation: none; }

@keyframes t-digit-in {
  0% { transform: translateY(calc(var(--digit-distance) * 1 + var(--digit-lift) * 0)) scale(var(--digit-start-scale)); opacity: 0; filter: blur(calc(var(--digit-blur) * 1)); }
  5% { transform: translateY(calc(var(--digit-distance) * 0.941 + var(--digit-lift) * 0.216)) scale(var(--digit-start-scale)); opacity: 0.059; filter: blur(calc(var(--digit-blur) * 1)); }
  10% { transform: translateY(calc(var(--digit-distance) * 0.755 + var(--digit-lift) * 0.648)) scale(var(--digit-start-scale)); opacity: 0.245; filter: blur(calc(var(--digit-blur) * 1)); }
  15% { transform: translateY(calc(var(--digit-distance) * 0.475 + var(--digit-lift) * 0.972)) scale(var(--digit-start-scale)); opacity: 0.525; filter: blur(calc(var(--digit-blur) * 1)); }
  20% { transform: translateY(calc(var(--digit-distance) * 0.206 + var(--digit-lift) * 0.792)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.792)); opacity: 0.794; filter: blur(calc(var(--digit-blur) * 0.9)); }
  25% { transform: translateY(calc(var(--digit-distance) * 0.041 + var(--digit-lift) * 0.392)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.392)); opacity: 0.959; filter: blur(calc(var(--digit-blur) * 0.75)); }
  30% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0.033)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.033)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.6)); }
  35% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * -0.194)) scale(calc(1 + (var(--digit-peak) - 1) * 0.711)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.45)); }
  40% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * -0.272)) scale(calc(1 + (var(--digit-peak) - 1) * 0.997)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.3)); }
  45% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * -0.238)) scale(calc(1 + (var(--digit-peak) - 1) * 0.87)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.15)); }
  50% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * -0.146)) scale(calc(1 + (var(--digit-peak) - 1) * 0.535)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  55% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * -0.05)) scale(calc(1 + (var(--digit-peak) - 1) * 0.183)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  60% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0.019)) scale(calc(1 + (var(--digit-peak) - 1) * -0.069)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  65% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0.05)) scale(calc(1 + (var(--digit-peak) - 1) * -0.185)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  70% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0.051)) scale(calc(1 + (var(--digit-peak) - 1) * -0.187)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  75% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0.035)) scale(calc(1 + (var(--digit-peak) - 1) * -0.128)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  80% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0.016)) scale(calc(1 + (var(--digit-peak) - 1) * -0.057)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  85% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0.002)) scale(calc(1 + (var(--digit-peak) - 1) * -0.007)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  90% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * -0.004)) scale(calc(1 + (var(--digit-peak) - 1) * 0.013)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  95% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * -0.003)) scale(calc(1 + (var(--digit-peak) - 1) * 0.011)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  100% { transform: translateY(calc(var(--digit-distance) * 0 + var(--digit-lift) * 0)) scale(1); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
}
@keyframes t-digit-out {
  0% { transform: translateY(calc(var(--digit-exit-distance) * 0)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0)); }
  10% { transform: translateY(calc(var(--digit-exit-distance) * -0.009)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.009)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.009)); }
  20% { transform: translateY(calc(var(--digit-exit-distance) * -0.042)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.042)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.042)); }
  30% { transform: translateY(calc(var(--digit-exit-distance) * -0.112)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.112)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.112)); }
  40% { transform: translateY(calc(var(--digit-exit-distance) * -0.252)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.252)); opacity: 1; filter: blur(calc(var(--digit-blur) * 0.252)); }
  50% { transform: translateY(calc(var(--digit-exit-distance) * -0.5)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.5)); opacity: 0.833; filter: blur(calc(var(--digit-blur) * 0.5)); }
  60% { transform: translateY(calc(var(--digit-exit-distance) * -0.748)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.748)); opacity: 0.42; filter: blur(calc(var(--digit-blur) * 0.748)); }
  70% { transform: translateY(calc(var(--digit-exit-distance) * -0.888)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.888)); opacity: 0.187; filter: blur(calc(var(--digit-blur) * 0.888)); }
  80% { transform: translateY(calc(var(--digit-exit-distance) * -0.958)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.958)); opacity: 0.069; filter: blur(calc(var(--digit-blur) * 0.958)); }
  90% { transform: translateY(calc(var(--digit-exit-distance) * -0.991)) scale(calc(1 + (var(--digit-start-scale) - 1) * 0.991)); opacity: 0.015; filter: blur(calc(var(--digit-blur) * 0.991)); }
  100% { transform: translateY(calc(var(--digit-exit-distance) * -1)) scale(calc(1 + (var(--digit-start-scale) - 1) * 1)); opacity: 0; filter: blur(calc(var(--digit-blur) * 1)); }
}

@media (prefers-reduced-motion: reduce) {
  .t-digit-group .t-digit { animation: none !important; }
  .t-digit-group .t-digit-old { display: none; }
}
```

Rules that the snippet depends on:

- `tabular-nums` is required. Without it the old digit and the new digit have
  different widths, and the row jitters while they cross. On Android, and with
  custom fonts, check that the font actually has tabular figures.
- Never put `overflow: hidden` on the slot, the group, or a close ancestor such
  as a table cell or a card. The exit travels about half a line up, and the blur
  spreads past the glyph, so clipping cuts both off. If a container must clip,
  give the number `padding-block: 0.3em` inside it.
- Engineering adds an `.sr-only` utility if the project lacks one:
  `position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;`

## Build: the diff rule (what moves)

Compare the old and new formatted strings:

- Characters before the first difference (from the left) get `data-same` and
  stay still.
- From the first difference onward, every **digit** gets a slot holding the new
  digit (`t-digit`). It also gets an old digit (`t-digit-old`) when one lines up
  from the right *and* that old character was not already part of the still
  prefix.
- If the new value is the old one with characters cut off the end (`$120` to
  `$12`), the prefix rule would leave nothing to animate. So the last digit
  swaps in place over its own old copy, and the cut-off characters disappear
  at once. Pairing from the right here would flash `$10`, a value that was
  never true.
- Non-digits (`.` `,` `$` `%` `k` and spaces) never animate.
- The second-to-last character gets `data-stagger="1"`, and the last gets
  `data-stagger="2"`. With a suffix (`38k`, `12%`) the stagger lands on the
  suffix, which is a non-digit and does not move, so only the earlier digit
  trails. That is fine.

Worked examples:

| Old → new | Still | Swaps | Note |
| --- | --- | --- | --- |
| `65.78` → `65.91` | `65.` | `9` (over `7`), `1` (over `8`) | Same length |
| `1,299` → `1,305` | `1,` | `3`, `0`, `5` | |
| `$12` → `$120` | `$12` | `0` enters with no old digit | The upstream driver draws a ghost `2` here. The `same` guard fixes it |
| `$120` → `$12` | `$1` | `2` swaps over the old `2`; the `0` disappears at once | Without the shrink guard nothing moves and the toggle snaps; pairing from the right would flash `$10` |
| `9.99` → `10.49` | nothing | `1` enters; `0` swaps over `9`; `4` and `9` swap | Pairs from the right |
| `10.49` → `9.99` | nothing | `9`, `9`, `9` swap | The old leading `1` disappears at once, with no exit. This is an accepted limitation, because the eye is on the changed digits |

The upstream vanilla driver also animates the whole value on first render.
Upstream ships no product React driver; the one below is ours, and it
survives unrelated re-renders.

## Build: React driver (engineering copies)

`value` is the formatted string. The `key` remounts the group on each change,
which replays the animation. The previous value lives in state using React's
"store information from previous renders" pattern, so an unrelated re-render
during the 730 ms does not cut the animation short. The first render shows the
value plainly.

```tsx
"use client";
import { useState } from "react";

// Number pop-in. Transition from transitions.dev (https://transitions.dev).
export function DigitPopIn({ value, live = false }: { value: string; live?: boolean }) {
  const [pair, setPair] = useState({ value, from: value });
  if (pair.value !== value) setPair({ value, from: pair.value });
  const from = pair.value !== value ? pair.value : pair.from;

  let same = 0;
  while (same < from.length && same < value.length && from[same] === value[same]) same++;
  // New value is a prefix of the old one ($120 → $12): swap the last digit in place.
  const shrink = from !== value && same >= value.length;
  if (shrink) same = Math.max(0, value.search(/\d(?=\D*$)/));

  return (
    <span>
      <span className="sr-only" aria-live={live ? "polite" : undefined}>{value}</span>
      <span
        key={value}
        aria-hidden="true"
        className={"t-digit-group" + (from !== value ? " is-animating" : "")}
      >
        {value.split("").map((ch, i) => {
          if (i < same || !/\d/.test(ch)) {
            return <span key={i} className="t-digit" data-same="">{ch}</span>;
          }
          const fromEnd = value.length - 1 - i;
          const j = shrink ? i : from.length - (value.length - i); // old index
          const old = j >= same ? from[j] : undefined;
          return (
            <span
              key={i}
              className="t-digit-slot"
              data-stagger={fromEnd === 1 ? "1" : fromEnd === 0 ? "2" : undefined}
            >
              {old && /\d/.test(old) && <span className="t-digit-old">{old}</span>}
              <span className="t-digit">{ch}</span>
            </span>
          );
        })}
      </span>
    </span>
  );
}
```

Use it as `<DigitPopIn value={formatCurrency(total)} />`. Pass `live` (which
adds `aria-live="polite"` to the `.sr-only` span) only when someone who is not
looking needs to hear the change, such as a cart total. Never pass it for a
value that updates on its own.

## Build: vanilla driver (engineering copies; no framework)

```js
// Number pop-in. Transition from transitions.dev (https://transitions.dev).
// el is a <span class="t-digit-group" aria-hidden="true">; next is a formatted string.
// The first call renders plainly; later calls animate the change.
export function setDigits(el, next) {
  const prev = el.getAttribute("data-value");
  el.setAttribute("data-value", next);
  el.classList.remove("is-animating");
  if (prev === null || prev === next) { el.textContent = next; return; }
  let same = 0;
  while (same < prev.length && same < next.length && prev[same] === next[same]) same++;
  // New value is a prefix of the old one ($120 → $12): swap the last digit in place.
  const shrink = same >= next.length;
  if (shrink) same = Math.max(0, next.search(/\d(?=\D*$)/));
  el.textContent = "";
  next.split("").forEach((ch, i) => {
    const fresh = document.createElement("span");
    fresh.className = "t-digit";
    fresh.textContent = ch;
    if (i < same || ch < "0" || ch > "9") {
      fresh.setAttribute("data-same", "");
      el.appendChild(fresh);
      return;
    }
    const slot = document.createElement("span");
    slot.className = "t-digit-slot";
    const fromEnd = next.length - 1 - i;
    if (fromEnd <= 1) slot.setAttribute("data-stagger", fromEnd === 1 ? "1" : "2");
    const j = shrink ? i : prev.length - (next.length - i); // old index
    const oldCh = j >= same ? prev[j] : undefined;
    if (oldCh !== undefined && oldCh >= "0" && oldCh <= "9") {
      const old = document.createElement("span");
      old.className = "t-digit-old";
      old.textContent = oldCh;
      slot.appendChild(old);
    }
    slot.appendChild(fresh);
    el.appendChild(slot);
  });
  void el.offsetHeight; // force a reflow so re-adding the class replays
  el.classList.add("is-animating");
}
```

Keep a sibling `.sr-only` span that holds the same `next` string for screen
readers.

## Tuning (each change is a named divergence from the reference)

| Want | Change | Leave alone |
| --- | --- | --- |
| Calmer (finance, settings, medical, high-frequency) | `--digit-peak: 1; --digit-lift: 0` removes the overshoot | The rise, blur, and stagger |
| Dense table cell | `--digit-distance: 0.3em; --digit-exit-distance: 0.3em` | Duration |
| Bigger hero number | Nothing. The em and blur values already scale | Everything |

Never edit the keyframe percentages, and never swap `linear` for an easing.
The spring is already baked into the stops, so adding an easing applies the
curve twice.

## Mobile (Expo) equivalent

design-uiux specifies the behavior. `animate-expo` builds the motion,
`frontend-mobile-engineering` keeps the data and state plumbing, and no
Reanimated code goes into the design plan.

- Port it as a Reanimated `Keyframe` entering/exiting pair with the same
  percentage stops, keyed on the value so each change remounts the digit.
  Use `translateY`, `scale`, and `opacity` only.
- Splitting per digit is allowed here, because only the changed digits of one
  number split (usually 1 to 4 views). This is the one written exception to
  the "no per-glyph split on device" rule in
  [mobile equivalents](05-mobile-reanimated.md), which still applies to words
  and headlines.
- Drop the blur. React Native core has no CSS-style blur on text. Name this
  substitution in the option sheet. An audit does not mark the port down for
  missing blur.
- Convert the em distances to px: `0.52 × fontSize` and `0.125 × fontSize`.
- Use `fontVariant: ['tabular-nums']`.
- Honor the OS Reduce Motion setting with a plain text swap.
- The target proof rung is `device`. A simulator recording reaches
  `interactive` at most.

## Proof: what correct frames look like

Who and when: before the option is shown a second time, the designer may prove
the feel on a scratch page built only from this file. That proof is
`rendered`. Engineering repeats the check in the product before claiming
`interactive`. A canvas board alone is `declared`.

Change `65.78` to `65.91` and capture frames at 0, 100, 250, 450, and 730 ms.
To get exact frames, pause every animation and set its time:
`document.getAnimations().forEach(a => { a.pause(); a.currentTime = T; })`.
A live recording drops frames. Expect the frames below. They were captured
on 2026-11-09 from a scratch page built only from this file's code blocks, in
headless Chrome. The screenshots are not stored, so treat this as `inferred`
until you reproduce them with the method above, which takes about a minute:

- `65.` is in the same place in every frame.
- At 100 ms, the old `7` has lifted and is starting to blur, but it is still
  solid. The new `9` is a faint smudge below the baseline. The old `8` has
  barely moved, because of the stagger.
- At 250 ms, the `9` is close to its place but still soft. The `1` is lower and
  more blurred.
- At 450 ms, everything reads as settled. The overshoot is subtle (3%, about
  1.5 px on a 40 px number), so you feel it in motion more than you see it in
  a still.
- At 730 ms, the value is sharp. When the length did not change, the group is
  the same width as before.
- `$12` → `$120`: no second `2` appears. Only the `0` enters.
- `$120` → `$12`: the `2` lifts out and rises back in, and no frame reads
  `$10`. The value does not snap.
- Three changes within 300 ms each restart cleanly, with no stuck old digit.
- With reduced motion on, the final value appears at once.
- A screen reader reads the full value once, not digit by digit.

## Failure modes (the audit checks these)

- A value the user changed snaps with no transition.
- A count-up shows made-up in-between values for what was a discrete change.
- Every character animates, including the unchanged prefix and the separators.
- A ghost old digit appears when the length changes (`$12` → `$120`), or a
  shrinking value snaps (`$120` → `$12`).
- The row width jitters during the swap because `tabular-nums` is missing.
- The exit or blur is clipped by an `overflow: hidden` container.
- A pop-in or count-up fires on polling or live ticks, where
  number-subtle-change or nothing belongs.
- There is no reduced-motion path, or the screen reader hears split digits.
- Two different number motions run on values that are visible at the same
  time.

---
Transition from [transitions.dev](https://transitions.dev) by Jakub Antalik,
used under the Transitions.dev License: free to use and modify in products,
not to be redistributed as a transitions library. See
[NOTICE.md](../../../../../NOTICE.md). The driver fixes (the ghost-digit
guard, the shrinking-value swap, plain first render, and re-render safety) are
our adaptations.
