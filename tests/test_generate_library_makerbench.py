"""generate_library.py: the MakerBench badge and the Run tonight link (tonykoop/makerbench-hwe#1112)."""
import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import generate_library  # noqa: E402
import visibility  # noqa: E402


def _promotion(repo: Path, stamp: str, tool: str, route: str, checks: str, promoted: str) -> dict:
    folder = f"cad/makerbench/{stamp}-{tool.lower()}"
    (repo / folder).mkdir(parents=True)
    (repo / folder / "provenance.json").write_text(json.dumps(
        {"schema": "makerbench-control-room-promotion-v1", "entrant": tool, "tool_and_model": route,
         "checks_passed": checks, "promoted_utc": promoted}))
    (repo / folder / "x.glb").write_bytes(b"glTF")
    return {"promoted_utc": promoted, "tool_and_model": route, "checks_passed": checks, "folder": folder,
            "glb": f"{folder}/x.glb", "hero": None}


def _workspace(tmp_path: Path) -> Path:
    """Synthetic repos: one with three promotions, one with none, one with a hostile provenance."""
    fam = generate_library.INSTRUMENT_FAMILY_DIRS[0]
    ws = tmp_path / "ws"
    kora = ws / "instruments" / fam / "kora"
    kora.mkdir(parents=True)
    (kora / "explorer.html").write_text("<html></html>")
    promotions = [
        _promotion(kora, "20261017", "CADAM", "OpenRouter · Claude Fable 5.1 · OpenSCAD", "4/5", "2026-10-17T05:00:00+00:00"),
        _promotion(kora, "20261018", "FreeCAD", "Claude Code · Opus 5.5 · subscription", "5/5", "2026-10-18T05:00:00+00:00"),
        _promotion(kora, "20261019", "SolidWorks", "Codex · GPT-6.1 Sol · live bridge", "4/5", "2026-10-19T05:00:00+00:00"),
    ]
    (kora / "capstone-manifest.json").write_text(json.dumps({"title": "Kora", "makerbench_promotions": promotions}))
    lyre = ws / "instruments" / fam / "lyre"
    lyre.mkdir(parents=True)
    (lyre / "capstone-manifest.json").write_text(json.dumps({"title": "Lyre"}))
    erhu = ws / "instruments" / fam / "erhu"
    erhu.mkdir(parents=True)
    bad = {"promoted_utc": "2026-10-18T05:00:00+00:00", "checks_passed": "5/5", "folder": "../../kora/cad/makerbench/20261018-freecad",
           "tool_and_model": '<img src=x onerror="alert(1)"> · Model'}
    (erhu / "capstone-manifest.json").write_text(json.dumps({"title": "Erhu", "makerbench_promotions": [bad]}))
    return ws


def _gen(tmp_path, ws, monkeypatch, *extra):
    monkeypatch.setattr(visibility, "repo_visibility", lambda s: "PUBLIC")
    out = tmp_path / "out"
    assert generate_library.main(["--workspace", str(ws), "--output-html", str(out / "library.html"),
                                  "--output-data", str(out / "m.json"), *extra]) == 0
    return (out / "library.html").read_text(), json.loads((out / "m.json").read_text())


def test_best_promoted_design_wins_on_checks_then_date(tmp_path, monkeypatch):
    html, data = _gen(tmp_path, _workspace(tmp_path), monkeypatch)
    entries = {e["slug"]: e for e in data["entries"]}
    assert entries["kora"]["makerbench"]["tool"] == "FreeCAD"  # 5/5 beats the later 4/5
    assert entries["kora"]["makerbench"]["model"] == "Opus 5.5"
    assert entries["lyre"]["makerbench"] == {}
    assert "MakerBench · FreeCAD/Opus 5.5 · 5/5 checks · 18 Oct" in html
    assert html.count("MakerBench · ") == 2  # kora, and erhu (text only, see below)


def test_badge_links_to_the_explorer_3d_view_when_published(tmp_path, monkeypatch):
    ws = _workspace(tmp_path)
    published = tmp_path / "published.txt"
    published.write_text("kora\n")
    html, _ = _gen(tmp_path, ws, monkeypatch, "--base-url", "https://tonykoop.github.io", "--published", str(published))
    assert 'href="https://tonykoop.github.io/kora/explorer.html#cad"' in html
    # Without the promoted .glb on disk there is no 3D view of it: the badge opens the explorer page.
    (ws / "instruments" / generate_library.INSTRUMENT_FAMILY_DIRS[0] / "kora" / "cad" / "makerbench"
     / "20261018-freecad" / "x.glb").unlink()
    html, _ = _gen(tmp_path, ws, monkeypatch, "--base-url", "https://tonykoop.github.io", "--published", str(published))
    assert 'href="https://tonykoop.github.io/kora/explorer.html"' in html and "explorer.html#cad" not in html


def test_provenance_outside_the_repo_is_never_read_and_text_is_escaped(tmp_path, monkeypatch):
    html, data = _gen(tmp_path, _workspace(tmp_path), monkeypatch)
    erhu = {e["slug"]: e for e in data["entries"]}["erhu"]["makerbench"]
    assert erhu["tool"] == '<img src=x onerror="alert(1)">'  # from the manifest; the ../ provenance is ignored
    assert '<img src=x onerror="alert(1)">' not in html
    assert "&lt;img src=x onerror=&quot;alert(1)&quot;&gt;/Model" in html


def test_run_tonight_is_hidden_and_opt_in_only(tmp_path, monkeypatch):
    html, _ = _gen(tmp_path, _workspace(tmp_path), monkeypatch)
    assert html.count('class="card-run-tonight"') == 3 and html.count(" hidden>Run tonight</a>") == 3
    script = generate_library.RUN_TONIGHT_JS
    # No probe happens until this browser opted in with ?control-room=<port>.
    assert script.index("if(!port") < script.index("img.src=base")
    assert "fetch(" not in script and "no-cors" not in script
    assert "127.0.0.1" in script and "localhost" not in script


def test_regeneration_stays_byte_identical(tmp_path, monkeypatch):
    ws = _workspace(tmp_path)
    first = _gen(tmp_path, ws, monkeypatch, "--generated-at", "2026-10-20T00:00:00Z")
    second = _gen(tmp_path, ws, monkeypatch, "--generated-at", "2026-10-20T00:00:00Z")
    assert first == second


@pytest.mark.skipif(os.name != "posix", reason="symlinks")
def test_a_symlinked_provenance_is_ignored(tmp_path):
    repo = tmp_path / "repo"
    (repo / "cad" / "makerbench").mkdir(parents=True)
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "provenance.json").write_text(json.dumps({"entrant": "LEAKED", "tool_and_model": "x · y"}))
    (repo / "cad" / "makerbench" / "d").symlink_to(outside, target_is_directory=True)
    manifest = {"makerbench_promotions": [{"promoted_utc": "2026-10-18T00:00:00+00:00", "checks_passed": "5/5",
                                           "folder": "cad/makerbench/d", "tool_and_model": "FreeCAD · Opus 5.5"}]}
    assert generate_library.best_makerbench_design(repo, manifest)["tool"] == "FreeCAD"


def test_the_explorer_shows_the_promoted_model_ahead_of_an_older_one(tmp_path):
    import generate_explorer_v2 as ex

    ws = _workspace(tmp_path)
    kora = ws / "instruments" / generate_library.INSTRUMENT_FAMILY_DIRS[0] / "kora"
    (kora / "cad" / "old-model.glb").write_bytes(b"glTF" * 1000)  # bigger, older, top-level
    data = ex.gather(kora, generate_library.INSTRUMENT_FAMILY_DIRS[0], {})
    assert data.glb_rel == "cad/makerbench/20261018-freecad/x.glb"  # the best promotion (5/5)
    page = ex.render_explorer(data)
    assert 'id="cad"' in page and "cad/makerbench/20261018-freecad/x.glb" in page and "old-model.glb" not in page
    # A promotion pointing outside the repo or through a symlink is never shown.
    manifest = json.loads((kora / "capstone-manifest.json").read_text())
    for item in manifest["makerbench_promotions"]:
        item["glb"] = "../../elsewhere/x.glb"
    (kora / "capstone-manifest.json").write_text(json.dumps(manifest))
    assert ex.gather(kora, generate_library.INSTRUMENT_FAMILY_DIRS[0], {}).glb_rel == "cad/old-model.glb"


_PROBE_HARNESS = r"""
const vm = require('vm');
const [script, scenario] = [process.argv[1], process.argv[2]];
const links = [{hidden: true, href: '', attrs: {'data-slug': 'kora'}, getAttribute(k) { return this.attrs[k]; }}];
const images = [];
class FakeImage { constructor() { images.push(this); }
  set src(v) { this._src = v; if (!v) return;
    if (scenario === 'beacon') { this.naturalWidth = 23; this.naturalHeight = 7; this.onload(); }
    else if (scenario === 'other-image') { this.naturalWidth = 1; this.naturalHeight = 1; this.onload(); }
    else if (scenario === 'error') { this.onerror(); } } get src() { return this._src; } }
const store = {'makerbench-control-room': scenario === 'not-opted-in' ? null : '8080'};
const ctx = {Image: FakeImage, Date, setTimeout: (f) => 0, clearTimeout() {}, encodeURIComponent, URLSearchParams,
  location: {search: ''}, localStorage: {getItem: (k) => store[k] ?? null, setItem() {}, removeItem() {}},
  document: {querySelectorAll: () => links}, window: {}};
vm.runInNewContext(script.replace(/^<script>|<\/script>\s*$/g, ''), ctx);
console.log(JSON.stringify({hidden: links[0].hidden, href: links[0].href, probes: images.length,
  src: images[0] && images[0].src}));
"""


@pytest.mark.parametrize("scenario, revealed, probes", [
    ("beacon", True, 1),          # Control Room's exact 23x7 beacon decoded
    ("other-image", False, 1),    # some other server's image on that port
    ("error", False, 1),          # 404, refused connection, not an image
    ("not-opted-in", False, 0),   # a public visitor: no probe at all
])
def test_run_tonight_appears_only_for_the_control_room_beacon(scenario, revealed, probes):
    import shutil
    import subprocess

    node = shutil.which("node")
    if node is None:
        pytest.skip("node is not installed")
    out = subprocess.run([node, "-e", _PROBE_HARNESS, generate_library.RUN_TONIGHT_JS, scenario],
                         capture_output=True, text=True, check=True).stdout
    result = json.loads(out)
    assert result["hidden"] is (not revealed) and result["probes"] == probes
    if probes:
        assert result["src"].startswith("http://127.0.0.1:8080/api/control-room/beacon.png?t=")
    if revealed:
        assert result["href"] == "http://127.0.0.1:8080/#/newrun?instrument=kora"
