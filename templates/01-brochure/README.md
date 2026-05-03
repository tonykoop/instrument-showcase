# Template 01 — Art-Fair Brochure

A printable, customer-facing brochure to accompany an instrument while it's for sale at an art fair, market, or gallery. The buyer should be able to pick this up next to the instrument and learn enough to decide.

## Format

- **Bi-fold letter** (8.5×11 → 8.5×5.5 folded, 4 panels) by default. The template can be re-flowed to tri-fold.
- **Print on cream uncoated stock**, 80–100lb cover. Avoid gloss.
- **Page 1 (front cover):** wordmark + mark, instrument name, hero photo.
- **Page 2 (inside left):** marketing paragraph + pull quote.
- **Page 3 (inside right):** spec block + build method summary + materials.
- **Page 4 (back cover):** maker bio + provenance (where built, when, by whom) + serial + colophon.

## Files this template consumes

| Source file in instrument folder | Used for |
|---|---|
| `README.md` | Repo intent, instrument family, hero image path |
| `design.md` | Master catalog row → spec block (serial, key, materials, target price) |
| `bom.csv` | Material list summary (top, body, hardware, finish) |
| `assembly-manual.md` | Build-method summary (3–5 step abstract) |
| `study/README.md` (if present) | One-line summary of the engineering/DoE story |
| `images/*.jpg/png` | Hero photo (largest), inside photo (build/process) |
| `tonykoop/README.md` (cross-repo) | Maker bio paragraph |

## Voice

See `brand/voice.md`. Brochure voice is the warmest of the document types: second-person allowed ("Pick it up. Strike it with the included mallet."), but every claim must remain testable. No marketing puffery.

## How to render

```bash
python ../../scripts/render.py <instrument-folder> 01-brochure
```

The script reads the source files above, fills `template.html`, and writes to `<instrument-folder>/showcase/brochure.html`. Convert to PDF via the `pdf` skill or print directly to PDF from the browser. Hand off to Claude Design for typography/photo polish.

## What "done" looks like

- Folds correctly when printed at letter size.
- Bison mark in correct position.
- Spec block matches `design.md` master catalog row exactly.
- Hero photo isn't a white-sweep cutout — instrument on cream/linen ground.
- One pull quote, one accent stripe, no other color.
- Maker bio includes provenance (Santa Clara, CA · year built).
