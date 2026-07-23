from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.check_ecosystem_conformance_consumer import evaluate

ROOT = Path(__file__).resolve().parents[1]
TUPLE_RAW = (ROOT / "contracts/qso-ecosystem-consumer-source-v1.json").read_bytes()
MANIFEST_RAW = (ROOT / "fixtures/qso-fabric-manifest-v1.json").read_bytes()


def encode(value):
    return (json.dumps(value, indent=2) + "\n").encode("utf-8")


class EcosystemConsumerTests(unittest.TestCase):
    def accepted(self, raw=MANIFEST_RAW, tuple_raw=TUPLE_RAW):
        result = evaluate(tuple_raw, raw)
        self.assertEqual(result["disposition"], "SYNTHETIC_CONFORMANCE_MATCH", result)
        self.assertEqual(result["authority_effect"], "none")
        return result

    def rejected(self, reason, raw=MANIFEST_RAW, tuple_raw=TUPLE_RAW):
        result = evaluate(tuple_raw, raw)
        self.assertEqual(result["disposition"], "REJECTED_FAIL_CLOSED", result)
        self.assertEqual(result["reasons"], [reason], result)
        self.assertEqual(result["authority_effect"], "none")
        return result

    def manifest(self):
        return json.loads(MANIFEST_RAW)

    def source_tuple(self):
        return json.loads(TUPLE_RAW)

    def test_accepts_exact_producer_fixture(self):
        result = self.accepted()
        self.assertEqual(result["component"], "QSO-FABRIC")
        self.assertEqual(result["capability_count"], 3)
        self.assertEqual(result["interface_count"], 2)

    def test_rejects_source_byte_drift_before_semantics(self):
        value = self.manifest()
        self.rejected("SOURCE_BYTE_DRIFT", encode(value))

    def test_rejects_stale_producer_head(self):
        value = self.source_tuple()
        value["producer"]["exact_head"] = "0" * 40
        self.rejected("SOURCE_TUPLE_DRIFT", tuple_raw=encode(value))

    def test_rejects_wrong_producer_path(self):
        value = self.source_tuple()
        value["producer"]["path"] = "wrong.json"
        self.rejected("SOURCE_TUPLE_DRIFT", tuple_raw=encode(value))

    def test_rejects_resolver_verifier_collision(self):
        value = self.source_tuple()
        value["resolution"]["verifier"] = value["resolution"]["resolver"]
        self.rejected("SOURCE_TUPLE_DRIFT", tuple_raw=encode(value))

    def test_rejects_duplicate_manifest_key_at_source_gate(self):
        raw = MANIFEST_RAW.replace(
            b'  "schema_version": "1.0.0",',
            b'  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",',
            1,
        )
        self.rejected("SOURCE_BYTE_DRIFT", raw)

    def test_strict_parser_rejects_duplicate_key_after_valid_source_gate(self):
        raw = MANIFEST_RAW.replace(
            b'  "schema_version": "1.0.0",',
            b'  "schema_version": "1.0.0",\n  "schema_version": "1.0.0",',
            1,
        )
        value = self.source_tuple()
        import hashlib
        value["producer"]["sha256"] = hashlib.sha256(raw).hexdigest()
        import scripts.check_ecosystem_conformance_consumer as consumer
        original = consumer.EXPECTED_SOURCE
        consumer.EXPECTED_SOURCE = value
        try:
            self.rejected("DUPLICATE_KEY", raw, encode(value))
        finally:
            consumer.EXPECTED_SOURCE = original

    def test_rejects_non_finite_number(self):
        raw = MANIFEST_RAW.replace(b'"max_seconds": 300', b'"max_seconds": NaN', 1)
        value = self.source_tuple()
        import hashlib
        value["producer"]["sha256"] = hashlib.sha256(raw).hexdigest()
        import scripts.check_ecosystem_conformance_consumer as consumer
        original = consumer.EXPECTED_SOURCE
        consumer.EXPECTED_SOURCE = value
        try:
            self.rejected("NON_FINITE_NUMBER", raw, encode(value))
        finally:
            consumer.EXPECTED_SOURCE = original

    def semantic_rejection(self, reason, mutation):
        value = self.manifest()
        mutation(value)
        raw = encode(value)
        source = self.source_tuple()
        import hashlib
        source["producer"]["sha256"] = hashlib.sha256(raw).hexdigest()
        import scripts.check_ecosystem_conformance_consumer as consumer
        original = consumer.EXPECTED_SOURCE
        consumer.EXPECTED_SOURCE = source
        try:
            self.rejected(reason, raw, encode(source))
        finally:
            consumer.EXPECTED_SOURCE = original

    def test_rejects_boolean_as_integer(self):
        self.semantic_rejection(
            "TYPE_MISMATCH",
            lambda value: value["runtime_bounds"].__setitem__("max_seconds", True),
        )

    def test_rejects_unknown_nested_field(self):
        self.semantic_rejection(
            "FIELD_SET_MISMATCH",
            lambda value: value["interfaces"][0].__setitem__("extra", "no"),
        )

    def test_rejects_unsafe_network_default(self):
        self.semantic_rejection(
            "UNSAFE_DEFAULT",
            lambda value: value["capabilities"][1].__setitem__("default", "allow"),
        )

    def test_rejects_duplicate_capability_identity(self):
        def mutate(value):
            value["capabilities"][1]["name"] = value["capabilities"][0]["name"]
        self.semantic_rejection("DUPLICATE_IDENTITY", mutate)

    def test_rejects_duplicate_interface_identity(self):
        def mutate(value):
            value["interfaces"][1]["name"] = value["interfaces"][0]["name"]
        self.semantic_rejection("DUPLICATE_IDENTITY", mutate)

    def test_rejects_governance_identity_drift(self):
        self.semantic_rejection(
            "GOVERNANCE_IDENTITY_DRIFT",
            lambda value: value["governance"].__setitem__("review_component", "Aequitas"),
        )

    def test_rejects_human_override_removal(self):
        self.semantic_rejection(
            "GOVERNANCE_SAFETY_DRIFT",
            lambda value: value["governance"].__setitem__("human_override", False),
        )

    def test_rejects_unsafe_evidence_path(self):
        self.semantic_rejection(
            "PATH_INVALID",
            lambda value: value["conformance"].__setitem__("evidence_path", "../escape"),
        )

    def test_rejects_invalid_conformance_level(self):
        self.semantic_rejection(
            "BOUND_VIOLATION",
            lambda value: value["conformance"].__setitem__("claimed_level", 6),
        )

    def test_rejects_invalid_component_identifier(self):
        self.semantic_rejection(
            "IDENTIFIER_INVALID",
            lambda value: value.__setitem__("component", "bad component"),
        )

    def test_rejects_invalid_semver(self):
        self.semantic_rejection(
            "VERSION_INVALID",
            lambda value: value.__setitem__("version", "latest"),
        )

    def test_rejects_authority_promotion_in_tuple(self):
        value = self.source_tuple()
        value["authority_effect"] = "activate"
        self.rejected("SOURCE_TUPLE_DRIFT", tuple_raw=encode(value))


if __name__ == "__main__":
    unittest.main()
