# Template 08 — Spec Sheet (1-Page Datasheet)

A one-page technical reference for an instrument. Aimed at buyers, dealers, and press. Tighter than the brochure, denser than the hangtag, no marketing copy.

## Format

- **One letter page, portrait.**
- **Top:** wordmark + mark + instrument name + serial + family-accent stripe.
- **Hero photo** (1/3 page, right side).
- **Tables (2/3 page, left side):**
  1. Identity (serial, family, type, variant, key/scale).
  2. Materials (top, body, hardware, finish, with species names).
  3. Geometry (overall L/W/H, weight, tongue/string/hole count, key dimensions).
  4. Acoustics (fundamental, range, predicted vs measured if available).
  5. Provenance (built location, year, maker).
- **Footer:** repo URL + price (if applicable) + colophon.

## Files this template consumes

Compressed subset of brochure inputs.

| Source | Used for |
|---|---|
| `design.md` | Identity + provenance |
| `bom.csv` + `cut-list.csv` | Materials + geometry |
| `validation.csv` | Acoustics measured values |
| `<instrument>-design-table.xlsx` | Acoustics predicted values |
| `images/` | Hero photo |

## Voice

Tabular. Almost no prose. Every line is a fact.

## What "done" looks like

- Fits on one letter page without scrolling.
- Every value has a unit (Hz, mm, in, g).
- No marketing language anywhere.
- Reusable as the back-of-postcard companion to a hangtag.
