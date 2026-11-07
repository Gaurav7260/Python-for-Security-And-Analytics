# Mini SOC Login Detection System

A beginner-friendly Python project that analyzes **simulated authentication events**, counts failed login attempts by source IP, and flags IPs that meet a configurable threshold.

This project demonstrates Python fundamentals used in small SOC automation tasks: lists, dictionaries, loops, functions, validation, exception handling, logging, and automated unit testing.

## Features

- Processes a list of simulated login-event dictionaries.
- Counts failed login attempts separately for each IP address.
- Ignores successful logins when calculating failed-attempt counts.
- Skips malformed records and logs a warning.
- Flags IP addresses with five or more failed attempts by default.
- Supports a custom detection threshold.
- Includes automated tests using Python's built-in `unittest` framework.

## Project structure

```text
Mini-SOC-Login-Detection/
├── README.md
├── login_detection.py
├── test_login_detection.py
└── bug_documentation.md
```

## Requirements

- Python 3.8 or later
- No third-party packages required

## Run the detection program

Open a terminal in this project directory and run:

```bash
python login_detection.py
```

The demonstration uses simulated events embedded in the script. It prints failed-login counts and the IP addresses that meet the detection threshold.

## Run the unit tests

Run:

```bash
python -m unittest -v
```

The test suite covers:
1. Five failed attempts are flagged.
2. Two failed attempts are not flagged.
3. Successful logins are not counted as failures.
4. Malformed records are skipped.
5. An empty dataset returns empty results.
6. Multiple suspicious IPs are detected.
7. A custom threshold is respected.
8. An invalid threshold is rejected.

## Detection logic

The default threshold is five failed attempts per IP address in the supplied dataset.

This is a simple demonstration rule. It does not use a time window, correlate usernames, or establish that an IP is malicious. A real SOC investigation should consider additional context such as event timestamps, targeted accounts, source reputation, successful logins after failures, and other telemetry.

## Data and safety note

All events in this project are simulated. Do not add private, personal, or sensitive production authentication logs to a public repository.

The IP addresses are documentation-style example addresses used for demonstration, not indicators of real attacks.

## Learning outcomes

- Iterate through structured event data.
- Read values from dictionaries.
- Maintain counters with `dict.get()`.
- Validate records and handle malformed input.
- Separate data processing from detection logic.
- Use Python logging to report processing activity.
- Write repeatable tests with `unittest` and assertions.
- Document bugs, fixes, assumptions, and limitations.
