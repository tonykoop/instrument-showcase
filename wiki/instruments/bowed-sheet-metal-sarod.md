---
title: Bowed Sheet-Metal Sarod
slug: bowed-sheet-metal-sarod
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/bowed-sheet-metal-sarod/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/bowed-sheet-metal-sarod/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/bowed-sheet-metal-sarod/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bowed-string-fretless
  - fabrication/brake-formed-sheet-metal
  - synthesis/sympathetic-strings
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has the sheet-metal body (1000×250×100 mm waisted box, 1.2 mm CR steel) been fabricated?"
  - "Has the polished steel fingerboard been fitted and meend-playability tested?"
  - "Have all 12 strings (4 main + 8 sympathetic) been installed and tuned?"
  - "Has body resonance been measured against the sheet-metal acoustic model?"
  - "Has FEA been run on the body under 445 N total string tension with ribbing?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - strings
  - sarod
  - bowed
  - fretless
  - sheet-metal
  - indian-classical
  - sympathetic-strings
  - cross-cultural
---

# Bowed Sheet-Metal Sarod

## Overview

The `bowed-sheet-metal-sarod` repo is an L2 V5 build-packet candidate for a bowed sarod — a fretless Indian classical lute reimagined for the bow. Sheet-metal body, polished steel fingerboard, 4 bowable melody strings plus 8 sympathetic strings. Status: `v0.1.0-blueprint`; fabrication CAD/DXF, runtime acoustic validation, FEA, and measured prototype evidence are still pending.

Primary repo links:

- [README](../../../../strings/bowed-sheet-metal-sarod/README.md)
- [Design](../../../../strings/bowed-sheet-metal-sarod/design.md)
- [Validation](../../../../strings/bowed-sheet-metal-sarod/validation.csv)

## Current Status

- Release state: L2 V5 build-packet candidate; blueprint stage.
- Build target: bowed sarod, D minor raga base tuning, 660 mm main scale / 350 mm sympathetic.
- Acoustic class: [[acoustic-classes/bowed-string-fretless]] — continuous bow excitation; polished steel fingerboard for meend (pitch glide).
- Fabrication: 1000 × 250 × 100 mm waisted 1.2 mm CR steel box body; internal ribbing for 445 N string tension.
- Wolfram model: `bowed-sheet-metal-sarod-starter.wl` live at Public-Execute cloud URL.
- Release blockers: fabrication CAD/DXF; FEA under string tension; body fabrication; string installation; acoustic validation.

## Design Thesis

Three departures from tradition:

1. **Bowed, not plucked** — sustained bowing enables meend across the full raga arc (traditional sarod sustain decays in 1–2 s; the bow drives strings indefinitely).
2. **Sheet-metal body, not gourd + skin** — 1.2 mm steel box radiates ~1.5–2× louder at typical playing levels; no seasonal pitch drift.
3. **Polished steel fingerboard** — enables continuous sliding contact for meend; eliminates fret buzz risk.

## Strings

- 4 main bowable melody strings: G4 / D4 / A3 / D3 (D minor base raga), scale 660 mm.
- 8 sympathetic strings: D minor scale D3–D4, scale 350 mm.
- Total string tension: ~445 N (≈45 kgf).

## Source Notes

- [repo] [README](../../../../strings/bowed-sheet-metal-sarod/README.md) — design thesis, string spec, V5 authority note, body dimensions.
- [repo] [design.md](../../../../strings/bowed-sheet-metal-sarod/design.md) — detailed acoustic and structural design.
- [spreadsheet] [validation.csv](../../../../strings/bowed-sheet-metal-sarod/validation.csv) — tuning, meend, resonance, and structural checks; all rows pending until build.

## Cross-Links

- [[acoustic-classes/bowed-string-fretless]]
- [[fabrication/brake-formed-sheet-metal]]
- [[synthesis/sympathetic-strings]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has the sheet-metal body (1000×250×100 mm, 1.2 mm CR steel) been fabricated?
2. Has the polished steel fingerboard been fitted and meend-playability tested?
3. Have all 12 strings (4 main + 8 sympathetic) been installed and tuned?
4. Has body resonance been measured against the sheet-metal acoustic model?
5. Has FEA been run on the body under 445 N total string tension with ribbing?

## Maintenance Notes

Next ingest should pull in fabrication results, FEA output, and first-play meend measurements. Update [[synthesis/sympathetic-strings]] with any empirical coupling data between main and sympathetic strings.
