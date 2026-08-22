# Current platform watch

Policy and portal requirements change. This snapshot was researched on
2026-08-23. Re-open the linked official pages during every Release audit and
record the date checked. Do not treat a date here as a substitute for the live
portal or policy page.

## Contents

- [Apple current watch](#apple-current-watch)
- [Google Play current watch](#google-play-current-watch)
- [How to use this watch](#how-to-use-this-watch)

## Apple current watch

| Item | Current signal | Audit action |
| --- | --- | --- |
| Upload toolchain | Apple says that from April 28, 2026, App Store Connect uploads need the iOS/iPadOS 26 SDK or later and points developers to Xcode 26 | Verify the exact Xcode/SDK and uploaded artifact, not only local config |
| Age ratings | Apple updated age ratings for newer OS releases and requires honest questionnaire answers | Reconcile questionnaire, content, social features, and listing rating |
| Social media descriptor | Starting July 2026, the age questionnaire includes social media capabilities; starting September 2026, the answer is required for submissions/updates | If feeds, likes, comments, shares, or UGC amplification exist, verify the new field and age implications |
| Accessibility metadata | Apple is introducing App Store accessibility information such as VoiceOver, Voice Control, Larger Text, and Captions support | Make claims only after testing the named support; do not confuse metadata with accessibility compliance |
| App Store improvements | Apple says apps not updated for three years with extremely low rolling-12-month downloads may be contacted, with 90 days to update; launch crashes can be removed immediately | For existing apps, include maintenance, latest-OS, and launch-stability review |
| Spam/low differentiation | Current 4.3 language explicitly addresses indistinguishable apps, saturated categories, low-effort categories, and repeated submissions | Audit concept, binary, metadata, assets, and visible differentiation before submission |

Primary sources:

- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Submitting](https://developer.apple.com/app-store/submitting/)
- [What’s New](https://developer.apple.com/app-store/whats-new/)
- [App Store Improvements](https://developer.apple.com/support/app-store-improvements/)
- [App Review Information](https://developer.apple.com/help/app-store-connect/reference/platform-version-information/)
- [Export compliance](https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance)

## Google Play current watch

| Item | Current signal | Audit action |
| --- | --- | --- |
| Target API | From August 31, 2026, new apps and updates must target Android 16/API 36 or higher; existing apps need API 35+ to remain available to new users on newer Android | Inspect `targetSdkVersion`, artifact manifest, device coverage, and exception/form-factor scope |
| 16 KB page sizes | Apps targeting Android 15/API 35+ must support 16 KB page sizes; from February 1, 2027, unsupported updates cannot be released | Check native libraries, Expo/EAS build support, and a 16 KB test path where applicable |
| Developer verification | Verification and package registration are rolling out; package registration is required by September 30, 2026, with initial device protections in Brazil, Indonesia, Singapore, and Thailand and broader rollout planned | Check identity verification, package registration, and Play Console warnings; separate this from app policy approval |
| New personal accounts | Personal developer accounts created after November 13, 2023 need at least 12 testers continuously opted in for 14 days before production access | Verify account creation date, closed-test evidence, tester continuity, and production-access status |
| Photo/video permissions | Broad `READ_MEDIA_IMAGES`/`READ_MEDIA_VIDEO` access requires core functionality; the Photo Picker is the minimum-scope alternative, with full compliance required since May 28, 2025 | Inspect manifest, picker path, declaration, and denied-permission experience |
| Contacts permission | For Android 17/API 37+ apps, `READ_CONTACTS` requires a declaration and justification that Contact Picker is insufficient; compliance is scheduled for January 2027 | If relevant, document core use case and prepare the declaration before the deadline |
| Policy deadlines | The live deadline table includes location, anonymous/random chat, Families, SMS/call-log, foreground-service, and account-transfer changes | Re-check the live table for category- and region-specific items rather than copying a generic checklist |

Primary sources:

- [Target API requirements](https://developer.android.com/google/play/requirements/target-sdk)
- [16 KB page sizes](https://developer.android.com/guide/practices/page-sizes)
- [Android developer verification](https://support.google.com/android-developer-console/answer/16561738)
- [Registering Play package names](https://support.google.com/googleplay/android-developer/answer/16984799)
- [New personal-account testing](https://support.google.com/googleplay/android-developer/answer/14151465)
- [Data Safety](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Prepare app for review](https://support.google.com/googleplay/android-developer/answer/9859455)
- [Policy deadlines](https://support.google.com/googleplay/android-developer/table/12921780)
- [Restricted permissions](https://support.google.com/googleplay/android-developer/answer/16935362)

## How to use this watch

1. Record the current date and the live page checked.
2. Mark each item **Applicable**, **Not applicable**, or **Unknown** with
   evidence. Do not turn a future date into a present blocker without checking
   the app’s target, account, region, track, and platform.
3. Add deadlines to the release plan with an owner and buffer.
4. When a live page conflicts with this snapshot, follow the live official page,
   preserve the observed discrepancy in the report, and update this reference
   in a separate maintenance change.
