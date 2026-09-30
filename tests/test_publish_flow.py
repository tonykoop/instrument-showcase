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


def test_checked_library_is_the_published_library():
    # generated into docs/library.html (what check_site validates) ...
    assert '--output-html "$SHOWCASE/docs/library.html"' in SH
    assert '--output-data "$SHOWCASE/data/library-manifest.json"' in SH
    # ... and that same file is what the mirror push copies, not a separate temp render.
    assert 'cp "$SHOWCASE/docs/library.html" "$SITE/library.html"' in SH
    assert "hz_library.html" not in SH


def test_generator_runs_before_check_site_and_uses_workspace_for_explorers():
    assert _at('--output-html "$SHOWCASE/docs/library.html"') < _at("scripts/check_site.py")
    assert 'MB_SOURCE_ROOT="$WORKSPACE"' in SH
