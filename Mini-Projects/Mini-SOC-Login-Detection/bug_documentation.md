# Development Bug Log

This document records the logic errors and edge cases identified while developing the Mini SOC Login Detection System.

## Bugs identified during development

| ID | Issue | Impact | Resolution |
|---|---|---|---|
| BUG-01 | The login-status condition was checking for `success` while the goal was to count failed attempts. | Successful events could be counted instead of failed events. | Changed the counting condition to process only records whose status is `failed`. |
| BUG-02 | Incrementing a dictionary key before it exists can raise a `KeyError`. | The first failed event from a new IP could stop processing. | Used `failed_count.get(ip, 0) + 1` to start unseen IP counters at zero. |
| BUG-03 | Some records may not contain the required `ip` or `status` key. | Accessing a missing key can raise `KeyError`. | Added record validation and handled malformed records so processing can continue. |
| BUG-04 | A record may not be a dictionary at all. | Accessing a key on an unsuitable record can raise `TypeError`. | Checked the record type before reading its fields and skipped invalid records. |

## Additional edge cases covered by tests

| Case | Expected behaviour |
|---|---|
| Successful login | Does not increase the failed-login counter. |
| Empty event list | Returns empty count and detection results. |
| Several IPs exceed the threshold | Each qualifying IP is returned independently. |
| Custom threshold | Detection uses the threshold supplied by the caller. |
| Invalid threshold | Raises a clear `ValueError`. |
| Invalid status or IP field | Record is logged and skipped. |

## Current limitations

- Events are simulated and are not collected from a live endpoint or SIEM.
- The threshold is applied to the entire supplied list; there is no time-window calculation.
- IP validation currently checks that the value is a non-empty string. It does not verify IP address syntax.
- A threshold match is a potential brute-force indicator, not proof of malicious activity.
- The project does not correlate usernames, geolocation, threat intelligence, or successful logins after repeated failures.

## Development note

The bug table distinguishes the issues encountered while learning and debugging from additional edge cases handled in the final implementation and tests.
