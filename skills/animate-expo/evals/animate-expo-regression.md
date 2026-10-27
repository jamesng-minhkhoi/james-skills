# Animate Expo regression cases

Use these forward-test fixtures when changing the `animate-expo` skill. They
are review prompts with expected gates, not executable tests.

## Case 1: gesture sheet

Prompt: "Add a drag-to-dismiss sheet to my Expo app."

Expected behavior:

- use Reanimated shared values + `Gesture` + `useAnimatedStyle`, running on
  the UI thread;
- no `setState` per frame; `scheduleOnRN` / JS-thread work only at commit
  time;
- use a spring with a damping-ratio config, not a hardcoded duration;
- apply momentum-based dismissal (velocity check, not just a distance
  threshold);
- say the feel must be judged on a release build on device — dev builds and
  the simulator cannot prove gesture quality.

## Must not have

A completion claim fails if it contains any of these:

- an Animated/Reanimated value driven through React state per frame;
- a gesture handler fighting the scroll view or edge-back gesture with no
  ownership note;
- "smooth" claimed from a simulator or debug build;
- haptics used as the only threshold-crossing signal.
