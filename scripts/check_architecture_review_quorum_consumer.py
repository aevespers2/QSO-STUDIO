#!/usr/bin/env python3
"""Independent QSO-STUDIO consumers for architecture-review quorum corpora.

Matching synthetic outcomes are conformance evidence only. They do not appoint
reviewers, establish a real quorum, decide architecture, or activate work.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Callable

APPROVAL = frozenset(("APPROVE", "APPROVE_WITH_CONDITIONS"))
EXPECTED_CANONICAL_SHA256 = "a8b65c3fce4b7cf80fdefab76c497720b2bf17086d431a53f9bacf82e58bd9ec"
EXPECTED_EXTENSION_SHA256 = "6e767141e6c76ec43366b661db0fee9090a56c9ce7d50eda28da7f1094d5e3c2"
Rule = Callable[[dict[str, Any], dict[str, Any]], set[str]]

EXTENSION_TOP_KEYS = {"schema", "profile_version", "data_class", "extends", "defaults", "cases"}
EXTENSION_LINK_KEYS = {"fixture", "base_case_count", "base_fixture_generation", "contract"}
EXTENSION_FACTS = {
    "class_coverage_complete",
    "common_control_disclosed",
    "conflicts_and_recusals_resolved",
    "incompatible_role_double_count",
    "appeal_present",
    "appeal_authorized_and_current",
    "appeal_panel_complete_and_independent",
    "emergency_review_present",
    "emergency_scope_bounded",
    "superseded",
    "dependent_findings_invalidated",
}
EXTENSION_REASON_ORDER = (
    "INCOMPLETE_REVIEW_CLASS_COVERAGE",
    "UNDISCLOSED_COMMON_CONTROL",
    "UNRESOLVED_CONFLICT_OR_RECUSAL",
    "INCOMPATIBLE_ROLE_DOUBLE_COUNT",
    "UNAUTHORIZED_OR_EXPIRED_APPEAL",
    "INCOMPLETE_OR_CONFLICTED_APPEAL_PANEL",
    "EMERGENCY_SCOPE_BROADENING",
    "STALE_REVIEW_AFTER_SUPERSESSION",
)
EXTENSION_DISPOSITIONS = {"COVERAGE_EXTENSION_CLEAR", "REVIEW_INCOMPLETE", "APPEAL_BLOCKED"}


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def _constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number is prohibited: {value}")


def load_strict(path: Path) -> Any:
    raw = path.read_bytes()
    if len(raw) > 1_000_000:
        raise ValueError("fixture exceeds the one-megabyte validation bound")
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError(f"invalid UTF-8: {exc}") from exc
    value = json.loads(text, object_pairs_hook=_pairs, parse_constant=_constant)
    _finite(value)
    return value


def _finite(value: Any, location: str = "root") -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"non-finite number at {location}")
    if isinstance(value, dict):
        for key, item in value.items():
            _finite(item, f"{location}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _finite(item, f"{location}[{index}]")


def _canonical_sha256(value: Any) -> str:
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _exact_keys(value: Any, expected: set[str], location: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{location} must be an object")
    actual = set(value)
    if actual != expected:
        raise ValueError(
            f"{location}: missing={sorted(expected - actual)} unknown={sorted(actual - expected)}"
        )
    return value


def reviewers(case: dict[str, Any]) -> list[dict[str, Any]]:
    value = case.get("reviewers", [])
    return value if isinstance(value, list) else []


def exact_rule(case: dict[str, Any], _: dict[str, Any]) -> set[str]:
    return set() if case.get("source_exact") and case.get("policy_exact") else {"MISSING_EXACT_SOURCE_OR_POLICY"}


def class_rule(case: dict[str, Any], policy: dict[str, Any]) -> set[str]:
    found = {item.get("reviewer_class") for item in reviewers(case)}
    return set() if set(policy["required_classes"]) <= found else {"INCOMPLETE_REVIEW_CLASS_COVERAGE"}


def eligibility_rule(case: dict[str, Any], _: dict[str, Any]) -> set[str]:
    findings: set[str] = set()
    for item in reviewers(case):
        if item.get("qualified") is not True:
            findings.add("STALE_OR_UNQUALIFIED_REVIEWER")
        if not (item.get("appointed") is True and item.get("accepted") is True):
            findings.add("MISSING_APPOINTMENT_OR_ACCEPTANCE")
        if item.get("conflict_clear") is not True:
            findings.add("UNRESOLVED_CONFLICT_OR_RECUSAL")
        roles = frozenset(item.get("roles", []))
        if "author" in roles and item.get("reviewer_class") == "architecture":
            findings.add("SELF_REVIEW")
    return findings


def eligible_approvals(case: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        item for item in reviewers(case)
        if all(item.get(field) is True for field in ("qualified", "appointed", "accepted", "conflict_clear"))
        and item.get("disposition") in APPROVAL
    ]


def claimed_rule(case: dict[str, Any], _: dict[str, Any]) -> set[str]:
    lookup = {item.get("reviewer_id"): item.get("disposition") for item in reviewers(case)}
    findings: set[str] = set()
    for reviewer_id in case.get("claimed_counted_reviewers", []):
        if lookup.get(reviewer_id) == "ABSTAIN":
            findings.add("ABSTENTION_COUNTED_AS_APPROVAL")
        elif lookup.get(reviewer_id) == "RECUSE":
            findings.add("RECUSAL_COUNTED_AS_APPROVAL")
    return findings


def quorum_rule(case: dict[str, Any], policy: dict[str, Any]) -> set[str]:
    approvals = eligible_approvals(case)
    findings: set[str] = set()
    if len(approvals) < policy["minimum_approvals"]:
        findings.add("QUORUM_NOT_MET")
    groups = {item.get("independence_group") for item in approvals if item.get("independence_group")}
    if len(groups) < policy["minimum_independent_groups"]:
        findings.add("INDEPENDENCE_VIOLATION")
    return findings


def integrity_rule(case: dict[str, Any], _: dict[str, Any]) -> set[str]:
    findings: set[str] = set()
    if case.get("dissent_required") and not case.get("dissent_preserved"):
        findings.add("DISSENT_NOT_PRESERVED")
    if case.get("decision_record_present"):
        findings.add("REVIEW_PROMOTED_TO_DECISION")
    return findings


RULES: tuple[Rule, ...] = (exact_rule, class_rule, eligibility_rule, claimed_rule, quorum_rule, integrity_rule)


def project(case: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    if case.get("superseded"):
        state, findings = "SUPERSEDED_REVIEW", set()
    elif case.get("appeal_status") == "PENDING":
        state, findings = "APPEAL_REVIEW_PENDING", set()
    else:
        findings = set().union(*(rule(case, policy) for rule in RULES))
        state = "REVIEW_INCOMPLETE" if findings else "REVIEW_COMPLETE_PENDING_DECISION"
    return {"state": state, "reason_codes": sorted(findings), "authority_effect": "none"}


def run(path: Path) -> dict[str, Any]:
    corpus = load_strict(path)
    if not isinstance(corpus, dict) or not isinstance(corpus.get("policy"), dict) or not isinstance(corpus.get("cases"), list):
        raise ValueError("base corpus must contain object policy and array cases")
    canonical_sha256 = _canonical_sha256(corpus)
    mismatches = []
    seen: set[str] = set()
    for case in corpus["cases"]:
        if not isinstance(case, dict):
            raise ValueError("base cases must be objects")
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id or case_id in seen:
            raise ValueError("base case_id values must be unique non-empty strings")
        seen.add(case_id)
        observed = project(case, corpus["policy"])
        expected = dict(case["expected"])
        expected["reason_codes"] = sorted(expected["reason_codes"])
        if observed != expected:
            mismatches.append({"case_id": case_id, "expected": expected, "observed": observed})
    return {
        "consumer": "QSO-STUDIO",
        "profile_id": corpus["profile_id"],
        "case_count": len(corpus["cases"]),
        "result": "PASS" if not mismatches else "FAIL",
        "mismatches": mismatches,
        "authority_effect": "none",
        "canonical_payload_sha256": canonical_sha256,
        "canonical_payload_matches": canonical_sha256 == EXPECTED_CANONICAL_SHA256,
    }


def project_extension(facts: dict[str, bool]) -> tuple[str, list[str]]:
    predicates = (
        (not facts["class_coverage_complete"], "INCOMPLETE_REVIEW_CLASS_COVERAGE"),
        (not facts["common_control_disclosed"], "UNDISCLOSED_COMMON_CONTROL"),
        (not facts["conflicts_and_recusals_resolved"], "UNRESOLVED_CONFLICT_OR_RECUSAL"),
        (facts["incompatible_role_double_count"], "INCOMPATIBLE_ROLE_DOUBLE_COUNT"),
        (facts["appeal_present"] and not facts["appeal_authorized_and_current"], "UNAUTHORIZED_OR_EXPIRED_APPEAL"),
        (facts["appeal_present"] and not facts["appeal_panel_complete_and_independent"], "INCOMPLETE_OR_CONFLICTED_APPEAL_PANEL"),
        (facts["emergency_review_present"] and not facts["emergency_scope_bounded"], "EMERGENCY_SCOPE_BROADENING"),
        (facts["superseded"] and not facts["dependent_findings_invalidated"], "STALE_REVIEW_AFTER_SUPERSESSION"),
    )
    reasons = [reason for reason in EXTENSION_REASON_ORDER if any(active and candidate == reason for active, candidate in predicates)]
    if not reasons:
        return "COVERAGE_EXTENSION_CLEAR", reasons
    if set(reasons) <= {"UNAUTHORIZED_OR_EXPIRED_APPEAL", "INCOMPLETE_OR_CONFLICTED_APPEAL_PANEL"}:
        return "APPEAL_BLOCKED", reasons
    return "REVIEW_INCOMPLETE", reasons


def run_extension(path: Path) -> dict[str, Any]:
    corpus = _exact_keys(load_strict(path), EXTENSION_TOP_KEYS, "extension")
    if corpus["schema"] != "qso.architecture-review-quorum.coverage-extension.corpus.v1":
        raise ValueError("unexpected extension schema")
    if corpus["profile_version"] != "1.0.0" or corpus["data_class"] != "synthetic_only_non_operational":
        raise ValueError("unexpected extension profile metadata")
    link = _exact_keys(corpus["extends"], EXTENSION_LINK_KEYS, "extension.extends")
    expected_link = {
        "fixture": "fixtures/architecture-review-quorum-v1.json",
        "base_case_count": 12,
        "base_fixture_generation": "historical-byte-preserved",
        "contract": "docs/architecture-review-quorum-contract-v0.yaml",
    }
    if link != expected_link:
        raise ValueError("extension linkage drift")
    defaults = _exact_keys(corpus["defaults"], EXTENSION_FACTS, "extension.defaults")
    if any(type(value) is not bool for value in defaults.values()):
        raise ValueError("extension defaults must be Boolean")
    cases = corpus["cases"]
    if not isinstance(cases, list) or len(cases) != 9:
        raise ValueError("extension must contain exactly nine cases")
    seen: set[str] = set()
    covered_reasons: set[str] = set()
    covered_dispositions: set[str] = set()
    mismatches: list[dict[str, Any]] = []
    for index, item in enumerate(cases):
        case = _exact_keys(item, {"id", "overrides", "expected"}, f"extension.cases[{index}]")
        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id or case_id in seen:
            raise ValueError("extension case ids must be unique non-empty strings")
        seen.add(case_id)
        overrides = case["overrides"]
        if not isinstance(overrides, dict) or set(overrides) - EXTENSION_FACTS:
            raise ValueError(f"{case_id}: invalid overrides")
        if any(type(value) is not bool for value in overrides.values()):
            raise ValueError(f"{case_id}: override values must be Boolean")
        expected = _exact_keys(case["expected"], {"disposition", "reasons"}, f"{case_id}.expected")
        if expected["disposition"] not in EXTENSION_DISPOSITIONS:
            raise ValueError(f"{case_id}: unsupported disposition")
        reasons = expected["reasons"]
        if not isinstance(reasons, list) or len(reasons) != len(set(reasons)) or any(reason not in EXTENSION_REASON_ORDER for reason in reasons):
            raise ValueError(f"{case_id}: invalid reason list")
        facts = dict(defaults)
        facts.update(overrides)
        disposition, observed_reasons = project_extension(facts)
        if disposition != expected["disposition"] or observed_reasons != reasons:
            mismatches.append({"case_id": case_id, "expected": expected, "observed": {"disposition": disposition, "reasons": observed_reasons}})
        covered_dispositions.add(expected["disposition"])
        covered_reasons.update(reasons)
    if covered_dispositions != EXTENSION_DISPOSITIONS or covered_reasons != set(EXTENSION_REASON_ORDER):
        raise ValueError("extension does not cover every disposition and reason")
    digest = _canonical_sha256(corpus)
    return {
        "consumer": "QSO-STUDIO",
        "profile_id": corpus["schema"],
        "case_count": len(cases),
        "result": "PASS" if not mismatches else "FAIL",
        "mismatches": mismatches,
        "authority_effect": "none",
        "canonical_payload_sha256": digest,
        "canonical_payload_matches": digest == EXPECTED_EXTENSION_SHA256,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=Path("fixtures/architecture-review-quorum-v1.json"))
    parser.add_argument("--extension", type=Path, default=Path("fixtures/architecture-review-quorum-extension-v1.json"))
    args = parser.parse_args()
    result = {"base": run(args.fixture), "extension": run_extension(args.extension)}
    print(json.dumps(result, indent=2, sort_keys=True))
    accepted = all(item["result"] == "PASS" and item["canonical_payload_matches"] for item in result.values())
    return 0 if accepted else 1


if __name__ == "__main__":
    raise SystemExit(main())
