# Transitions catalogue (transitions.dev)

Use this map to brainstorm motion for ordinary product components. Each row
names a moment, the transitions.dev transition that fits it, and the rule that
decides whether it belongs on this screen. The code is not here. It lives in
the globally installed `transitions-dev` skill
(`~/.claude/skills/transitions-dev/NN-slug.md`), whose license forbids
republishing the collection in this repo. If the skill is missing, install it:
`npx skills add Jakubantalik/transitions.dev -g -s transitions-dev -s transitions-polish`.

**How to use it in a design.**

1. Name the component's state change, and say what the motion explains:
   cause and effect, continuity, progress, or result. If you cannot say what
   it explains, propose no motion.
2. Find the row below and apply its check.
3. In the option sheet, describe the feel in one plain sentence, in your own
   words.
4. In the handoff, cite the slug and file, for example "`transitions-dev`
   `05-menu-dropdown.md`, verbatim". Do not paste or retype the CSS.
   `frontend-web-engineering` installs it through the `transitions-dev`
   skill. When a row asks for tuning (a calmer toggle, no like burst), name
   it in the handoff as a divergence that goes through the tunable variables
   listed in that upstream file. Engineering changes only those variables,
   and never the keyframes.
5. For Expo, cite the same slug as the *behavior* reference. `animate-expo`
   ports it with Reanimated: blur usually drops, and hover rows have no
   equivalent.

These snippets come pre-tuned. For a catalogued component they take priority
over hand-written timings and over generic motion advice. Use `animate` for
motion the catalogue does not cover, and
[motion and gesture](motion-and-gesture.md) for gesture-driven mobile
contracts.

## Surfaces that open, close, or move

| Moment | Slug (file) | Check |
| --- | --- | --- |
| A menu grows from its trigger | menu-dropdown (`05`) | It must be anchored to its trigger; use the modal when nothing anchors it |
| A centred dialog opens and closes | modal (`06`) | Closing is softer and faster than opening; keep that asymmetry |
| A panel slides into a region of the page | panel-reveal (`07`) | Prefer card-resize when the surface only changes height |
| A container changes width or height | card-resize (`01`) | The lightest option; try it first |
| A header expands its body | accordion (`21`) | The body must hold real content, not one line |
| A hint appears over a trigger | tooltip (`17`) | Hover or focus only; a touch device needs a visible path instead |
| A transient message rises and leaves | toast (`22`) | Show one at a time unless the messages truly stack |
| Several notices stack | banner-stacking (`32`) | Use only when more than one can be alive at once |
| A round + button becomes the menu it opens | plus-menu-morph (`20`) | When the menu is a separate popover, use the dropdown |
| Two steps or list↔detail side by side | page-side-by-side (`08`) | Inside one surface; route changes follow platform navigation |
| A highlight slides between tabs or segments | tabs-sliding (`16`) | Works on touch too; set the first position without animation |

## Text and numbers that change

| Moment | Slug (file) | Check |
| --- | --- | --- |
| A number the user just changed | number-pop-in (`02`), but **build from [digit pop-in](library/signature-motion/06-digit-pop-in.md)**, which has the fixed drivers | Once per user action |
| A number the data changes often (live or polled) | number-subtle-change (`36`) | Quiet by design; never a pop-in or a count-up on a poll |
| A number change that is an event (points, a reward) | spinning-counter (`26`) | Once per event; at most one per screen |
| A label whose old and new text share letters (Copy→Copied) | text-morph (`33`) | Short labels, such as buttons and chips |
| A label whose old and new text share nothing (Processing→Done) | text-states-swap (`04`) | Short labels |
| Values re-render because the view's data changed (period, currency) | text-swap-soft (`34`) | Every changed value uses the same treatment |
| Stacked headline and support lines enter | texts-reveal (`18`) | Hero copy, empty states, onboarding; never on every list row |
| Words stream in from a model | streaming-text (`30`) | Only while real tokens arrive |
| A donut or ring chart updates | donut-chart (`35`) | The chart must answer a named question |

## Feedback on an action

| Moment | Slug (file) | Check |
| --- | --- | --- |
| Something finished (paid, uploaded, saved) | success-check (`10`) | Only when the success is real and persisted; pair it with icon-swap when a spinner precedes it |
| A form value is wrong | error-state-shake (`12`) | The message carries the meaning; the shake only points to it |
| Two icons share one slot (play/pause, copy/check) | icon-swap (`09`) | Same size slot |
| A checkbox is ticked | checkbox-check (`25`) | Keep the native semantics |
| A switch flips | toggle (`27`) | Calm the double bounce in settings-heavy or finance products |
| A like or favourite | like-button (`23`) | The particle burst is a celebration, so allow one per screen, and drop the burst under the frequency rule |
| A field is cleared | input-clear-dissolve (`13`) | Search or filter fields; dark mode needs the documented overrides |
| A new-item dot lands on an icon | notification-badge (`03`) | The count or dot must be real |

## Loading and AI work in progress

| Moment | Slug (file) | Check |
| --- | --- | --- |
| A placeholder hands over to real content | skeleton-reveal (`14`) | The skeleton matches the real layout |
| A status line says work is happening | shimmer-text (`15`) | Only while real work is pending; stop it on done or error |
| An agent moves through states (thinking→searching→writing) | thinking-states (`28`) | The states must reflect real steps |
| A reasoning transcript scrolls | reasoning-stream (`29`) | Only while the stream is real |
| A compact loader | matrix-loader (`31`) | Brand fit; prefer the platform spinner in utility screens |

## Hover and pointer (web, pointer devices only)

| Moment | Slug (file) | Check |
| --- | --- | --- |
| Hovering a row of avatars or chips | avatar-group-hover (`11`) | Touch gets nothing; that is fine |
| A card tilts toward the pointer | card-tilt (`19`) | One hero card, not a grid; skip it on touch |
| A "learn more" arrow extends | learn-more-hover (`24`) | Text links only |

## Rules that apply to every row

- **Frequency rule** (design-uiux SKILL.md): something seen 100 times a day
  gets the calm variant or nothing.
- **Honesty:** never animate a state the data does not have. That rules out
  a success check before the write lands, a shimmer after the work stops, and
  a badge with no new item.
- **One voice per screen:** use one number treatment and one celebration at
  most, and give components of the same kind the same transition.
- **Reduced motion:** every upstream snippet ships a guard, and the handoff
  says to keep it.
- Upstream Pro transitions (confetti-burst and others) need a paid plan. Do
  not propose them unless the user has one.

To check motion that already exists against the token scale, `transitions-polish`
runs a read-only `transitions review`. That output is audit evidence at the
`declared` rung. It is not proof that the motion looks right.
