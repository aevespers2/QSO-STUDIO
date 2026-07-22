from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_architecture_review_quorum_consumer import project, run, run_extension

BASE_FIXTURE = Path("fixtures/architecture-review-quorum-v1.json")
EXTENSION_FIXTURE = Path("fixtures/architecture-review-quorum-extension-v1.json")


class QSOStudioQuorumConsumerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.corpus = json.loads(BASE_FIXTURE.read_text(encoding="utf-8"))
        cls.extension = json.loads(EXTENSION_FIXTURE.read_text(encoding="utf-8"))

    def test_consumer_matches_all_committed_cases(self) -> None:
        result = run(BASE_FIXTURE)
        self.assertEqual(result["result"], "PASS")
        self.assertTrue(result["canonical_payload_matches"])

    def test_extension_matches_all_committed_cases(self) -> None:
        result = run_extension(EXTENSION_FIXTURE)
        self.assertEqual(result["result"], "PASS")
        self.assertTrue(result["canonical_payload_matches"])
        self.assertEqual(result["case_count"], 9)

    def test_incompatible_self_review_is_rejected(self) -> None:
        case = copy.deepcopy(self.corpus["cases"][0])
        case["reviewers"][0]["roles"] = ["author", "architecture"]
        observed = project(case, self.corpus["policy"])
        self.assertEqual(observed["state"], "REVIEW_INCOMPLETE")
        self.assertIn("SELF_REVIEW", observed["reason_codes"])

    def test_independence_requires_distinct_groups(self) -> None:
        case = copy.deepcopy(self.corpus["cases"][0])
        for reviewer in case["reviewers"]:
            reviewer["independence_group"] = "one-controller"
        observed = project(case, self.corpus["policy"])
        self.assertIn("INDEPENDENCE_VIOLATION", observed["reason_codes"])

    def test_appeal_is_non_self_executing(self) -> None:
        case = copy.deepcopy(self.corpus["cases"][0])
        case["appeal_status"] = "PENDING"
        observed = project(case, self.corpus["policy"])
        self.assertEqual(observed["state"], "APPEAL_REVIEW_PENDING")
        self.assertEqual(observed["authority_effect"], "none")

    def test_fixture_expectation_tampering_is_detected(self) -> None:
        corpus = copy.deepcopy(self.corpus)
        corpus["cases"][0]["expected"]["authority_effect"] = "activate"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tampered.json"
            path.write_text(json.dumps(corpus), encoding="utf-8")
            result = run(path)
            self.assertEqual(result["result"], "FAIL")
            self.assertFalse(result["canonical_payload_matches"])

    def test_duplicate_keys_fail_closed(self) -> None:
        text = EXTENSION_FIXTURE.read_text(encoding="utf-8")
        text = text.replace('"profile_version": "1.0.0",', '"profile_version": "1.0.0",\n  "profile_version": "1.0.0",', 1)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate key"):
                run_extension(path)

    def test_non_finite_numbers_fail_closed(self) -> None:
        text = EXTENSION_FIXTURE.read_text(encoding="utf-8").replace('"base_case_count": 12', '"base_case_count": NaN', 1)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "non-finite"):
                run_extension(path)

    def test_extension_unknown_field_fails_closed(self) -> None:
        corpus = copy.deepcopy(self.extension)
        corpus["cases"][0]["unexpected"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unknown.json"
            path.write_text(json.dumps(corpus), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unknown"):
                run_extension(path)

    def test_extension_reason_drift_is_detected(self) -> None:
        corpus = copy.deepcopy(self.extension)
        corpus["cases"][1]["expected"]["reasons"] = []
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "drift.json"
            path.write_text(json.dumps(corpus), encoding="utf-8")
            result = run_extension(path)
            self.assertEqual(result["result"], "FAIL")
            self.assertFalse(result["canonical_payload_matches"])


if __name__ == "__main__":
    unittest.main()
