"""
Mini SOC Login Detection System

Processes simulated authentication events, counts failed login attempts
by source IP, and flags IPs that meet a configurable threshold.

Dataset: simulated examples only.
"""

import logging


logger = logging.getLogger(__name__)

DEFAULT_THRESHOLD = 5


def count_failed_attempts(logs):
    """Count failed login events by IP, skipping malformed records."""
    if not isinstance(logs, list):
        raise TypeError("logs must be provided as a list")

    failed_count = {}

    for index, log in enumerate(logs, start=1):
        try:
            if not isinstance(log, dict):
                raise TypeError("record must be a dictionary")

            ip = log["ip"]
            status = log["status"]

            if not isinstance(ip, str) or not ip.strip():
                raise ValueError("IP address must be a non-empty string")

            if status not in ("failed", "success"):
                raise ValueError("status must be 'failed' or 'success'")

            if status == "failed":
                failed_count[ip] = failed_count.get(ip, 0) + 1

        except (KeyError, TypeError, ValueError) as error:
            logger.warning(
                "Skipping malformed record at position %s: %r (%s)",
                index,
                log,
                error,
            )
            continue

    logger.info("Processed %s login records", len(logs))
    return failed_count


def identify_suspicious_ips(failed_count, threshold=DEFAULT_THRESHOLD):
    """Return IPs whose failed-login count meets the threshold."""
    if not isinstance(threshold, int) or isinstance(threshold, bool) or threshold < 1:
        raise ValueError("threshold must be a positive integer")

    suspicious_ips = {}

    for ip, attempts in failed_count.items():
        if attempts >= threshold:
            suspicious_ips[ip] = attempts
            logger.warning(
                "Potential brute-force indicator: %s has %s failed attempts",
                ip,
                attempts,
            )

    return suspicious_ips


def main():
    """Run the demonstration against simulated login events."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    simulated_logs = [
        {"ip": "10.0.0.1", "status": "failed"},
        {"ip": "10.0.0.1", "status": "failed"},
        {"ip": "10.0.0.2", "status": "success"},
        {"ip": "10.0.0.1", "status": "failed"},
        {"ip": "10.0.0.1", "status": "failed"},
        {"ip": "10.0.0.1", "status": "failed"},
        {"ip": "10.0.0.3", "status": "failed"},
        {"ip": "10.0.0.3", "status": "failed"},
        {"ip": "10.0.0.4", "status": "failed"},
        {"status": "failed"},
        "invalid_record",
    ]

    failed_counts = count_failed_attempts(simulated_logs)
    suspicious_ips = identify_suspicious_ips(failed_counts)

    print("\nFailed login counts:")
    print(failed_counts)

    print("\nPotentially suspicious IP addresses:")
    print(suspicious_ips)


if __name__ == "__main__":
    main()
