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

CHECK_MODULE_PATH = REPO_ROOT / "scripts" / "check_site_hub.py"
CHECK_SPEC = importlib.util.spec_from_file_location("check_site_hub", CHECK_MODULE_PATH)
CHECK_MODULE = importlib.util.module_from_spec(CHECK_SPEC)
assert CHECK_SPEC and CHECK_SPEC.loader
CHECK_SPEC.loader.exec_module(CHECK_MODULE)


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

    def test_checked_in_site_hub_check_passes_on_rendered_output(self) -> None:
        manifest_path = REPO_ROOT / "data" / "deliverables-manifest.json"
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir) / "site"
            MODULE.render_site(manifest_path, output_dir)

            self.assertEqual([], CHECK_MODULE.run_checks(output_dir))

    def test_site_hub_check_catches_local_paths_and_stale_availability(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            site_dir = Path(tmp_dir) / "site"
            (site_dir / "assets").mkdir(parents=True)
            (site_dir / "index.html").write_text(
                '<a href="/mnt/c/Users/Tony/Documents/GitHub/clarinet">bad</a>\n'
                '<button data-filter-group="readiness" data-filter-value="availability-check">bad</button>\n',
                encoding="utf-8",
            )
            (site_dir / "assets" / "deliverables-manifest.json").write_text(
                '{"items": [{"slug": "sambuca", "readiness_label": "availability-check"}]}\n',
                encoding="utf-8",
            )

            findings = CHECK_MODULE.run_checks(site_dir)

        self.assertTrue(any("/mnt/" in finding for finding in findings))
        self.assertTrue(any("readiness filter" in finding for finding in findings))
        self.assertTrue(any("readiness_label" in finding for finding in findings))


if __name__ == "__main__":
    unittest.main()
