from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from scripts import check_architecture_review_quorum_consumer as consumer
from scripts import check_architecture_review_source_identity as identity

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "fixtures" / "architecture-review-quorum-v1.json"
EXTENSION = ROOT / "fixtures" / "architecture-review-quorum-extension-v1.json"


def canonical_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class QSOStudioSourceIdentityTests(unittest.TestCase):
    def test_committed_fixture_bytes_match_frozen_identities(self) -> None:
        self.assertEqual(identity.raw_sha256(BASE), identity.EXPECTED_BASE_RAW_SHA256)
        self.assertEqual(identity.raw_sha256(EXTENSION), identity.EXPECTED_EXTENSION_RAW_SHA256)

    def test_matching_bytes_reach_semantic_parser_once(self) -> None:
        parser = Mock(return_value={"result": "PASS"})
        result = identity.verify_identity_then_parse(BASE, identity.EXPECTED_BASE_RAW_SHA256, parser)
        self.assertEqual(result, {"result": "PASS"})
        parser.assert_called_once_with(BASE)

    def test_semantically_equal_reserialization_is_rejected_before_parse(self) -> None:
        original = json.loads(BASE.read_text(encoding="utf-8"))
        reserialized = json.dumps(original, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
        self.assertEqual(canonical_sha256(original), consumer.EXPECTED_CANONICAL_SHA256)
        self.assertEqual(canonical_sha256(json.loads(reserialized)), consumer.EXPECTED_CANONICAL_SHA256)

        with tempfile.TemporaryDirectory() as tmp:
            altered = Path(tmp) / BASE.name
            altered.write_text(reserialized, encoding="utf-8")
            self.assertNotEqual(identity.raw_sha256(altered), identity.EXPECTED_BASE_RAW_SHA256)
            parser = Mock(side_effect=AssertionError("semantic parser must not run after raw-byte drift"))
            with self.assertRaisesRegex(ValueError, "raw fixture identity mismatch"):
                identity.verify_identity_then_parse(altered, identity.EXPECTED_BASE_RAW_SHA256, parser)
            parser.assert_not_called()

    def test_extension_byte_drift_is_rejected_before_parse(self) -> None:
        altered_bytes = EXTENSION.read_bytes() + b"\n"
        with tempfile.TemporaryDirectory() as tmp:
            altered = Path(tmp) / EXTENSION.name
            altered.write_bytes(altered_bytes)
            parser = Mock(side_effect=AssertionError("extension parser must not run after raw-byte drift"))
            with self.assertRaisesRegex(ValueError, "raw fixture identity mismatch"):
                identity.verify_identity_then_parse(
                    altered,
                    identity.EXPECTED_EXTENSION_RAW_SHA256,
                    parser,
                )
            parser.assert_not_called()

    def test_complete_pair_passes_without_authority_effect(self) -> None:
        result = identity.run_pair(BASE, EXTENSION)
        self.assertEqual(result["identity_gate"], "raw_sha256_before_parse")
        self.assertEqual(result["authority_effect"], "none")
        self.assertEqual(result["base"]["result"], "PASS")
        self.assertEqual(result["extension"]["result"], "PASS")


if __name__ == "__main__":
    unittest.main()
