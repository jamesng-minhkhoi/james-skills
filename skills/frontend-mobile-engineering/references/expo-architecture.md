# Expo architecture and native boundaries

Use this reference before changing project structure, navigation, dependencies,
or native configuration.

## Reconnaissance checklist

Read the exact Expo version from `package.json` and inspect:

- `app.json` or `app.config.{js,ts}`;
- `eas.json`, `ios/`, `android/`, config plugins, and native permissions;
- `app/` or `src/app/` route tree, layouts, groups, dynamic routes, and links;
- `src/screens`, `src/components`, hooks, services, stores, API clients, and
  tests;
- `tsconfig`, Metro, Babel, lint, test, and build scripts.

Classify the project as managed/CNG, prebuild, or bare. Existing structure is
the source of truth. Do not delete native directories, move routes, or migrate
navigation merely to match a preferred template.

## Preferred new-project shape

For a genuinely new Expo Router app, keep routes separate from implementation:

```text
src/
  app/          # routes and layouts only
  screens/      # screen bodies and private screen composition
  components/   # reusable components
  hooks/        # reusable hooks
  services/     # API/native integrations
  stores/       # shared client state, if needed
  utils/        # pure helpers and colocated tests
assets/
app.config.ts
eas.json
package.json
```

Use platform files (`.ios`, `.android`, `.native`, `.web`) when the
implementation genuinely differs. Keep compatible props and a default file.

## Dependencies and native changes

- Use `npx expo install` for Expo-compatible packages so versions match the
  SDK; inspect the package's native requirements first.
- Prefer an Expo module/config plugin before hand-editing native projects.
- Rebuild the development client after adding native code, a config plugin,
  permissions, URL schemes, or native app configuration.
- Use Expo Go only for work supported by its fixed native runtime. Use a custom
  development build for production-oriented projects or native libraries.
- Keep app config deterministic per environment. Do not put secrets in
  `EXPO_PUBLIC_*` values or any bundle-visible configuration.

## Navigation rules

For Expo Router:

- routes belong in `app`/`src/app`; route files should remain thin;
- `_layout.tsx` owns stack/tab/modal configuration;
- preserve route params, deep links, back behavior, and notification links;
- use SDK-pinned Expo Router guidance; SDK 56+ projects must not import
  external `@react-navigation/*` packages directly in application code;
- regenerate `.expo/types/router.d.ts` or the repository's equivalent after
  route additions before typechecking when typed routes are enabled.

## Official references

- [Expo overview and skill routing](https://docs.expo.dev/)
- [Expo Router SDK 56 reference](https://docs.expo.dev/versions/v56.0.0/sdk/router/)
- [Expo app configuration](https://docs.expo.dev/workflow/configuration/)
- [Development builds](https://docs.expo.dev/develop/development-builds/introduction/)
- [EAS Build](https://docs.expo.dev/build)
