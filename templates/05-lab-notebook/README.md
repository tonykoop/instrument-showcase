# Template 05 — Lab Notebook (Build Log + Correction-Factor Tables)

A printable lab notebook for an instrument's build and DoE study. Pre-populated columns ready for measurement entry. Procedure on the left page; data table on the right. The lab notebook is **filled in by hand at the bench**; this skill produces the empty form.

## Format

- **Letter, two-page spread per phase.**
- **Left page:** procedure, fixed inputs (geometry, material, environmental), instrumentation list, what-to-record-when reminders.
- **Right page:** the data table — one row per strike / blow / pluck / measurement event. Columns derived from `study/data-template.csv` if present.
- **Top-right of every right-hand page:** drum/instrument ID, phase, date row, signed-by line.
- **Final spread per phase:** a "correction factors" table — empty rows where Tony writes the offset between predicted and measured values.

## Files this template consumes

| Source file | Used for |
|---|---|
| `study/README.md` | DoE protocol — phases, research questions, instrumentation list |
| `study/data-template.csv` | Column headers — copied verbatim into the data tables |
| `validation.csv` | Build-time validation rows (separate page) |
| `bom.csv` | Reference list at the top of each phase |
| `design.md` | Master catalog row at the top of the notebook |

## Voice

Declarative column headers + procedure steps. No prose anywhere. Headers verbatim from the data schema. Procedure steps in imperative tense.

## Correction-factor tables

For each model used (e.g., `f₁ ≈ 0.162 · (h/L²) · √(E/ρ)`), include a table:

| Tongue | Predicted f₁ (Hz) | Measured f₁ (Hz) | Δ (cents) | Suggested K-correction | Notes |
|---|---|---|---|---|---|
| 1 | (filled from study) | _____ | _____ | _____ | _____ |
| 2 | ... | _____ | _____ | _____ | _____ |

Rows are pre-populated with the predicted column from the design table; the rest is blank.

## What "done" looks like

- Strike-level data schema columns appear exactly as they do in `study/data-template.csv`.
- Phase headers match `study/README.md` (Phase 1 / 2 / 3 for the tongue drum).
- Page numbers + serial + phase in every footer.
- Correction-factor table has the predicted column filled and other columns blank.
- Print without text wrap on letter paper at landscape orientation.
