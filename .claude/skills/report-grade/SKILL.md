---
name: report-grade
description: Grade the biomimicry report against the official ZHAW rubric from Report_template_26_V3_final.docx — 1-4 points per criterion with file:line evidence, weighted score, Swiss grade, and a priority list of fixes ranked by grade impact. Use when the user asks to grade, assess, mark, review or sanity-check the report or one of its sections, asks what grade it would get, what is still missing, or whether it is ready for hand-in ("bewerte den Report", "welche Note", "Rubrik", "was fehlt noch", "abgabebereit?", "grade section 3").
---

# Report grading against the course rubric

Grade the LaTeX report against the rubric the instructors actually use.

All paths below are relative to the **project root** --- the directory that holds
`main.tex`. Depending on where the session was started that is either the current
directory or `Report_LaTeX/`; resolve it once with `ls main.tex || ls Report_LaTeX/main.tex`
and keep every path and every `file:line` pointer relative to it. Be the strict
external examiner, not the supportive teammate: the value of this skill is an honest
number the team can act on. An inflated grade is a failure of the skill.

## Arguments

- no argument → grade the whole report
- a section number, file or criterion (`3`, `02_scoping`, `Kriterium 6`) → grade only
  that, but still show how it moves the overall score
- `formal` → run only the hand-in checks in step 2

## Step 1 — read the rubric and the report

1. Read `rubric.md`, next to this `SKILL.md` in the skill's own directory. It holds the
   seven criteria with all four level descriptors, the weights, the score→grade table and
   the template's per-section content checklist. Never grade from memory.
2. Read the sources in scope under `sections/`. Grade the **LaTeX source**,
   not the built PDF, so you can quote `file:line`.

## Step 2 — formal checks (mechanical, run these first)

```bash
# from the project root (the directory holding main.tex)
grep -rn '\\todo{' sections/ | wc -l          # must be 0 at hand-in
grep -rn '\\todo{' sections/                  # where the holes are
grep -rho '\\parencite\[[^]]*\]{[^}]*}\|\\parencite{[^}]*}' sections/ \
  | grep -o '{[^}]*}$' | tr -d '{}' | tr ',' '\n' | sort -u   # cited keys
grep -c '^@' references.bib                   # entries in the bib
latexmk -pdf -interaction=nonstopmode main.tex >/dev/null 2>&1
grep -ao '([0-9]* pages' main.log | tail -1     # page count (-a: the log is binary)
```

Report: `\todo` count and locations, page count against the 15–25 guideline, number of
**cited** keys (uncited bib entries do not count towards the ~20 guideline), bib entries
never cited, citation-style consistency, whether the template headings are unchanged, and
whether Appendix A (AI use) is filled in. These feed criteria 6 and 7 and are the cheapest
points on the table.

## Step 3 — score each criterion

For each of the seven criteria:

1. Quote the **evidence** — two or three `sections/file.tex:line` pointers to the text
   that earns the score. A criterion with no pointer cannot be scored above 2.
2. Pick the level descriptor that the text actually matches, and name the descriptor
   clause that fails if it is not the top one.
3. State the **gap to the next level** as one concrete, doable action.

Rules that keep the number honest:

- A `\todo{}` is missing content, not planned content. Score the text as it stands.
- A promise ("will be validated in 3.2") earns nothing until the content exists.
- Section 2 carries criterion 1 only. Criteria 2–4 live in Section 3; if Section 3 is a
  scaffold, criteria 2–4 are 1 point, and say so plainly — that is the real state, and it
  is what makes the priority list below useful.
- The rubric's headline applies: a visually attractive idea is not enough. Sketches
  without components, flows, materials and parameters cap criterion 3 at 2.
- Quantitative checks must show formula, assumptions, units, result and consequence.
  A number without its assumptions caps criterion 4 at 2.
- "Sustainable" or "resource efficient" without evidence is a criterion-5 deduction, not
  a plus.

## Step 4 — compute and convert

Weighted score = Σ (points × weight): 0.15, 0.20, 0.25, 0.15, 0.10, 0.10, 0.05. Show the
arithmetic. Round to the nearest 0.25 (exact tie → down) and read the Swiss grade off the
table in `rubric.md`. Give the unrounded score too, so the team sees how close the next
step is.

When the report is still work in progress, give **two** numbers: the grade as it stands
today, and the grade reachable if every open `\todo` in scope is completed at the level
the finished sections already demonstrate. Label them clearly; never report the second
one alone.

## Step 5 — priority list

Rank the open actions by **grade impact = weight × points gainable**, highest first, and
give the arithmetic for the top three (e.g. "criterion 3 from 1 → 3 = +0.50 weighted =
one half grade step"). Effort is the tiebreaker: at equal impact, the cheaper action goes
first. Cap the list at seven actions — a list nobody can finish is not a plan.

## Output

Answer in the language the user used (German unless they switch), but quote report text
in its original English.

```
## Bewertung — <scope>, Stand <date>

| # | Kriterium | Gew. | Punkte | Beleg | Lücke zur nächsten Stufe |
|---|-----------|------|--------|-------|--------------------------|

**Gewichteter Score:** <sum> → gerundet <x.xx> → **Note <n.n>** (<interpretation>)
**Potenzial nach Abarbeitung aller \todo:** Score <y.yy> → Note <m.m>

### Formale Checks
<todo count, pages, citations, headings, Appendix A>

### Prioritäten (nach Notenwirkung)
1. ... (+0.xx gewichtet)
```

Then, in two or three sentences of prose: the single biggest risk to the grade, and the
one thing to do next. No pep talk.

## What this skill does not do

It grades; it does not rewrite. If the user wants the findings fixed, ask which ones and
edit in a separate step — a grade produced by the same pass that wrote the text is worth
nothing.
