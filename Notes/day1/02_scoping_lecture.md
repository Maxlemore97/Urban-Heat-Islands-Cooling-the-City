# Scoping lecture — the deck Section 2 is built on

Source: `2 Scoping V6.pptx` (Musiolik), 32 slides.

## What scoping is for (slides 3–4)

> "The goal of this step is **not to decide what you will make** but to understand **what
> your design needs to do, for whom, and in what context**."

Three first steps: **1.** consider context · **2.** take a systems view · **3.** state the
challenge as a question ("How might we…?").

Context, per the speaker notes, = **stakeholders, type of locations, system boundaries**.
And the warning that cuts both ways:

> "Without this context a design challenge is often too broad. On the other hand, be careful
> not to define the context too narrowly. **Applying too many constraints before beginning
> the design process can limit the number and variety of potential solutions.**"

## The systems view (slides 6–12)

```
SUPER SYSTEM      What larger system is the challenge embedded in?
SYSTEM OF INTEREST  What exactly do we want to improve or design?
PARALLEL SYSTEMS  Which systems operate alongside it and interact with it?
SUBSYSTEMS        Which components or functions are inside the system of interest?
      ↓
DRAW THE PROJECT BOUNDARY —  IN: what will the team actually design/analyse?
                             OUT: what belongs to the larger system but will
                                  deliberately not be solved?
```

> **"A systems view should make the project more focused — not larger."**
> "The hierarchy prevents tunnel vision. The boundary prevents scope explosion."

**Example 3 · Water-Harvesting Façade** (slide 12) is the worked example closest to our
project, and the one to compare our own system view against:

| | |
|---|---|
| Super system | Building / urban water system |
| System of interest | Façade water-harvesting system |
| Parallel systems | Roof rainwater collection · building drainage |
| Subsystems | Capture surface · transport channels · collector · storage interface |
| IN | capture + transport + collection + transfer to storage + basic façade integration |
| OUT | drinking-water treatment · municipal distribution · wastewater · complete building design |
| What it adds | the functional chain **capture → transport → collect → transfer**, and KPIs: water collected [L/m²/day], capture efficiency [%], transport losses [%], material use [kg/m²] |

Our F6–F8 chain is the same chain. If we ever need to justify the water path as legitimate
scope, this slide is the course's own precedent.

The closing sentence of the systems-view task (slide 10) is the one we must answer in the
report: **"The systems view changed our project scope because …"**

## The design question (slide 8)

| Too broad | Just right | Too narrow |
|---|---|---|
| How might we end hunger? | How might we connect institutional food surpluses to those in need? | How might we design an app to help food pantries get more donations? |
| How can we make cycling safer? | How might we make urban cyclists more visible to drivers at night? | How can we make better lights for cyclists? |

The failure modes named: too broad = "doesn't target a specific area of intervention"; too
narrow = "presupposes too many details about the solution and doesn't leave enough room for
innovation".

## Functions (slides 13–20, 25–26)

The polar bear example the lecture builds on — and which our Section 2 already reuses:

> One purpose of polar bear fur is to keep the bear warm. Stated technically, **the function
> of the fur is to insulate**. The fur is a *strategy* for insulation; the *characteristics*
> of the fur are what make it good insulation.

The rule for finding functions:

> "Rather than thinking about what you want to make, ask yourself **'What do I want my
> design to DO?'** Carefully choosing the verb that completes this question — **that verb is
> the function you are looking for in nature.**"
>
> "You wouldn't ask nature how to make a fan. Instead you might ask *'How does nature move
> air?'* or *'How does nature cool?'* It is often helpful to come up with a few variations
> of your How question."

Definitions from the quiz answers (slides 25–26), worth using verbatim in the report:

- **Function** — the purpose or activity of a characteristic, mechanism or process; what an
  adaptation does for an organism, or what a design does for its users.
- **Strategy** — a characteristic, mechanism or process; **"how" a function is
  accomplished**.
- **Context** — the conditions in which a strategy developed and is used. *"Strategies vary
  depending on the context. What works in one context might not work in another."*
- The most important question when starting: **"What function do I want to solve for, and in
  what conditions?"**

Slide 17 (sun leaf vs shade leaf, same function, different form by position on the tree) is
the same example the Genius of Biome develops at p. 92 — see
[`../day2/05_genius_of_biome.md`](../day2/05_genius_of_biome.md).

## KPIs (slides 21–23)

```
FUNCTION            KPI                                   TARGET / BENCHMARK
what must it DO?    what observable quantity tells us     how good should it be?
                    HOW WELL it does it?
reduce heat    →    cooling energy demand [kWh]      →    ≥ 30 % lower than reference
```

Why they exist: make goals measurable (replace "efficient", "lightweight", "quiet" with
quantities and units) · compare concepts on a common basis · guide what must be calculated,
tested or simulated.

> **Key rule: "Do not invent KPIs first. Derive them from the functions, interfaces and
> constraints revealed by the system view."**

The chain the lecture wants visible: *system view → boundary → interfaces → functions and
constraints → KPIs*. Student checkpoint: for every important function or interface, ask
**"What observable quantity would tell us whether this works?"**

The water-harvesting façade KPI set (slide 23) again overlaps ours, and includes one we
should not lose: **"Remain functional → performance after fouling / weathering"** — our
KPI 7.

## Required output and quality check (slides 28–29)

Required output of the afternoon task, which is the specification for our Section 2:

1. Context & constraints
2. System view figure — super-system · system of interest · parallel systems · subsystems ·
   **project boundary IN/OUT**
3. Function list / functional diagram
4. KPI table — **Function → KPI → Unit → Target**, **4–7 KPIs**
5. Final "How might we…?" question

Quality check (all six are already answered in our Section 2.7):

- [ ] Is our system of interest clearly defined?
- [ ] Is our project boundary manageable?
- [ ] Are our functions solution-neutral?
- [ ] Did the systems view reveal additional functions or constraints?
- [ ] Are our most important functions measurable with KPIs?
- [ ] Is our final "How might we…?" question open to different solutions?

> Goal for the next phase: "You should now know **WHAT** the solution must achieve — but not
> yet **HOW** it will achieve it."

**Note the count: the task says 4–7 KPIs and the rubric repeats it. We currently have 8.**

## Result of scoping: the design brief (slide 24)

Challenge / design question · context & constraints · system view + project boundary ·
functions / functional diagram · performance criteria / KPIs · **Life's Principles most
relevant to the specific type of design challenge**.
