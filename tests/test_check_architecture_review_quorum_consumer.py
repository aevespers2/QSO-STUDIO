from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_architecture_review_quorum_consumer import project, run


FIXTURE = Path("fixtures/architecture-review-quorum-v1.json")


class QSOStudioQuorumConsumerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.corpus = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_consumer_matches_all_committed_cases(self) -> None:
        result = run(FIXTURE)
        self.assertEqual(result["result"], "PASS")
        self.assertTrue(result["canonical_payload_matches"])

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


if __name__ == "__main__":
    unittest.main()
