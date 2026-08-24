# Testing and device proof

Use this reference to choose evidence proportionate to the mobile risk. A
passing JavaScript test does not prove native behavior, and a simulator does
not prove every physical-device or provider condition.

## Test layers

| Layer | Proves | Typical coverage |
| --- | --- | --- |
| Unit | Pure logic | Parsing, formatting, reducers, query keys, permissions |
| Component/integration | React behavior at declared boundaries | States, forms, queries, mutations, navigation callbacks |
| E2E | A real user journey in a built app | Login, deep link, primary action, recovery, back/resume |
| Native/device | Platform capability | Permissions, camera/location, notifications, secure storage, keyboard |
| Build | Artifact/config integrity | Typecheck, bundle, native config, signing/profile boundary |

Use the repository's existing test runner and selectors. Prefer observable
state and user actions over implementation-detail assertions. Keep fixtures
realistic: long content, nulls, stale responses, duplicate taps, expired
sessions, rejected permissions, slow network, and server errors.

## Minimum runtime matrix

For a core feature, record:

- iOS and Android behavior when both are supported;
- simulator/emulator and at least one physical device for native or performance
  risk when available;
- exact Expo SDK, app build/development-client profile, OS version, fixture,
  auth role, theme, locale, and network condition;
- cold launch, warm launch, background/resume, process restart, deep link,
  back navigation, permission first-run and denial, offline/retry, and account
  switch when relevant;
- push token registration/rotation, logout cleanup, notification-open links,
  and update-check behavior when those capabilities are present;
- loading, success, empty, validation error, server error, timeout, stale,
  cancellation, and recovery states.

If a device, provider, push service, database, or auth environment was not
available, mark the gate Unknown and say what remains unobserved.

## OTA/update proof

When EAS Update or `expo-updates` is present, record the exact build/runtime,
channel or branch, update ID, rollout audience, and whether the update was
accepted, rejected as incompatible, or rolled back. Test a JS-only update on
the matching runtime and separately prove that a native/config change received
a new build. Do not treat a dashboard publish event as device proof.

## Development build versus Expo Go

Use Expo Go for supported JavaScript iteration. Use a development build when
the app uses native libraries, config plugins, custom permissions, production-
like app configuration, or any behavior Expo Go does not contain. Rebuild when
native code/config changes; reload alone is insufficient evidence.

## Performance proof

For performance-sensitive work, compare the same production-like build, device,
fixture, and network before/after. Record startup/first usable screen, JS
thread work, list scroll, memory/crash observations, image/network behavior,
animation stability, and recovery after backgrounding. Do not report “fast” from
development mode, a single screenshot, or an unmeasured memoization change.

## Handoff evidence

Report implementation, automated, simulator/emulator, physical-device,
development-build, EAS-build, and provider evidence separately. Include exact
commands and results, screenshots/recordings where useful, known limitations,
and the next gate. Store-submission metadata and review readiness belong to the
separate store audit skill.

## Official references

- [Expo development builds](https://docs.expo.dev/develop/development-builds/introduction/)
- [EAS Build](https://docs.expo.dev/build)
- [Expo environment variables](https://docs.expo.dev/guides/environment-variables/)
