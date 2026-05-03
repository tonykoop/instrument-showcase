---
name: instrument-showcase
description: Produce human-facing showcase documents for any instrument repo in Tony Koop's musical-instrument portfolio (Heifer Zephyr brand) — art-fair brochures, build methods, landing pages, sales pages, lab notebooks, DoE reports, capstone documents, spec sheets, certificates of authenticity, care cards, hangtags, press kits, acoustic measurement reports, wholesale line sheets, and catalog/lookbook spreads. Use this skill whenever the user asks to make a brochure, build method, landing page, sales page, lab notebook, DoE report, capstone, spec sheet, certificate, hangtag, press kit, line sheet, catalog, lookbook, "showcase," "portfolio piece," or "art-fair piece" for one of the instrument folders, or when they say something like "package this for sale," "write the buyer-facing version," "make a Claude Design handoff for this instrument," or "produce the Heifer Zephyr version of this build." Trigger even if the user names only the document type and the instrument family without saying "showcase." This skill consumes outputs from instrument-maker (BOM, design table, validation, study/) and produces brand-styled documents ready for Claude Design polish.
---

# Instrument Showcase

A skill for turning any instrument folder in Tony Koop's portfolio into branded, customer-facing or shop-facing documents under the **Heifer Zephyr** maker brand.

## When to use

Trigger this skill when Tony asks to produce any of these document types for a specific instrument folder (e.g., `tongue-drum`, `djembe`, `flutes`, `handpan`, `kora`):

| # | Document type | Audience | Format |
|---|---|---|---|
| 1 | Art-fair brochure | Buyers at fairs/markets | Print PDF, tri-fold or bi-fold |
| 2 | Workshop print packet | Tony at the workbench | Letter-size print, tools/PPE/materials reminders |
| 3 | Online build-method landing page | Web visitors | Single-page HTML |
| 4 | Online sales page (serialized) | Web buyers, one specific instrument | Single-page HTML |
| 5 | Lab notebook | Tony during testing | Print, columns ready for measurement entry |
| 6 | Design of Experiments report | Engineering audiences | Long-form HTML/PDF, charts + decision trees |
| 7 | Capstone document | Portfolio reviewers | Multi-page document showcasing repo files |
| 8 | Spec sheet / 1-page datasheet | Buyers, dealers, press | One-page PDF |
| 9 | Certificate of authenticity | Buyer of one specific serialized unit | One-page printable |
| 10 | Care & tuning card | Owner of the instrument | Wallet-card or postcard |
| 11 | Hangtag / box label / packaging | Retail/POP | Small printable, tag-die-cut |
| 12 | EPK / press kit one-pager | Media, galleries, booking | One-page PDF |
| 13 | Acoustic measurement report | Engineering audiences | Multi-page PDF, FFT/SPL charts |
| 14 | Wholesale dealer line sheet | Stockists, dealers | One-page printable |
| 15 | Catalog / lookbook | Multi-instrument browsers | Magazine-style, multiple pages |

## How this skill is structured

```
instrument-showcase/
├── SKILL.md                   ← you are here
├── brand/                     ← Heifer Zephyr design system seed
│   ├── tokens.css             ← color, type, spacing variables
│   ├── voice.md               ← copy voice and tone rules
│   ├── components.html        ← exemplar headers, cards, dividers, footers
│   └── assets/                ← logos, mark, hero treatments (drop yours here)
├── templates/                 ← one folder per document type
│   ├── 01-brochure/
│   │   ├── README.md          ← what this template is, what files it consumes
│   │   ├── template.html      ← the renderable HTML/Jinja-style template
│   │   └── content-spec.yaml  ← which fields the template needs
│   ├── 02-workshop-print-packet/
│   ├── 03-build-method-landing-page/
│   ├── 04-sales-page/
│   ├── 05-lab-notebook/
│   ├── 06-doe-report/
│   ├── 07-capstone-document/
│   ├── 08-spec-sheet/
│   ├── 09-certificate-of-authenticity/
│   ├── 10-care-and-tuning-card/
│   ├── 11-hangtag-and-packaging/
│   ├── 12-press-kit/
│   ├── 13-acoustic-measurement-report/
│   ├── 14-wholesale-line-sheet/
│   └── 15-catalog-lookbook/
├── scripts/
│   └── render.py              ← reads an instrument folder + a doc type, emits the rendered file
└── examples/
    └── tongue-drum-brochure/  ← the pilot artifact
```

## How to invoke

When Tony says something like:

> "Make an art-fair brochure for the tongue drum"
> "Generate a wholesale line sheet for the steel-tongue-drum"
> "Refresh the build method print packet for the djembe under the Heifer Zephyr brand"

Do this:

1. **Identify the instrument folder.** Look in `/sessions/<id>/mnt/GitHub/<instrument-name>/`. Confirm with Tony if ambiguous (e.g., `tongue-drum` vs. `wood-shell-tongue-drum` vs. `steel-tongue-drum`).
2. **Identify the doc type.** Match against the 15 templates above. If the request is novel (e.g., "year-end review"), confirm with Tony whether to add a new template or adapt the closest existing one.
3. **Read the canonical files** that the template's `content-spec.yaml` declares. Typical inputs:
   - `README.md` — repo intent, family, status, hero photo path
   - `design.md` — catalog row, intent, validation plan
   - `bom.csv` — bill of materials
   - `sourcing.csv`, `cut-list.csv`, `supplier-rfq.md` — supply chain
   - `assembly-manual.md` — workshop sequence, tools, fixtures, safety, tuning
   - `drawing-brief.md`, `visual-bom-brief.md` — drawing/imagery briefs
   - `validation.csv`, `study/data-template.csv`, `study/README.md` — DoE protocol + measurement schema
   - `images/` — hero photos, magazine references, drawings
   - `<instrument>-design-table.xlsx` — design parameter spreadsheet
   - `capstone-deck.md`, `print-packet.md` — pre-existing showcase artifacts (refresh source)
4. **Render through the template.** Either by hand for one-offs, or by running `scripts/render.py <instrument-folder> <doc-type>` for systematic runs.
5. **Output to `<instrument>/showcase/<doc-type>.html`** (or .pdf/.docx via the docx/pdf skills as appropriate). Keep this folder under the instrument repo so it stays co-located with source files.
6. **Hand off to Claude Design** by pointing Claude Design at the `brand/` folder + the rendered output. Claude Design will apply the design system; the skill's job is to assemble correct content in correct structure.

## Design rules (Heifer Zephyr brand)

Every output must obey the rules in `brand/voice.md` and `brand/tokens.css`. In summary:

- **Wordmark:** "Heifer Zephyr" set in italic serif (script-leaning calligraphic italic).
- **Mark:** naturalistic line-art bison head, monochrome.
- **Palette:** monochrome editorial baseline (deep ink + warm cream + bone). One restrained accent per document type (e.g., terracotta for percussion, slate for winds, walnut for strings) — defined per-template in `tokens.css`.
- **Typography:** italic serif for the wordmark and section titles; an upright text serif for body; a mono for spec tables; never sans-serif as a primary face.
- **Voice:** engineering-honest, instrument-aware, first-person when Tony is the subject, concise. The maker bio in the `tonykoop` README is the canonical voice sample.
- **Imagery:** woodgrain, raw materials, in-process workshop photos, finished hero shots. Avoid stock photos.
- **Layout:** generous margins, asymmetric grids, lots of white space. The bison mark sits top-left or as a colophon.

## How this skill relates to other skills

- **`instrument-maker`** is a **soft dependency**. instrument-maker computes the physics, sizes the parts, generates the BOM. instrument-showcase consumes those outputs. If a needed input file is missing, suggest Tony run instrument-maker first.
- **`docx`, `pdf`, `pptx`, `xlsx`** are used as the export backends. When a template targets a Word doc or PDF, read the corresponding skill before producing the file.
- **`skill-creator`** is the right home if Tony wants to add a new document type or improve a template's triggering.
- **Claude Design** is the styling/polish layer that runs *after* this skill assembles content. The `brand/` folder is what you point Claude Design at as the "design system."

## Adding a new document type

1. Create `templates/NN-<doc-type>/`.
2. Write `README.md` (what it is, who it's for, what files it consumes).
3. Write `content-spec.yaml` (the structured fields the template needs).
4. Write `template.html` (renderable, brand-token-aware).
5. Add a row to the table at the top of this SKILL.md.
6. Add a test instrument folder + expected output to `examples/` if helpful.

## Failure modes to avoid

- **Don't invent content.** If a template needs a "tuning protocol" but the instrument folder has no `study/`, ask Tony what should fill that slot — do not fabricate measurement data.
- **Don't break Heifer Zephyr brand.** No emoji-laden copy, no sans-serif body, no neon accents. The brand is editorial and quiet.
- **Don't duplicate `instrument-maker`.** This skill formats; it does not compute. If physics work is needed, defer to instrument-maker.
- **Don't reproduce copyrighted reference material verbatim.** When a folder cites a magazine plan (e.g., the WOOD magazine tongue drum pattern), credit the original and summarize — do not regurgitate plans.
