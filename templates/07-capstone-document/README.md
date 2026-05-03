# Template 07 — Capstone Document

A long-form portfolio document showcasing **all the files** in a built-with-instrument-maker repo. Maps every file to a section, summarizes its content, and renders the whole thing as a single document or deck. Replaces / refreshes the existing `capstone-deck.md` pattern.

## Format

- **Multi-page, letter portrait, web + PDF (and optionally PPTX via the `pptx` skill).**
- **Sections (one per repo file family):**
  1. Cover — instrument name, serial, status, hero photo, capstone date.
  2. Project intent — distilled from `design.md`.
  3. Master catalog row — full table.
  4. Design table summary — formulas, predictions, cells (from `<instrument>-design-table.xlsx`).
  5. BOM — `bom.csv`.
  6. Sourcing — `sourcing.csv`.
  7. Cut list — `cut-list.csv`.
  8. Drawings — `drawing-brief.md` + `drawings/` index.
  9. CAD/CNC — `cad/`, `cnc/` indices.
  10. Assembly — `assembly-manual.md`.
  11. Validation — `validation.csv`.
  12. DoE study — `study/README.md` summary.
  13. Skills index — `SKILLS.md`.
  14. References + colophon.

## Files this template consumes

Essentially: every file in the instrument folder. The template is a survey, not a deep-dive. Each section is 1–2 paragraphs + a code/table excerpt.

## Voice

Portfolio voice — engineering-honest. Self-contained: a reviewer should be able to read this document without opening any other file in the repo. Cross-references are explicit (file paths in monospace).

## How this differs from `capstone-deck.md`

The pre-existing `tongue-drum/capstone-deck.md` is the right shape but generic. This template wraps it in Heifer Zephyr design tokens, adds the cover/colophon, and standardizes the section order so any instrument repo can be capstone'd identically.

## What "done" looks like

- Every file in the repo gets at least a one-line mention.
- A reviewer can read it cover-to-cover in ~10 minutes.
- Wordmark + mark on cover and colophon.
- Optional .pptx export via `pptx` skill (one slide per section).
