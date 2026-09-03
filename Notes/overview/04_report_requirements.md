# Report requirements — structure, style, formal rules

Sources: `Template Challenge Report .docx` (the template our LaTeX mirrors),
`How to write a report.pdf` (ZHAW SoE BION-EN workbook) and
`The Dos and Donts of Academic Writing.pdf`.

The **grading rubric** from the template is machine-readable in the repo at
`../../Report_LaTeX/.claude/skills/report-grade/rubric.md`; run the `report-grade` skill rather
than re-reading it.

## Template rules (the ones that are checkable)

- All chapters must be addressed; emphasis may differ by challenge.
- **15–25 pages** excluding references and appendices; no fixed length.
- **Use the headings from this template** — do not rename sections.
- Refer to all sources including AI tools. **AI output is not evidence.**
- Appendix A: AI use statement — tool / used for / how it influenced the project / how the
  output was verified.

## A discrepancy worth knowing about

| Source | Reference count |
|---|---|
| `Template Challenge Report .docx` | "**approximately 20** references… source quality and relevance matter more than a fixed number" |
| `How to write a report.pdf`, §2.2 | "include **at least 15** references from a variety of sources (journals, asknature.org, online sources)" |

15 is the floor, 20 the guideline. We currently cite 19 of 22 bib entries — above the floor,
just under the guideline, and **with no AskNature entry cited at all**, which both documents
name explicitly as an expected source type.

## Academic style — the rules we are marked against

From the Dos and Don'ts table:

| Avoid | Use instead |
|---|---|
| long nested sentences | short sentences, **one thought each**, first-degree subordinate clauses at most |
| synonyms for technical terms | **consistent, repeated use of technical terms**; define them |
| contractions, colloquialisms, phrasal verbs | formal single-word verbs (*examine*, not *look at*) |
| vague expressions ("very big", "really important") | precise, concise language |
| extensive "we"; judgements ("luckily", "surprisingly") | impersonal constructions ("This report focuses on…"); **well-founded** judgements, confined to the discussion |
| unproven certainties | **cautious language**: seem, appear, indicate, suggest, possibly, could, might |
| truisms, repetitions, fillers, long-winded explanations | only relevant facts, high information density |
| "chapter" for part of a paper | **"section"** |

Number formatting: **34,000** (not 34'000) · **1.7 km** (not 1,7 km) · **83 %, 16 cm**.

Note the tension between "avoid extensive *we*" and the rubric's demand for a visible
reasoning chain and an honest account of team decisions. The resolution the guide itself
offers: impersonal for method and results, first person allowed sparingly where the *team's
decision* is the subject.

## Figures and tables

- **Table title goes above the table; figure title goes below the figure.** *(Our LaTeX
  already does this — `\caption` before the tabular, after the tikzpicture.)*
- Number them consecutively; include a legend for symbols and colours.
- **Never let a table or figure substitute for the discussion.** Every one must be referred
  to and interpreted in the running text: *"As can be seen in Table 2…"*
- Four stages for describing a figure: introduce the topic → explain what it shows →
  highlight what is of particular interest → comment on it.

This is a real risk in our report: Section 2 is table-heavy and several tables are not yet
discussed in the text.

## Report structure per the writing guide (§2.2)

Title page (specific title, authors, submission date, course, department, university,
lecturers) · table of contents · introduction (background, purpose, aim and scope) ·
methods · results · discussion · conclusion · references.

Our template's structure differs — it is the biomimicry-specific one — but the **title page
requirements** are worth checking against ours, which is still missing names, the submission
date and the contribution table.

## Useful phrase sources

Manchester Academic Phrasebank (`phrasebank.manchester.ac.uk`) is recommended twice, with
per-section phrases. Also `uefap.com/writing/writfram.htm`, Purdue OWL, and
`oxfordlearnersdictionaries.com/wordlist/english/academic/`.
