"""check_site rule 6: docs/ must not link to non-PUBLIC repos."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run(tmp_path, link):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "library.html").write_text(
        '<div class="k">Repos in library</div><div class="v">1</div>'
        '<article class="card" data-slug="a"></article>')
    (docs / "page.md").write_text(f"see https://github.com/tonykoop/{link}\n")
    man = tmp_path / "m.json"
    man.write_text(json.dumps({"entries": [
        {"slug": "a", "visibility": "PUBLIC"},
        {"slug": "priv", "visibility": "PRIVATE"}]}))
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_site.py"),
         "--library", str(docs / "library.html"), "--index", str(docs / "none.html"),
         "--manifest", str(man), "--published", str(tmp_path / "none.txt")],
        capture_output=True, text=True)


def test_private_link_fails(tmp_path):
    r = _run(tmp_path, "priv")
    assert "LINKS" in r.stdout and "priv" in r.stdout


def test_non_manifest_private_fails(tmp_path):
    assert "instrument-maker" in _run(tmp_path, "instrument-maker").stdout


def test_public_link_passes(tmp_path):
    assert "LINKS" not in _run(tmp_path, "a").stdout
