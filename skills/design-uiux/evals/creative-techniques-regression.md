# Creative techniques regression cases

Prompts and expected decisions for the creative-reference library
(`references/creative-catalog.md` and `references/library/`). Use when revising
the catalog's routing, the honesty gate, or the module topic rules.

## Case C1: 3D hero request must pass the honesty gate

Prompt: "Our fintech landing page needs a signature moment. Add a 3D animated
hero scene — products, particles, something people remember on scroll."

Expected behavior:

- open the creative catalog first, then three-canvas and scroll-story modules
  only as needed;
- state the moment's job in one sentence before proposing any technique;
- present at least one honest 2D alternative (motion-only hero or pre-rendered
  video) as a distinct option beside the 3D option, with the bundle cost
  declared as an `unverified` estimate (a measured chunk size is impossible
  before a build exists and is not demanded at option time);
- define the quiet frame (the un-animated camera/lighting still defined in the
  three-canvas module), the reduced-motion variant, and the no-WebGL fallback
  for any 3D option;
- name the single primary driver (scroll) and designed keyframes rather than
  coupled ambient effects.

Must not have: a single 3D-heavy proposal with no 2D twin; claims about bundle
size presented as measured; a 3D option whose fallback is a blank canvas.

## Case C2: Shader look must be keyed to brand and story

Prompt: "Make the analytics dashboard's empty states cooler — a nice shader
gradient like the ones on that French studio site."

Expected behavior:

- route through the creative catalog to shader-recipes and state the gradient's
  metaphor (or report that none exists and propose the static token gradient);
- map gradient colors to the project's brand tokens, never hand-picked hex;
- name the transparency/banding designed fix (dithering) if the ramp is
  low-contrast;
- keep per-fragment cost in view (a daily-touched dashboard panel differs from
  a landing hero: the frequency gate from motion-and-gesture decides).

Must not have: "aurora blob" decoration with no stated job; noise speed fast
enough to swallow the copy; a shader where a CSS gradient is the honest answer
and the CSS option is not also presented.

## Case C3: Mobile reality over desktop pin

Prompt: "Steal Webflow's scroll-pinned storytelling for our Expo onboarding."

Expected behavior:

- call out the desktop technique falling back on touch (pin degraded to native
  scroll rhythm or step cards; `PagerView`/`scroll-snap` cited as the
  platform-grade equivalent);
- present the step-card sequence as a real option, not an apology; the 390
  column on the sheet is a designed option, not a scaled screenshot;
- named reduction: reduced-motion variant is a designed still, not the default
  layout left unanimated;
- note any device-permission-dependent technique (gyro parallax) as its own
  trade-off with the permission prompt cost, or skip it.

Must not have: build-level wiring (Reanimated implementation code in the
handoff plan); the motion spec presented as worklet code rather than behavior
contract; pin/scroll-jack behavior that intercepts swipe; per-glyph split
animation on Android; a claim that the ideas in the sheet are the only
possible reference (research step still applies).

## Case C4: Creative request must not bypass project truth

Prompt: "Make our app feel creative and avant-garde everywhere."

Expected behavior:

- reuse the established signature palette/tokens/type first; derive new
  techniques within the existing system;
- route to the creative catalog as an options conversation, not a one-sided
  code dump — the option sheet carries the job, cost, reduced-motion variant,
  and quiet frame per technique;
- mark any invented data (particle counts claiming revenue, testimonial motion)
  as placeholder or bind it to real fixtures;
- hand the plan to frontend-*-engineering and keep this skill out of product
  code.

Must not have: an advanced request downgraded to a basic card-fade-and-stagger
answer without naming why; a shader/GLSL snippet copied verbatim into product
code by this skill; tokens or copy invented to make the mockup work.

## Case C5: Non-creative request must not open the catalog

Prompt: "Redesign our settings page empty state to feel calmer and more
consistent."

Expected behavior:

- route to web principles/patterns and the slop-and-consistency sweep only;
- the creative catalog is not opened and no technique proposal is made;
- static design is preserved unless evidence justifies a scoped change.

Must not have: a signature-moment option sheet or an animated-hero proposal
for a settings empty state.

## Case C6: High-frequency placement rejects the marketing technique

Prompt: "Add a rippling shader glow under every row of our checkout list — our
users hit it dozens of times a day."

Expected behavior:

- the motion-and-gesture frequency table decides: dozens per day lands in the
  near-imperceptible or platform-default rows, so the ripple is rejected with
  the verdict cited, not silently ignored;
- any acceptable alternative (a static emphasis state, a sub-150 ms press
  response) is proposed within the gate;
- the frequency carve-out for rare moments is named as not applicable because
  the placement is daily-use product flow.

Must not have: shipping the shader as decoration with the gate skipped, or a
claim that landing-page latitude covers a checkout list.

## Case C7: Signature hero on a home screen resolves the ordering

Prompt: "Add an animated signature hero to our app's home screen."

Expected behavior:

- the creative feature bullet owns the request: options with named techniques
  appear at the option stage, not after a static lock;
- the motion bullet's "after static lock" clause is not cited as a reason to
  stall — that clause covers motion polish on an already-designed screen;
- the hero option carries the mechanism contract per the motion rules and the
  reduced-motion/static variant per the creative catalog.

Must not have: waiting for sign-off on a static design before proposing any
technique, or proposing motion with no static twin at all.

## Case C8: 3D option without an existing route build

Prompt: "Design a scroll-driven 3D product hero. The project isn't on a
canvas-capable shape yet — there's nothing to measure."

Expected behavior:

- estimate is declared `unverified` on the option sheet; the design does not
  block the sheet or fabricate a measured KB figure;
- the handoff plan names the measurement as an engineering gate (real
  `next build` chunk size for the route) alongside the SSR/never-block rules;
- the honesty gate's 2D twin and fallback-design duties still appear.

Must not have: a fabricated measured number, a 3D option with no cost line
at all, or a skipped 2D twin without the concrete constraint that defeats one
named on the sheet.

## Case C9: Behavior spec, not implementation, in the handoff

Prompt: (from C2/C3 context) after picking an onboarding scroll story option,
"write the implementation plan."

Expected behavior:

- motion spec is behavior-level: names the Reanimated behaviors, drivers,
  durations, and named degradations per screen, and cites the module topics;
- no worklet code, dependency installation steps, or build wiring appear in
  the plan — implementation belongs to frontend-mobile-engineering;
- open questions and `NOT_RUN`/`UNKNOWN` items are marked rather than glossed.
