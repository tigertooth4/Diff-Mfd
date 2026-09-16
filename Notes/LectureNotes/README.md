# Warner study reprint

The entry point is `main.tex`; the compiled reading copy is `output/main.pdf`.
The colored companion uses `main_color.tex` and produces `output/main_color.pdf`.
Both editions share the same chapter, figure and notation sources. The colored
edition directly uses the original, unmodified `elegantbook.cls` and its default
blue theme: green definitions, orange theorems, bright blue propositions and
numbered remarks, blue chapter headings, and the original illustrated cover.
`reprint-color.sty` contains only compatibility and layout refinements.
The plain edition uses `book` plus `reprint.sty`.
OCR markdown and original scan figures remain as reference material; all body
illustrations in both PDFs use the redrawn vector sources. Only the colored
edition's original cover is raster artwork.

## Build

Requirements: XeLaTeX, latexmk, makeindex and the packages in `reprint.sty`,
`reprint-color.sty` and `elegantbook.cls`
(included in a full TeX Live installation). Run from this directory:

```sh
uv run --no-project scripts/build_notation.py
latexmk -xelatex -synctex=1 -interaction=nonstopmode -halt-on-error -outdir=output main.tex
uv run --no-project --with pymupdf --with pillow scripts/verify_reprint.py
```

Build and verify the colored edition separately:

```sh
latexmk -xelatex -synctex=1 -interaction=nonstopmode -halt-on-error -outdir=output main_color.tex
uv run --no-project --with pymupdf --with pillow scripts/verify_reprint.py --jobname main_color
```

To render the entire book into page contact sheets for visual review:

```sh
uv run --no-project --with pymupdf --with pillow scripts/verify_reprint.py --render ../../tmp/reprint-review
```

Add `--jobname main_color` to render and check the colored edition.

Both the source checks and rendering report progress. The verification command
fails for mismatched original item numbers, incorrect equation tags, duplicate
equation destinations, unresolved references, missing glyphs, font substitutions,
overflow, missing vector sources, unexpected raster images or invalid internal PDF links.
The original color-cover artwork is the sole allowed raster exception.
It complements visual review; it does not prove mathematical correctness.

Only the final PDFs in `output/` are versioned. Compiler auxiliaries, temporary
verification reports and rendering contact sheets are generated locally and ignored.

## Editing conventions

- Chapters 1--6 use Warner's item numbers. `\warnernumber{17}` immediately
  before a theorem or discussion restores item 17 in the current chapter.
  `\discuss{5.17}{Title}` shares the theorem counter; it is not a subsection.
- Original local equation numbers are explicit tags: for example,
  `\tag{4}\label{eq:5.17:4}`. Keep the chapter/item prefix in the label even
  when the printed tag is just `(4)`. Equation PDF destinations are unique.
- The supplied scan itself skips (2) in item 5.6 (printed p. 166). This gap
  is retained rather than silently renumbering the subsequent formulas.
- Original source pages differ from the pages in this reprint. Refer to
  numbered items and labels when reporting a correction.
- All 52 replacements have editable sources in `figures/redrawn/` and an
  entry in `figures/manifest.json`. Use `\redrawn{figure-01}` to insert one.
  Geometric drawings are schematic. Preserve objects, arrows, incidence,
  orientation and labels when changing their appearance.
- Further native exchange diagrams in Chapter 5 use `tikz-cd`; long labels
  are abbreviated only with accompanying definitions.
- Edit `notation.json`, then run `scripts/build_notation.py`; do not hand-edit
  generated `chapters/notation.tex`. The index links to the current PDF pages.
- Appendices A and B are editorial supplements. Keep additions and source
  acknowledgments distinct from Warner's Chapters 1--6.

See `REVISION.md` for the changes and the scope of verification.
