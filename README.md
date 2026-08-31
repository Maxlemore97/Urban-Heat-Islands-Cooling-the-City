# Urban Heat Islands — Cooling the City

Biomimicry challenge report (Challenge 1) — ZHAW Blockweek Bionics 2026,
Institute for Sustainable Development.

LaTeX version of `Report_template_26_V3_final.docx`. Section 2
(*Challenge & Scoping*) is pre-filled with the Day-1 afternoon task from
`2 Scoping V6.pptx`; all other sections are scaffolds that carry the
template's own instructions as LaTeX comments.

## Repository layout

```
main.tex                    document class, packages, TikZ styles, includes
main.pdf                    the built report — tracked, refreshed by CI
references.bib              starting set of sources — verify before hand-in
sections/
  00_titlepage.tex          cover table: topic, picture, students, contributions
  01_introduction.tex       1. Introduction                (scaffold)
  02_scoping.tex            2. Challenge & Scoping         (FILLED IN)
  03_bioinspired_design.tex 3. Bio-Inspired Design Process (scaffold)
  04_sustainability.tex     4. Sustainability & Life's Principles (scaffold)
  05_discussion.tex         5. Discussion & Conclusion     (scaffold)
  06_appendix.tex           Appendix A (AI use) + Appendix B
figures/                    put images here
.github/workflows/          CI: builds the PDF on every push
```

The section headings match the .docx template exactly — the assignment
says *"Use the headings from this template"*, so please do not rename them.

## Working on Overleaf

1. Download this repository as a ZIP (**Code → Download ZIP**).
2. Overleaf → **New Project → Upload Project** → select the ZIP.
3. **Menu → Compiler → pdfLaTeX**. Overleaf runs `biber` automatically.

Overleaf premium accounts can also sync directly with GitHub
(**Menu → GitHub**), which keeps the CI build below in sync with your edits.

## Building locally

```bash
latexmk -pdf main.tex     # runs pdflatex + biber as often as needed
latexmk -c                # clean auxiliary files
```

Requires a TeX distribution with `biber` (TeX Live, MacTeX, MiKTeX).

## Automatic PDF build

`.github/workflows/build-pdf.yml` compiles `main.tex` on every push that
touches a `.tex`, `.bib` or figure file.

- **Every branch:** the PDF is attached to the workflow run as an artifact
  (Actions → pick the run → *biomimicry-report*).
- **`main` only:** the rebuilt `main.pdf` is committed back to the repository,
  so the current PDF is always readable directly on GitHub — no download
  needed. These commits are authored by `github-actions[bot]`.
- **`main` only:** the PDF is also published to a rolling pre-release tagged
  `latest-pdf`, so there is always one stable download link for the team:
  [latest-pdf](../../releases/tag/latest-pdf).

The build is byte-reproducible (`SOURCE_DATE_EPOCH` is pinned), so identical
sources produce an identical PDF and the commit-back step stays quiet unless
the document really changed. To reproduce a CI build locally:

```bash
SOURCE_DATE_EPOCH=1735689600 FORCE_SOURCE_DATE=1 latexmk -pdf main.tex
```

If you do not want the bot commits, delete the *Commit rebuilt PDF back to the
repository* step from the workflow and add `main.pdf` to `.gitignore`.

A red cross on a commit means the LaTeX did not compile — open the run log,
the `-file-line-error` flag points at the exact file and line.

## Conventions for the team

- `\todo{...}` marks everything still open; it renders in red. **The document
  must contain no `\todo` at hand-in** — search for it before submitting.
- One `\input` file per section so several people can edit in parallel
  without merge conflicts.
- Put every source in `references.bib` and cite with `\parencite{key}`.
  AI output is not a source for factual claims.
- Guideline length: 15–25 pages excluding references and appendices.

## Grading (for orientation)

The report is 70 % of the course grade. Weights: scoping and functional
analysis 15 %, biological discovery and abstraction 20 %, engineering concept
development 25 %, engineering validation and iteration 15 %, sustainability
10 %, scientific quality and critical AI use 10 %, report quality 5 %.
