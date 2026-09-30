"""generate_library.py: regeneration is byte-identical; pills come from live visibility."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import generate_library  # noqa: E402
import visibility  # noqa: E402

VIS = {"pub-flute": "PUBLIC", "priv-horn": "PRIVATE"}


def _workspace(tmp_path):
    fam = generate_library.INSTRUMENT_FAMILY_DIRS[0]
    for slug, status in (("pub-flute", "private-review"), ("priv-horn", "public")):
        d = tmp_path / "ws" / "instruments" / fam / slug
        d.mkdir(parents=True)
        (d / "capstone-manifest.json").write_text(json.dumps({"title": slug, "release_status": status}))
    return tmp_path / "ws"


def _gen(tmp_path, ws, monkeypatch, *extra):
    monkeypatch.setattr(visibility, "repo_visibility", lambda s: VIS[s])
    out = tmp_path / "out"
    rc = generate_library.main(["--workspace", str(ws), "--output-html", str(out / "library.html"),
                                "--output-data", str(out / "m.json"), *extra])
    assert rc == 0
    return (out / "library.html").read_bytes(), (out / "m.json").read_bytes()


def test_two_runs_byte_identical(tmp_path, monkeypatch):
    ws = _workspace(tmp_path)
    first = _gen(tmp_path, ws, monkeypatch)
    second = _gen(tmp_path, ws, monkeypatch)
    assert first == second


def test_pills_follow_visibility_and_private_not_rendered(tmp_path, monkeypatch):
    ws = _workspace(tmp_path)
    html, data = _gen(tmp_path, ws, monkeypatch)
    entries = {e["slug"]: e for e in json.loads(data)["entries"]}
    assert entries["pub-flute"]["status"] == "public"      # was private-review in its own manifest
    assert entries["priv-horn"]["status"] == "private"     # was public in its own manifest
    assert entries["priv-horn"]["visibility"] == "PRIVATE"
    assert b"priv-horn" not in html and b"pub-flute" in html


def test_content_change_bumps_timestamp(tmp_path, monkeypatch):
    ws = _workspace(tmp_path)
    _gen(tmp_path, ws, monkeypatch, "--generated-at", "2020-01-01T00:00:00Z")
    monkeypatch.setitem(VIS, "pub-flute", "PRIVATE")
    _, data = _gen(tmp_path, ws, monkeypatch)
    assert json.loads(data)["generated_at"] != "2020-01-01T00:00:00Z"
