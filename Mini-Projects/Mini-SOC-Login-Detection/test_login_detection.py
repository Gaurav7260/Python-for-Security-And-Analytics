"""Unit tests for the Mini SOC Login Detection System."""

import unittest

from login_detection import count_failed_attempts, identify_suspicious_ips


class TestLoginDetection(unittest.TestCase):

    def test_five_failed_attempts_are_flagged(self):
        logs = [
            {"ip": "10.0.0.1", "status": "failed"}
            for _ in range(5)
        ]

        counts = count_failed_attempts(logs)
        suspicious = identify_suspicious_ips(counts)

        self.assertEqual(counts, {"10.0.0.1": 5})
        self.assertEqual(suspicious, {"10.0.0.1": 5})

    def test_two_failed_attempts_are_not_flagged(self):
        logs = [
            {"ip": "10.0.0.2", "status": "failed"},
            {"ip": "10.0.0.2", "status": "failed"},
        ]

        counts = count_failed_attempts(logs)
        suspicious = identify_suspicious_ips(counts)

        self.assertEqual(counts, {"10.0.0.2": 2})
        self.assertEqual(suspicious, {})

    def test_successful_logins_are_not_counted(self):
        logs = [
            {"ip": "10.0.0.3", "status": "success"},
            {"ip": "10.0.0.3", "status": "success"},
        ]

        self.assertEqual(count_failed_attempts(logs), {})

    def test_malformed_records_are_skipped(self):
        logs = [
            {"ip": "10.0.0.4", "status": "failed"},
            {"status": "failed"},
            "invalid_record",
            {"ip": "10.0.0.5", "status": "unknown"},
            {"ip": 123, "status": "failed"},
        ]

        self.assertEqual(
            count_failed_attempts(logs),
            {"10.0.0.4": 1},
        )

    def test_empty_dataset_returns_empty_results(self):
        counts = count_failed_attempts([])
        suspicious = identify_suspicious_ips(counts)

        self.assertEqual(counts, {})
        self.assertEqual(suspicious, {})

    def test_multiple_suspicious_ips_are_detected(self):
        logs = (
            [{"ip": "10.0.0.6", "status": "failed"} for _ in range(5)]
            + [{"ip": "10.0.0.7", "status": "failed"} for _ in range(6)]
        )

        counts = count_failed_attempts(logs)
        suspicious = identify_suspicious_ips(counts)

        self.assertEqual(
            suspicious,
            {"10.0.0.6": 5, "10.0.0.7": 6},
        )

    def test_custom_threshold_is_respected(self):
        counts = {"10.0.0.8": 3, "10.0.0.9": 2}

        suspicious = identify_suspicious_ips(counts, threshold=3)

        self.assertEqual(suspicious, {"10.0.0.8": 3})

    def test_invalid_threshold_is_rejected(self):
        with self.assertRaises(ValueError):
            identify_suspicious_ips({"10.0.0.1": 5}, threshold=0)


if __name__ == "__main__":
    unittest.main()
