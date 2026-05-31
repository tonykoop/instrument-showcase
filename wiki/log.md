# Heifer Zephyr Instrument Wiki Log

Append-only record of wiki maintenance, source ingests, queries, and lint passes. Use entries like:

```markdown
## [2026-05-18] ingest | Source Title

- Source: `path/or/url`
- Pages touched: [[instruments/kora]], [[acoustic-classes/harp-lute]]
- Summary: One or two sentences.
- Follow-ups: Open questions or next actions.
```

## [2026-05-18] scaffold | Initial wiki bridge

- Source: User request to incorporate the LLM Wiki pattern alongside the generated Heifer Zephyr instrument library.
- Pages touched: [[index]], [[log]]
- Summary: Created the instrument wiki scaffold and reserved `data/wiki-manifest.json` as the generated bridge into `site/library.html`.
- Follow-ups: Ingest the first pilot instrument page and begin linking source notes from Obsidian, second_brain, explorer pages, and capstone manifests.

## [2026-05-18] ingest | Kora and cajon pilot pages

- Source: `../../../kora/README.md`, `../../../kora/design.md`, `../../../kora/assembly-manual.md`, `../../../kora/risks.md`, `../../../kora/capstone-manifest.json`, `../../../cajon/README.md`, `../../../cajon/design.md`, `../../../cajon/assembly-manual.md`, `../../../cajon/validation-report.md`, `../../../cajon/risks.md`, and related CSV/brief files.
- Pages touched: [[index]], [[instruments/kora]], [[instruments/cajon]]
- Summary: Created the first two active instrument wiki pages with direct source links, design knowledge, validation state, release constraints, cross-links, and open questions.
- Follow-ups: Create the first reusable acoustic-class pages for `harp-lute` and `box-drum`, then add synthesis pages for public-release blockers and CAD readiness.

## [2026-05-18] synthesize | First acoustic classes and release blockers

- Source: [[instruments/kora]], [[instruments/cajon]], `../../../wood-shell-tongue-drum/README.md`, `../../../wood-shell-tongue-drum/design.md`, `../../../wood-shell-tongue-drum/validation-report.md`, and related validation/risk files.
- Pages touched: [[index]], [[acoustic-classes/harp-lute]], [[acoustic-classes/box-drum]], [[acoustic-classes/tongue-drum-wood]], [[synthesis/public-release-blockers]], [[instruments/wood-shell-tongue-drum]]
- Summary: Added reusable acoustic-class pages for harp-lute, box drum, and wooden tongue drum patterns; added a portfolio release-blocker rollup; ingested the wood-shell tongue drum as the third active instrument example.
- Follow-ups: Create CAD-readiness and Wolfram-pattern synthesis pages, then ingest `sambuca` or the legacy rectangular `tongue-drum` source stream.

## [2026-05-18] ingest | Multi-agent wiki round 1

- Source: `../../../sambuca/`, `../../../ceramic-hang/`, `../../../ceramic-tongue-drum/`, `../../../tongue-drum/`, `../../data/library-manifest.json`, `../../scripts/generate_library.py`, and `../../../wolfram-cloud-sync/manifest/wolfram_embed_urls.json`.
- Pages touched: [[index]], [[instruments/sambuca]], [[instruments/ceramic-hang]], [[instruments/ceramic-tongue-drum]], [[acoustic-classes/arched-harp]], [[acoustic-classes/tuned-shell]], [[acoustic-classes/tongue-drum-ceramic]], [[sources/legacy-rectangular-tongue-drum]], [[synthesis/cad-readiness-roadmap]], [[synthesis/wolfram-model-patterns]], [[synthesis/public-release-blockers]]
- Summary: Added three active instrument pages, three reusable acoustic-class pages, one source distillation page, and two synthesis pages covering CAD readiness and Wolfram model patterns.
- Follow-ups: Ingest a wind/reed pair next so the wiki is not over-weighted toward strings, tongue drums, and ceramic idiophones; likely candidates are `shakuhachi`, `flutes`, `duduk`, or `clarinet`.
