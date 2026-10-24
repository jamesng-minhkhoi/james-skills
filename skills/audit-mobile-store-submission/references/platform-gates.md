# Platform gates

Stable Apple and Google checks. Pair with [current platform watch](current-platform-watch.md) for deadlines and new requirements.

Use the current official policies and the platform watch reference. At minimum,
check:

### Apple

- App Completeness: crashes, blank/placeholder content, broken links, missing
  review information, unavailable backend, incomplete IAP, and unreproducible
  login or purchase flows;
- accurate metadata and age rating; no hidden/dormant functionality or mismatch
  between listing and binary, including marketplace name versus installed
  display name under Guideline 2.3.8;
- minimum functionality, web wrapper/content aggregator, copycat, spam,
  repackaged template, or saturated-category risk;
- privacy, account deletion, permissions, tracking, third-party AI disclosure,
  privacy manifest, Sign in with Apple, and export compliance;
- in-app purchase rules, reader/physical-goods distinctions, subscriptions,
  restore/cancel flows, and review visibility;
- current SDK, launch screen, accessibility metadata, supported platforms,
  device behavior, and any regional legal or content requirements.

### Google Play

- stable install, launch, responsiveness, no blank pages, broken controls,
  ANRs, crashes, and meaningful functionality/content;
- accurate store listing, screenshots, ads declaration, content rating,
  target audience, privacy policy, and reviewer access;
- Data Safety and account deletion accuracy, including SDKs and web deletion
  path;
- high-risk/sensitive permissions, minimum-scope alternatives, photo/video,
  contacts, location, SMS/call-log, foreground service, and full-screen intent
  declarations when applicable;
- target API, 16 KB page-size compatibility, device/form-factor support,
  Play Billing or permitted regional alternatives, and test-track requirements;
- developer identity, package registration, account status, repeated-rejection
  risk, and production-access requirements.
