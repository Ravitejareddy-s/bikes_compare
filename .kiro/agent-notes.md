# Agent Notes — bikes_compare

Agent-maintained context for this repo. Not meant for humans. Keep it short; update it when something lasting changes.

## What this project is
Spec data for three **Ultraviolette electric motorcycles**, pulled from their official PDF spec sheets:

1. **F77 Mach 2** — race-bred sport.
2. **F77 Superstreet** — street-oriented sport. Mechanically identical to the Mach 2; differs only in stance/positioning and colour options.
3. **X-47** — versatile adventure bike. Unique bits: UV Hypersense 77 GHz radar, MRF Revz-AT adventure tyres, 200 mm ground clearance, 610 Nm rear-wheel torque, 145 km/h top speed (lower than the F77s' 155).

Each bike comes in a **base (7.1 kWh / SRB7)** and a **top (10.3 kWh / SRB10)** battery variant. Headline figures use the top variant; many values differ by variant.

## Source files
- `*.pdf` — the three original spec sheets (source of truth).
- `extract.py` — PyMuPDF script; dumps text to `extracted/text/*.txt` and page renders to `extracted/images/*.png`.
- `extracted/text/*.txt` — clean extracted text per bike.
- `extracted/data/bikes.json` — **master structured data** (10 spec categories; cells are a string or `{base, top}` where variants differ). This is the canonical dataset — edit here first.
- `extracted/data/bikes_comparison.csv` — flat CSV (62 rows) generated from the JSON by `make_csv.py`. Regenerate with `python3 extracted/data/make_csv.py`.

## Environment notes
- `python3` + PyMuPDF (`import fitz`) available. No pdftotext/poppler/tesseract.
- Reading the PNGs via file tools returns raw bytes (not visually useful) — rely on the extracted text.

## Data accuracy
All values in `bikes.json` were verified against the extracted PDF text. If specs change, update `bikes.json` then rerun `make_csv.py`.
