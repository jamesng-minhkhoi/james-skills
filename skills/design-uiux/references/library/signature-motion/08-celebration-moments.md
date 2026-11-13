# Celebration moments (confetti, party poppers, milestone alerts)

How to celebrate in a product without it reading as cheap: when a moment
earns confetti at all, which of three treatments it gets, and the values that
make the pieces feel physical. The rules are cross-product. The worked example
is Petio (2026-11): a pet's birthday, gotcha day and days-together counts.

**Status.** Approved at the Petio review on 2026-11-12: the whole ladder
below, not a single option. A, B and C each own a tier; the new-member,
first-of-a-task and purchase rows came from that review. Turn any later
rejection into a rule here.

**Who does what.** design-uiux decides whether a moment celebrates and which
tier it gets, and names this file in the handoff (→ "Values"). `animate` (web)
or `animate-expo` (Expo) owns the feel. `frontend-*-engineering` owns the
trigger, the once-a-day claim, the layer and accessibility.

## 1. Earn it first (gates, in order)

1. **It's real and it's saved.** Celebrate a date the product already holds,
   or an event the server confirmed. Never an optimistic write, a step in a
   form, or "you opened the app".
2. **It belongs to someone.** The moment names its subject (the pet, the
   person, the project) and the fact ("Mochi turns 3 today"). A generic
   "Congrats!" has no subject and fails this gate.
3. **It's rare.** Use the frequency ladder below. Something that happens daily
   gets a calm check or a toast, never confetti.
4. **It fires once.** Claim it per subject, per day, on the device; a
   session-only guard is the fallback. Revisiting the screen, restarting the
   app or pulling to refresh never replays it.
5. **It isn't grief.** Never celebrate a subject marked as passed away,
   archived or deleted, or a date stored with partial precision (month or year
   only), or a "birthday" whose age works out to 0 or below.

## 2. The ladder: tier → treatment

| Tier | Examples | Treatment |
| --- | --- | --- |
| Yearly | Birthday, adoption ("gotcha") day, account anniversary | **B · milestone card** on the first open that day. Afterwards the subject's own screen wears a marker (a ribbon) and gets **A** on the first visit |
| Rare count | Day 100, 500, 1000; 10th, 100th record | **C · mascot or voice announces it**, with a small popper |
| A new member | A pet added (every pet: each one's first day happens once), joining someone's family, someone joining yours | **A · burst from the newcomer** where it lands (its card, the ceremony's hero), with the existing toast or ceremony. No takeover: the user is mid-flow |
| A first of a task | The first document, first reminder, first scan | **Small popper (about 10) + one toast** naming the subject, the first time only. The second one is routine |
| A purchase | Subscription started, a code redeemed | **Calm welcome, no pieces:** the paywall's own hero object settles in (never a tick in a ring or disc), plain-type title, what just unlocked in the paywall's feature card, then back to where the paywall interrupted. No gradient text, no blurred blob backdrop. Paying is a decision, not a party, but it must not just vanish |
| Weekly or routine | Weekly quest done, a save, a scan, a reminder done | Calm check or toast only (see the transitions catalogue `success-check`) |
| Never | Memorial or remembrance dates, deleting things, errors recovered | Nothing celebratory. A quiet, respectful line at most |

**Pieces fly only for a subject:** a pet, a person, a relationship. Never for
money, paperwork volume or a daily chore. A first gets its moment; the tenth
of the same thing does not.

Only one celebration per open. When two land on the same day, the higher tier
wins and the other waits for its own screen.

## 3. The three treatments

**A · Burst from the subject (party popper).** Pieces shoot up from behind
the subject's avatar and fall away. The avatar's plate gives one small squeeze
(about 0.94×, then back on a bouncy spring); the subject's marker text comes
into focus ([text focus-in](07-text-focus-in.md)). Nothing covers the page and
scrolling stays live. Best for celebrating on the subject's own screen.

**B · Milestone card (alert).** A dim scrim (about 38%) fades in, and a card
rises 40 pt into place, 0.94× → 1, on a smooth spring with no overshoot. It
holds a date stamp, the subject's avatar, one headline that focuses in, one
line of fact, **one** primary action that keeps the moment (save as a memory,
share), and a quiet "Not now". Pieces fall **behind** the card, so the words
stay readable. Tapping outside closes it too, and it never comes back that
day. It's the only treatment that interrupts, so it's limited to yearly tiers.

**C · Mascot announces it.** The mascot plays its existing celebrate reaction
(one hop), a small popper of about 10 pieces goes off from it, and the
bubble grows from its tail with the line focusing in. Tapping the bubble goes
to the subject. The least intrusive and the easiest to miss: right for rare
counts, too small for a birthday. The mascot's own colour never changes. Only
the pieces are colourful.

## 4. The pieces

- **Made of the brand.** Mix about a third brand silhouettes (Petio: the four
  pet-mask shapes) with soft ribbons (5 × 12–16 pt, radius 2). Colours come
  from the brand's existing palette (Petio: `CONFETTI_COLORS`). Never use emoji,
  generic rainbow squares, stars or a stock Lottie.
- **Physical, not floaty.**
  - **Burst (A):** about 22 pieces, launched −155° to −25°, 420–720 pt/s, with
    exponential drag (k ≈ 2.4) and gravity (≈ 540 pt/s² effective). Spin up to
    ±540°/s. Each lives 1.2–1.4 s and fades over the last 40%. All launch
    within 60 ms of each other: one pop, not a stream.
  - **Fall (B):** about 30 pieces start above the top edge, staggered over
    700 ms. They fall at 230–370 pt/s with a 12–30 pt sway, last 2.6 s and
    fade over the last 30%.
  - **Small popper (C):** about 10 pieces at 260–440 pt/s; each lives 1.2 s.
- **Count caps:** 30 on phones. More reads as noise and costs frames.

## 5. Layering and platform rules

- The pieces are **their own layer** over the screen, ignore touches and are
  removed when done. They never wrap the content, so a masked avatar, blur or
  glass underneath is never under their transforms. (On iOS a transformed
  parent flattens a native blur.)
- Draw more than about 15 pieces in one canvas (Skia, or a single
  Reanimated-driven layer), not one native view each.
- **One haptic:** a single *success* haptic at the moment it lands, never one
  per piece.
- **Reduce Motion:** no pieces, no rise, no squeeze. The card or line fades in
  and the focus-in stays (it doesn't move anything). The news must still
  arrive. Never gate the message on the animation.
- **Accessibility:** announce the line once (an accessibility live region or
  announcement). The pieces are hidden from assistive tech.
- **Never block.** The celebration never delays navigation or a save. A card
  can always be closed at once.

## 6. Copy

Use the subject and the fact, in the product's voice: "Mochi turns 3 today",
"1 year home", "Day 100 with Mochi". Avoid exclamation stacks, "Congrats!!",
and invented stats ("you're in the top 5% of pet parents"). New lines go
through `content-design`.

## Values (handoff block)

```
celebration:
  tier: yearly | rare | member | first | purchase | routine | never
  treatment: A burst | B card | C mascot | small popper + toast | calm welcome | check | none
  claim: per subject per local day, device storage, session fallback
  pieces: {count, mix: silhouettes 1/3 + ribbons, palette token}
  physics: see §4 for the treatment
  haptic: success x1 at land
  reduceMotion: no pieces/rise/squeeze; fade + focus-in only
  a11y: announce line once; pieces hidden
  exclusions: memorial, archived, partial-precision dates, age < 1
```

## Failure modes seen

- A purchase welcome built from a tick in a rainbow ring, rainbow gradient
  text and a blurred gradient backdrop was called "AI slop" (Petio,
  2026-11-12). Its own sticker on plain black, with white type, read clean.

- Confetti on every visit to the subject's screen, which wore out by the third
  visit. Claim per day (gate 4).
- Confetti drawn inside the screen's view tree, wrapping a masked avatar or
  glass: the blur went flat. Use its own layer (§5).
- A card with two buttons and a share sheet competing. One action plus
  "Not now" (§3 B).
