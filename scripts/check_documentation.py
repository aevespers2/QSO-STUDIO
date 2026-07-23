#!/usr/bin/env python3
"""Fail-closed documentation checks for the QSO-STUDIO charter candidate."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
    "docs/onboarding.md",
    "docs/developer-guide.md",
    "docs/accessibility.md",
    "docs/security-privacy.md",
]
PLANNING_MARKER = "QSO-STUDIO-DOCS-CANDIDATE-001"
CONSENT_MARKER = "QSO-CONSENT-CAPACITY-LOCK-v1"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check() -> list[str]:
    errors: list[str] = []
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

    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    if "published" in readme.lower() and "not published" not in readme.lower():
        errors.append("README contains an unsupported publication claim")

    release = (ROOT / "release.md").read_text(encoding="utf-8") if (ROOT / "release.md").is_file() else ""
    taskchain = (ROOT / "taskchain.md").read_text(encoding="utf-8") if (ROOT / "taskchain.md").is_file() else ""
    punchlist = (ROOT / "punchlist.md").read_text(encoding="utf-8") if (ROOT / "punchlist.md").is_file() else ""
    changelog = (ROOT / "changelog.md").read_text(encoding="utf-8") if (ROOT / "changelog.md").is_file() else ""
    for name, text in {"release.md": release, "taskchain.md": taskchain, "punchlist.md": punchlist, "changelog.md": changelog}.items():
        if "documentation candidate" not in text.lower():
            errors.append(f"{name} does not describe the documentation candidate")
        if "publication" not in text.lower():
            errors.append(f"{name} omits publication boundary")

    return sorted(set(errors))


def main() -> int:
    errors = check()
    report = {
        "profile": PLANNING_MARKER,
        "required_files": len(REQUIRED),
        "status": "PASS" if not errors else "FAIL_CLOSED",
        "errors": errors,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
