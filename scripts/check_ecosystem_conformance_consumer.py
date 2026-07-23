#!/usr/bin/env python3
"""Independent, fail-closed QSO ecosystem manifest consumer."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

EXPECTED_SOURCE = {
    "contract_id": "QSO-ECOSYSTEM-CONSUMER-SOURCE-V1",
    "producer": {
        "repository": "aevespers2/QSO-FABRIC",
        "pull_request": 21,
        "exact_head": "738cf25aec9b2bae0b71c50374585bab36934ef3",
        "path": "qso.manifest.json",
        "git_blob_sha": "5070ac6615b8127b14a9f230678f58a081c6c2c4",
        "sha256": "c5e6d2e42fdbe9703d9f28c7f65ffff02208bff52fa96ee7090bfcbcb5dea728",
    },
    "consumer": {
        "repository": "aevespers2/QSO-STUDIO",
        "path": "fixtures/qso-fabric-manifest-v1.json",
        "relation": "BYTE_IDENTICAL",
    },
    "resolution": {
        "resolver": "QSO-STUDIO-source-resolver",
        "resolver_independence_group": "studio-resolution",
        "verifier": "QSO-STUDIO-consumer-verifier",
        "verifier_independence_group": "studio-verification",
    },
    "authority_effect": "none",
}

TOP_FIELDS = {
    "schema_version", "component", "version", "purpose", "conformance",
    "runtime_bounds", "capabilities", "interfaces", "governance",
}
CONFORMANCE_FIELDS = {"claimed_level", "evidence_path"}
RUNTIME_FIELDS = {
    "max_seconds", "max_rounds", "max_messages", "max_memory_mb", "network_default"
}
CAPABILITY_FIELDS = {"name", "authority", "default", "constraints"}
INTERFACE_FIELDS = {"name", "role", "protocol", "schema_version", "idempotent", "retry_limit"}
GOVERNANCE_FIELDS = {"review_component", "deprecated_aliases", "human_override", "audit_log"}
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(?:[-+][A-Za-z0-9.-]+)?$")
IDENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{1,127}$")
SAFE_PATH = re.compile(r"^(?!/)(?!.*(?:^|/)\.\.(?:/|$))[A-Za-z0-9._/-]+$")


class ConformanceError(ValueError):
    def __init__(self, reason: str, message: str):
        super().__init__(message)
        self.reason = reason


def _reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ConformanceError("DUPLICATE_KEY", f"duplicate key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ConformanceError("NON_FINITE_NUMBER", f"non-finite number: {value}")


def strict_load_bytes(raw: bytes) -> Any:
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ConformanceError("INVALID_UTF8", str(exc)) from exc
    try:
        return json.loads(
            text,
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_constant,
        )
    except ConformanceError:
        raise
    except json.JSONDecodeError as exc:
        raise ConformanceError("INVALID_JSON", str(exc)) from exc


def _exact_keys(value: Any, expected: set[str], context: str) -> dict[str, Any]:
    if type(value) is not dict:
        raise ConformanceError("TYPE_MISMATCH", f"{context} must be an object")
    actual = set(value)
    if actual != expected:
        raise ConformanceError(
            "FIELD_SET_MISMATCH",
            f"{context} fields differ: missing={sorted(expected-actual)} unknown={sorted(actual-expected)}",
        )
    return value


def _exact_int(value: Any, context: str, minimum: int = 0, maximum: int | None = None) -> int:
    if type(value) is not int:
        raise ConformanceError("TYPE_MISMATCH", f"{context} must be an integer")
    if value < minimum or (maximum is not None and value > maximum):
        raise ConformanceError("BOUND_VIOLATION", f"{context} is out of bounds")
    return value


def _nonempty_string(value: Any, context: str) -> str:
    if type(value) is not str or not value:
        raise ConformanceError("TYPE_MISMATCH", f"{context} must be a non-empty string")
    return value


def verify_source_tuple(tuple_raw: bytes, manifest_raw: bytes) -> None:
    source = strict_load_bytes(tuple_raw)
    if source != EXPECTED_SOURCE:
        raise ConformanceError("SOURCE_TUPLE_DRIFT", "source tuple does not match frozen generation")
    resolution = source["resolution"]
    if resolution["resolver"] == resolution["verifier"]:
        raise ConformanceError("ROLE_COLLISION", "resolver and verifier must differ")
    if resolution["resolver_independence_group"] == resolution["verifier_independence_group"]:
        raise ConformanceError("INDEPENDENCE_COLLISION", "resolver and verifier groups must differ")
    observed = hashlib.sha256(manifest_raw).hexdigest()
    if observed != source["producer"]["sha256"]:
        raise ConformanceError("SOURCE_BYTE_DRIFT", f"manifest SHA-256 drift: {observed}")


def validate_manifest(manifest: Any) -> dict[str, Any]:
    manifest = _exact_keys(manifest, TOP_FIELDS, "manifest")

    if manifest["schema_version"] != "1.0.0":
        raise ConformanceError("SCHEMA_VERSION_MISMATCH", "unsupported schema_version")
    component = _nonempty_string(manifest["component"], "component")
    if not IDENT.fullmatch(component):
        raise ConformanceError("IDENTIFIER_INVALID", "component identifier is invalid")
    version = _nonempty_string(manifest["version"], "version")
    if not SEMVER.fullmatch(version):
        raise ConformanceError("VERSION_INVALID", "version is not semver")
    purpose = _nonempty_string(manifest["purpose"], "purpose")
    if len(purpose) < 20:
        raise ConformanceError("PURPOSE_TOO_SHORT", "purpose must be at least 20 characters")

    conformance = _exact_keys(manifest["conformance"], CONFORMANCE_FIELDS, "conformance")
    _exact_int(conformance["claimed_level"], "claimed_level", 0, 5)
    evidence_path = _nonempty_string(conformance["evidence_path"], "evidence_path")
    if not SAFE_PATH.fullmatch(evidence_path):
        raise ConformanceError("PATH_INVALID", "evidence_path is unsafe")

    runtime = _exact_keys(manifest["runtime_bounds"], RUNTIME_FIELDS, "runtime_bounds")
    for field in ("max_seconds", "max_rounds", "max_messages", "max_memory_mb"):
        _exact_int(runtime[field], field, 1)
    if runtime["network_default"] not in {"deny", "allow-declared"}:
        raise ConformanceError("ENUM_INVALID", "network_default is invalid")

    capabilities = manifest["capabilities"]
    if type(capabilities) is not list or not capabilities:
        raise ConformanceError("TYPE_MISMATCH", "capabilities must be a non-empty array")
    capability_names: set[str] = set()
    for index, item in enumerate(capabilities):
        item = _exact_keys(item, CAPABILITY_FIELDS, f"capabilities[{index}]")
        name = _nonempty_string(item["name"], f"capabilities[{index}].name")
        if not IDENT.fullmatch(name):
            raise ConformanceError("IDENTIFIER_INVALID", f"invalid capability name: {name}")
        if name in capability_names:
            raise ConformanceError("DUPLICATE_IDENTITY", f"duplicate capability: {name}")
        capability_names.add(name)
        if item["authority"] not in {"observe", "propose", "execute"}:
            raise ConformanceError("ENUM_INVALID", f"invalid capability authority: {name}")
        if item["default"] not in {"deny", "allow"}:
            raise ConformanceError("ENUM_INVALID", f"invalid capability default: {name}")
        constraints = item["constraints"]
        if type(constraints) is not list or not constraints:
            raise ConformanceError("TYPE_MISMATCH", f"constraints must be non-empty: {name}")
        if any(type(value) is not str or not value for value in constraints):
            raise ConformanceError("TYPE_MISMATCH", f"constraints must be strings: {name}")
        if len(set(constraints)) != len(constraints):
            raise ConformanceError("DUPLICATE_IDENTITY", f"duplicate constraint: {name}")
        if name in {"external-network", "consequential-action"} and item["default"] != "deny":
            raise ConformanceError("UNSAFE_DEFAULT", f"{name} must default deny")

    interfaces = manifest["interfaces"]
    if type(interfaces) is not list or not interfaces:
        raise ConformanceError("TYPE_MISMATCH", "interfaces must be a non-empty array")
    interface_names: set[str] = set()
    for index, item in enumerate(interfaces):
        item = _exact_keys(item, INTERFACE_FIELDS, f"interfaces[{index}]")
        name = _nonempty_string(item["name"], f"interfaces[{index}].name")
        if not IDENT.fullmatch(name):
            raise ConformanceError("IDENTIFIER_INVALID", f"invalid interface name: {name}")
        if name in interface_names:
            raise ConformanceError("DUPLICATE_IDENTITY", f"duplicate interface: {name}")
        interface_names.add(name)
        if item["role"] not in {"producer", "consumer", "bidirectional"}:
            raise ConformanceError("ENUM_INVALID", f"invalid interface role: {name}")
        _nonempty_string(item["protocol"], f"interfaces[{index}].protocol")
        schema_version = _nonempty_string(item["schema_version"], f"interfaces[{index}].schema_version")
        if not SEMVER.fullmatch(schema_version):
            raise ConformanceError("VERSION_INVALID", f"invalid interface schema version: {name}")
        if type(item["idempotent"]) is not bool:
            raise ConformanceError("TYPE_MISMATCH", f"idempotent must be Boolean: {name}")
        _exact_int(item["retry_limit"], f"interfaces[{index}].retry_limit", 0)

    governance = _exact_keys(manifest["governance"], GOVERNANCE_FIELDS, "governance")
    if governance["review_component"] != "Jacob Redmond":
        raise ConformanceError("GOVERNANCE_IDENTITY_DRIFT", "review_component must be Jacob Redmond")
    aliases = governance["deprecated_aliases"]
    if type(aliases) is not list or any(type(value) is not str or not value for value in aliases):
        raise ConformanceError("TYPE_MISMATCH", "deprecated_aliases must be strings")
    if len(set(aliases)) != len(aliases):
        raise ConformanceError("DUPLICATE_IDENTITY", "deprecated_aliases must be unique")
    if governance["human_override"] is not True or governance["audit_log"] is not True:
        raise ConformanceError("GOVERNANCE_SAFETY_DRIFT", "human_override and audit_log must be true")

    return {
        "disposition": "SYNTHETIC_CONFORMANCE_MATCH",
        "reasons": [],
        "component": component,
        "version": version,
        "claimed_level": conformance["claimed_level"],
        "capability_count": len(capabilities),
        "interface_count": len(interfaces),
        "authority_effect": "none",
    }


def evaluate(tuple_raw: bytes, manifest_raw: bytes) -> dict[str, Any]:
    try:
        verify_source_tuple(tuple_raw, manifest_raw)
        manifest = strict_load_bytes(manifest_raw)
        return validate_manifest(manifest)
    except ConformanceError as exc:
        return {
            "disposition": "REJECTED_FAIL_CLOSED",
            "reasons": [exc.reason],
            "message": str(exc),
            "authority_effect": "none",
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-tuple",
        default="contracts/qso-ecosystem-consumer-source-v1.json",
    )
    parser.add_argument(
        "--manifest",
        default="fixtures/qso-fabric-manifest-v1.json",
    )
    args = parser.parse_args()
    result = evaluate(Path(args.source_tuple).read_bytes(), Path(args.manifest).read_bytes())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["disposition"] == "SYNTHETIC_CONFORMANCE_MATCH" else 1


if __name__ == "__main__":
    raise SystemExit(main())
