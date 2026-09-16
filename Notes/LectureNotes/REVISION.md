# Revision of 16 September 2026

## Changes

- Provided two A4/11pt editions sharing the same corrected content. `main.pdf`
  uses a restrained book layout and typographic vector cover. `main_color.pdf`
  directly uses the original, unmodified `elegantbook.cls`, retaining its exact
  blue/green/orange palette, theorem frames, ornaments and illustrated cover.
  Local refinements address line spacing, long title wrapping, numbered
  discussions, and figures inside boxed statements.
- Added an editorial note, PDF title/author metadata, matching text and math
  fonts, upright definitions, and normal Roman front-matter numbering.
- Restored the original numbered-item sequence in all six chapters: 64, 34,
  68, 19, 46 and 36 items, respectively. Numbered discussions share that sequence
  instead of generating blank subsection headings.
- Restored local equation tags and unique PDF destinations. Reinstated the
  missing tags for the lattice 5.23(3) and diagram 5.43(9). Compared 6.31 and
  6.32 with source pp. 243--246: restored 6.31(2)--(5), associated 6.32(1) and
  6.32(5) with their numbered assertions, and removed spurious numbers from
  the following unnumbered calculations. The source's own gap 5.6(2) is retained.
- Replaced 43 chapter JPGs and eight bitmap-containing appendix PDFs with
  editable TikZ sources. Also recovered and redrew the compact-exhaustion
  illustration on source p. 9, which OCR had turned into a row of circle symbols.
  Archival scans remain in the repository but are not included in the PDF.
- Rebuilt Chapter 5 exchange diagrams with explicit object-to-object arrows,
  removed a duplicated formula number inside an arrow row, aligned identity
  maps, and clarified the two large resolution-comparison diagrams using
  explicitly defined abbreviations. Retained the distinction between barred
  and Cech cohomology in diagram 5.33(20).
- Rebuilt the notation index as 154 explained entries with original item
  numbers and automatically linked current page numbers, including material
  omitted from the inherited OCR-based index.
- Completed Appendix B with the implicit function theorem, regular level
  sets, the constant rank theorem, proofs, and dual-map/annihilator facts.
  Labeled both appendices as editorial supplements and corrected their hierarchy.
- Removed the duplicate bibliography heading/empty page, appendix manual
  page breaks, the isolated final formula in Chapter 4, and hanging proof marks.
  Restored proof boundaries before discussions 1.33 and 5.37 and the complete
  scope of Definition 2.3.
- Added reproducible build and validation instructions. The verification script
  supports both job names and optional page rendering. Added `.gitignore` and
  stopped tracking 11 compiler/index auxiliary files; only final PDFs are
  versioned in `output/`. Source TeX, vector drawings and notation data remain
  versioned, while local review images, caches and macOS metadata are ignored.

## Selected text and notation corrections

- Repaired malformed inline mathematics in Definition 2.7, the non-singular
  pairing definition; restored ordinary text that had been typeset as variables.
- Corrected the set-index notation in 1.1 and OCR-spaced `lim`, `id`, `for`,
  `and` and other text fragments in formulas.
- Replaced digit 8 misreadings of the sheaf symbol, repaired the degree-zero
  cohomology statement in 5.33, and corrected the cup-product notation in 5.44.
- Corrected the matrix coordinate subscript in 3.10, left translation in 3.31,
  and the missing scalar complex conjugate in the Hermitian-product explanation
  in 6.15.
- Corrected the notation index's sheaf/stalk symbols, matrix Lie algebras,
  Jacobian determinant, simplex integral, and multilinear-function space.
- In 1.34, wrote `r_i(a)` instead of the scanned source's `x_i(a)` because
  `a` belongs to the Euclidean chart image. This is an explicit editorial
  clarification of the coordinate domain, rather than an OCR-only correction.

## Verification scope

The supplied scan was used for targeted comparisons of numbering, figures,
notation and the corrections above. All pages of the revised book are rendered
for layout review, with detailed inspections of illustrations, exchange
diagrams, chapter transitions, appendices and the index. Automated checks cover
the original item sequence, equation labels and destinations, notation targets,
PDF links and assets, and compilation diagnostics.

This is a revised study reprint, not a line-by-line critical edition or an
independent mathematical proof audit of every theorem and exercise. Existing
OCR material remains the starting text; later substantive corrections should
be recorded with their source page and original item number.

Run the commands in `README.md` to regenerate the checks. Machine-readable
results are printed to stdout and, with `--render`, saved as `verification.json`
alongside the rendered review pages. These intermediate artifacts are ignored.
The color edition retains one raster image on its original cover; body figures
in both editions are vectors. Underfull-box diagnostics and ElegantBook's
automatically repaired bookmark-anchor warnings are distinguished from broken
references, missing glyphs and actual overflow, which fail validation.
