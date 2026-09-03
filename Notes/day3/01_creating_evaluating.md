# Creating & Evaluating — lecture notes

Source: `5 Creating_Evaluating.pptx`, 44 slides
(`Course material/Day 3 Creating  Evaluating/`).

This is the specification for Sections 3.2 and 3.3 — the 40 % of the grade we have not
started. Read the required-output list first; everything else explains how to produce it.

---

## The required output (slide 41)

Nine artefacts. This is stricter and more explicit than the process-summary deck.

| # | Artefact | Quantity demanded |
|---|---|---|
| 1 | Crazy 8s / ideation evidence | **8 initial ideas** |
| 2 | Morphological Matrix | **3–5 functions × 2–4 solution principles** |
| 3 | Concept generation | **at least 3 concept combinations** |
| 4 | Technical concept development | **select 2**, produce **annotated** concept sketches |
| 5 | Engineering Canvas | one **for each** of A and B |
| 6 | Critical engineering questions | **2–3** |
| 7 | Engineering checks | **1–2** |
| 8 | Evaluation | KPI comparison **+ Life's Principles** |
| 9 | Final Concept V2 | with what changed and why |

Note item 2: **3–5 functions**, not all of them. We have thirteen (F0–F12), so the matrix
requires a deliberate selection — and the lecture tells us exactly how to make it.

## Which functions become matrix rows (slide 22)

The single most useful slide in the deck, because it stops the matrix from becoming a
function dump.

| Verdict | Criterion | Their example |
|---|---|---|
| **YES** | different mechanisms fundamentally change the concept | "generate signal" |
| **YES** | different principles lead to different architectures | "direct / distribute signal" |
| **YES** | passive vs. sensor-based response creates real alternatives | "detect / respond to conditions" |
| **YES / MAYBE** | include if the choice materially affects the concept | "supply energy", "attach / integrate" |
| **USUALLY NO** | better treated as a requirement or an engineering check | "protect from rain / dirt" |
| **NO** | it is a KPI or a constraint, not a function | "minimize mass" |
| **NO** | it is the main function — too broad for a row | "increase detectability" |

> **Rule of thumb: choose 3–6 key sub-functions for which alternative principles would lead
> to meaningfully different concepts.**

**Applied to us**, that filter produces a defensible five-row matrix:

| Row | Our functions | Why it qualifies |
|---|---|---|
| Reduce heat input | F1, F5 | reflect vs. shade vs. structural colour are different concepts |
| Move heat away | F2, F3 | radiate to the sky vs. hand it to the air vs. transport it elsewhere |
| Store and buffer | F4 | mass vs. phase change vs. no storage at all |
| Handle water | F6–F8 | wick vs. reservoir vs. no water path |
| Couple response to load | **F9** | material switch vs. valve vs. movement — the core of our question |

And the ones to keep **out** of the matrix, with the lecture's own reasoning: F0 is the main
function; F10 keep clean and F11 resist degradation are requirements and engineering checks;
F12 attach is a maybe, worth a row only if the mounting really changes the architecture.

The lecture's own worked matrix (slide 16) is a passive-cooling one and overlaps ours almost
completely: *reduce heat input* → self-shading · reflective surface · insulating layer;
*transport heat* → flow channels · conductive network · convection; *release heat* →
evaporation · radiation · ventilation; *adapt* → open/close · change colour · change
geometry. If our matrix comes out looking like this, we have copied the lecture instead of
using our own abstractions — ours have to carry the models we actually found.

---

## How literal may the transfer be (slide 10)

Three levels, and the course states a preference:

| Level | Example given | Ours |
|---|---|---|
| **More literal** — a direct structural feature | shark riblets → engineered riblet surface | cactus ribs → a ribbed façade |
| **Functional / mechanistic** — the working mechanism | termite ventilation → pressure-driven network | stomata → a load-driven valve; snail → reflect + air gap |
| **Highly abstract** — an organisational principle | swarm behaviour → decentralised algorithm | bee thresholds → a distribution of trigger points |

> **Course rule: prefer functional / mechanistic transfer whenever possible — explain HOW
> the biological mechanism leads to the technical principle.**

Useful calibration for us: our strongest ideas sit at both ends. The bee-threshold principle
is highly abstract and needs the "how" spelled out carefully; the ribbed façade is close to
literal and needs to be justified by the mechanism (self-shading plus convection), not by the
resemblance.

## Combining several organisms is explicitly allowed (slide 11)

The lecture's example of a multi-organism concept **is our challenge**:

> "A building may mimic a form that allows the building to cool itself (termite mound),
> transfer heat (Dorcas gazelle), be a colour that reflects the sun's radiation (herring
> gull), utilise evaporative cooling (kangaroo), and incorporate a landscape structure to
> manage heat (forest structure)."

Two consequences for us:

1. Our plan to combine models — reflect like the snail, move heat like the jackrabbit, meter
   water like the camel, switch like the bees — is exactly what is being asked for, not a
   dilution of the method.
2. **We should revisit our de-selection of the Dorcas gazelle.** We dropped the carotid rete
   as "internal physiology, and a wall has neither". But a rete is a **counter-current heat
   exchanger between two fluid streams**, and the lecturer names it for precisely this
   challenge. If we build a passive liquid loop, counter-current arrangement is a real and
   transferable design question. The de-selection may be too quick — either strengthen the
   argument or move the gazelle back in.

---

## Concept, functional model, prototype (slide 28)

| | Concept | Functional model | Prototype |
|---|---|---|---|
| Main question | *What could work?* | *Does this principle work?* | *Does the integrated solution work?* |
| Form | sketch / architecture | simplified physical or digital test | integrated system |
| Detail | low–medium | focused | high |
| Purpose | explore alternatives | learn / test | verify / validate |

> Course focus: **a strong concept first.** A functional model belongs to a later course.

So we are not expected to build anything. We are expected to produce a concept that can be
questioned, calculated and compared — which is what the Engineering Canvas is for.

## What a concept sketch has to contain (slides 24–27)

> Concept sketch = **architecture + mechanism + components + flows + key parameters**

Annotate: ① inlet ② channels ③ the driving effect ④ outlet ⑤ heat path ⑥ materials ⑦ key
dimensions ⑧ expected performance — and **state what is inspired by biology and what is
conventional engineering**.

Their tips worth following: quick sketches are enough; label the biological inspiration in
the drawing itself ("passive airflow inspired by termite mound"); link every feature to the
function it serves; and use multiple views — sections, exploded views, or the biological
model and the concept side by side.

That last one matters for us: **biology on the left, concept on the right, in one figure**
is the format that makes the transfer visible at a glance.

---

## Critical questions: weak vs. strong (slide 33)

| Weak | Strong |
|---|---|
| Which material looks best? | Is passive airflow large enough to remove the required heat? |
| Is the idea innovative? | How large must the inlet / outlet area be? |
| Can AI improve it? | Will the pressure difference still work at building scale? |
| Is it sustainable? | |

The pattern: a strong question names a **quantity**, a **threshold** and a **scale**. Our
three current candidates pass that test, which is a good sign:

- Is the buoyancy in a passive loop enough to move the heat we need, over the height
  available in a five-storey block?
- At what wind speed must a self-deploying shade furl, and what furls it?
- Can a switching material be produced with a deliberate **spread** of switching
  temperatures, or does the chemistry force a single sharp one?

Documentation format demanded: **question → assumption → method → result → implication**, and
for calculations **formula · assumptions · units · result · meaning for the concept**.

## AI as a critical reviewer (slide 34)

Give the AI the concept sketch, the Engineering Canvas, the functions and KPIs, the
assumptions and the biological mechanism. The suggested prompt, verbatim:

> "Act as a critical engineering reviewer. Identify the three assumptions most likely to make
> this concept fail. Suggest simple calculations, tests or evidence that could check them.
> Flag weak biomimetic transfer. Do not redesign the concept for us."

And the rule that turns it into evidence: **for each AI comment, decide ACCEPT · REJECT ·
INVESTIGATE, and justify the decision.** That table is Section 3.3 content and Appendix A
content at the same time — and a documented REJECT is worth more than ten accepted comments,
because it shows judgement.

---

## Evaluation (slides 36–37)

The comparison table has **more rows than our KPIs**:

| Criterion | |
|---|---|
| KPI 1, 2, 3 … | our Section 2 performance criteria |
| **Feasibility** | |
| **Biomimetic transfer** | how well the concept actually carries the biology |
| **Evidence / uncertainty** | how well supported the ratings are |

> "(Qualitative) ratings need justification using calculations or reasoned estimates."

Our decision matrix in `03_bioinspired_design.tex` currently has only the KPI rows. The last
three belong in it — especially *evidence / uncertainty*, which is the one that stops a
confident-looking table from hiding guesswork.

**Required evidence of iteration (slide 37):**

> "Identify at least one important weakness or uncertainty in the earlier concept and show how
> the final concept responds to it."

One named weakness, one documented response. That is the minimum for V2, and it is a low bar
we can clear deliberately rather than accidentally.

---

## Typical failure modes the lecture warns about (slide 40)

1. **Too literal copying** instead of functional transfer — biological systems are
   multifunctional, so a clean technical equivalent is hard to find.
2. **Material and technology limits** — not everything can be implemented 1:1; spider silk is
   the standing example. The task becomes finding a substitute that carries the function.
3. **Problems of scale** — *"many effects, for example micro-scale ones such as the lotus
   effect or beetle structures, only work at certain scales. Upscaling → the function may
   break away."*
4. **Complexity and simplification** — reduce to the decisive principle without losing the
   benefit.

Number 3 is aimed straight at us. **Four of our models are micro-scale**: the *Cyphochilus*
white, the Morpho structural colour, the lichen roughness and the stomatal valve. A façade is
square metres. We have to say explicitly, for each of them, at which scale the effect lives
and whether it survives being made large — and for the lotus effect the honest answer is
partly known, because Lotusan is a commercial product that does exactly this scaling.

---

## Process reminders worth keeping (slides 2–3)

- Stay solution-neutral as long as possible. **Do not fall in love with your first solution.**
- Think in functions, not products: *"What must the system DO?"* rather than *"What should we
  build?"*
- Use the world cafés for feedback and **iterate**.
- Take biology papers for describing the mechanism — understand it fully **before** starting
  the creating phase.
- Work on the report template **in parallel**; describe the research path in detail.
- Use AI as a mentor, critically; do not just copy.
- **Tell a coherent story.** Show the reasoning, not only the final concept:
  *Challenge → Function → Biology → Abstraction → Concepts → Engineering checks → Evaluation
  → Iteration.*

One more rule of thumb, from slide 4: a functional diagram should carry **3–7 key
functions**, solution-neutral. Ours lists thirteen. They are not all at the same level — F0 is
the main function and F10–F12 are supporting — but it is worth grouping them visibly, for the
same reason the matrix takes only five rows.

## New sources the lecture cites (slide 44)

Three we do not have in `references.bib` and could use:

- **Nagel, Nagel, Stone & McAdams (2010)**, *Function-based, biologically inspired concept
  generation*, AI EDAM — the method behind exactly what we are doing in 3.2. The natural
  citation for the morphological approach.
- **MacKinnon et al. (2022)**, *Biomimicry as a Sustainable Design Methodology — Introducing
  the Biomimicry for Sustainability Framework* — cited by the lecturer as the critical
  sustainability perspective. Section 4 material.
- **BiomiMETRIC (2019)**, *A Quantitative Performance Tool for Biomimetic Design* — Life's
  Principles plus quantitative evaluation, which is precisely what our Section 4 has to do
  and currently does not.

Adding these three would also lift the citation count towards the guideline and broaden the
source mix, which criterion 6 rewards.
