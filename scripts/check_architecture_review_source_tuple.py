#!/usr/bin/env python3
"""Strict validator for the externally resolved QSO Field review tuple.

The tuple is evidence only. Passing never appoints a reviewer, completes a real
quorum, decides architecture, or authorizes merge, release, publication, or
runtime action.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

MAX_TUPLE_BYTES = 64_000
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
EXPECTED_PROFILE_ID = "qso.studio.architecture-review-producer-source.v1"
EXPECTED_PROFILE_VERSION = "1.1.0"
EXPECTED_RESOLVED_HEAD = "a56b1fa93f151ee14f3cdd4183b89a10e268e352"
EXPECTED_PREVIOUS_HEAD = "49a93b25f1b04c13b97fef93a786afa4bf1048c4"
EXPECTED_BASE_HEAD = "2d7adf88ce84f01f0ff1067cef09388481f7e4ae"
EXPECTED_REPOSITORY = "aevespers2/qso-field.github.io"
EXPECTED_PR = 24
EXPECTED_FREEZE = {
    "workflow_run": 30000668553,
    "artifact_id": 8560824564,
    "artifact_digest": "sha256:f266006a19bd8a5d95b4c7aeedfc0bac950f1932d7b58eef88ee7eac6f62e77a",
    "expires_at": "2026-08-22T10:48:09Z",
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
TOP_KEYS = {"profile_id", "profile_version", "status", "authority_effect", "producer", "resolution", "supersession", "artifacts"}
PRODUCER_KEYS = {"repository", "pull_request", "base_head", "resolved_head", "observed_pr_head", "head_state", "freeze_evidence"}
RESOLUTION_KEYS = {"resolver_id", "resolver_independence_group", "verifier_id", "verifier_independence_group", "independent"}
SUPERSESSION_KEYS = {"previous_source_head", "previous_evidence_status", "current_source_head", "link_complete"}
ARTIFACT_KEYS = {"name", "producer_path", "producer_blob_sha", "producer_raw_sha256", "consumer_path", "consumer_blob_sha", "consumer_raw_sha256", "canonical_sha256", "copy_relation"}


def _constant(value: str) -> None:
    raise ValueError(f"non-finite JSON value is prohibited: {value}")


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
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
    value = json.loads(text, object_pairs_hook=_pairs, parse_constant=_constant)
    if not isinstance(value, dict):
        raise ValueError("source tuple root must be an object")
    return value


def _keys(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    if set(value) != expected:
        raise ValueError(f"{label} fields mismatch: missing={sorted(expected-set(value))} unknown={sorted(set(value)-expected)}")
    return value


def _sha1(value: Any, label: str) -> None:
    if not isinstance(value, str) or not SHA1_RE.fullmatch(value):
        raise ValueError(f"{label} must be a lowercase 40-character Git object id")


def validate_source_tuple(value: dict[str, Any]) -> dict[str, Any]:
    _keys(value, TOP_KEYS, "source tuple")
    if value["profile_id"] != EXPECTED_PROFILE_ID or value["profile_version"] != EXPECTED_PROFILE_VERSION:
        raise ValueError("source tuple profile identity mismatch")
    if value["status"] != "candidate_observation_only" or value["authority_effect"] != "none":
        raise ValueError("source tuple must remain current evidence only and non-authoritative")

    producer = _keys(value["producer"], PRODUCER_KEYS, "producer")
    if producer["repository"] != EXPECTED_REPOSITORY or producer["pull_request"] != EXPECTED_PR:
        raise ValueError("producer repository or pull request mismatch")
    if producer["base_head"] != EXPECTED_BASE_HEAD:
        raise ValueError("producer base head mismatch")
    for key in ("base_head", "resolved_head", "observed_pr_head"):
        _sha1(producer[key], f"producer {key}")
    if producer["resolved_head"] != EXPECTED_RESOLVED_HEAD:
        raise ValueError("stale producer head in source tuple")
    if producer["observed_pr_head"] != producer["resolved_head"]:
        raise ValueError("producer head moved after source resolution")
    if producer["head_state"] != "current_at_resolution":
        raise ValueError("producer head state is not current at resolution")
    if producer["freeze_evidence"] != EXPECTED_FREEZE:
        evidence = producer.get("freeze_evidence", {})
        if isinstance(evidence, dict) and evidence.get("evidence_status") == "historical":
            raise ValueError("superseded evidence cited as current")
        raise ValueError("producer freeze evidence mismatch")
    if not SHA256_RE.fullmatch(producer["freeze_evidence"]["artifact_digest"]):
        raise ValueError("freeze evidence artifact digest must be SHA-256")

    resolution = _keys(value["resolution"], RESOLUTION_KEYS, "resolution")
    if resolution["independent"] is not True:
        raise ValueError("source resolver and verifier must be independent")
    if resolution["resolver_id"] == resolution["verifier_id"]:
        raise ValueError("source resolver and verifier identities must differ")
    if resolution["resolver_independence_group"] == resolution["verifier_independence_group"]:
        raise ValueError("source resolver and verifier independence groups must differ")

    supersession = _keys(value["supersession"], SUPERSESSION_KEYS, "supersession")
    if supersession["previous_source_head"] != EXPECTED_PREVIOUS_HEAD or supersession["current_source_head"] != EXPECTED_RESOLVED_HEAD:
        raise ValueError("supersession source identity mismatch")
    if supersession["previous_evidence_status"] != "historical":
        raise ValueError("previous evidence must be historical")
    if supersession["link_complete"] is not True:
        raise ValueError("supersession link is incomplete")

    artifacts = value["artifacts"]
    if not isinstance(artifacts, list) or len(artifacts) != 2:
        raise ValueError("source tuple must contain exactly the base and extension artifacts")
    seen: set[str] = set()
    for item in artifacts:
        item = _keys(item, ARTIFACT_KEYS, "artifact")
        name = item["name"]
        if name not in EXPECTED_ARTIFACTS or name in seen:
            raise ValueError("artifact identity is missing, unknown, or duplicated")
        seen.add(name)
        for field, expected in EXPECTED_ARTIFACTS[name].items():
            if item[field] != expected:
                if field.endswith("_path"):
                    raise ValueError(f"wrong producer or consumer path for {name}")
                raise ValueError(f"source artifact identity mismatch for {name}.{field}")
    if seen != set(EXPECTED_ARTIFACTS):
        raise ValueError("source tuple artifact coverage is incomplete")

    return {
        "result": "PASS",
        "profile_id": EXPECTED_PROFILE_ID,
        "producer_repository": EXPECTED_REPOSITORY,
        "producer_pull_request": EXPECTED_PR,
        "resolved_head": EXPECTED_RESOLVED_HEAD,
        "artifact_names": sorted(seen),
        "authority_effect": "none",
    }


def run(path: Path) -> dict[str, Any]:
    return validate_source_tuple(strict_load(path))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-tuple", type=Path, default=Path("fixtures/architecture-review-producer-source-v1.json"))
    args = parser.parse_args()
    print(json.dumps(run(args.source_tuple), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
