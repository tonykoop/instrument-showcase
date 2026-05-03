# Template 06 — Design of Experiments Report

The full engineering write-up of an instrument's DoE study. Long-form, charts-and-graphs, decision-tree-laden. Suitable as a portfolio piece or a conference handout.

## Format

- **Multi-page, letter portrait, web + PDF.**
- **Sections:** Abstract → Hypotheses → Methods → Materials & instrumentation → Phase 1 results → Phase 2 results → Phase 3 results → Correction factors → Limitations → Future work → References.
- **Charts:** FFT spectra, frequency-error vs. predicted, K-factor scatter, prototype-history timeline.
- **Decision trees:** mitigation flowcharts (e.g., "if measured f₁ is ≥ +25 cents above predicted, then …").
- **Image plate spreads:** prototype evolution photos, side-by-side wood comparisons.

## Files this template consumes

| Source file | Used for |
|---|---|
| `study/README.md` | Spine of the report — sections map to study sections |
| `study/data-template.csv` and `study/data/*.csv` | Raw measurement data → charts |
| `images/` | Prototype evolution, build-history photos |
| `bom.csv`, `cut-list.csv` | Materials table |
| `design.md` | Hypotheses + assumptions section |

## Voice

Academic-honest. Hypotheses, methods, results, limitations. Number every figure and table. Cite sister repos (djembe, tensile-testing, cnc) where physics or methodology was originally derived.

## What "done" looks like

- Reads as a self-contained DoE report.
- Every chart has a caption referencing the underlying CSV path.
- Every numerical claim cites the row in `study/data/...csv`.
- Limitations section is honest about what the study didn't cover.
- References section credits any source plans (e.g., the WOOD magazine Oct 2008 plan).
