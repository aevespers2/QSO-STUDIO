#!/usr/bin/env python3
"""Independent QSO-STUDIO consumer for the architecture-review quorum corpus.

The implementation deliberately uses a rule pipeline rather than the reference
evaluator's control flow. Matching outcomes are synthetic conformance evidence,
not appointment, quorum, architecture-decision, or activation authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

APPROVAL = frozenset(("APPROVE", "APPROVE_WITH_CONDITIONS"))
EXPECTED_CANONICAL_SHA256 = "a8b65c3fce4b7cf80fdefab76c497720b2bf17086d431a53f9bacf82e58bd9ec"
Rule = Callable[[dict[str, Any], dict[str, Any]], set[str]]


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
    independent_groups = {item.get("independence_group") for item in approvals if item.get("independence_group")}
    if len(independent_groups) < policy["minimum_independent_groups"]:
        findings.add("INDEPENDENCE_VIOLATION")
    return findings


def integrity_rule(case: dict[str, Any], _: dict[str, Any]) -> set[str]:
    findings: set[str] = set()
    if case.get("dissent_required") and not case.get("dissent_preserved"):
        findings.add("DISSENT_NOT_PRESERVED")
    if case.get("decision_record_present"):
        findings.add("REVIEW_PROMOTED_TO_DECISION")
    return findings


RULES: tuple[Rule, ...] = (
    exact_rule,
    class_rule,
    eligibility_rule,
    claimed_rule,
    quorum_rule,
    integrity_rule,
)


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
    corpus = json.loads(path.read_text(encoding="utf-8"))
    canonical = json.dumps(corpus, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    canonical_sha256 = hashlib.sha256(canonical).hexdigest()
    mismatches = []
    for case in corpus["cases"]:
        observed = project(case, corpus["policy"])
        expected = dict(case["expected"])
        expected["reason_codes"] = sorted(expected["reason_codes"])
        if observed != expected:
            mismatches.append({"case_id": case["case_id"], "expected": expected, "observed": observed})
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=Path("fixtures/architecture-review-quorum-v1.json"))
    args = parser.parse_args()
    result = run(args.fixture)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["result"] == "PASS" and result["canonical_payload_matches"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
