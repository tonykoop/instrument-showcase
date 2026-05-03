# Pilot — Tongue Drum Art-Fair Brochure

This is the **fully populated pilot artifact**, demonstrating what `templates/01-brochure/` produces when all the content fields are filled in for a real instrument folder.

The companion auto-rendered version (with empty `tagline`, `marketing_paragraph`, `pull_quote`, etc. — fields the script can't auto-populate without additional input) lives at `tongue-drum/showcase/brochure.html`. This pilot here shows you what those fields look like once filled.

## What got filled in by hand vs. auto

| Field | Source |
|---|---|
| serial, family, family_accent, instrument_type, variant, key_or_scale | Auto from `design.md` |
| top_material, body_material, hardware, finish | Auto from `bom.csv` |
| hero_image_path, inside_image_path | Auto from `images/` |
| **tagline, marketing_paragraph, pull_quote, build_method_steps, maker_bio, engineering_hook** | **Filled by hand** — these are the fields the skill flags as "Tony writes per build" |

## How to view

Open `brochure.html` in a browser, then **Print → Save as PDF** with these settings:
- Layout: Landscape
- Margins: None
- Background graphics: ON
- Two pages → one bi-fold sheet (front/back outside, then inside spread)

Then fold once, vertically.

## Hand-off to Claude Design

To get the final typography/photo polish:
1. Open Claude Design.
2. Set up your design system by pointing at `instrument-showcase/brand/`.
3. Upload this `brochure.html` (or paste the content) and ask Claude Design to:
   - Replace the `[mark]` placeholders with the bison mark SVG once you've dropped it into `brand/assets/`.
   - Tighten the type pairing (italic display + Caslon body).
   - Polish the hero photo placement, possibly suggest a duotone treatment.
   - Generate alt sizes — Instagram square, story, and a postcard variant.
