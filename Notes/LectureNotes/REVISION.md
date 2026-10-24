# Revision of 16 September 2026

## Differential and pushforward chain rules (21 October 2026)

- Section 1.22 now presents the differential and its coordinate formula,
  the scalar and multivariable chain rules, the pushforward definition,
  and the pushforward chain rules before introducing pullbacks.
- Added the formula for a pushed-forward tangent vector acting on a
  composite function and a test-function proof of the composition law.
- Rebuilt both editions (236 plain / 253 colored pages) and visually
  checked the affected pages in both PDFs.

## Section 1.22 teaching order (16 October 2026)

- Reordered 1.22: definition of df_m, its coordinate total-differential
  formula and derivation, tangent maps, pullback, then df = f^*(dr).
- Renumbered this rewritten section (1)--(8) in presentation order and
  updated the semantic references in 1.23(a) and 1.26. The reprint note
  explicitly records this exception to the original local numbering.
  Reordered the corresponding notation-index entries.
- Rebuilt both editions (236 plain / 252 colored pages).
  All automated checks pass, with 837 local equation labels. Visually
  reviewed the reordered section in both editions.

## Book-wide pushforward notation (16 October 2026)

- Extended the subscript-star convention from 1.22 throughout the book.
  Updated tangent maps in Chapters 1--4, including exercises, chain rules,
  inverse maps, tangent bundles, related vector fields, flows, Lie-group
  homomorphisms, exponential maps, actions and induced Riemannian metrics.
  Scanned all six chapters and both appendices; Chapters 5--6 and the
  appendices require no tangent-map substitutions.
- Distinguished indexed maps from pointwise evaluation: for example,
  `(exp_X)_*` is the pushforward of the one-parameter subgroup, whereas
  `exp_{*,0}` is the derivative of the exponential map at zero.
  Higher tangent maps in 1.26 now use `varphi_*^{(k)}` with their duals;
  revised the paragraph connecting the first-order case to 1.22.
- Clarified the 1-form interpretation of df in 2.19. Kept ordinary
  derivative fractions, coordinate differentials, exterior derivatives,
  integration measures and cochain differentials unchanged in meaning.
  Updated three vector figures, the notation index and the global reprint
  note. Preserved all original item/equation labels and explicit tags.
- Rebuilt both editions (235 plain / 252 colored pages); full verification
  passes with zero errors. Reviewed representative changed pages in both
  editions, including the chain rule, flows, Lie groups and notation.

## Section 1.22 rewrite: tangent maps versus covectors (16 October 2026)

- Rewrote 1.22 with subscript-star tangent maps and superscript-star
  pullbacks, reserving `df_m` for a covector. Retained the six original
  numbered equations and their labels. An editorial notice explains the
  notation and its relation to `d psi_m` elsewhere in the book.
- Equation (5) now gives `f_{*,m} v` in `T_{f(m)} R`; equation (6)
  gives `df_m(v)` in `R`. Added the computation of the coefficient using
  the coordinate r, the canonical identification of the tangent line with
  R, and the pointwise verification of `df_m = f_m^*(dr_{f(m)})`.
  Explained the global 1-form identity `df = f^*(dr)`.
- Updated the reprint note and notation index to remove the superseded
  ambiguous `f_* = df` entry. The index now contains 156 entries.
- Rebuilt both editions (235 plain / 252 colored pages), with zero
  verification errors. Reviewed the rewritten section visually in both PDFs.

## Pushforward notation note (16 October 2026)

- Added an explicitly editorial note in 1.22 matching the course slides:
  `psi_{*,m} = d psi_m`, `f_{*,p} = df_p`, and `f_* = df` when the
  base point is understood. Included the coordinate-vector example and
  distinguished subscript-star pushforward from superscript-star pullback.
- Added `sigma_{*,t} = d sigma_t` in the velocity formula in 1.23(e),
  and a linked pushforward entry in the notation index (now 155 entries).
  Original numbered equations and item labels remain unchanged.
- Rebuilt both editions (235 plain / 252 colored pages); all automated
  checks pass. Visually inspected the new note and velocity formula
  in both PDFs.

## Chapter 1 equation-number repair (16 October 2026)

- Restored 27 missing local equation tags in items 1.9--1.26, retaining
  all existing labels. In particular, the differential in 1.22 is now
  numbered (1), matching the reference in the non-singularity definition.
  Removed two obsolete commented-out tag/hypertarget lines.
- Rebuilt both PDFs (235 plain / 252 colored pages). Both complete
  verification runs now pass with zero errors, including all 835 local
  equation numbers, unique equation destinations and internal PDF links.
  Visually checked the corrected 1.22 page in both editions.
- This resolves the 27 numbering failures reported in the earlier entries
  below; those entries retain the historical verification results.

## Curve illustration update (16 October 2026)

- Redrew figure-03 in 1.23(e) as a non-self-intersecting curve with an
  arrow indicating increasing parameter. The marked point lies exactly
  on the curve; the two Bezier pieces share the derivative `(1.2, 1.5)`
  there, and the velocity arrow is parallel to that derivative.
- Updated both PDF editions and visually checked the resulting figure.

## Dual-map and pullback notation update (16 October 2026)

- Replaced the prefix-delta notation for transposes and pullbacks throughout
  Chapters 1--4 and their exercises by a superscript star. At a source point
  m, the transpose is now `psi_m^* = (d psi_m)^*`; on forms the global
  pullback is `psi^*`. Updated the source-point subscripts in 1.30 rather
  than retaining the old target-point restriction notation.
- The transpose of a higher differential is written `$(d^k\varphi)^*$`.
  Indexed maps, compositions, flows, translations and simplex face maps
  retain their indices inside the pullback notation. Updated the reprint
  note and generated notation index. Covector names, Kronecker symbols,
  Lebesgue numbers and the Chapter 6 codifferential are unchanged.
- Corrected the right-hand side of the unnumbered final equality in the
  proof of 3.27 from `varphi^*` to `psi^*`: psi is the prescribed Lie-algebra
  map, and the graph construction in (1) gives `varphi^*(omega_i) =
  psi^*(omega_i)`. This is a contextual editorial correction of the
  inherited transcription, not a claim of scan collation.
- Rebuilt both PDFs (235 plain / 252 colored pages), inspected the changed
  definitions, pullback formulas, Lie-group argument, Stokes formula and
  notation index visually, and verified all chapter labels and explicit
  equation tags unchanged. Both verification reports have exactly the same
  27 pre-existing Chapter 1 numbering errors as before this update, with
  no new compile, font, overflow or PDF-link failures.

## Tangent-space notation update (16 October 2026)

- Unified tangent and cotangent spaces as `$T_mM$` and `$T_m^*M$`,
  and bundles as `$TM$` and `$T^*M$`, across the textbook body, exercises,
  notation index and three vector figures. Updated Lie-group, Euclidean,
  product, boundary and quotient tangent spaces as well.
- Section 1.26 uses `$T_m^{(k)}M$` for higher order derivations and
  `$T_m^{*(k)}M$` for higher order differentials; their canonical duality
  remains explicit. The reprint note explains these editorial conventions.
- Retained base-point names, differential/pullback notation and unrelated
  subscripted objects such as Grassmann manifolds and tensor spaces.
  Archival OCR and the original scan remain unchanged.
- Rebuilt both PDFs (235 plain / 252 colored pages) and visually reviewed
  definitions, differentials, higher order notation, three changed figures
  and notation-index pages in both editions. No overflow, font or link
  errors were reported. The verifier still reports only the 27 pre-existing
  Chapter 1 equation-number mismatches documented below; Chapter 1 labels
  and explicit equation tags were checked unchanged against HEAD.

## Germ notation update (12 October 2026)

- Replaced bold function germs by `$[f]_m$`, abbreviated to `$[f]$` when
  the base point is clear, in Chapter 1 and the function-sheaf example and
  exercise in Chapter 5. Vector typography is unchanged.
- Distinguished the scalar value `$f(m)$` from the constant-function
  germ `$[f(m)]$`; retained braces for cosets in powers of the vanishing ideal.
  Explained the coordinate tuple shorthand in 1.26 and regenerated the
  notation index from `notation.json`.
- While updating these formulas, corrected the coordinate index `1` to `i`
  in 1.20(a), and the exponent `a` to `alpha` in 1.26(5), consistently with
  the adjacent formulas. Used set braces for the collection in 1.26(5) and
  the basic open set of germs in 5.2. These are editorial notation corrections;
  the archival OCR markdown is unchanged.
- Rebuilt both editions (235 plain / 252 colored PDF pages) and visually
  reviewed the changed definitions, derivation, higher-order formulas, sheaf
  example/exercise and notation index. Compilation has no overflow, undefined
  references or font errors. The existing verifier reports 27 Chapter 1
  equation-number mismatches: these equations already use automatic chapter
  numbering while the verifier expects local tags. All Chapter 1 equation
  labels and explicit tags are unchanged from the branch base. No other
  verification errors were reported; this notation update does not resolve
  the pre-existing numbering inconsistency.

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
