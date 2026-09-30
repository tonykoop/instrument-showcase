"""publish.sh chains sync -> build -> visibility gate -> check_site -> push (#195)."""
from pathlib import Path

SH = (Path(__file__).resolve().parent.parent / "scripts" / "publish.sh").read_text()


def _at(needle):
    assert needle in SH, needle
    return SH.index(needle)


def test_gates_run_before_any_push():
    order = [_at("sync_manifest_visibility.py"), _at("build_pages.py"),
             _at("scripts/visibility.py"), _at("scripts/check_site.py"),
             _at("git -C \"$SITE\" push")]
    assert order == sorted(order)
    assert _at("git -C \"$SHOWCASE\" push") > _at("scripts/check_site.py")


def test_fails_fast():
    assert "set -euo pipefail" in SH
