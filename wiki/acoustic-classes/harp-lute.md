---
title: Harp-Lute Acoustic Class
wiki_type: acoustic-class
status: active
last_updated: 2026-05-18
source_count: 1
open_questions: 6
tags:
  - acoustic-class
  - string
  - harp-lute
---

# Harp-Lute Acoustic Class

## Overview

This page tracks instruments where many open strings are carried over a bridge into a resonant body, with the bridge and body acting as load-bearing and tone-shaping systems. In the current wiki, the first active member is [[instruments/kora]].

This class is different from a simple frame harp or zither because the bridge, neck/spine, tail anchoring, membrane or soundboard behavior, and player hand access are coupled. The design problem is structural, acoustic, ergonomic, and cultural at the same time.

## Active Instruments

- [[instruments/kora]] - 21-string kora-inspired hybrid prototype with segmented wooden bowl, membrane/head decision, tall bridge, through-neck or internal-spine load path, and private cultural/safety review gates.

Potential future members:

- `ngoni`
- `sambuca`
- `egyptian-harps`
- `floor-harp`

## Governing Design Pattern

Reusable questions for this class:

- What is the string schedule, and what are the real unit weights and break margins?
- Does the neck or internal spine carry the string load continuously, or is the shell being asked to carry load accidentally?
- How does the bridge footprint distribute force into the head or soundboard?
- Is the resonator material a source of cultural meaning, acoustic behavior, or both?
- Does the player have safe hand access to both banks of strings?
- Which claims are engineering-study claims, and which claims require cultural or musical tradition review?

## Kora-Specific Notes From First Ingest

The kora page currently treats the instrument as a private-review hybrid prototype. The critical design issues are:

- Treble string break margins are too high under the current idealized schedule.
- The segmented wooden bowl is a shop substitute and should not be described as acoustically or culturally equivalent to a traditional calabash.
- The bridge is both tone-shaping and safety-critical because it is tall and head-loaded.
- The neck/tail load path needs proof-load validation before stringing.
- Public language needs cultural provenance review before release.

Source: [kora design notes](../../../../strings/kora/design.md)

## Cross-Instrument Knowledge To Build

This page should eventually compare:

- kora and ngoni bridge load paths
- arched-harp vs harp-lute string banking
- membrane resonator vs wooden soundboard behavior
- string tension ramps and practical break-margin conventions
- public-release language for culturally situated instruments

## Open Questions

1. Which other Heifer Zephyr string instruments should be grouped here versus under `harp`, `arched-harp`, or `zither`?
2. What break-margin threshold should be the default safety gate for nylon treble strings in this library?
3. Should bridge-foot pressure become a standard validation row for every harp-lute or bridge-harp packet?
4. What minimum proof-load factor should apply to neck/tail assemblies?
5. Which public wording constraints are class-level, and which are instrument-specific cultural review issues?
6. Should this class get a shared Wolfram string-schedule notebook template?

## Maintenance Notes

When `ngoni`, `sambuca`, or other related string instruments are ingested, update the active member list and split any historical/cultural release concerns into [[synthesis/public-release-blockers]] if they affect multiple projects.
