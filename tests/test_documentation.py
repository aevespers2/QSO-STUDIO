from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "check_documentation.py"
spec = importlib.util.spec_from_file_location("check_documentation", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class DocumentationIntegrityTests(unittest.TestCase):
    def write_baseline(self, root: Path) -> None:
        for rel in module.REQUIRED:
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            if rel.startswith("docs/"):
                path.write_text(f"# Page\n\n{module.CONSENT_MARKER}\n", encoding="utf-8")
            else:
                path.write_text(
                    f"# Control\n\n{module.PLANNING_MARKER}\n\nDocumentation candidate. Publication remains blocked.\n",
                    encoding="utf-8",
                )

    def run_check(self, root: Path):
        with mock.patch.object(module, "ROOT", root):
            return module.check()

    def test_repository_candidate_passes(self):
        self.assertEqual(module.check(), [])

    def test_missing_required_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            (root / "docs" / "architecture.md").unlink()
            self.assertTrue(any("missing required file" in x for x in self.run_check(root)))

    def test_invalid_utf8_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            (root / "docs" / "index.md").write_bytes(b"# x\n\xff")
            self.assertTrue(any("invalid UTF-8" in x for x in self.run_check(root)))

    def test_broken_link_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            p = root / "docs" / "index.md"
            p.write_text(f"# Page\n\n[Missing](missing.md)\n\n{module.CONSENT_MARKER}\n", encoding="utf-8")
            self.assertTrue(any("broken internal link" in x for x in self.run_check(root)))

    def test_link_escape_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            p = root / "docs" / "index.md"
            p.write_text(f"# Page\n\n[Escape](../../outside.md)\n\n{module.CONSENT_MARKER}\n", encoding="utf-8")
            self.assertTrue(any("link escapes repository" in x for x in self.run_check(root)))

    def test_missing_diagram_prose_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            p = root / "docs" / "architecture.md"
            p.write_text(f"# Architecture\n\n```mermaid\nflowchart LR\nA-->B\n```\n{module.CONSENT_MARKER}\n", encoding="utf-8")
            self.assertTrue(any("diagram lacks equivalent prose" in x for x in self.run_check(root)))

    def test_missing_governance_binding_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            (root / "docs" / "index.md").write_text("# Page\n", encoding="utf-8")
            self.assertTrue(any("missing consent/governance binding" in x for x in self.run_check(root)))

    def test_missing_planning_marker_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            (root / "release.md").write_text("# Release\n\nDocumentation candidate. Publication blocked.\n", encoding="utf-8")
            self.assertTrue(any("missing planning alignment marker" in x for x in self.run_check(root)))

    def test_unsupported_publication_claim_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.write_baseline(root)
            (root / "README.md").write_text(
                f"# Studio\n\n{module.PLANNING_MARKER}\n\nThe project is published from docs. Documentation candidate. Publication evidence pending.\n",
                encoding="utf-8",
            )
            self.assertTrue(any("unsupported publication claim" in x for x in self.run_check(root)))


if __name__ == "__main__":
    unittest.main()
