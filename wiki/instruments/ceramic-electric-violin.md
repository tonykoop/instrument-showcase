---
title: Ceramic Electric Violin
slug: ceramic-electric-violin
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/ceramic-electric-violin/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/ceramic-electric-violin/design.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/electric-string-piezo
  - fabrication/slip-cast-ceramic
  - fabrication/bolt-on-neck
  - synthesis/wolfram-model-patterns
open_questions:
  - "Have ceramic body shrinkage measurements been captured from fired test tiles?"
  - "Has the bolt-on maple neck been fitted to the ceramic body?"
  - "Has the Fishman V-200 piezo been installed and signal path tested?"
  - "Has CEV-P1 prototype been built and string-tuning validated?"
  - "Has the piezo-body coupling been characterized vs ceramic body modes?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - strings
  - violin
  - electric
  - ceramic
  - slip-cast
  - piezo
  - hybrid
---

# Ceramic Electric Violin

## Overview

The `ceramic-electric-violin` repo is a V5 issue-readiness scaffold (not yet a V5 build-packet candidate) for a slip-cast porcelain-bodied solid-body electric violin: bolt-on hard maple neck, ebony fingerboard, Fishman V-200 under-bridge piezo pickup, 1/4" endpin jack output. Status: v4.2 delivery bar; CAD remains conceptual until ceramic-body and electric-hardware gates close with measured/reviewed evidence.

Primary repo links:

- [README](../../../../strings/ceramic-electric-violin/README.md)
- [Design](../../../../strings/ceramic-electric-violin/design.md)
- [Wolfram model](../../../../strings/ceramic-electric-violin/build/wolfram/ceramic-electric-violin-wolfram-model.wl)

## Current Status

- Release state: V5 issue-readiness scaffold; not build-ready.
- Build target: CEV-P1 ceramic-bodied solid electric violin, standard GDAE tuning at 330 mm scale.
- Acoustic class: [[acoustic-classes/electric-string-piezo]] — primary signal from Mersenne–Taylor string; body is a rigid platform, not a top-plate resonator; piezo captures at bridge, bypassing ceramic body modes.
- Fabrication: three shop pipelines — slip-cast ceramic body + woodworking (bolt-on maple neck + ebony FB) + electronics (Fishman V-200 + endpin jack).
- Wolfram model: `ceramic-electric-violin-wolfram-model.wl` and `ceramic-electric-violin-packet-starter.wl` live at Public-Execute cloud URL.
- Release blockers: ceramic shrinkage gates; body-fit measurements; neck fit; piezo installation; prototype.

## Design Overview

The dominant acoustic model is the standard vibrating string — Mersenne–Taylor at L = 13 in (330 mm), tuned G3-D4-A4-E5. The ceramic body intentionally is **not** a top-plate resonator; the piezo captures at the bridge and bypasses ceramic body modes. Secondary Helmholtz coloration from the porcelain shell is incidental.

This is a deliberate hybrid stress test of three shop pipelines simultaneously:

1. **Slip-cast ceramic** — same Bambu+kiln pipeline as ocarina, udu, gemshorn, ceramic-tongue-drum.
2. **Woodworking** — bolt-on maple neck + ebony fingerboard from electric-violin.
3. **Electronics** — Fishman V-200 under-bridge piezo + endpin jack signal path.

## Source Notes

- [repo] [README](../../../../strings/ceramic-electric-violin/README.md) — design rationale, hybrid pipeline description, string physics.
- [repo] [design.md](../../../../strings/ceramic-electric-violin/design.md) — detailed acoustic and structural design.

## Cross-Links

- [[acoustic-classes/electric-string-piezo]]
- [[fabrication/slip-cast-ceramic]]
- [[fabrication/bolt-on-neck]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Have ceramic body shrinkage measurements been captured from fired test tiles?
2. Has the bolt-on maple neck been fitted to the ceramic body?
3. Has the Fishman V-200 piezo been installed and signal path tested?
4. Has CEV-P1 prototype been built and string-tuning validated?
5. Has the piezo-body coupling been characterized vs ceramic body modes?

## Maintenance Notes

Next ingest should pull in ceramic shrinkage data, neck-fit results, and CEV-P1 first-play measurements. Update [[acoustic-classes/electric-string-piezo]] with any empirical piezo-body coupling observations.
