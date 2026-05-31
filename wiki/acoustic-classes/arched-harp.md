---
title: Arched Harp Acoustic Class
slug: arched-harp
wiki_type: acoustic-class
status: active
sources:
  - path: ../../../sambuca/reverse-engineering.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/design.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/assembly-manual.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/wolfram/sambuca-acoustics-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
crosslinks:
  - instruments/sambuca
  - acoustic-classes/harp-lute
  - synthesis/public-release-blockers
open_questions:
  - "Where should the library draw the boundary between arched harp, harp-lute, frame harp, and zither?"
  - "Should arched-harp packets standardize string-holder strip pull-tests and voicing logs?"
  - "What default break-margin and proof-load factors should apply to curved cantilever necks?"
  - "Should every arched-harp page carry an explicit cultural/provenance language section when it derives from archaeological or living-tradition forms?"
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
review_due: 2026-08-18
tags:
  - acoustic-class
  - string
  - arched-harp
---

# Arched Harp Acoustic Class

## Overview

This page tracks instruments where strings run from a single curved or arched neck into a resonant body, usually terminating on or near the soundboard with a string-holder strip rather than crossing a separate raised bridge. The first active member in the wiki is [[instruments/sambuca]].

The class differs from [[acoustic-classes/harp-lute]] because the neck is a curved cantilever and the string termination is part of the soundboard load path. The main design problem is the coupled behavior of string schedule, curved neck bending, neck/body joint, soundboard strip load, cavity volume, and player posture.

## Active Instruments

- [[instruments/sambuca]] - modern boat-shaped arched harp inspired by the Royal Cemetery at Ur, with a walnut boat hull, cedar soundboard, sapele curved neck, keel port, multi-strip inlay program, and MULE validation path.

Potential future members:

- `egyptian-harps`
- `floor-harp`
- `saung-gauk-inspired`
- `chang-inspired`

## Governing Design Pattern

Reusable questions for this class:

- What string schedule, speaking-length curve, and unit weights keep total tension inside a safe band?
- Does the curved neck and neck/body joint carry the full cantilever load with a documented proof test?
- Is string force transferred through a glued strip, tied holes, pins, or another termination method?
- Can the string-holder strip position be moved during voicing before it becomes permanent?
- What soundboard thickness, bracing, and cavity/port tuning support the bass range?
- Does the player posture block the primary sound radiation path?
- Which visual claims are archaeological, which are modern design choices, and which require cultural review?

## Sambuca Notes From First Ingest

The sambuca packet treats the direct string-holder strip as the correct arched-harp pattern and explicitly rejects a separate raised bridge bar. The strip is mounted with reversible glue during MULE voicing so its bow-end position can be tuned before committing the ROOT build.

The high-risk structural element is the curved neck as a cantilever rooted in the boat hull. The sambuca packet uses a MULE 30-day hold and neck-deflection limit before allowing the ROOT build to reach calibrated full tension.

The acoustic model combines:

- vibrating-string tension and length
- boat-hull cavity and keel-port Helmholtz behavior
- soundboard plate-mode estimates
- coupled cavity/plate response

The first sambuca ingest also surfaced a useful class-level maintenance lesson: arched-harp packets need one authoritative geometry source before acoustic predictions are repeated, because small changes in depth, cavity volume, string length, or port area alter both structural and voicing claims.

Source: [sambuca design notes](../../../../strings/sambuca/design.md)

## Cross-Instrument Knowledge To Build

This page should eventually compare:

- boat-shaped arched harps versus harp-lutes
- string-holder strip load transfer versus raised bridge transfer
- curved cantilever neck proof testing
- keel/side port projection versus soundboard rose projection
- archaeological-fingerprint preservation language
- MULE-first validation patterns for stringed instruments

## Open Questions

1. Should `sambuca` remain the only initial arched-harp member, or should the existing `kora` page cross-link here as a bridge-harp neighbor while staying primarily under [[acoustic-classes/harp-lute]]?
2. What minimum validation rows should every arched-harp packet include: total tension, neck deflection, strip pull-test, soundboard deflection, and acoustic sweep?
3. Should string-holder strip position always be treated as a MULE voicing decision rather than a CAD-locked value?
4. How should cultural review be generalized for instruments derived from ancient archaeological forms with modern interpretive reconstructions?

## Maintenance Notes

Update this page after the sambuca SAM-13-MULE build records real neck deflection, strip position, total tension, and acoustic measurements. If more arched-harp repos appear, split reusable structural guidance into fabrication pages for string-holder strips and curved-neck proof testing.
