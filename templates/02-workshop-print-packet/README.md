# Template 02 — Workshop Print Packet

The away-from-keyboard build guide. Tony prints this and uses it at the workbench. Includes tools, materials, PPE, and document references at the top of each section.

## Format

- **Letter, single-sided print, ~6–12 pages.**
- **Top of each section:** a "before you start" callout with required tools, fixtures, materials, PPE, and which other documents (drawings, drawing brief, BOM rows) you should have within reach.
- **Body of each section:** imperative-tense steps. No prose. No paragraphs. Each step is one verb.
- **Bottom of each section:** a "verify before moving on" checkbox list.

## Files this template consumes

| Source file | Used for |
|---|---|
| `assembly-manual.md` | Step sequence (this is the spine of the document) |
| `bom.csv` | Materials list at top of each step |
| `cut-list.csv` | Stock prep section |
| `sourcing.csv` | "Have on hand" supplier reference |
| `drawing-brief.md` | Required drawings / dimension callouts |
| `validation.csv` | Validation checkpoints between steps |
| `print-packet.md` | If present, refresh source — refactor existing into this template's structure |

## Voice

Imperative, terse, safety-aware. *"Set the spoilboard. Verify zero. Drop the bit."* No second person. No marketing.

## What "done" looks like

- Prints in landscape or portrait without text bleeding.
- PPE callout is visible above any cutting/turning step.
- Every CNC/lathe/laser step references the corresponding drawing or toolpath file by name.
- Validation checkboxes between major sections.
- Page numbers + serial in footer (so a packet on the bench can't be confused with another).
