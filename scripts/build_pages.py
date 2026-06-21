#!/usr/bin/env python3
"""
build_pages.py — assemble a self-contained GitHub Pages bundle (into docs/)
for the published instrument subset. Source repos stay private; only the
referenced-file closure of each explorer.html is copied, so huge galleries,
raw CAD, and third-party PDFs that aren't shown never enter the public bundle.

Per instrument:
  - parse explorer.html for local href/src references
  - copy explorer + those files into docs/instruments/<family>/<slug>/
  - for any .gltf, also copy sibling buffers/textures
  - optimize raster images: photos/renders -> JPEG q82 <=1600px (rename + rewrite
    refs); diagrams/tables/screenshots -> keep PNG (resize+optimize, no rename)
Then build a landing index.html with one card per published instrument.

Usage:
  python3 scripts/build_pages.py              # full build
  python3 scripts/build_pages.py --dry-run    # list instruments, no writes
"""
import os, re, json, shutil, html as _html, urllib.parse, argparse
from pathlib import Path
from PIL import Image, ImageOps

ROOT = "/mnt/c/Users/Tony/Documents/GitHub"
HERE = Path(__file__).resolve().parent
DOCS = str(HERE.parent / "docs")
MAXEDGE, JPEG_Q = 1600, 82

FAMILY_MAP = {
    "string":    "strings",
    "wind":      "woodwind",
    "drum":      "percussion",
    "idiophone": "idiophones",
    "brass":     "brass",
}


def load_publish_list():
    published = (HERE.parent / "scripts" / "published.txt").read_text().split()
    manifest = json.loads((HERE.parent / "data" / "library-manifest.json").read_text())
    slug_to_family = {e["slug"]: e["family"] for e in manifest["entries"]}
    result = []
    for slug in published:
        if not slug:
            continue
        lib_family = slug_to_family.get(slug)
        if not lib_family:
            print(f"  WARN {slug}: not found in library-manifest.json, skipping")
            continue
        folder_family = FAMILY_MAP.get(lib_family, lib_family)
        result.append((folder_family, slug))
    return result


def title_of(folder_family, slug):
    rd = f"{ROOT}/instruments/{folder_family}/{slug}/README.md"
    if os.path.exists(rd):
        m = re.search(r"^#\s+(.+)", open(rd, encoding="utf-8", errors="ignore").read(), re.M)
        if m:
            return m.group(1).strip()
    return slug.replace("-", " ").title()


def local_refs(html):
    out = set()
    for r in re.findall(r'(?:href|src)="([^"]+)"', html):
        if r.startswith(("http://", "https://", "#", "mailto:", "data:")):
            continue
        if any(c in r for c in ("'", "+", "$")):
            continue
        if r in ("explorer.html", ""):
            continue
        out.add(r)
    return out


def is_diagram(path):
    p = path.lower()
    name = os.path.basename(p)
    return ("design-table" in p or "table" in name or "screenshot" in p
            or "chart" in p or "diagram" in p)


def is_raster(path):
    return os.path.splitext(path)[1].lower() in (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff")


def optimize(src, dst_base, to_jpeg):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im.thumbnail((MAXEDGE, MAXEDGE), Image.LANCZOS)
    if to_jpeg:
        dst = dst_base + ".jpg"
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        im.save(dst, "JPEG", quality=JPEG_Q, optimize=True, progressive=True)
    else:
        dst = dst_base + ".png"
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        im.save(dst, "PNG", optimize=True)
    return dst


def build_instrument(folder_family, slug):
    rp = f"{ROOT}/instruments/{folder_family}/{slug}"
    exp = f"{rp}/explorer.html"
    if not os.path.exists(exp):
        print(f"  SKIP {slug}: no explorer.html")
        return None
    html = open(exp, encoding="utf-8", errors="ignore").read()
    refs = local_refs(html)

    out_dir = f"{DOCS}/instruments/{folder_family}/{slug}"
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir, exist_ok=True)

    rename = {}
    missing_img = []
    copied = missing = 0
    total_out = 0
    for ref in sorted(refs):
        relfs = urllib.parse.unquote(ref)
        src = f"{rp}/{relfs}"
        if not os.path.exists(src):
            missing += 1
            if is_raster(relfs):
                missing_img.append(ref)
            continue
        if is_raster(relfs):
            to_jpeg = not is_diagram(relfs)
            base = os.path.join(out_dir, os.path.splitext(relfs)[0])
            dst = optimize(src, base, to_jpeg)
            new_rel = os.path.relpath(dst, out_dir)
            if new_rel != relfs:
                rename[ref] = urllib.parse.quote(new_rel)
            copied += 1
            total_out += os.path.getsize(dst)
        else:
            dst = os.path.join(out_dir, relfs)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            copied += 1
            total_out += os.path.getsize(dst)
            if relfs.lower().endswith(".gltf"):
                sdir = os.path.dirname(src)
                ddir = os.path.dirname(dst)
                for f in os.listdir(sdir):
                    if f == os.path.basename(src):
                        continue
                    sp = os.path.join(sdir, f)
                    if os.path.isfile(sp):
                        shutil.copy2(sp, os.path.join(ddir, f))
                        total_out += os.path.getsize(sp)

    for old, new in rename.items():
        html = html.replace(f'"{old}"', f'"{new}"')
    for ref in missing_img:
        html = re.sub(r'<figure>\s*<img[^>]*src="' + re.escape(ref) + r'"[^>]*>\s*</figure>', "", html)
        html = re.sub(r'<img[^>]*src="' + re.escape(ref) + r'"[^>]*>', "", html)
    open(f"{out_dir}/explorer.html", "w", encoding="utf-8").write(html)

    hero = ""
    for candidate in ("images/hero-render.jpg", "images/hero-render.png"):
        if os.path.exists(f"{out_dir}/{candidate}"):
            hero = candidate
            break

    print(f"  {slug}: {copied} files, {missing} missing-ref, {total_out/1048576:.1f}MB, {len(rename)} img-rewrites")
    return {
        "family": folder_family,
        "slug": slug,
        "title": title_of(folder_family, slug),
        "explorer": f"instruments/{folder_family}/{slug}/explorer.html",
        "hero": f"instruments/{folder_family}/{slug}/{hero}" if hero else "",
    }


CARD = """    <a class="card" href="{explorer}">
      {img}
      <div class="card-body"><span class="fam">{family}</span><h2>{title}</h2></div>
    </a>"""

INDEX = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Heifer Zephyr — Instrument Design Catalog</title>
<style>
:root{{--bg:#0f1115;--card:#171a21;--rule:#262b36;--ink:#e7e9ee;--mut:#9aa3b2;--accent:#c9a24a}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);
font:16px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
header{{padding:64px 24px 28px;max-width:1040px;margin:0 auto}}
h1{{font-size:34px;margin:0 0 8px}}.sub{{color:var(--mut);max-width:60ch}}
.grid{{max-width:1040px;margin:0 auto;padding:8px 24px 64px;display:grid;
grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}}
.card{{background:var(--card);border:1px solid var(--rule);border-radius:14px;overflow:hidden;
text-decoration:none;color:inherit;transition:.15s border-color,.15s transform}}
.card:hover{{border-color:var(--accent);transform:translateY(-2px)}}
.card img{{width:100%;aspect-ratio:1/1;object-fit:cover;display:block;background:#0b0d11}}
.card-body{{padding:14px 16px}}.fam{{color:var(--accent);font-size:12px;text-transform:uppercase;
letter-spacing:.08em}}.card h2{{font-size:18px;margin:4px 0 0;line-height:1.3}}
footer{{max-width:1040px;margin:0 auto;padding:0 24px 60px;color:var(--mut);font-size:13px}}
a.brand{{color:var(--accent);text-decoration:none}}
</style></head><body>
<header>
  <h1>Heifer Zephyr — Instrument Design Catalog</h1>
  <p class="sub">A curated, open look at original and traditional musical-instrument designs —
  engineering packets, acoustic models, and build documentation. A growing public preview,
  eventually living at <a class="brand" href="https://heiferzephyr.com">heiferzephyr.com</a>.</p>
</header>
<main class="grid">
{cards}
</main>
<footer>Design files and documentation &copy; Tony Koop &middot; licensed CERN-OHL-W-v2 (hardware) + CC-BY-4.0 (docs)
unless noted. Source designs are maintained privately; this site publishes a curated subset.</footer>
</body></html>"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="list instruments only, no writes")
    args = parser.parse_args()

    publish = load_publish_list()
    print(f"{'DRY-RUN: ' if args.dry_run else ''}building {len(publish)} instruments -> {DOCS}")

    if args.dry_run:
        for fam, slug in publish:
            print(f"  would build: {fam}/{slug}")
        return

    os.makedirs(DOCS, exist_ok=True)
    instr_dir = f"{DOCS}/instruments"
    if os.path.isdir(instr_dir):
        shutil.rmtree(instr_dir)

    cards = []
    for fam, slug in publish:
        e = build_instrument(fam, slug)
        if not e:
            continue
        img = (f'<img src="{e["hero"]}" alt="{_html.escape(e["title"])}" loading="lazy">'
               if e["hero"] else "")
        cards.append(CARD.format(
            explorer=e["explorer"],
            img=img,
            family=_html.escape(fam),
            title=_html.escape(e["title"]),
        ))

    open(f"{DOCS}/index.html", "w", encoding="utf-8").write(INDEX.format(cards="\n".join(cards)))
    open(f"{DOCS}/.nojekyll", "w").write("")
    print(f"\nbuilt {len(cards)} instrument(s) -> {DOCS}/index.html")


if __name__ == "__main__":
    main()
