#!/usr/bin/env python3
"""Validate the externally resolved QSO Field producer source tuple.

This gate validates immutable source identity, path, evidence, independence, and
supersession metadata before the QSO-STUDIO consumer parses either synthetic
review corpus. Passing remains non-authoritative conformance evidence only.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

MAX_TUPLE_BYTES = 64_000
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^(?:sha256:)?[0-9a-f]{64}$")

EXPECTED_PROFILE_ID = "qso.studio.architecture-review-producer-source.v1"
EXPECTED_PROFILE_VERSION = "1.0.0"
EXPECTED_STATUS = "candidate_observation_only"
EXPECTED_REPOSITORY = "aevespers2/qso-field.github.io"
EXPECTED_PULL_REQUEST = 24
EXPECTED_BASE_HEAD = "2d7adf88ce84f01f0ff1067cef09388481f7e4ae"
EXPECTED_RESOLVED_HEAD = "49a93b25f1b04c13b97fef93a786afa4bf1048c4"
EXPECTED_PREVIOUS_HEAD = "13f5f1a6cb4ba589c1a0e616ca40fc3f8dcfe028"

EXPECTED_FREEZE_EVIDENCE = {
    "workflow_run": 29968017117,
    "artifact_id": 8548564982,
    "artifact_digest": "sha256:70d6bc755440f97c2ae0aafa594f9c6c920464e3255c55a13a6cc33c9898a9a2",
    "expires_at": "2026-08-22T00:04:26Z",
    "evidence_status": "current_at_resolution",
}

EXPECTED_ARTIFACTS = {
    "base": {
        "producer_path": "fixtures/architecture-review-quorum-v1.json",
        "producer_blob_sha": "9e01e92d8abec20da6594857d6f064fbba8e73ae",
        "producer_raw_sha256": "dea97fcfd54cd71e9bf38af0c8ca4eeeedd83156ab4d1ae2a7f91513a32485f5",
        "consumer_path": "fixtures/architecture-review-quorum-v1.json",
        "consumer_blob_sha": "22fe2513bffc865a6483b96285d7ad323b1a245a",
        "consumer_raw_sha256": "521622728f55c947f345e3e6cb6bd2e6b0d38bb62272871c84cdb9e24d5b2116",
        "canonical_sha256": "a8b65c3fce4b7cf80fdefab76c497720b2bf17086d431a53f9bacf82e58bd9ec",
        "copy_relation": "canonical_equivalent_not_byte_identical",
    },
    "extension": {
        "producer_path": "fixtures/architecture-review-quorum-extension-v1.json",
        "producer_blob_sha": "e638e7cac904a25b76ff8ec96f7e3ca18ae82dc4",
        "producer_raw_sha256": "14ed2b65dea7b3c5fc0b026e839144beff34f07fc416f0a54b77b8acf17a6ed4",
        "consumer_path": "fixtures/architecture-review-quorum-extension-v1.json",
        "consumer_blob_sha": "e638e7cac904a25b76ff8ec96f7e3ca18ae82dc4",
        "consumer_raw_sha256": "14ed2b65dea7b3c5fc0b026e839144beff34f07fc416f0a54b77b8acf17a6ed4",
        "canonical_sha256": "6e767141e6c76ec43366b661db0fee9090a56c9ce7d50eda28da7f1094d5e3c2",
        "copy_relation": "byte_identical",
    },
}

TOP_KEYS = {
    "profile_id",
    "profile_version",
    "status",
    "authority_effect",
    "producer",
    "resolution",
    "supersession",
    "artifacts",
}
PRODUCER_KEYS = {
    "repository",
    "pull_request",
    "base_head",
    "resolved_head",
    "observed_pr_head",
    "head_state",
    "freeze_evidence",
}
RESOLUTION_KEYS = {
    "resolver_id",
    "resolver_independence_group",
    "verifier_id",
    "verifier_independence_group",
    "independent",
}
SUPERSESSION_KEYS = {
    "previous_source_head",
    "previous_evidence_status",
    "current_source_head",
    "link_complete",
}
ARTIFACT_KEYS = {"name", *next(iter(EXPECTED_ARTIFACTS.values())).keys()}


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON value is prohibited: {value}")


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_load(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if len(raw) > MAX_TUPLE_BYTES:
        raise ValueError("source tuple exceeds the 64-kilobyte bound")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError("source tuple must be valid UTF-8") from exc
    value = json.loads(
        text,
        object_pairs_hook=_reject_duplicates,
        parse_constant=_reject_constant,
    )
    if not isinstance(value, dict):
        raise ValueError("source tuple root must be an object")
    return value


def _exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    observed = set(value)
    if observed != expected:
        missing = sorted(expected - observed)
        unknown = sorted(observed - expected)
        raise ValueError(f"{label} fields mismatch: missing={missing} unknown={unknown}")


def _require_sha1(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SHA1_RE.fullmatch(value):
        raise ValueError(f"{label} must be a lowercase 40-character Git object id")
    return value


def _require_sha256(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ValueError(f"{label} must be a SHA-256 value")
    return value


def validate_source_tuple(value: dict[str, Any]) -> dict[str, Any]:
    _exact_keys(value, TOP_KEYS, "source tuple")
    if value["profile_id"] != EXPECTED_PROFILE_ID:
        raise ValueError("source tuple profile id mismatch")
    if value["profile_version"] != EXPECTED_PROFILE_VERSION:
        raise ValueError("source tuple profile version mismatch")
    if value["status"] != EXPECTED_STATUS:
        raise ValueError("superseded evidence cannot be represented as the current source tuple")
    if value["authority_effect"] != "none":
        raise ValueError("source tuple must not claim authority")

    producer = value["producer"]
    if not isinstance(producer, dict):
        raise ValueError("producer must be an object")
    _exact_keys(producer, PRODUCER_KEYS, "producer")
    if producer["repository"] != EXPECTED_REPOSITORY or producer["pull_request"] != EXPECTED_PULL_REQUEST:
        raise ValueError("producer repository or pull request mismatch")
    if producer["base_head"] != EXPECTED_BASE_HEAD:
        raise ValueError("producer base head mismatch")
    _require_sha1(producer["base_head"], "producer base head")
    _require_sha1(producer["resolved_head"], "producer resolved head")
    _require_sha1(producer["observed_pr_head"], "observed producer PR head")
    if producer["resolved_head"] != EXPECTED_RESOLVED_HEAD:
        raise ValueError("stale producer head in source tuple")
    if producer["observed_pr_head"] != producer["resolved_head"]:
        raise ValueError("producer head moved after source resolution")
    if producer["head_state"] != "current_at_resolution":
        raise ValueError("producer head state is not current at resolution")
    evidence = producer["freeze_evidence"]
    if not isinstance(evidence, dict) or evidence != EXPECTED_FREEZE_EVIDENCE:
        raise ValueError("producer freeze evidence mismatch or superseded evidence cited as current")
    _require_sha256(evidence["artifact_digest"], "freeze evidence artifact digest")

    resolution = value["resolution"]
    if not isinstance(resolution, dict):
        raise ValueError("resolution must be an object")
    _exact_keys(resolution, RESOLUTION_KEYS, "resolution")
    for field in (
        "resolver_id",
        "resolver_independence_group",
        "verifier_id",
        "verifier_independence_group",
    ):
        if not isinstance(resolution[field], str) or not resolution[field]:
            raise ValueError(f"{field} must be a non-empty string")
    if resolution["independent"] is not True:
        raise ValueError("source resolver and verifier must be independent")
    if resolution["resolver_id"] == resolution["verifier_id"]:
        raise ValueError("source resolver and verifier identities must differ")
    if resolution["resolver_independence_group"] == resolution["verifier_independence_group"]:
        raise ValueError("source resolver and verifier independence groups must differ")

    supersession = value["supersession"]
    if not isinstance(supersession, dict):
        raise ValueError("supersession must be an object")
    _exact_keys(supersession, SUPERSESSION_KEYS, "supersession")
    if supersession["previous_source_head"] != EXPECTED_PREVIOUS_HEAD:
        raise ValueError("supersession previous source head mismatch")
    if supersession["current_source_head"] != EXPECTED_RESOLVED_HEAD:
        raise ValueError("supersession current source head mismatch")
    if supersession["previous_evidence_status"] != "historical":
        raise ValueError("superseded evidence must be marked historical")
    if supersession["link_complete"] is not True:
        raise ValueError("supersession link is incomplete")

    artifacts = value["artifacts"]
    if not isinstance(artifacts, list) or len(artifacts) != len(EXPECTED_ARTIFACTS):
        raise ValueError("source tuple must contain exactly the base and extension artifacts")
    observed_names: set[str] = set()
    for item in artifacts:
        if not isinstance(item, dict):
            raise ValueError("artifact entries must be objects")
        _exact_keys(item, ARTIFACT_KEYS, "artifact")
        name = item["name"]
        if name not in EXPECTED_ARTIFACTS or name in observed_names:
            raise ValueError("artifact identity is missing, unknown, or duplicated")
        observed_names.add(name)
        expected = EXPECTED_ARTIFACTS[name]
        for field, expected_value in expected.items():
            if item[field] != expected_value:
                if field.endswith("_path"):
                    raise ValueError(f"wrong producer or consumer path for {name}")
                raise ValueError(f"source artifact identity mismatch for {name}.{field}")
        _require_sha1(item["producer_blob_sha"], f"{name} producer blob")
        _require_sha1(item["consumer_blob_sha"], f"{name} consumer blob")
        _require_sha256(item["producer_raw_sha256"], f"{name} producer bytes")
        _require_sha256(item["consumer_raw_sha256"], f"{name} consumer bytes")
        _require_sha256(item["canonical_sha256"], f"{name} canonical payload")
    if observed_names != set(EXPECTED_ARTIFACTS):
        raise ValueError("source tuple artifact coverage is incomplete")

    return {
        "result": "PASS",
        "profile_id": EXPECTED_PROFILE_ID,
        "producer_repository": EXPECTED_REPOSITORY,
        "producer_pull_request": EXPECTED_PULL_REQUEST,
        "resolved_head": EXPECTED_RESOLVED_HEAD,
        "artifact_names": sorted(observed_names),
        "authority_effect": "none",
    }


def run(path: Path) -> dict[str, Any]:
    return validate_source_tuple(strict_load(path))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-tuple",
        type=Path,
        default=Path("fixtures/architecture-review-producer-source-v1.json"),
    )
    args = parser.parse_args()
    result = run(args.source_tuple)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
