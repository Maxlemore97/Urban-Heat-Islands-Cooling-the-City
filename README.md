# Blockweek Bionics 2026 — Challenge 1, Urban Heat Islands

Team project folder. The deliverable is the report in `Report_LaTeX/`; everything else
supports it.

**Design question.** *How might we let the heat that Zurich's existing buildings absorb
during a summer day drive its own removal, so that the hotter it gets, the more the building
cools itself?*

---

## Where things are

| Folder | What is in it |
|---|---|
| **`Report_LaTeX/`** | The report itself. A git repository — commit and push from inside it, not from here. Sections are one file each under `sections/`. CI rebuilds `main.pdf` on every push. |
| **`Working documents/`** | Everything we wrote: task notes, idea lists, the AskNature research, image prompts. This is where the thinking lives before it goes into the report. |
| **`Notes/`** | The course material distilled into readable notes, one file per lecture or document, with a source and a "what this is worth for our challenge" line. Start at `Notes/00_index.md`. |
| **`Course material/`** | The original downloads from Moodle — Day 1 to Day 3, the semester overview, and the report template. Untouched. |
| **`Referenz Material/`** | The City of Zurich source documents (Fachplanung Hitzeminderung, Merkblatt, Teilpläne). These are cited in `Report_LaTeX/references.bib`, so do not rename this folder. |
| **`Output/`** | Finished artefacts: the Discovering & Abstracting slide deck and the script that generates it. |

---

## Where to start

**If you are picking the project up:** read `Working documents/auftrag_2.md`. It carries the
current state — what we found, what it means, and the nine decisions still open — and points
at everything else.

**If you are writing a report section:** read the matching note in `Notes/` first. The
requirements per section are in `Notes/overview/04_report_requirements.md`, and the operating
manual for Sections 3.2 and 3.3 is `Notes/overview/01_process_summary.md`.

**If you want to know how the report is graded:** the rubric is machine-readable at
`Report_LaTeX/.claude/skills/report-grade/rubric.md`. From inside `Report_LaTeX/`, running
the `report-grade` skill scores the current draft against it with file and line evidence.

---

## Working documents, in the order they were written

| File | What it is |
|---|---|
| `auftrag_1.md` | Day 1 scoping notes, raw. The origin of Section 2. |
| `auftrag_2.md` | **The current working document.** Findings from Days 2–3, the concept options, and the open decisions. |
| `Cooling_the_City.md` | The team's four biological models, with mechanism, abstraction and image prompts. |
| `ideen.md` | Eight further models in the same format, city-focused, with image prompts. |
| `lifes_principles_options.md` | Life's Principles applied to our challenge, plus Concept options A and B written out in full. |
| `asknature_innovation_options.md` | AskNature *Innovations* — prior art and technical routes. Feeds Section 2.3 and the abstraction table. |
| `asknature_cooling_collection.md` | AskNature *Strategies* from the "Cooling Down in the Heat" collection — models for Section 3.1. |
| `image_prompts.md` | 29 image-generation prompts, self-contained. The per-organism ones are also embedded in the two documents above. |

---

## Conventions

- **The report is written in English.** The working documents are mixed; that is fine, but
  anything that will be pasted into the report should be drafted in English.
- **`\todo{}` marks anything open in the report.** The document must contain none at hand-in.
- **AI output is not evidence.** Anything AI-assisted needs a primary source before it enters
  the report, and the use belongs in Appendix A.
- **Generated images are illustrations, not measurements.** Caption them as schematic, and
  never produce anything that looks like a thermal-camera reading.

## Note on this folder

Reorganised on 02.09.2026. Nothing was deleted or renamed — files were only grouped into the
six folders above, and cross-references inside the documents were updated to match.

## Repository layout

The repository root is the project folder. Everything below it is versioned
except the course handouts and the generated animations, which are listed in
`.gitignore` with the reason.

| Path | What it holds |
|------|---------------|
| `Report_LaTeX/` | the report itself. `main.tex` is the root document; CI builds it and commits `main.pdf` back |
| `Notes/` | lecture notes per day, written up from the slides |
| `Working documents/` | scoping drafts, idea lists, image prompts |
| `Output/` | the transient wall model, its figures, and the presentation decks |
| `.claude/skills/report-audit/` | grades the report against the official rubric and the template's Structure & Content checklist |

Run the audit with `/report-audit` from the project root, or build its evidence
bundle directly:

```bash
python3 .claude/skills/report-audit/scripts/collect.py
```

Build the report locally:

```bash
cd Report_LaTeX && latexmk -pdf main.tex
```
