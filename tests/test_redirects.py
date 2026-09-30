"""build_pages.write_redirects: moved slugs keep working via meta-refresh stubs."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_pages  # noqa: E402

SLUGS = ("steel-tongue-drum", "tongue-drum", "wood-shell-tongue-drum")


def test_moved_table_covers_issue_slugs():
    assert {s for (_, s) in build_pages.MOVED} == set(SLUGS)
    assert all(old == "idiophones" and new == "percussion" for (old, _), new in build_pages.MOVED.items())


def test_stub_resolves_to_new_page(tmp_path):
    for s in SLUGS:
        d = tmp_path / "instruments" / "percussion" / s
        d.mkdir(parents=True)
        (d / "explorer.html").write_text("<html>new</html>")
    assert build_pages.write_redirects(str(tmp_path)) == 3
    for s in SLUGS:
        for name in ("explorer.html", "index.html"):
            stub = tmp_path / "instruments" / "idiophones" / s / name
            html = stub.read_text()
            target = re.search(r'http-equiv="refresh" content="0; url=([^"]+)"', html).group(1)
            assert f'<a href="{target}">' in html          # visible link fallback
            assert (stub.parent / target).resolve().read_text() == "<html>new</html>"


def test_no_stub_when_target_missing(tmp_path):
    assert build_pages.write_redirects(str(tmp_path)) == 0
    assert not (tmp_path / "instruments" / "idiophones").exists()
