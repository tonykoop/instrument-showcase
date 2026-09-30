import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from visibility import VisibilityError, public_slugs


def test_only_public_kept():
    vis = {"a": "PUBLIC", "b": "PRIVATE", "c": "INTERNAL"}
    assert public_slugs(vis, lookup=vis.__getitem__) == (["a"], ["b", "c"])


def test_unknown_visibility_fails_loudly():
    def lookup(s):
        if s == "x":
            raise VisibilityError("x: gh repo view failed")
        return "PUBLIC"
    with pytest.raises(VisibilityError, match="x: gh repo view failed"):
        public_slugs(["a", "x"], lookup=lookup)


def test_check_published_flags_private(tmp_path):
    from visibility import check_published
    f = tmp_path / "published.txt"
    f.write_text("a\nb\n")
    vis = {"a": "PUBLIC", "b": "PRIVATE"}
    assert check_published(f, lookup=vis.__getitem__) == ["b"]


def test_check_published_unknown_fails(tmp_path):
    from visibility import check_published
    f = tmp_path / "published.txt"
    f.write_text("a\n")

    def boom(s):
        raise VisibilityError("a: gh repo view failed")
    with pytest.raises(VisibilityError):
        check_published(f, lookup=boom)


def test_cli_exit_codes(tmp_path, monkeypatch):
    import visibility
    f = tmp_path / "published.txt"
    f.write_text("a\nb\n")
    monkeypatch.setattr(visibility, "repo_visibility", lambda s: "PRIVATE" if s == "b" else "PUBLIC")
    assert visibility.main(["--published", str(f)]) == 1
