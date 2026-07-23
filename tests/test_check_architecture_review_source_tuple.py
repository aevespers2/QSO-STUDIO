from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts import check_architecture_review_source_tuple as source_tuple

ROOT = Path(__file__).resolve().parents[1]
SOURCE_TUPLE = ROOT / "fixtures" / "architecture-review-producer-source-v1.json"


def load_value() -> dict[str, object]:
    return json.loads(SOURCE_TUPLE.read_text(encoding="utf-8"))


def write_value(directory: str, value: object) -> Path:
    path = Path(directory) / SOURCE_TUPLE.name
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    return path


class ArchitectureReviewSourceTupleTests(unittest.TestCase):
    def test_committed_source_tuple_passes_without_authority(self) -> None:
        result = source_tuple.run(SOURCE_TUPLE)
        self.assertEqual(result["result"], "PASS")
        self.assertEqual(result["resolved_head"], source_tuple.EXPECTED_RESOLVED_HEAD)
        self.assertEqual(result["artifact_names"], ["base", "extension"])
        self.assertEqual(result["authority_effect"], "none")

    def test_stale_resolved_head_is_rejected(self) -> None:
        value = load_value()
        value["producer"]["resolved_head"] = source_tuple.EXPECTED_PREVIOUS_HEAD
        value["producer"]["observed_pr_head"] = source_tuple.EXPECTED_PREVIOUS_HEAD
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "stale producer head"):
                source_tuple.run(write_value(tmp, value))

    def test_moved_observed_head_is_rejected(self) -> None:
        value = load_value()
        value["producer"]["observed_pr_head"] = "0" * 40
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "producer head moved"):
                source_tuple.run(write_value(tmp, value))

    def test_wrong_producer_path_is_rejected(self) -> None:
        value = load_value()
        value["artifacts"][0]["producer_path"] = "fixtures/wrong.json"
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "wrong producer or consumer path"):
                source_tuple.run(write_value(tmp, value))

    def test_superseded_evidence_cannot_be_current(self) -> None:
        value = load_value()
        value["producer"]["freeze_evidence"]["evidence_status"] = "historical"
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "superseded evidence cited as current"):
                source_tuple.run(write_value(tmp, value))

    def test_missing_supersession_link_is_rejected(self) -> None:
        value = load_value()
        value["supersession"]["link_complete"] = False
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "supersession link is incomplete"):
                source_tuple.run(write_value(tmp, value))

    def test_same_resolution_group_is_rejected(self) -> None:
        value = load_value()
        value["resolution"]["verifier_independence_group"] = value["resolution"][
            "resolver_independence_group"
        ]
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "independence groups must differ"):
                source_tuple.run(write_value(tmp, value))

    def test_duplicate_key_is_rejected(self) -> None:
        text = SOURCE_TUPLE.read_text(encoding="utf-8")
        altered = text.replace(
            '  "profile_version": "1.0.0",',
            '  "profile_version": "1.0.0",\n  "profile_version": "1.0.0",',
            1,
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / SOURCE_TUPLE.name
            path.write_text(altered, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                source_tuple.run(path)

    def test_non_finite_value_is_rejected(self) -> None:
        text = SOURCE_TUPLE.read_text(encoding="utf-8").replace(
            '"pull_request": 24', '"pull_request": NaN', 1
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / SOURCE_TUPLE.name
            path.write_text(text, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "non-finite JSON value"):
                source_tuple.run(path)

    def test_unknown_field_is_rejected(self) -> None:
        value = copy.deepcopy(load_value())
        value["producer"]["branch"] = "governance/consent-capacity-lock"
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "producer fields mismatch"):
                source_tuple.run(write_value(tmp, value))


if __name__ == "__main__":
    unittest.main()
