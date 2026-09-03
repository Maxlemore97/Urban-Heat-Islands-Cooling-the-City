---
name: report-audit
description: Audit and grade the Biomimicry Challenge report against the official ZHAW rubric and the template's Structure & Content checklist. Fans out one subagent per rubric criterion plus a checklist auditor and a sources auditor, then returns a 1-4 score per criterion, the weighted score, the Swiss grade, every failed checklist item, and a fix list ranked by grade impact. Use when the user asks to check, audit, grade, mark or sanity-check the report, asks what grade it would get, what is still missing, whether every required element is present, or whether it is ready for hand-in ("bewerte den Report", "welche Note", "prüfe die Kriterien", "was fehlt noch", "abgabebereit?").
---

# Report audit — rubric score and compliance check

Two questions, answered separately and then combined:

1. **Compliance.** Is every element the template's *Structure & Content* section
   demands actually present? This is a checklist, not a judgement — each item is
   `PRESENT`, `PARTIAL` or `MISSING`, with a page or `file:line` as evidence.
2. **Quality.** How would the instructors score each of the seven rubric criteria,
   1–4? This is a judgement, and it is made by an independent subagent per criterion
   so that a weak section cannot be carried by a strong one.

Be the strict external examiner, not the supportive teammate. **An inflated grade is
a failure of this skill.** A criterion only earns 4 if the report would survive a
sceptical reader looking for the gap; when the evidence is thin, score 3 and say what
would move it.

## Reference files

| File | Use |
|------|-----|
| `rubric.md` | the seven weighted criteria, the Swiss-grade conversion, the formal requirements and the per-section content checklist |
| `structure-checklist.md` | the *Structure & Content* bullets broken into atomic, individually checkable items with IDs |
| `scripts/collect.py` | builds the evidence bundle the subagents read |

## Arguments

- no argument → full audit
- a section (`2`, `3.2`, `04_sustainability`) → audit only that, but still report how it
  moves the overall score
- `formal` → only the hand-in checks (length, headings, references, Appendix A)
- `checklist` → only the compliance pass, no grading

## Step 0 — build the evidence bundle

```bash
python3 .claude/skills/report-audit/scripts/collect.py
```

It writes `report-audit/` in the scratchpad: `report.txt` (the compiled PDF as text,
one `=== PAGE n ===` marker per page), `metrics.json` (body page count, headings,
figure and table counts, todo count, bibliography entries, cited keys, uncited keys)
and prints a summary. If the PDF is stale it rebuilds it first.

Read `metrics.json` yourself before fanning out — several formal findings come straight
from it and need no agent.

## Step 1 — fan out

Send **all of these in a single message** so they run concurrently. Give each the path
to `report.txt` and to the reference file it needs. Use `model: fable` — these are
bounded reading-and-judging tasks and the fleet is the point.

| # | Subagent | Brief |
|---|----------|-------|
| 1 | `criterion-1` | Challenge, Scoping & Functional Analysis (15 %) |
| 2 | `criterion-2` | Biological Discovery & Abstraction (20 %) |
| 3 | `criterion-3` | Engineering Concept Development (25 %) |
| 4 | `criterion-4` | Engineering Validation & Iteration (15 %) |
| 5 | `criterion-5` | Sustainability & Life's Principles (10 %) |
| 6 | `criterion-6` | Scientific Quality & Critical AI Use (10 %) |
| 7 | `criterion-7` | Communication & Report Quality (5 %) |
| 8 | `checklist` | every item in `structure-checklist.md`, PRESENT / PARTIAL / MISSING + evidence |
| 9 | `sources` | citation-style consistency, source variety and count, every claim that carries a number but no citation, AskNature entries used as evidence rather than as a lead |

Each criterion agent must return exactly:

- `score`: 1, 2, 3 or 4
- `verdict`: one sentence naming the descriptor it matched and why
- `evidence`: 2–4 page or `file:line` pointers
- `gap`: the single most valuable change that would raise the score by one point,
  phrased as an action
- `overclaim`: anything the report asserts that its own evidence does not support —
  empty if none

Tell every agent: **unwritten scaffolding scores low.** A `[TODO:]` marker, an empty
table cell or a heading with no content under it is a missing element, never a
placeholder to be credited. `metrics.json` reports the todo count per section; a
section that is mostly todos cannot score above 2.

## Step 2 — aggregate

Compute `Σ (score × weight)` with the weights in `rubric.md`, round to the nearest
0.25, **ties round down**, then convert to the Swiss grade. Report the unrounded score
alongside it so the team can see how close the next step is.

## Step 3 — report

In this order, and nothing else:

1. **Grade.** Weighted score, Swiss grade, and the one criterion costing the most
   points right now.
2. **Score table.** Criterion, weight, score, contribution, one-line verdict.
3. **Failed checklist items.** Only `MISSING` and `PARTIAL`, grouped by section, each
   with the evidence pointer. A long list here is the useful output — do not soften it.
4. **Fix list, ranked by grade impact.** For each: the action, the criterion it moves,
   and the points it is worth. Compute the impact — a 1-point gain on criterion 3
   (25 %) is worth five times the same gain on criterion 7 (5 %).
5. **Overclaims.** Anything the report asserts beyond its evidence, quoted. This
   section protects criterion 6 and is the one the team will least want to read.

Formal findings from `metrics.json` — page count against the 15–25 guideline, headings
that do not match the template verbatim, reference count, uncited bibliography entries,
missing Appendix A rows — go into the fix list with the criterion they belong to
(length and headings are criterion 7, sources and AI statement are criterion 6).

## What not to do

- Do not grade a section you have not read in `report.txt`. No inference from filenames.
- Do not average away a weak criterion. Report it and let the weighting do its work.
- Do not credit intent. "This will be filled in" is `MISSING`.
- Do not rewrite the report in this skill. The output is a diagnosis; the team decides
  what to act on.
