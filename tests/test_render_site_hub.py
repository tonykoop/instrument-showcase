from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "render_site_hub.py"
SPEC = importlib.util.spec_from_file_location("render_site_hub", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class RenderSiteHubTests(unittest.TestCase):
    def test_resolve_reference_supports_workspace_root_paths(self) -> None:
        manifest_path = REPO_ROOT / "data" / "deliverables-manifest.json"
        resolved = MODULE.resolve_reference("/docs/plans/2026-05-17-instrument-wolfram-site-r24/matrix.md", manifest_path)
        self.assertEqual(
            resolved,
            MODULE.WORKSPACE_ROOT / "docs" / "plans" / "2026-05-17-instrument-wolfram-site-r24" / "matrix.md",
        )

    def test_resolve_reference_supports_repo_root_relative_paths(self) -> None:
        manifest_path = REPO_ROOT / "data" / "deliverables-manifest.json"
        resolved = MODULE.resolve_reference("../clarinet/design.md", manifest_path)
        self.assertEqual(
            resolved,
            MODULE.WORKSPACE_ROOT / "clarinet" / "design.md",
        )

    def test_render_site_generates_index_detail_and_manifest_pages(self) -> None:
        manifest_path = REPO_ROOT / "data" / "deliverables-manifest.json"
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir) / "site"
            MODULE.render_site(manifest_path, output_dir)

            index_html = (output_dir / "index.html").read_text(encoding="utf-8")
            detail_html = (output_dir / "instruments" / "clarinet.html").read_text(encoding="utf-8")
            manifest_html = (output_dir / "manifest.html").read_text(encoding="utf-8")

            self.assertIn("Instrument Deliverables Hub", index_html)
            self.assertIn("Clarinet", detail_html)
            self.assertIn("Deliverables manifest", manifest_html)
            self.assertTrue((output_dir / "assets" / "hub.css").exists())
            self.assertTrue((output_dir / "assets" / "deliverables-manifest.json").exists())

    def test_render_site_uses_canonical_relative_links(self) -> None:
        manifest_path = REPO_ROOT / "data" / "deliverables-manifest.json"
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir) / "site"
            MODULE.render_site(manifest_path, output_dir)

            index_html = (output_dir / "index.html").read_text(encoding="utf-8")
            detail_html = (output_dir / "instruments" / "clarinet.html").read_text(encoding="utf-8")

            self.assertIn('href="../../docs/plans/2026-05-17-instrument-wolfram-site-r24/matrix.md"', index_html)
            self.assertIn('href="../../clarinet"', index_html)
            self.assertIn('href="../../../clarinet"', detail_html)
            self.assertIn('href="../../../clarinet/design.md"', detail_html)

    def test_render_site_does_not_emit_local_filesystem_paths(self) -> None:
        manifest_path = REPO_ROOT / "data" / "deliverables-manifest.json"
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir) / "site"
            MODULE.render_site(manifest_path, output_dir)

            generated = "\n".join(
                path.read_text(encoding="utf-8")
                for path in output_dir.rglob("*")
                if path.is_file() and path.suffix in {".html", ".json"}
            )
            forbidden_fragments = ["/mnt/", "/tmp/", "/home/", "/Users/", "file://", "C:\\"]
            for fragment in forbidden_fragments:
                self.assertNotIn(fragment, generated)

    def test_availability_check_is_status_filter_not_readiness_filter(self) -> None:
        manifest_path = REPO_ROOT / "data" / "deliverables-manifest.json"
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir) / "site"
            MODULE.render_site(manifest_path, output_dir)

            index_html = (output_dir / "index.html").read_text(encoding="utf-8")

            self.assertIn('data-filter-group="status" data-filter-value="availability-check"', index_html)
            self.assertNotIn('data-filter-group="readiness" data-filter-value="availability-check"', index_html)


if __name__ == "__main__":
    unittest.main()
