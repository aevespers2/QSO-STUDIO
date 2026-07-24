#!/usr/bin/env python3
"""Fail-closed documentation checks for the QSO-STUDIO charter candidate."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACCESSIBILITY_EVIDENCE = "docs/accessibility-review-evidence.md"
REQUIRED = [
    "README.md",
    "taskchain.md",
    "release.md",
    "punchlist.md",
    "changelog.md",
    "docs/index.md",
    "docs/product-charter.md",
    "docs/architecture.md",
    "docs/read-only-review-workflow.md",
    "docs/integration-contracts.md",
    "docs/ecosystem-conformance-consumer.md",
    "docs/onboarding.md",
    "docs/developer-guide.md",
    "docs/accessibility.md",
    ACCESSIBILITY_EVIDENCE,
    "docs/security-privacy.md",
]
PLANNING_MARKER = "QSO-STUDIO-DOCS-CANDIDATE-001"
CONSENT_MARKER = "QSO-CONSENT-CAPACITY-LOCK-v1"
ACCESSIBILITY_STATUS = "DOCUMENTED_NOT_CERTIFIED"
EVIDENCE_STATES = {
    "NOT_REVIEWED",
    "PARTIAL",
    "PASS",
    "FAIL",
    "BLOCKED",
    "UNKNOWN",
    "SUPERSEDED",
    "WITHDRAWN",
    "CORRECTED",
}
AUTHORITY_CLASSES = {
    "OBSERVATION",
    "INTERPRETATION",
    "ANNOTATION",
    "PROPOSAL",
    "REVIEW_DIAGNOSTIC",
    "HUMAN_DISPOSITION",
    "EXTERNAL_ACTION",
}
DENIED_AUTHORITY_FLAGS = {
    "certifies_accessibility: false",
    "approves_pages_publication: false",
    "approves_product_charter: false",
    "approves_release: false",
    "grants_runtime_authority: false",
    "grants_repository_write: false",
    "appoints_reviewers: false",
    "decides_architecture: false",
    "grants_payment_authority: false",
}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check() -> list[str]:
    errors: list[str] = []
    loaded: dict[str, str] = {}
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing required file: {rel}")
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
        except UnicodeDecodeError:
            errors.append(f"invalid UTF-8: {rel}")
            continue
        loaded[rel] = text
        if rel.endswith(".md") and not re.search(r"^#\s+\S", text, re.M):
            errors.append(f"missing H1: {rel}")
        if rel.startswith("docs/") and CONSENT_MARKER not in text:
            errors.append(f"missing consent/governance binding: {rel}")
        if rel in {"README.md", "taskchain.md", "release.md", "punchlist.md", "changelog.md"} and PLANNING_MARKER not in text:
            errors.append(f"missing planning alignment marker: {rel}")
        if "```mermaid" in text and "Equivalent prose" not in text:
            errors.append(f"diagram lacks equivalent prose: {rel}")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {rel} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken internal link: {rel} -> {target}")

    readme = loaded.get("README.md", "")
    if "published" in readme.lower() and "not published" not in readme.lower():
        errors.append("README contains an unsupported publication claim")

    release = loaded.get("release.md", "")
    taskchain = loaded.get("taskchain.md", "")
    punchlist = loaded.get("punchlist.md", "")
    changelog = loaded.get("changelog.md", "")
    for name, text in {
        "release.md": release,
        "taskchain.md": taskchain,
        "punchlist.md": punchlist,
        "changelog.md": changelog,
    }.items():
        if "documentation candidate" not in text.lower():
            errors.append(f"{name} does not describe the documentation candidate")
        if "publication" not in text.lower():
            errors.append(f"{name} omits publication boundary")
        if "accessibility" not in text.lower() or "evidence" not in text.lower():
            errors.append(f"{name} omits accessibility-evidence alignment")

    evidence = loaded.get(ACCESSIBILITY_EVIDENCE, "")
    if evidence:
        if ACCESSIBILITY_STATUS not in evidence:
            errors.append("accessibility evidence omits documented-not-certified status")
        for state in sorted(EVIDENCE_STATES):
            if state not in evidence:
                errors.append(f"accessibility evidence omits state: {state}")
        for authority_class in sorted(AUTHORITY_CLASSES):
            if authority_class not in evidence:
                errors.append(f"accessibility evidence omits authority class: {authority_class}")
        for flag in sorted(DENIED_AUTHORITY_FLAGS):
            if flag not in evidence:
                errors.append(f"accessibility evidence omits denied authority flag: {flag}")
        if "200%" not in evidence or "400%" not in evidence:
            errors.append("accessibility evidence omits 200%/400% zoom review")
        if "screen reader" not in evidence.lower():
            errors.append("accessibility evidence omits screen-reader review")
        if "correction" not in evidence.lower() or "supersession" not in evidence.lower():
            errors.append("accessibility evidence omits correction/supersession handling")

    return sorted(set(errors))


def main() -> int:
    errors = check()
    report = {
        "profile": PLANNING_MARKER,
        "required_files": len(REQUIRED),
        "accessibility_status": ACCESSIBILITY_STATUS,
        "status": "PASS" if not errors else "FAIL_CLOSED",
        "errors": errors,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
