# instrument-showcase

A Cowork / Claude Code skill that turns any of Tony Koop's instrument repos into branded, customer-facing or shop-facing documents under the **Heifer Zephyr** maker brand — and hands them off cleanly to **Claude Design** for typography/photo polish.

## What this skill produces

Fifteen document types, each rendered from the canonical files (`design.md`, `bom.csv`, `assembly-manual.md`, `validation.csv`, `study/`, `images/`, etc.) inside any instrument folder:

1. Art-fair brochure
2. Workshop print packet (build method)
3. Build-method landing page
4. Sales page (serialized instrument)
5. Lab notebook with DoE columns
6. Design of Experiments report
7. Capstone document
8. Spec sheet (1-page datasheet)
9. Certificate of authenticity
10. Care & tuning card
11. Hangtag / box label / packaging insert
12. EPK / press kit
13. Acoustic measurement report
14. Wholesale dealer line sheet
15. Catalog / lookbook

## How it relates to other skills

- **`instrument-maker`** is a **soft dependency.** instrument-maker computes the physics, sizes the parts, generates the BOM. instrument-showcase consumes those outputs and produces human-facing documents. Two separate skills — one engineers the instrument, one packages it.
- **`docx`, `pdf`, `pptx`, `xlsx`** are the export backends.
- **`skill-creator`** is the right home if you want to add a new document type.
- **Claude Design** is the *styling/polish* layer that runs *after* this skill assembles content. The `brand/` folder is what you point Claude Design at as the "design system."

## Install

The skill is a self-contained folder. To install it as a Cowork/Claude Code user skill:

```bash
# Mac/Linux
cp -R ~/Documents/GitHub/instrument-showcase ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse C:\Users\Tony\Documents\GitHub\instrument-showcase $env:USERPROFILE\.claude\skills\
```

Or, if you'd rather track changes via git, leave the skill in `~/Documents/GitHub/instrument-showcase` and create a symlink:

```bash
ln -s ~/Documents/GitHub/instrument-showcase ~/.claude/skills/instrument-showcase
```

After installing, restart your Cowork or Claude Code session and the skill will appear in `/skills`.

## Usage from the chat

Just say one of:

> Make an art-fair brochure for the tongue drum.
> Generate a wholesale line sheet for the steel-tongue-drum.
> Refresh the build method print packet for the djembe under the Heifer Zephyr brand.
> Produce a capstone document for the kora.

The skill will identify the instrument folder, the doc type, and run the rendering.

## Usage from the command line

```bash
python ~/.claude/skills/instrument-showcase/scripts/render.py \
  ~/Documents/GitHub/tongue-drum 01-brochure
```

Output goes to `<instrument-folder>/showcase/<doc-type>.html`.

## Static deliverables hub

Round 24 adds a separate multi-repo site flow for browsing sprint deliverables across
instrument repos. It does not replace the per-instrument document templates above.

Render the hub from the checked-in manifest seed:

```bash
python scripts/render_site_hub.py
python scripts/check_site_hub.py
```

This writes a fully static site under `site/` with:

- `site/index.html` — landing page with instrument cards, filters, and sprint metadata
- `site/instruments/*.html` — detail pages per repo
- `site/manifest.html` — browsable copy of the machine-readable manifest

The source manifest lives in `data/deliverables-manifest.json`. Keep readiness and
runtime evidence honest: Wolfram outputs and showcase HTML are review artifacts, not
fabrication authority.

## The Heifer Zephyr brand

The brand identity lives in `brand/`:

- `tokens.css` — single source of truth for color, typography, spacing, rule weights.
- `voice.md` — voice and tone rules, with words to use and words to avoid.
- `components.html` — visual exemplar of the wordmark+mark lockup, document header, spec block, hero photo slot, pull quote, colophon footer, and family-accent stripes.
- `assets/` — drop your bison-mark SVG, wordmark file, hero photo treatments, and signature here.

**To set up Claude Design with this brand:**

1. Open Claude Design (research preview, Pro/Max/Team/Enterprise).
2. Choose "Set up design system."
3. Point it at this folder (upload or paste the `tonykoop/instrument-showcase/brand` GitHub URL).
4. Claude Design will read `tokens.css`, `voice.md`, `components.html`, and `assets/` and learn the Heifer Zephyr style.
5. Every artifact you generate after that inherits the design system automatically.

See [Anthropic's design-system setup guide](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design).

## The pipeline, end-to-end

```
                      ┌──────────────────────┐
   instrument repo    │  instrument-maker    │   ← computes physics,
   (e.g. tongue-drum) │  skill               │     sizes parts, BOM,
                      │                      │     design table, study/
                      └──────────┬───────────┘
                                 │
                                 ▼
                      ┌──────────────────────┐
                      │ instrument-showcase  │   ← assembles 15 doc-type
                      │ skill (this repo)    │     content from canonical
                      │                      │     files; outputs HTML
                      │  brand/    ◄─────┐   │     under <repo>/showcase/
                      │  templates/      │   │
                      │  scripts/        │   │
                      └──────────┬───────┘   │
                                 │           │
                                 ▼           │
                      ┌──────────────────────┐│
                      │  Claude Design       ││   ← reads brand/ as the
                      │                      ◄┘     design system, applies
                      │  (typography, photo  │      it to every artifact;
                      │   polish, mobile,    │      exports to PDF, PPTX,
                      │   alt sizes, export) │      Canva, internal URL,
                      └──────────────────────┘      or Claude Code handoff
```

## Adding a new document type

1. Create `templates/NN-<doc-type>/`.
2. Write `README.md` (what it is, who it's for, what it consumes).
3. Write `content-spec.yaml` (structured fields the template needs).
4. Write `template.html` (renderable, brand-token-aware, mustache-style placeholders).
5. Add an assembler function in `scripts/render.py` if the field-pulling logic is non-trivial.
6. Add a row to the table at the top of `SKILL.md`.

## What's pre-built vs. stub

- **Brand layer** — fully built. Tokens, voice, components.
- **Template 01 — Art-Fair Brochure** — fully built (template.html + content-spec.yaml + README + render.py assembler + populated pilot in `examples/`).
- **Templates 02–15** — README + content-spec scaffolded. `template.html` and `render.py` assembler grow on demand. Each stub README documents exactly what the template needs to consume.

The first time you ask for a stub doc type (e.g., "make a wholesale line sheet for the cajon"), the skill will: (a) read the stub's README + content-spec, (b) build the missing `template.html`, (c) add the assembler to `render.py`, (d) render. After that, the doc type is fully baked for any instrument.
