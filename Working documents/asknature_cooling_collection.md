# AskNature collection *"Cooling Down in the Heat"* — biological models

Source: <https://asknature.org/collection/cooling-down-in-the-heat/>, reviewed 01.09.2026.
Companion document: `asknature_innovation_options.md` (technical implementations).

## Sourcing caveat

AskNature returns **HTTP 403 to automated access**, so this was assembled through search
rather than by opening the collection page. **Nine items surfaced; the collection may hold
more.** Descriptions come from search summaries plus the primary literature behind them.
Open each entry before citing it — AskNature is the discovery tool, the paper is the
evidence.

## Why this collection is worth more than the Innovations catalogue

The innovations catalogue gave us prior art. **This collection gives us models** — organism,
mechanism, conditions — which is exactly what the Section 3.1 model table and the
selection/de-selection column need. Several of these are better fits for our functions than
what we currently have in that table.

One caveat runs through all of them, and stating it is worth marks under criterion 2:
**most cooling biology is metabolic or behavioural.** A bee fans, a jackrabbit dilates blood
vessels, an elephant redirects blood. A façade has neither metabolism nor behaviour, so the
transfer must be to a *passive* analogue or it is not a transfer at all. The two entries that
escape this problem entirely — the desert snail's shell and the cactus's ribs — are therefore
the most directly transferable, and it is not an accident that both are **structures rather
than processes**.

---

## The collection, mapped to our functions

| Model | Mechanism | Our function | Verdict |
|---|---|---|---|
| [Honeybee varying response thresholds](https://asknature.org/strategy/varying-response-thresholds-aid-hive-thermoregulation/) | individuals differ in the temperature at which they start fanning | **F9** | **The most important find. Resolves our open question about F9.** |
| [Desert snail shell](https://asknature.org/strategy/shell-protects-from-heat/) | 90–95 % reflectance + an insulating air space behind it | **F1, F4, F11** | **Add to the model table.** Passive, non-metabolic, and it beats our KPI 2 target. |
| [Sea star thermal buffering](https://asknature.org/strategy/body-buffers-thermal-variations/) | takes up cold water at high tide, cued by the previous hot low tide | **F4, F7, F9** | **Add.** The charge/discharge logic of our whole night window. |
| [Jackrabbit ear vasodilation](https://asknature.org/strategy/how-blood-flow-keeps-jackrabbits-cool/) | variable blood flow to a large radiating surface | **F2, F3, F9** | **Add.** The *water-free* route to F9. |
| [Elephant skin hot spots](https://asknature.org/strategy/skin-fine-tunes-internal-temperature/) | vasodilation in scattered patches, not the whole surface | **F9** | Pairs with the elephant-skin cracks we already cite (Martins 2018). |
| [Cactus ribs](https://asknature.org/strategy/shape-shades-and-enhances-heat-radiation/) | peaks shade troughs; cooled trough air absorbs heat and rises | **F5, F3, F2** | **Add.** Pure geometry — no material, no water, no maintenance. |
| [Honeybee hive water collection](https://asknature.org/strategy/water-collection-cools-hive/) | foragers collect water, distribute it, fan to evaporate | F6–F8 | Useful for the *distribution* logic; the fanning does not transfer. |
| [Prairie dog burrow ventilation](https://asknature.org/strategy/) | differing opening shapes create pressure-driven flow | F3 | Weak fit — our boundary is a surface, not a cavity. |
| Thomson's gazelle carotid rete · tenrec estivation | counter-current brain cooling · dormancy | — | **De-select.** Internal physiology and behaviour; nothing to transfer to an envelope. |

---

## 1 · Honeybee response thresholds — this answers our F9 question

**The mechanism.** Individual worker bees differ in the temperature at which they begin
fanning, and the variation is genetically determined — the colony has one mother but many
fathers, so a hive contains patrilines with different thresholds. The consequence: *"as the
hive gets hotter a few bees take up fanning duties; as the temperature continues to climb,
even more join"*. The diversity is reported to prevent excessive colony-level responses to
temperature fluctuations, and nurses have a lower threshold than dedicated fanners.

**Why this is the most valuable thing in the collection.** `auftrag_2.md` leaves open the
question: *is F9 satisfied by a threshold, or does it require a continuous response?* Our
worry was that a thermochromic coating gives a step — an enormous ∂P/∂T<sub>s</sub> at the
switching point and roughly zero either side.

The bees answer it: **each individual is a binary switch, and the population response is
proportional.** A graded response is assembled out of many all-or-nothing units by giving the
units **different thresholds**.

**The design consequence, stated as a transferable principle:**

> *Distribute a population of binary responders across a range of trigger points; the
> aggregate response then scales continuously with the load, with no controller and no
> proportional element anywhere in the system.*

Applied to Concept option A, this changes the concept: not one thermochromic formulation with
one switching temperature, but **a coating whose domains carry a distribution of switching
temperatures** — so that at 30 °C a fraction has switched, at 40 °C more, at 50 °C nearly all.
The same logic applies to a valve-type or wicking-type design: many small pores with
different opening points beat one large pore with one.

This is also the **"lots of littles"** pattern the Genius of Biome names on p. 59 — many
small, seemingly weak elements combining into a powerful process — so the two documents
agree, from different directions.

**What to check:** the primary literature on threshold distributions in *Apis mellifera*
fanning behaviour, and whether a material analogue is manufacturable — can a formulation
carry a deliberate *spread* of switching temperatures, or does chemistry force a sharp one?
That is a good critical engineering question.

## 2 · Desert snail — a passive envelope that already beats our KPI 2

*Sphincterochila boissieri* survives desert exposure to about **50 °C**. Its shell is
reported at **95 % reflectance in the near infrared and 90 % in the visible**. During
aestivation the snail secretes a **calcified epiphragm** across the aperture and retracts
into the second whorl, leaving an **insulating air space** in the body whorl that buffers
both heat and water flux, keeping the living tissue below its lethal temperature.

**Why it belongs in our model table.**

- It is **not metabolic**. The shell is a passive mineral structure doing exactly what our
  envelope must do — which makes it more transferable than any of the vasodilation models.
- Its reflectance is **above our KPI 2 target of ≥ 0.80** and close to the ultra-white
  laboratory paints we cite via Li 2021 — but achieved with calcium carbonate, a locally
  abundant mineral. That is *be locally attuned* and *life-friendly chemistry* in one model.
- The **air space** is the part we would otherwise miss: reflectance alone is not the
  strategy, reflectance **plus a decoupling gap** is. Our build-up is a layered retrofit, so
  an insulating cavity is available to us in a way it is not available to a paint.
- The epiphragm is a **seasonal, reversible seal** — a second, independent instance of the
  "adapt to changing conditions" principle in the same organism.

**And there is already an innovation built on it:**
[Architecture for Hot Climates Inspired by Desert Snail and Saharan Silver Ant](https://asknature.org/innovation/architecture-for-hot-climates/)
— a domed housing concept whose form comes from the ant's back and the snail's shell, with
triangular prisms echoing the ant's hairs, tested in a solar simulation. Note that it
combines the snail with the **Saharan silver ant we already cite (Shi 2015)**. Three further
silver-ant innovations exist and are worth ten minutes each:
[cooling roof tiles (ant + desert scorpion)](https://asknature.org/innovation/cooling-roof-tiles-inspired-by-the-saharan-silver-ant-and-desert-scorpion/),
[rooftop heat reflector (ant + pangolin)](https://asknature.org/innovation/reflective-roof-tiles-inspired-by-saharan-ants-and-pangolins/) and
[temporary housing insulation (ant + nacre)](https://asknature.org/innovation/temporary-housing-insulation-inspired-by-saharan-silver-ants-and-nacre/).
Our silver-ant row currently has no technical interpretation; these are it.

## 3 · Sea star — the charge/discharge model for our night window

After a hot low tide, the sea star **takes up more cold water into its coelomic cavity during
the following high tide**, which lowers its body temperature through the next low tide. The
hot low tide is the *cue*; the cold high tide is the *opportunity*; the buffering happens one
half-cycle later.

**Why this maps onto our project almost line for line:**

| Sea star | Our system |
|---|---|
| hot low tide = the stress period | the load window, 11:00–18:00 |
| cold high tide = the charging opportunity | the night window, 00:00–06:00 |
| takes up cold water into the coelom | charges the store — water reserve, or cold mass |
| the previous stress sets how much it takes up | **the load itself sets the charge** = F9, on a daily cycle |

And the honest limitation, which is *also* ours: *"this strategy only works when the sea water
is colder than the air"* — researchers note ocean warming may break the mechanism. Our
equivalent is the **reset condition**: if the night no longer discharges the store, the
concept saturates over the five-day design case. The sea star fails in exactly the way our
concept can fail, which makes it a good model *and* a good honest caveat to cite in
Section 5.

**One thing it adds that we did not have:** F9 need not act instantaneously. A response that
is *cued by today's load and delivered tomorrow* is still load-coupled and still
controller-free.

## 4 · Jackrabbit and elephant — F9 without spending water

**Jackrabbit.** When air temperature is slightly below body temperature, vessels in the outer
ear **dilate**, sending more warm blood to a large, thin, well-vascularised surface, where
heat is lost to the air. At around **30 °C air temperature, the ears can shed all of the
animal's excess heat** — and the point of the mechanism is that it **conserves water** that
sweating or panting would cost.

**Elephant.** Vasodilation in **scattered patches** ("hot spots") over the body rather than
uniformly; barrel-bodied and unable to afford sweating, elephants also flood the ears with
blood and fan them.

**Why this matters to our concept.** Section 2 concluded that the *latent* path has the
steepest self-regulation gradient, and it does. But these two models show biology also
achieves F9 by **modulating transport to a radiating surface**, not by modulating a material
property — and it does so *specifically to avoid spending water*. That is directly relevant
to the redundancy question in `auftrag_2.md`: if our evaporative path runs dry on day three,
a variable-flow radiative path is the biological precedent for what should still be working.

**The transfer problem, stated honestly.** Vasodilation is active: a heart pumps and a nervous
system decides. Our passive analogues would be a **thermosiphon** (density-driven flow needing
no pump), a **wicking network whose transport rate rises with temperature**, or a **contact
area that grows as a bimetal or hygroscopic element deflects**. Whether any of these gives a
useful ∂P/∂T<sub>s</sub> is a calculation, not an assumption — and a good one for Section 3.2.

## 5 · Cactus ribs — the option with no material and no water

The corrugation does three things at once, all geometric:

1. **peaks shade the troughs**, reducing solar gain into them (F5);
2. the **shaded trough air is cooler**, so it can absorb more heat from the body than warmer
   air could (F3);
3. **warmed air rises out of the troughs to the peaks, where wind carries it away** — a
   passive, buoyancy-plus-wind chimney at millimetre scale (F3 again), while the folded
   surface also enlarges the area available for long-wave emission (F2).

**Why to take this seriously.** Every other option on our list costs something — a dye that
bleaches, a water reserve that empties, a coating that soils. A rib profile costs geometry
only. It needs no maintenance, cannot run out, has no chemistry to justify, and survives a
Swiss winter by construction. It is also compatible with everything else: ribs can carry a
reflective coating *and* a water path in the troughs.

The obvious conflict is the **townscape constraint**: a corrugated façade is a visible change
on a building that may be listed. That is a real constraint, not a fatal one — and worth
naming, because our Section 2 says townscape acceptability is hard.
[A passively-cooled shirt](https://asknature.org/innovation/passively-cooled-shirt-inspired-by-cactus/)
exists as the technical interpretation, using "unnoticeably small" ribs — which suggests the
feature size can be tuned below the threshold of visual disturbance.

## 6 · Honeybee hive water collection — the distribution half

Water foragers collect water, it is **distributed around the hive and into cells**, and
fanning plus regurgitation accelerates evaporation. The transferable half is the
**distribution**: the reserve is not stored in one place and evaporated from one surface, it
is spread thinly across many small sites before it is evaporated. Combined with the camel
bilayer from the innovations document — which slows evaporation with an insulating cover —
we now have two independent biological answers to F8, and they can be combined: *spread thin,
then cover*.

The fanning does not transfer: it costs metabolic energy, and our energy constraint is hard.

---

## What to do with this

1. **Four new rows for the model table** (`03_bioinspired_design.tex:38`): honeybee response
   thresholds (F9), desert snail (F1/F4), sea star (F4/F7/F9), cactus ribs (F5/F3/F2). All
   four have a mechanism, a source and a clear function — which is what the selected column
   needs.
2. **Two documented de-selections**, which the rubric rewards: gazelle carotid rete and tenrec
   estivation — internal physiology and behaviour, nothing an envelope can adopt. State the
   *criterion* (must be passive and must live in a surface), not just the verdict.
3. **The F9 question in `auftrag_2.md` now has an answer to test**: a distribution of
   thresholds turns binary switches into a proportional response. That upgrades Concept
   option A from "a switch, which may not satisfy F9" to "a population of switches, which
   does" — and it gives us a new critical engineering question about whether such a spread is
   manufacturable.
4. **The redundancy decision also has an answer to test**: the jackrabbit's water-free
   variable radiator is the biological precedent for the second removal path that keeps
   working when the water reserve is empty.
5. **The cactus belongs in the morphological matrix** as the geometry column across F5, F3
   and F2 — the one option that adds no material and no chemistry.

## Still to browse by hand

The collection page itself, for the items search did not surface; the keyword pages
[desert](https://asknature.org/keyword/desert/) and
[temperate](https://asknature.org/keyword/temperate/) — the second is our own biome and the
"local lens" the Discovering lecture asks for.
