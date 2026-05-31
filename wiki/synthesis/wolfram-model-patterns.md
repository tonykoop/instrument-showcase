---
title: Wolfram Model Patterns
slug: wolfram-model-patterns
wiki_type: synthesis
status: active
sources:
  - path: ../../data/library-manifest.json
    kind: repo
    last_seen: 2026-05-18
  - path: ../../scripts/generate_library.py
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../wolfram-cloud-sync/manifest/wolfram_embed_urls.json
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../wolfram-cloud-sync/INTEGRATION-CONTRACT.md
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../kora/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../sambuca/wolfram/sambuca-acoustics-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../cajon/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../wood-shell-tongue-drum/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../gemshorn/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../ocarina/docs/ceramic-vessel-lab/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../udu/docs/ceramic-vessel-lab/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../duntong/wolfram/instrument-model.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../glockenspiel/wolfram/instrument-model.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../handpan/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../chalumeau/build/packet/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../duduk/wolfram/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../didgeridoo/analysis/wolfram-study-notes.md
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../dundun/analysis/membrane-shell-study.wl
    kind: wolfram
    last_seen: 2026-05-18
crosslinks:
  - synthesis/public-release-blockers
  - instruments/kora
  - instruments/cajon
  - instruments/wood-shell-tongue-drum
open_questions:
  - "Should public Wolfram embeds be held behind the same release gates as public explorer pages?"
  - "Which owner-only notebooks should be published first after source and safety review?"
  - "Should local-only and would-publish permissions get their own library state instead of collapsing to pending?"
  - "Should every Wolfram notebook include a standard validation block with Wolfram version, command, input data, and measured-vs-predicted output?"
  - "Should the generator surface multiple Wolfram files per repo instead of using only the first entry for the library card?"
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
review_due: 2026-08-18
tags: [synthesis, wolfram, cloud-embed, acoustic-model, validation]
---

# Wolfram Model Patterns

## Overview

Wolfram is the portfolio's interactive acoustic workbench: notebooks hold first-pass formulas, design sweeps, validation plots, and Cloud embeds for explorer pages. The current library should treat a live Wolfram badge as an embed-availability signal, not as proof that an instrument packet is public-ready or acoustically validated.

The state machine is defined in [generate_library.py](../../scripts/generate_library.py) and the Wolfram Cloud bridge contract in [INTEGRATION-CONTRACT.md](../../../../_meta/wolfram-cloud-sync/INTEGRATION-CONTRACT.md):

| Library state | Contract meaning | Publish implication |
| --- | --- | --- |
| `live` | `permission == "Public-Execute"` and `cloud_url` is present. | Explorer can iframe the notebook. Still needs release and validation review. |
| `owner-only` | `permission == "Private"`. | Uploaded to Wolfram Cloud, visible to the owner, rendered as a grey-dot non-embed for public viewers. |
| `pending` | No usable entry, blank URL with unrecognized permission, local-only manifest row, or string-only Wolfram entry. | Needs manifest reconciliation, upload, publish, or a deliberate "not ready" decision. |
| `diagnostic` | `permission == "failed"` or `permission == "missing"`. | Sync or publish ran but hit a cloud-object problem. Re-run the Wolfram sync/publish diagnostics before embedding. |

## Current Status

As of [library-manifest.json](../../data/library-manifest.json) generated 2026-05-18T21:09:42Z, the instrument library has 50 entries with Wolfram states:

| State | Count | Notes |
| --- | ---: | --- |
| `live` | 2 | `kora`, `sambuca` have Public-Execute URLs. |
| `owner-only` | 37 | The dominant state: uploaded private notebooks are available to the owner but not public embeds. |
| `pending` | 11 | All pending library entries are currently public-release blocked packets. |
| `diagnostic` | 0 | No current library card reports `failed` or `missing`; this is not proof that every cloud object was runtime-validated. |

Family distribution:

| Family | Entries | Wolfram state summary |
| --- | ---: | --- |
| wind | 24 | 18 owner-only, 6 pending |
| idiophone | 11 | 11 owner-only |
| drum | 8 | 6 owner-only, 2 pending |
| string | 7 | 2 live, 2 owner-only, 3 pending |

The broader [wolfram_embed_urls.json](../../../../_meta/wolfram-cloud-sync/manifest/wolfram_embed_urls.json) manifest currently lists 96 Wolfram files across instrument and support repos: 94 `Private` and 2 `Public-Execute`. The two public rows are `kora/kora-starter.wl` and `sambuca/wolfram/sambuca-acoustics-starter.wl`.

Important portfolio wrinkle: `generate_library.py` reads `capstone-manifest.json` first, then falls back to `wolfram_embed_urls.json`. Some repos therefore show `pending` in the library even though the cloud-sync manifest has a private uploaded row, because their local manifest still says `permission: local` or has a string-only Wolfram list. Examples include `chalumeau`, `duduk`, and `hulusi`.

Live does not mean release-ready. [[instruments/kora]] is still public-release blocked, and `sambuca` is in private review. That mismatch should be intentional and reviewed, because a Public-Execute cloud object is reachable even if the surrounding repo is not being marketed as public-ready.

## Source Notes

- [repo] [library-manifest.json](../../data/library-manifest.json) - 50 library entries; Wolfram state counts are 2 live, 37 owner-only, 11 pending, 0 diagnostic.
- [repo] [generate_library.py](../../scripts/generate_library.py) - state derivation maps `Public-Execute` plus URL to `live`, `Private` to `owner-only`, `failed` or `missing` to `diagnostic`, and everything else to `pending`.
- [wolfram] [wolfram_embed_urls.json](../../../../_meta/wolfram-cloud-sync/manifest/wolfram_embed_urls.json) - cloud-sync manifest has 96 rows: 94 `Private`, 2 `Public-Execute`, and no `failed` or `missing` rows at read time.
- [wolfram] [INTEGRATION-CONTRACT.md](../../../../_meta/wolfram-cloud-sync/INTEGRATION-CONTRACT.md) - the intended pipeline is inventory, sync, publish, then emit `engineering.wolfram[]` into each repo manifest.
- [wolfram] [kora/wolfram-starter.wl](../../../../strings/kora/kora-starter.wl) - string percent-break, target tension, diameter, and segmented-bowl ring summary for the 21-string prototype.
- [wolfram] [sambuca-acoustics-starter.wl](../../../../strings/sambuca/wolfram/sambuca-acoustics-starter.wl) - arched-harp family model with hull volume, axial modes, Helmholtz keel port, string tension, soundboard plate mode, and coupled cavity/plate response.
- [wolfram] [cajon/wolfram-starter.wl](../../../../percussion/cajon/wolfram-starter.wl) - corrected Helmholtz back-port model, clamped tapa plate mode, two-zone strike sketch, snare-wire frequency schedule, and first-prototype acceptance notes.
- [wolfram] [wood-shell-tongue-drum/wolfram-starter.wl](../../../../idiophones/wood-shell-tongue-drum/wolfram-starter.wl) - 3-DOF tongue, shell, and Helmholtz cavity model with per-family correction hooks for measured calibration.
- [wolfram] [gemshorn/wolfram-starter.wl](../../../../woodwind/gemshorn/wolfram-starter.wl) - vessel-flute Helmholtz family sweep using volume, window area, wall thickness, and cents error.
- [wolfram] [ocarina ceramic-vessel-lab starter](../../../../woodwind/ocarina/docs/ceramic-vessel-lab/wolfram-starter.wl) and [udu ceramic-vessel-lab starter](../../../../percussion/udu/docs/ceramic-vessel-lab/wolfram-starter.wl) - compact Helmholtz variants for vessel flutes and vessel-membrane drums.
- [wolfram] [duntong/wolfram/instrument-model.wl](../../../../percussion/duntong/wolfram/duntong-wolfram-model.wl) - cantilever tongue table plus Helmholtz, stopped-pipe, open-pipe, validation plot, and audio preview scaffolds.
- [wolfram] [glockenspiel/wolfram/instrument-model.wl](../../../../idiophones/glockenspiel/wolfram/glockenspiel-wolfram-model.wl) - free-free metal beam model with material K constants, bar length, node positions, validation plot scaffold, and audio previews.
- [wolfram] [handpan/wolfram-starter.wl](../../../../idiophones/handpan/handpan-starter.wl) - first-order gu resonance, note partials, field layout estimates, and explicit warning that plate behavior needs calibration from measured shells or FEM.
- [wolfram] [chalumeau/build/packet/wolfram-starter.wl](../../../../woodwind/chalumeau/build/packet/chalumeau-packet-starter.wl) and [duduk/wolfram/wolfram-starter.wl](../../../../woodwind/duduk/wolfram/wolfram-starter.wl) - closed-pipe reed-bore estimates, bore/reed/end corrections, tone-hole position estimates, and explicit empirical-validation warnings.
- [wolfram] [didgeridoo wolfram-study-notes.md](../../../../woodwind/didgeridoo/analysis/wolfram-study-notes.md) and [dundun membrane-shell-study.wl](../../../../percussion/dundun/analysis/membrane-shell-study.wl) - source-only or starter-only examples where runtime evidence and measured inputs are still explicitly missing.

## Design Knowledge

### Reusable Acoustic Model Patterns

| Pattern | Recurring repos | Core inputs | Outputs to standardize |
| --- | --- | --- | --- |
| String tension and load path | `kora`, `sambuca`, future `erhu`/`konghou` | speaking length, target pitch, string density or gauge, target tension, break stress | tension table, percent-break plot, total load, bridge/neck proof-load targets |
| Helmholtz vessel/cavity | `cajon`, `gemshorn`, `ocarina`, `udu`, `handpan`, `wood-shell-tongue-drum`, `sambuca` | cavity volume, port/window area, wall or neck length, end correction, speed of sound | resonance estimate, cents error, port sensitivity, measured correction factor |
| Pipe and tone-hole layout | `transverse-flute`, `flutes`, `siku-zampona`, `chalumeau`, `duduk`, `didgeridoo`, `tin-whistle` | bore length, bore radius, open/stopped condition, reed or embouchure correction, hole diameter, chimney height | body length, hole position schedule, predicted fingering frequencies, trim/cents sensitivity |
| Cantilever and free-free beams | `wood-shell-tongue-drum`, `duntong`, `glockenspiel`, `marimba`, `xylophone`, `steel-tongue-drum` | material K or E/rho, thickness, length, target pitch, support or slit geometry | cut-long length, trim schedule, node positions, predicted-vs-measured plot |
| Plate and shell modes | `cajon`, `sambuca`, `handpan`, `ceramic-hang`, `steel-pan`, `wooden-hang` | plate dimensions, thickness, E, rho, boundary condition, curvature coefficient | first-mode estimate, modal ratios, coupled response with cavity, "needs FEM/measured" warning |
| Coupled oscillators | `wood-shell-tongue-drum`, `sambuca`, `udu`, `cajon` | two or three uncoupled frequencies, coupling coefficient, effective mass/stiffness assumptions | split frequencies, coupling ratio, sustain or radiation heuristic, calibration slot |
| Membrane and shell studies | `dundun`, `djembe`, `frame-drum`, `udu` | head diameter, membrane surface density, tension, shell geometry, tap tone | f01 range, tuning sensitivity, measured strike/pitch comparison |
| Notebook evidence shell | many packets | constants, source CSV, validation CSV, `centsError`, `Dataset`, `Manipulate`, `ListPlot` | repeatable runtime note, measured vs predicted table, committed plot/table artifact, explicit assumption labels |

### Patterns Worth Promoting Into Templates

- Standard header block: source file, generated date, acoustic class, status label, and "assumption vs measurement" warning.
- Unit helpers: speed of sound with temperature note, inch/meter conversions, MIDI-to-frequency, cents error.
- Validation block: import `validation.csv`, compute measured-vs-predicted cents, and render a plot that gracefully says "No numeric validation rows yet."
- Publish block: notebook name, cloud path, permission, public URL, Wolfram version, command used, and whether the cloud object was only uploaded or actually Public-Execute.
- Coupling disclaimer: every coupled oscillator, membrane, plate, or shell model should state which coefficients are empirical placeholders and where measured calibration will enter.
- Release-gate note: notebooks can be interactive and useful before an instrument is release-safe; the explorer should not let a live iframe imply production readiness.

## Next Actions

1. Reconcile local manifests against cloud-sync output.
   Run the emit step from `wolfram-cloud-sync` after review so repos with uploaded private rows do not remain `pending` only because their `capstone-manifest.json` says `local` or lists a string path. Do not hand-edit shared manifests during multi-agent wiki ingest.

2. Decide whether live embeds obey release gates.
   `kora` and `sambuca` are Public-Execute now. Review whether their notebooks are safe to leave public while their instrument packets remain private-review or public-release blocked.

3. Publish in small reviewed batches.
   Use `wolfram_publish.wls --repos ...` for a controlled subset only. Good candidates should have a clean notebook, no cultural/safety overclaim, a useful owner-only cloud row, and an explorer section that accurately labels the model as predictive or validated.

4. Add a validation minimum before promotion.
   Each promoted notebook should record Wolfram version, command or notebook entry point, source constants or CSV, generated plots/tables, and the distinction between measured rows and assumptions.

5. Add an embed smoke test.
   For `live`, confirm the public URL loads and the explorer iframe mounts. For `owner-only`, confirm the grey-dot state renders without a broken iframe. For `pending`, confirm whether the cause is no upload, local-only manifest row, or deliberate hold. For `diagnostic`, capture the failed/missing cloud path.

6. Consider a richer library status.
   The current four-state display is useful, but it compresses `local`, `would-publish`, string-only manifest rows, and missing entries into `pending`. A separate `local-only` or `manifest-drift` status would make the publish queue easier to manage.

## Cross-Links

- [[synthesis/public-release-blockers]] - release posture and validation gates that should constrain public embed decisions.
- [[instruments/kora]] - live Wolfram URL but still public-release blocked.
- [[instruments/cajon]] - owner-only Wolfram notebook with predicted plate and Helmholtz values pending measured CJ-S data.
- [[instruments/wood-shell-tongue-drum]] - owner-only Wolfram notebook with root-mode coupled tongue/cavity model pending V1 measurements.

## Open Questions

1. Should Public-Execute Wolfram objects be reverted to `Private` when the surrounding packet is public-release blocked?
2. Which owner-only notebook should be the next controlled public embed after `kora` and `sambuca`?
3. Should `generate_library.py` prefer the cloud-sync manifest over local `permission: local` rows when a matching uploaded row exists?
4. What is the minimum validation artifact for an embed to be called "validated" instead of "interactive"?
5. Should the library card expose multiple notebooks per repo, or keep the first notebook as the representative state?

## Maintenance Notes

Update this page after any `wolfram-cloud-sync` publish or emit pass, after a generator state change, or after a notebook moves from source-only to measured validation evidence. Do not use this page as a substitute for the machine manifests; it is the human synthesis layer for deciding what the state means.
