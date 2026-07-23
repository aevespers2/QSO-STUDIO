#!/usr/bin/env python3
"""Fail-closed source-tuple and raw-byte gate for the QSO-STUDIO consumer.

The externally resolved producer tuple is validated before either committed
synthetic fixture is parsed. The local fixture copies are then bound by exact
SHA-256 before any semantic evaluator is invoked. Matching outcomes remain
conformance evidence only and grant no reviewer, decision, activation, or
runtime authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

if __package__:
    from scripts import check_architecture_review_quorum_consumer as consumer
    from scripts import check_architecture_review_source_tuple as source_tuple
else:
    import check_architecture_review_quorum_consumer as consumer
    import check_architecture_review_source_tuple as source_tuple

Parser = Callable[[Path], dict[str, Any]]
MAX_FIXTURE_BYTES = 1_000_000
EXPECTED_BASE_RAW_SHA256 = "521622728f55c947f345e3e6cb6bd2e6b0d38bb62272871c84cdb9e24d5b2116"
EXPECTED_EXTENSION_RAW_SHA256 = "14ed2b65dea7b3c5fc0b026e839144beff34f07fc416f0a54b77b8acf17a6ed4"
DEFAULT_SOURCE_TUPLE = Path("fixtures/architecture-review-producer-source-v1.json")


def raw_sha256(path: Path) -> str:
    raw = path.read_bytes()
    if len(raw) > MAX_FIXTURE_BYTES:
        raise ValueError("fixture exceeds the one-megabyte identity bound")
    return hashlib.sha256(raw).hexdigest()


def verify_identity_then_parse(path: Path, expected_sha256: str, parser: Parser) -> dict[str, Any]:
    """Verify exact local bytes before invoking the supplied semantic parser."""
    observed = raw_sha256(path)
    if observed != expected_sha256:
        raise ValueError(
            f"raw fixture identity mismatch for {path}: expected={expected_sha256} observed={observed}"
        )
    return parser(path)


def run_pair(
    base_path: Path,
    extension_path: Path,
    source_tuple_path: Path = DEFAULT_SOURCE_TUPLE,
    base_parser: Parser | None = None,
    extension_parser: Parser | None = None,
) -> dict[str, Any]:
    """Validate the external tuple before invoking either semantic parser."""
    tuple_result = source_tuple.run(source_tuple_path)
    selected_base_parser = consumer.run if base_parser is None else base_parser
    selected_extension_parser = consumer.run_extension if extension_parser is None else extension_parser
    base = verify_identity_then_parse(base_path, EXPECTED_BASE_RAW_SHA256, selected_base_parser)
    extension = verify_identity_then_parse(
        extension_path,
        EXPECTED_EXTENSION_RAW_SHA256,
        selected_extension_parser,
    )
    return {
        "consumer": "QSO-STUDIO",
        "source_tuple_gate": "external_tuple_before_fixture_parse",
        "identity_gate": "raw_sha256_before_parse",
        "authority_effect": "none",
        "source_tuple": tuple_result,
        "base_raw_sha256": raw_sha256(base_path),
        "extension_raw_sha256": raw_sha256(extension_path),
        "base": base,
        "extension": extension,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-tuple",
        type=Path,
        default=DEFAULT_SOURCE_TUPLE,
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("fixtures/architecture-review-quorum-v1.json"),
    )
    parser.add_argument(
        "--extension",
        type=Path,
        default=Path("fixtures/architecture-review-quorum-extension-v1.json"),
    )
    args = parser.parse_args()
    result = run_pair(args.fixture, args.extension, args.source_tuple)
    print(json.dumps(result, indent=2, sort_keys=True))
    accepted = (
        result["source_tuple"]["result"] == "PASS"
        and all(
            item["result"] == "PASS" and item["canonical_payload_matches"]
            for item in (result["base"], result["extension"])
        )
    )
    return 0 if accepted else 1


if __name__ == "__main__":
    raise SystemExit(main())
