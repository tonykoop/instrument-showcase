---
title: Heifer Zephyr Instrument Wiki Index
wiki_type: index
last_updated: 2026-05-18
---

# Heifer Zephyr Instrument Wiki

This wiki is the maintained knowledge layer for the musical instrument design library. It lives alongside the generated explorer library, but it has a different job: it captures cross-instrument knowledge, design rationale, source synthesis, open questions, and portfolio-level patterns.

## Start Here

- [[log]] records ingests, queries, lint passes, and maintenance work.
- [[synthesis/portfolio-map]] will become the high-level map of instrument families, design lanes, and current priorities.
- [[synthesis/public-release-blockers]] tracks what prevents instrument pages from becoming public-release candidates.
- [[synthesis/cad-readiness-roadmap]] tracks which instruments need CAD export, glTF packaging, or `.glb` inlining.
- [[synthesis/wolfram-model-patterns]] tracks shared Wolfram notebook and acoustic model patterns.

## Instrument Pages

Active pages:

- [[instruments/kora]] - private-review 21-string kora-inspired hybrid prototype; main issues are cultural provenance review, string safety, bridge/head load testing, and neck/tail proof-load.
- [[instruments/sambuca]] - private-review boat-shaped arched harp; main issues are MULE validation, depth/cavity/tuner inconsistencies, cultural/musicology review, and inherited CAD geometry.
- [[instruments/cajon]] - public-review three-member cajon family; main issues are pre-build measurement gates, corrected Helmholtz workbook formula, visual authority, and first CJ-S prototype validation.
- [[instruments/ceramic-hang]] - ceramic tuned-shell scaffold; main issues are fired shrinkage, tone-field coupon evidence, realistic note count, glaze damping, and fabrication authority.
- [[instruments/ceramic-tongue-drum]] - slip-cast ceramic tongue drum family; main issues are fired ceramic K, shrinkage, slot survival, glaze mass, and CTD-M chamber measurement.
- [[instruments/wood-shell-tongue-drum]] - round-body wooden tongue drum family; main issues are Padauk K calibration, Helmholtz end correction, airtight rim seal, and V1 Standard prototype measurements.

Suggested next pilot order:

- `shakuhachi` or `flutes`
- `duduk` or `clarinet`
- `steel-pan` or `handpan`
- `siku-zampona`

## Acoustic Classes

Active pages:

- [[acoustic-classes/harp-lute]] - string-bank instruments with bridge, resonator, neck/spine, and tail-load coupling.
- [[acoustic-classes/arched-harp]] - curved-neck harps with string-holder strip and boat/body load paths.
- [[acoustic-classes/box-drum]] - closed-box plate-and-Helmholtz drums, starting with cajon.
- [[acoustic-classes/tuned-shell]] - ceramic/handpan-like tuned shells with tone fields and body/gu coupling.
- [[acoustic-classes/tongue-drum-wood]] - wooden slit-tongue idiophones, including enclosed round-body designs.
- [[acoustic-classes/tongue-drum-ceramic]] - slip-cast ceramic slit-tongue instruments with fired-material correction factors.

Seed these next when multiple instruments start sharing the same design logic:

- `duct-flute`
- `open-pipe`
- `reed`
- `free-reed`
- `tuned-bar`
- `tongue-drum-steel`

## Fabrication

Candidate process pages:

- `stave-construction`
- `slip-casting`
- `laser-cutting`
- `cnc-routing`
- `bamboo-processing`
- `hide-or-membrane-mounting`
- `bridge-and-string-layout`

## Synthesis Pages

Active pages:

- [[synthesis/public-release-blockers]] - portfolio-level release evidence and blocker rollup.
- [[synthesis/cad-readiness-roadmap]] - GLB/glTF packaging state versus native CAD/fabrication authority.
- [[synthesis/wolfram-model-patterns]] - Wolfram cloud states, model families, and validation/publish patterns.

## Source Summaries

Active pages:

- [[sources/legacy-rectangular-tongue-drum]] - source distillation for the older rectangular wooden tongue drum repo, feeding [[acoustic-classes/tongue-drum-wood]] without becoming a library-linked instrument page yet.

## Source Streams

Likely source pools:

- Instrument repos in `C:\Users\Tony\Documents\GitHub`.
- `second_brain` and Obsidian notes.
- Existing explorer pages and capstone manifests.
- Wolfram notebooks and sync manifests.
- Build photos, CAD exports, spreadsheets, and lab notes.

## Maintenance

After adding or updating instrument pages, run:

```bash
python3 scripts/generate_library.py
```

That refreshes `data/library-manifest.json`, `data/wiki-manifest.json`, and `site/library.html`.
