# Catalog Lookbook Pilot — Instrument Selection

**Status:** scaffolding (concept images not yet generated — pending image-gen pipeline #182)  
**Template:** `templates/15-catalog-lookbook/`  
**Refs:** instrument-showcase#1

---

## Pilot Scope

Two instruments from validated packets in `instrument-maker`. These cover distinct
physics families and production pipelines, giving the lookbook visual contrast:

| # | Instrument | Repo | Packet tier | Why this pilot |
|---|------------|------|------------|---------------|
| 1 | Ocarina (Alto C) | tonykoop/ocarina | L2 full-packet | Helmholtz vessel; strong design doc; slip-cast pipeline |
| 2 | Udu Drum (S–XL family) | tonykoop/udu | L2 full-packet | Dual-mode Helmholtz; 4-member family; percussion contrast |

---

## Per-Instrument Lookbook Page Spec

### Ocarina (Alto C)

- **Hero image:** `images/hero-render.png` (concept only — pending Blender/image-gen)
- **Name:** Slip-Cast Ceramic Ocarina — Alto C
- **Serial prefix:** OCA
- **Description:** A transverse Helmholtz vessel flute in slip-cast ceramic. The
  chamber volume and port geometry are tuned to a concert-pitch Alto C family.
  Built from a parametric design table; every tone hole position is derived from
  the acoustic model.
- **Spec excerpt (4 lines):**
  - Physics: Helmholtz vessel resonator
  - Pipeline: slip-cast (Bambu Studio + kiln)
  - Family: single instrument (Alto C)
  - Status: design validated; fabrication authority pending CAD/DXF review
- **Repo:** https://github.com/tonykoop/ocarina
- **Authority note:** dimensions from design.md parametric table; no fabrication claim until CAD DXF reviewed

### Udu Drum (Family S/M/L/XL)

- **Hero image:** `images/hero-render.png` + `images/family-group.png` (concept — pending)
- **Name:** Slip-Cast Ceramic Udu Drum — S/M/L/XL Family
- **Serial prefix:** UDU
- **Description:** A dual-Helmholtz ceramic udu in four family sizes. Played with
  an open palm over the side hole, the coupled resonator modes produce the
  characteristic "two voices" of the traditional Igbo udu. Family-spec.csv
  tracks all four sizes against the governing physics model.
- **Spec excerpt (4 lines):**
  - Physics: dual Helmholtz (mouth port + side hole, coupled)
  - Pipeline: slip-cast (Bambu Studio + kiln)
  - Family: S / M / L / XL (scaled by Helmholtz law)
  - Status: L2 full-packet; measurement validation pending
- **Repo:** https://github.com/tonykoop/udu
- **Authority note:** family targets in family-spec.csv; no build-ready claim

---

## Image-Gen Provenance Plan

All lookbook images are `concept_only`. Provenance sidecars are in
`image-gen-sidecars/`.

| Image | Instrument | Status | Sidecar |
|-------|-----------|--------|---------|
| ocarina-hero.png | Ocarina Alto C | pending (image-gen-2 #182) | `image-gen-sidecars/ocarina-hero-sidecar.md` |
| udu-hero.png | Udu Drum (size M) | pending | `image-gen-sidecars/udu-hero-sidecar.md` |
| udu-family-group.png | Udu Drum S/M/L/XL | pending | `image-gen-sidecars/udu-family-group-sidecar.md` |
| cover-composite.png | All instruments | pending | `image-gen-sidecars/cover-composite-sidecar.md` |

**Non-dimensional guard:** every prompt sidecar includes the guard from
`instrument-maker/skills/v4/.../templates/image-prompts/hero.md`.

---

## Authority Checklist (per issue #1)

- [x] No fabrication dimension claimed in lookbook copy
- [x] Spec excerpts cite packet sources (design.md, family-spec.csv)
- [x] Hero images marked concept only in visual-output-register.csv (when generated)
- [x] Instrument names use validated naming (not "traditional-replica" language)
- [ ] Images generated via gemini/codex with provenance sidecars (pending #182)
- [ ] Lookbook HTML rendered from template 15 (pending art-director / image availability)
- [ ] Prompt sidecars committed alongside generated images

---

## Next Steps

1. Once image-gen pipeline (#182) is available: run `scripts/seed_image_gen.py`
   against the ocarina and udu packets to generate concept seeds.
2. Apply Adobe MCP refinement (remove background, adjust lighting).
3. Render `templates/15-catalog-lookbook/` to HTML using the pilot selection.
4. Commit generated images + provenance sidecars.
5. Close issue #1 with PR linking pilot HTML.
