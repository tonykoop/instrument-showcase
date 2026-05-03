#!/usr/bin/env python3
"""
instrument-showcase — render.py

Render a Heifer Zephyr showcase document for an instrument folder.

Usage:
    python render.py <instrument-folder> <doc-type>

Example:
    python render.py ~/Documents/GitHub/tongue-drum 01-brochure

This script reads the instrument folder, pulls the fields declared in the
template's content-spec.yaml, and emits the rendered HTML to:

    <instrument-folder>/showcase/<output_filename>

Then point Claude Design at the brand/ folder + the rendered output for the
final styling/polish pass.
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "ERROR: pyyaml is required.  pip install pyyaml\n"
    )
    sys.exit(1)

try:
    import chevron  # Mustache-compatible
    HAVE_CHEVRON = True
except ImportError:
    HAVE_CHEVRON = False


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_ROOT / "templates"


# ─── Family → accent class derivation ───────────────────────────
FAMILY_ACCENT_RULES = [
    (re.compile(r"drum|idiophone|percuss|tongue|bell|pan|marimba|xylo|glock", re.I),
     "hz-family-percussion"),
    (re.compile(r"flute|whistle|pipe|kena|fujara|shakuh|duduk|chalumeau|gemshorn|ocarin|didger", re.I),
     "hz-family-winds"),
    (re.compile(r"violin|guitar|kora|ngoni|lute|oud|harp|bass|ukulele|lyre|whamola", re.I),
     "hz-family-strings"),
    (re.compile(r"electric|midi|synth|electron", re.I),
     "hz-family-electronic"),
]


def derive_family_accent(family_text: str) -> str:
    """Return the CSS class for the family-accent stripe."""
    for pat, cls in FAMILY_ACCENT_RULES:
        if pat.search(family_text or ""):
            return cls
    return "hz-family-percussion"


# ─── Parsers for common instrument-folder files ────────────────

def read_design_md(folder: Path) -> dict:
    """Parse design.md → dict of master-catalog-row fields."""
    p = folder / "design.md"
    if not p.exists():
        return {}
    text = p.read_text(encoding="utf-8")
    out = {}
    # Master Catalog Row table — each line "| Field | Value |"
    in_table = False
    for line in text.splitlines():
        if "Master Catalog Row" in line:
            in_table = True
            continue
        if in_table:
            m = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
            if m and m.group(1).strip() not in ("Field", ":---", "---"):
                key = m.group(1).strip().lower().replace("/", "_").replace(" ", "_")
                out[key] = m.group(2).strip()
            elif line.strip() == "":
                in_table = False
    # Pull a "Generated" date if present
    m = re.search(r"^Generated:\s*(\S+)", text, re.M)
    if m:
        out["generated"] = m.group(1)
    return out


def read_csv_first_row(p: Path) -> dict:
    if not p.exists():
        return {}
    with p.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return next(reader, {}) or {}


def read_csv_all_rows(p: Path) -> list[dict]:
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_text(p: Path, default: str = "") -> str:
    return p.read_text(encoding="utf-8") if p.exists() else default


def find_hero_image(folder: Path) -> str:
    """Pick the first image from images/ — relative path."""
    images_dir = folder / "images"
    if not images_dir.exists():
        return ""
    candidates = sorted(
        [f for f in images_dir.iterdir()
         if f.suffix.lower() in (".png", ".jpg", ".jpeg")],
        key=lambda f: f.stat().st_size,
        reverse=True,
    )
    if not candidates:
        return ""
    return str(Path("images") / candidates[0].name)


# ─── Field assembly per template ───────────────────────────────

def assemble_fields_for_brochure(folder: Path) -> dict:
    """Pull the fields declared in 01-brochure/content-spec.yaml."""
    design = read_design_md(folder)
    bom = read_csv_all_rows(folder / "bom.csv")
    hero = find_hero_image(folder)

    family = design.get("family", "")
    family_accent = derive_family_accent(family)

    top_material = bom[0].get("Material", "") if bom else ""
    body_material = bom[0].get("Notes", "") if bom else ""
    hardware = bom[2].get("Notes", "") if len(bom) >= 3 else ""
    finish = bom[4].get("Notes", "") if len(bom) >= 5 else ""

    return {
        "serial":             design.get("instrument_id", ""),
        "family":             family,
        "family_accent":      family_accent,
        "instrument_type":    design.get("instrument_type", ""),
        "variant":            design.get("variant_size", ""),
        "tagline":            "",  # Tony writes per build
        "marketing_paragraph": "",  # Tony writes per build
        "pull_quote":         "",  # Tony writes per build, often from tonykoop bio
        "key_or_scale":       design.get("key_scale", ""),
        "top_material":       top_material,
        "body_material":      body_material,
        "hardware_summary":   hardware,
        "finish":             finish,
        "build_method_steps": [],  # distilled from assembly-manual.md
        "built_year":         (design.get("generated") or "").split("-")[0] or "2026",
        "built_location":     "Santa Clara, CA",
        "maker_bio":          "",  # from tonykoop/README.md
        "github_repo_url":    design.get("github_repo", ""),
        "hero_image_path":    hero,
        "inside_image_path":  "",
        "engineering_hook":   "",
    }


ASSEMBLERS = {
    "01-brochure": assemble_fields_for_brochure,
    # Other templates — add their assemblers here as they're built out.
}


# ─── Renderer ───────────────────────────────────────────────────

def render(template_text: str, fields: dict) -> str:
    if HAVE_CHEVRON:
        return chevron.render(template_text, fields)
    # Minimal fallback — handle simple {{ var }} and {{#section}}...{{/section}}.
    rendered = template_text
    # Sections (truthy)
    def section_replacer(m):
        name = m.group(1)
        body = m.group(2)
        val = fields.get(name)
        if not val:
            return ""
        if isinstance(val, list):
            return "".join(body.replace("{{ . }}", str(item)) for item in val)
        return body
    rendered = re.sub(
        r"\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}",
        section_replacer,
        rendered,
        flags=re.DOTALL,
    )
    # Plain variables
    def var_replacer(m):
        name = m.group(1)
        return str(fields.get(name, ""))
    rendered = re.sub(r"\{\{\s*(\w+)\s*\}\}", var_replacer, rendered)
    return rendered


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("instrument_folder", type=Path)
    ap.add_argument("doc_type", help="e.g., 01-brochure")
    args = ap.parse_args()

    folder = args.instrument_folder.expanduser().resolve()
    if not folder.exists():
        sys.exit(f"Instrument folder does not exist: {folder}")

    template_dir = TEMPLATES_DIR / args.doc_type
    if not template_dir.exists():
        sys.exit(f"Template not found: {template_dir}")

    template_html = template_dir / "template.html"
    if not template_html.exists():
        sys.exit(
            f"Template '{args.doc_type}' is a stub — no template.html yet.\n"
            f"Build it by following templates/01-brochure/ as a reference."
        )

    spec = yaml.safe_load((template_dir / "content-spec.yaml").read_text(encoding="utf-8"))
    output_filename = spec.get("output_filename", f"{args.doc_type}.html")

    assembler = ASSEMBLERS.get(args.doc_type)
    if not assembler:
        sys.exit(
            f"No field-assembler registered for {args.doc_type} in render.py.\n"
            f"Add one in scripts/render.py ASSEMBLERS dict."
        )
    fields = assembler(folder)

    rendered = render(template_html.read_text(encoding="utf-8"), fields)
    output_dir = folder / "showcase"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / output_filename
    output_path.write_text(rendered, encoding="utf-8")

    print(f"Rendered {args.doc_type} → {output_path}")
    print(f"Hand off to Claude Design: point it at {SKILL_ROOT}/brand/ + this file.")


if __name__ == "__main__":
    main()
