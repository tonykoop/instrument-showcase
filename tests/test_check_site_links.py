"""check_site rule 6: docs/ must not link to non-PUBLIC or unverifiable repos."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_site  # noqa: E402
import visibility  # noqa: E402


def _run(tmp_path, monkeypatch, link, live):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "library.html").write_text(
        '<div class="k">Repos in library</div><div class="v">1</div>'
        '<article class="card" data-slug="a"></article>')
    (docs / "page.md").write_text(f"see https://github.com/tonykoop/{link}\n")
    man = tmp_path / "m.json"
    man.write_text(json.dumps({"entries": [
        {"slug": "a", "visibility": "PUBLIC"}, {"slug": "priv", "visibility": "PRIVATE"}]}))
    monkeypatch.setattr(check_site, "repo_visibility", live)
    return check_site.main(["--library", str(docs / "library.html"), "--index", str(docs / "none.html"),
                            "--manifest", str(man), "--published", str(tmp_path / "none.txt")])


def _no_live(slug):
    raise AssertionError("manifest-known repo must not trigger a live lookup")


def test_manifest_private_link_fails(tmp_path, monkeypatch, capsys):
    assert _run(tmp_path, monkeypatch, "priv", _no_live) == 1
    assert "LINKS" in capsys.readouterr().out


def test_manifest_public_link_passes(tmp_path, monkeypatch, capsys):
    _run(tmp_path, monkeypatch, "a", _no_live)
    assert "LINKS" not in capsys.readouterr().out


def test_unknown_private_repo_fails(tmp_path, monkeypatch, capsys):
    assert _run(tmp_path, monkeypatch, "not-in-manifest", lambda s: "PRIVATE") == 1
    assert "not-in-manifest [PRIVATE]" in capsys.readouterr().out


def test_unknown_repo_lookup_failure_fails_closed(tmp_path, monkeypatch, capsys):
    def boom(slug):
        raise visibility.VisibilityError(f"{slug}: gh repo view failed")
    assert _run(tmp_path, monkeypatch, "not-in-manifest", boom) == 1
    assert "visibility unknown" in capsys.readouterr().out


def test_unknown_public_repo_passes(tmp_path, monkeypatch, capsys):
    _run(tmp_path, monkeypatch, "not-in-manifest", lambda s: "PUBLIC")
    assert "LINKS" not in capsys.readouterr().out


@pytest.mark.parametrize("vis", ["INTERNAL"])
def test_internal_is_non_public(tmp_path, monkeypatch, vis):
    assert _run(tmp_path, monkeypatch, "x", lambda s: vis) == 1
