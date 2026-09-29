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
