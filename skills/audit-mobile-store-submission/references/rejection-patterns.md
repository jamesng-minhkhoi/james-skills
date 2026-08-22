# Common rejection patterns

This is a practical signal library, not a replacement for current platform
policy. Official policy wins. Forum reports show how failures are often
encountered or phrased, but they are anecdotal and may be incomplete.

## Contents

- [Apple patterns](#apple-patterns)
- [Apple rejection/remediation signals](#apple-rejectionremediation-signals)
- [Google Play patterns](#google-play-patterns)
- [Cross-platform patterns](#cross-platform-patterns)
- [Forum evidence](#forum-evidence)

## Apple patterns

### 2.1 App Completeness / Information Needed

Common triggers:

- crash, freeze, blank route, dead button, broken deep link, or backend that is
  off during review;
- incomplete onboarding, placeholder copy, empty website, missing support or
  privacy URL;
- login, OTP, geo-gate, membership, hardware, or review-only setup is not
  explained or cannot be accessed;
- demo account is expired, lacks data, cannot reach important features, or
  requires the reviewer to invent test conditions;
- IAP/subscription products are not attached, visible, loadable, restorable,
  or testable in the submitted version;
- the app works in a developer or TestFlight setup but not in the review
  environment.

Audit the full reviewer path, not only the public happy path. Include a
reviewer note and a resettable account when access is needed.

### 2.3 Accurate Metadata

Check that name, subtitle, description, screenshots, previews, privacy details,
age rating, category, claims, and available features match the exact binary.
Remove hidden, dormant, undocumented, or unshipped functionality. Do not use
screenshots that show an internal build, fake data that implies unavailable
features, or claims that cannot be demonstrated quickly.

### 4.2 Minimum Functionality / Web Wrapper

Flag apps that are primarily a thin website, link collection, PDF/text viewer,
static shell, or generic AI wrapper with little app-specific value. Check for
native usefulness, meaningful interaction, reliable content, offline/empty
behavior, and a clear reason the app belongs on the platform.

### 4.3 Spam / Copycat / Low Differentiation

Flag:

- multiple bundle IDs that are the same app with minor branding or location
  changes;
- repackaged white-label templates, common source/assets, or similar metadata;
- a saturated category where the app has no visible, meaningful improvement;
- a listing whose first screenshots look indistinguishable from competing apps;
- a low-effort app that adds little value even if it technically functions.

Do not claim that a framework, AI use, or common UI library alone causes spam.
Document the observable binary, metadata, concept, content, and differentiation
evidence.

### 4.8 Login Services / 5.1 Privacy

Check equivalent Sign in with Apple where required, account deletion, consent
before data sharing, specific permission strings, third-party SDK disclosure,
third-party AI data flows, privacy policy coverage, ATT behavior, and retention
or deletion behavior. A privacy policy URL alone does not cure an undisclosed
in-app data flow.

### 3.1 Payments and business model

Identify whether a transaction is for digital goods/services, physical goods,
or an outside-the-app service. Verify the applicable Apple payment path,
subscription state, restore, cancellation, pricing copy, and review access.
When the business model is not obvious, explain it in metadata and review notes.

## Apple rejection/remediation signals

### 5.1.1 Permission pre-alerts that coach the user

An app can be rejected even when it uses the standard native permission prompt
if its custom screen appears to direct the user’s choice. Flag a pre-alert that:

- uses **Allow**, **Enable**, or equivalent as the app’s own CTA immediately
  before the system prompt;
- draws or imitates the system dialog, highlights Allow/Don’t Allow, adds an
  arrow, or tells the user which answer to select;
- frames a decline as a failure when the core product remains usable; or
- re-prompts after denial without a meaningful new context.

Require a neutral **Continue** or **Next** CTA, an honest feature explanation,
an unobstructed native prompt, and tested Maybe-later/denied/Settings paths.
The wording and visuals must be inspected on the exact build, not inferred from
the permission API call alone.

### 2.1 App Review Information requests

For a new app, Apple may request a complete review packet rather than only a
login. Prepare a physical-device recording starting at launch, tested device
and OS list, purpose and audience, setup and credentials, core external
services, regional behavior, and regulated/protected-content authorization.
Record the build and device used for every attachment. A simulator capture,
generic explanation, or source-level claim is insufficient evidence.

### 2.3.8 Marketplace versus installed name

Compare the App Store name with the signed name users see on the Home Screen,
Settings, and app switcher. Inspect `CFBundleDisplayName`, `CFBundleName`, Expo
or native overrides, and the installed binary. A stable bundle ID does not
resolve a confusing display-name mismatch. Repeat the check after every
resubmission because a metadata edit and a binary edit can drift independently.

### Resubmission evidence drift

Treat a rejection for build 47 and a resubmission with build 49 as separate
review snapshots. Preserve the original reviewer device/date and map each
requested fix to the new build, physical-device recording, screenshots, and
App Review Information notes. Do not claim that an attached recording proves a
fix unless its version/build and capture device are recorded.

## Google Play patterns

### Broken Functionality

Check install, first launch, loading, responsiveness, scrolling, buttons,
blank pages, back navigation, network failures, crashes, ANRs, and reviewer
device differences. Treat “works on my device” as low-confidence until the
exact artifact and a representative clean install are tested.

### Limited Functionality and Content

Flag static shells, single-purpose pages with no meaningful app behavior,
minimal content, generic wrappers, apps that do nothing, and repeated
template-generated apps. Assess the value and completeness of the whole
journey, not the number of screens.

### Misleading metadata / listing mismatch

Compare description, screenshots, title, claims, ads label, pricing, content
ratings, audience, and feature availability to the binary. Remove promises that
require unavailable backend, regions, accounts, hardware, or future features.

### User Data / Data Safety / Account Deletion

Reconcile app and SDK collection/sharing with the Data Safety form, privacy
policy, in-app disclosure, permission requests, data deletion answers, and
actual deletion behavior. If users can create accounts, verify both an in-app
deletion path and a web deletion resource.

### Login credentials and restricted access

Provide active credentials and every required step: username/password, OTP or
QR instructions, MFA exception, location or membership setup, reset behavior,
and test data. Credentials must work in the review environment and expose the
features promised in the listing.

### Permissions and sensitive APIs

Check whether the permission is necessary for core functionality, whether a
minimum-scope picker exists, whether a declaration is required, and whether the
privacy/listing explanation matches. Pay special attention to photos/videos,
contacts, location, SMS/call log, foreground services, and full-screen intents.

### Payments, testing, and account status

Verify Google Play Billing for digital goods unless a documented exception or
regional program applies. For new personal developer accounts, check the closed
test and production-access requirement. Also check developer identity,
package registration, policy warnings, and prior rejection/suspension history.

### Review-packet and evidence failures

If Play asks for access or additional information, use the same evidence
discipline as Apple: active credentials, every MFA/QR/location step, device and
OS coverage, external services, regional behavior, and exact artifact/build.
Do not substitute an internal-test result for a production-track observation.

## Cross-platform patterns

- Public privacy/support/account-deletion links are dead, generic, blocked,
  non-HTTPS, or describe another app.
- Store forms are filled from assumptions instead of an SDK/data/permission
  inventory.
- The review account cannot reach the first-value moment, or the app cannot
  recover after the reviewer backgrounds it.
- Version/build metadata, screenshots, backend environment, or feature flags do
  not describe the uploaded artifact.
- Health, financial, safety, AI, or privacy claims are stronger than the
  product evidence and supporting documentation.
- Repeatedly resubmitting without isolating the failure creates new review
  uncertainty and can escalate enforcement.

## Forum evidence

Use these discussions to recognize patterns and prepare diagnostic questions:

- [Apple 4.3(a) forum thread](https://developer.apple.com/forums/thread/825522)
  describes source/assets reuse, repackaged templates, and multiple similar
  submissions as factors discussed by Apple staff.
- [Apple 5.1.1/5.1.2 third-party AI thread](https://developer.apple.com/forums/thread/815842)
  shows a recent privacy rejection pattern where the app did not disclose what
  data was sent to which AI service and obtain permission.
- [Apple IAP review thread](https://developer.apple.com/forums/thread/828568)
  illustrates products working in Sandbox/TestFlight but failing to load for
  App Review.
- [Apple developer report of repeated rejections](https://www.reddit.com/r/iOSProgramming/comments/1s0nb97/got_rejected_by_the_app_store_5_times_before/)
  reports a combination of 4.3(b), 2.1, and privacy-string issues. Treat this
  as a case study, not a probability estimate.
- [Google broken-functionality discussion](https://support.google.com/googleplay/android-developer/thread/335168223/app-rejected-due-to-broken-functionality-but-everything-works-fine?hl=en)
  shows why review-environment, loading, and device-specific evidence matter.
- [Google broken-functionality checklist](https://support.google.com/googleplay/android-developer/thread/309771939/tips-and-best-practices-to-help-you-comply-with-broken-functionality-policy-requirements?hl=en)
  emphasizes install, launch, responsiveness, button outcomes, and feature
  behavior.
- [Google limited-functionality case](https://support.google.com/googleplay/android-developer/thread/356692753/looking-for-help-getting-my-app-approved?hl=en)
  shows a repeated-rejection path where a story app was judged to have too few
  screens or functions.
- [Google login-credentials guidance](https://support.google.com/googleplay/android-developer/thread/317411637/tips-and-best-practices-for-complying-with-login-credentials-requirements?hl=en)
  covers active accounts, QR codes, MFA, and other access resources.
- [Google 12-testers community guide](https://support.google.com/googleplay/android-developer/community-guide/255621488/everything-about-the-12-testers-requirement?hl=en)
  documents common confusion around the continuous closed-test requirement.
