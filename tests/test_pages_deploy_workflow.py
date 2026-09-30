"""The deploy workflow must gate on check_site and publish exactly /docs from main (#194)."""
from pathlib import Path

import yaml

WF = Path(__file__).resolve().parent.parent / ".github" / "workflows" / "pages-deploy.yml"


def _wf():
    return yaml.safe_load(WF.read_text())


def test_triggers_on_main_only():
    on = _wf()[True]  # PyYAML parses the bare key `on` as True
    assert on["push"]["branches"] == ["main"]
    assert "pull_request" not in on


def test_deploy_needs_green_check():
    jobs = _wf()["jobs"]
    assert jobs["deploy"]["needs"] == "check"
    runs = " ".join(s.get("run", "") for s in jobs["check"]["steps"])
    assert "scripts/check_site.py" in runs


def test_uploads_docs_with_pages_permissions():
    wf = _wf()
    assert wf["permissions"]["pages"] == "write" and wf["permissions"]["id-token"] == "write"
    up = [s for s in wf["jobs"]["deploy"]["steps"] if "upload-pages-artifact" in s.get("uses", "")]
    assert up and up[0]["with"]["path"] == "docs"
    assert wf["jobs"]["deploy"]["environment"]["name"] == "github-pages"
