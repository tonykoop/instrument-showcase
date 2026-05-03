# Template 13 — Acoustic Measurement Report

The instrument-specific acoustic characterization document. FFT spectra, frequency response, SPL, tuning deviation, T60. Built from the strike-level dataset in `study/data/`.

## Format

- **Multi-page, letter portrait, web + PDF.**
- **Sections:** Instrument under test → Measurement setup → Results per note/tongue → Aggregate plots → Discussion.
- **Per-note pages:** target Hz, measured Hz, cents error, FFT plot, harmonic ratio table, T60 decay curve, SPL @ 1 m.
- **Aggregate plots:** all-notes deviation chart, harmonic-ratio heatmap, prototype-vs-prototype comparison if multiple builds.

## Files this template consumes

| Source | Used for |
|---|---|
| `study/data/*.csv` | Raw measurement data |
| `study/data-template.csv` | Column definitions |
| `validation.csv` | Build-time targets |
| `<instrument>-design-table.xlsx` | Predicted values |
| `study/README.md` | Measurement setup section |

## Voice

Lab-report. Numbered figures and tables. Captions cite the source CSV row range.

## What "done" looks like

- Every chart has units on both axes.
- Every claim cites a CSV path and row range.
- Aggregate-deviation chart is the headline figure (Figure 1).
- Limitations section addresses environmental drift (T, RH, mallet variation).
