# Report-Audit vom 17.09.2026

Geprüft: `Urban Heat Island - Cooling the City - Report (1).docx` (Stand 17.09.2026, 19:54)
gegen die ZHAW-Rubrik in `Scoring.pages` (identisch mit `.claude/skills/report-audit/rubric.md`).

Zeilenangaben (Lxxx) beziehen sich auf `report_audit_2026-09-17_textdump.txt` im selben
Ordner, dem zeilennummerierten Textexport des Reports. Im Word-Dokument entsprechen sie
den genannten Abschnitten; die Zitate sind wörtlich und lassen sich per Suche finden.

Elf unabhängige Prüfdurchläufe: sieben Rubrik-Kriterien, Struktur-Checkliste, Quellen,
KI-Stil, Redundanz/Leersätze. Rechnungen in 3.2.7, 3.2.8 und 3.3.5 wurden von zwei
Prüfern nachgerechnet und sind korrekt.

---

## 1. Note

| Kriterium | Gewicht | Punkte | Beitrag | Urteil |
|---|---|---|---|---|
| 1 Challenge, Scoping & Functional Analysis | 15 % | **2** | 0.30 | Kontext und Constraints stark, aber Design Question zu breit und widerspricht der Systemgrenze; Funktionsdiagramm ist eine Textliste; KPIs ohne Einheiten-Logik, Baseline und Ziele |
| 2 Biological Discovery & Abstraction | 20 % | **3** | 0.60 | Neun Modelle sauber in Beobachtung/Abstraktion/Prinzip getrennt; aber kein Vergleich, keine benannten abgewählten Modelle, Hälfte der Mechanismen nur via AskNature belegt |
| 3 Engineering Concept Development | 25 % | **3** | 0.75 | Konzept A gut entwickelt; Konzept B bleibt ein Absatz ohne Parameter, Materialien, Zahl |
| 4 Engineering Validation & Iteration | 15 % | **3** | 0.45 | Zwei reproduzierbare Rechnungen, die V2 wirklich verändern; aber Q3 nie geprüft, Auswahl A/B nicht evidenzbasiert, V2 scheitert am eigenen Hydraulik-Check (Faktor 67) und bleibt "a layout to revise" |
| 5 Sustainability & Life's Principles | 10 % | **3** | 0.30 | Prinzipien kritisch angewendet, Trade-offs konkret; aber innere Widersprüche, tote Verweise ([27], [28], Table 4.1), "Design geändert" nur zur Hälfte durch Sektion 3 gedeckt |
| 6 Scientific Quality & Critical AI Use | 10 % | **2** | 0.20 | Quellenliste gut (12 Papers), aber Zitierapparat gebrochen und Appendix A unfertig (eine Zeile, vier leere) |
| 7 Communication & Report Quality | 5 % | **2** | 0.10 | Doppelte Abbildungsnummern, tote Verweise, zwei Zitierstile, leere Anhänge, Glossar-Kapitel ausserhalb der Vorlage |

**Gewichtete Punktzahl: 2.70 → gerundet 2.75 → Note 5.0.**

Nächste Stufe (5.5) braucht 3.25. Realistischer Weg: Kriterien 6 und 7 auf 3 (rein
formale Arbeit, +0.15), Kriterium 1 auf 3 (KPI-Tabelle neu, +0.15), dazu Kriterium 3
auf 4 (Konzept B ausbauen, +0.25) = 3.25. Ohne Konzept B: 3.00, bleibt 5.0.

---

## 2. Fix-Liste nach Notenwirkung

### A. Formal, billig, sofort (Kriterien 6 und 7, zusammen +0.15)

1. **Abbildungen durchnummerieren.** Figure 3.2, 3.3, 3.4 sind je doppelt bzw. dreifach
   vergeben (L298/L480, L344/L490, L362/L380/L598). Figures 3.5–3.8 zählen so, als gäbe es
   nur vier davor. L282 verweist auf "Figure 1". Figure 3.6 wird nie im Text referenziert.
2. **Tabellen.** Sektion 3 beginnt mit Table 3.4, Tabellen 3.1–3.3 existieren nicht. L454
   und L917 verweisen auf "Table 3.2" (gemeint: 3.4). L818 verweist auf "Table 4.1", die es
   nicht gibt. Tables 2.5, 3.8, 3.9 werden nie per Nummer referenziert.
3. **Referenzen [27] und [28]** (ECHA REACH, EuGH-Urteil) werden in 4.3 zitiert, die Liste
   endet bei [24]. Die RIS-Datei `Section 4 - Zotero-Import.ris` liegt dafür bereit.
   [25], [26] fehlen ebenfalls (Braungart/McDonough, Vorlesungsfolien Cradle to Cradle).
4. **Zitierstil vereinheitlichen.** Sieben Autor-Jahr-Zitate mitten im IEEE-System:
   (Stadt Zürich, 2020) L31/L54/L598, (Schmidt-Nielsen et al., 1956) L472, (Project team,
   2026) L524, (Harvey, 1998) L535, Raman et al. (2014) L568, Baechler et al. (2007) L708,
   (University of Notre Dame, 2021) L928. Harvey, Schmidt-Nielsen, Notre Dame haben keinen
   Eintrag. Drei davon tragen noch gelbe Markierung (L31, L54, L928).
5. **Zotero-Sprache auf Englisch.** Die Literaturliste ist deutsch formatiert ("und",
   "Bd.", "S.", "Zugegriffen", "Verfügbar unter", «…»), der Report ist englisch. Im Text
   "[19, S. 148–151]" neben "p. 128".
6. **Eintrag [19]** (Fachplanung Hitzeminderung) hat weder Autor, Jahr noch URL.
   **[22]** (Silberameise, Science) ohne Autoren, Jahr, Band. **[3]** ohne Jahr.
7. **Falsches Ziel:** L482 zitiert die Jackrabbit-Durchblutung mit [16], das ist das
   Kaktus-Paper. Richtig: [5]. Umgekehrt sollte [16] bei den Kaktusrippen (L310) stehen.
8. **Appendix A fertigstellen.** Nur eine Zeile (AskNature), vier leere Zeilen (L919–923).
   Der KI-Reviewer hinter Table 3.11 ist nirgends benannt. Text verweist auf "functions
   F1–F12" (es gibt F1–F5), "Table 3.2" (existiert nicht) und eine "23 %"-Zahl, die im
   Report nirgends vorkommt. Appendix A gibt zu, dass die sieben AskNature-Seiten nicht
   geöffnet wurden; genau diese tragen aber die Mechanismus-Aussagen in 3.1.
9. **Anhänge.** "Appendix B – Decision Log" ist eine leere Überschrift und benennt die
   Vorlage um; "Optional Supporting Material" ist nach Appendix C gerutscht und enthält
   nur "belong here". Extra-Kapitel "Glossary" zwischen References und Appendix A ist nicht
   in der Vorlage; "UHII" wird definiert, nie benutzt.
10. **Unterkapitel 3.2.2–3.3.6** sind fette Absätze statt Überschriften; 3.2.1 und 3.2.3
    fehlen in der Zählung.
11. **Sprachfehler** (Auswahl): L23 "negative feedback loop" (gemeint ist eine
    selbstverstärkende, also positive Rückkopplung), "air condition"; L31 "has an adopted",
    "thematics maps"; L45 "where chosen"; L150 "not formulated too narrow but also not to
    wide", "an too open"; L370 "I needs to be mentioned"; L384 "insolation" statt
    insulation; L742 "seasonal adaptions rather functions", "a remain risk"; L810 "which are
    be resource efficient written as constraints"; L812 "unacceptable. (Table 3.11), and
    Therefore … a separable external panels"; L828 "a unconventional".

### B. Kriterium 1 auf 3 (+0.15): KPI-Tabelle und Funktionsdiagramm

- **Table 2.5 neu schreiben.** KPI 3 "Heat dissipated / °C" und KPI 4 "Heat transferred /
  °C" messen Wärme in Grad und sind fast Duplikate. KPI 6 "efficiency factor" ist
  undefiniert. Keine Baseline, keine Zielwerte, keine Messbedingung. Sektion 3.3 muss die
  KPIs deshalb in kW umdeuten (L604) und gibt zu: "Existing KPI definitions are
  incomplete" (L637). Vorschlag: Einheit W/m² oder K Oberflächentemperatur-Reduktion,
  L/(m²·d), % Reflexion, % Leistung nach N Zyklen; Baseline für den Referenzblock;
  Zielwert aus der Fachplanung.
- **Funktionsdiagramm zeichnen.** Es gibt in Sektion 2 kein einziges Bild. L174–184 ist
  eine Liste mit zwei Pfeilketten, ohne Systemgrenze, ohne Energie-/Material-/
  Informationsflüsse.
- **Design Question.** L148 "reduce the urban heat island effect, in cities like Zurich"
  nennt keinen Eingriffspunkt, obwohl die Systemgrenze Fassade + Dach ist (L87). Kandidat 1
  wurde genau dafür abgelehnt (L135), der gut geformte Kandidat 3 als "zu eng". L150
  behauptet das Gegenteil.
- **Overclaims in 1–2:** L29 "makes … the KPI targets checkable" (es gibt keine Targets);
  L31 "documented baseline and published target values" (keine genannt); L33 "selected from
  measured data" (keine Daten gezeigt).

### C. Kriterium 3 auf 4 (+0.25): Konzept B ausbauen

- B ist ein Absatz (L484–490) plus ein unbeschriftetes Grenzschicht-Bild. Keine Schicht-
  aufbau-Zeichnung, keine Texturhöhe/-abstand, keine Beschichtungsdicke, kein Binder-
  oder Partikelmaterial, keine Abschätzung des Konvektionsgewinns. Table 3.10 sagt für B
  durchgehend "Not quantified"; die Auswahl von A ist deshalb qualitativ (L644).
- Widerspruch Text/Zeichnung: L478, L631, L648 sagen, V1 hatte die Rohre in der Wand
  eingebettet, die V1-Zeichnung (Figure "3.2") zeigt sie bereits aussen ("Uninsulated
  absorber"). Damit ist die dokumentierte V1→V2-Änderung durch die Skizze nicht gedeckt.

### D. Kriterium 4 auf 4 (+0.15): V2 muss den eigenen Check bestehen

- L700–702: vier Dachschlangen à 1'150 m ergeben 20 kPa Verlust gegen 0.30 kPa Auftrieb.
  Schluss: "must change", "remain a layout to revise". V2 (Fig. 3.5/3.6) ist damit in einer
  Form dokumentiert, von der der Report selbst sagt, dass sie nicht funktioniert.
  Fix: N kurze Parallelkreise mit Sammlern so dimensionieren, dass Σ Δp ≤ ~300 Pa bei
  44 kW / 10 K, D/N/Länge in Table 3.12, Fig. 3.5/3.6 neu zeichnen.
- Q3 (Spray) hat null Evidenz. Mindestens eine Zahl (h glatt vs. gerippt aus [6]/[21]).
- Overclaims: L740 "roof releases most of its heat to the night sky (Section 3.2.8)", aber
  3.2.8 rechnet nur den Tagfall (G = 800 W/m²). L734 "circulation is driven by buoyancy
  alone" als Fakt, während der einzige Loop-Check um Faktor 67 scheitert. L564/L736 "use
  most of the available buoyancy" ist per Konstruktion (Reibung = Auftrieb gesetzt) "alles".

### E. Kriterium 2 auf 4 (+0.20): Vergleichstabelle und Primärquellen

- Die fehlende "Table 3.2" (Kandidatenliste inkl. vier abgewählter Modelle), auf die
  Appendix A und L454 bereits verweisen, einfügen: Modell, Funktion F1–F5, Life's
  Principle, Evidenzqualität, Grund für Behalten/Verwerfen.
- Primärquellen in 3.1 zitieren statt AskNature: [22] Shi et al. 2015 für die Ameise
  (L326), [16] Lewis & Nobel für den Kaktus (L310), Schmidt-Nielsen für Kamel/Schnecke.
- Fachliche Overclaims: L326 stapelt "2 °C" und "5–10 °C" als zwei Effekte, bei Shi et al.
  ist 5–10 °C der Gesamteffekt; L412 Schwellenwert-Diversität der Bienen stammt von Jones
  et al. 2004, nicht von [14] Peters et al.; L310 "Air within the shaded troughs … rises"
  ist ein Kamineffekt ohne Beleg; L378 "fur blocks the hot air" ist eine lose Paraphrase.
- Vier von neun Modellen ohne Abbildung (Kaktus, Ameise, Zapfen, Biene); Figures 3.1/3.2
  ohne Bildquelle.

### F. Kriterium 5 auf 4 (+0.10): Sektion 4 konsistent machen

- **Widerspruch (aus meinem 4.2-Text):** L762 "Nothing emitted in operation. No water, no
  refrigerant, no additive and no noise leave the system" gegen L794 (Beschichtung wird in
  den Regenabfluss abgerieben) und L798 (Inhibitor kann austreten). Streichen oder auf
  "im Normalbetrieb, abgesehen von Abrieb" einschränken.
- L746 "not through a functional additive" gegen L802 (Reflexion kommt vom TiO₂-Pigment).
- L758 "cannot raise heat stress" – [15] untersuchte Wand-Albedo, nicht Dächer neben
  höheren Nachbarn. "cannot" → "does not, as far as [15] shows".
- L800 "eight cycle design principles" ohne Quelle, "answers three" und dann vier genannt.
- L806–814: Von vier "sustainability changed the design"-Fällen sind nur 1 und 2 in
  Sektion 3 belegt; Fall 3 war laut L631 ein Engineering-Review-Entscheid, Fall 4 hat in
  L708 keine Chemie-Begründung.
- L17, L25: "sustainable" als unbelegtes Adjektiv in Sektion 1–2 (Checkliste verbietet das).

---

## 3. Checkliste: PARTIAL-Punkte (kein Punkt MISSING)

| ID | Was fehlt |
|---|---|
| H8 / X2 | Appendix B umbenannt und leer; Glossar ausserhalb der Vorlage; 3.2.x/3.3.x keine Überschriften |
| S7 | Funktionsdiagramm ist Text, keine Material-/Informationsflüsse |
| D2 | Abgewählte Modelle nicht benannt, keine Begründung |
| C4 | Konzeptzeichnungen ohne technische Parameter und Materialangaben |
| E2 | Table 3.10 ohne Bewertungen; B-Spalte "Not quantified"; L624 verzichtet explizit auf eine gewichtete Entscheidung |
| F3 | Zwei Zitierstile gemischt |
| A1 | AI Use Statement: eine Zeile, vier leere, tote Verweise, KI-Reviewer nicht dokumentiert |
| A2 | Appendix B/C leer bzw. Platzhalter |
| X4 | [27], [28] und fünf Autor-Jahr-Zitate ohne Eintrag; [19] unvollständig; Bilder 3.1/3.2 ohne Quelle |

---

## 4. KI-Scan: Was nach KI klingt

**Rangfolge der Sektionen, von am stärksten KI-klingend zu am wenigsten:**

1. **Sektion 4** – 30 fette Einleitungsphrasen in Folge, jede als komprimierte Antithese
   ("Heat exported, not moved", "Used, not consumed", "met by exclusion, not by
   verification"), Schluss auf einem Aphorismus (L786). Das ist die Sektion, die ein
   Dozent markiert. Mein 4.2-Text von heute gehört dazu.
2. **Sektion 3.3** – perfekt gesetzte Hedges ("requirements, not demonstrated
   circulation"), Stakkato "X remains a check", Doppelpunkt-Urteile ("factor of 67: the
   long-coil arrangement must change").
3. **Sektion 3.2** – gleiche Stimme, telegraphisch, null Fehler, "benefit is a hypothesis".
4. **Appendix A** – "marked as open items rather than left implicit".
5. **Sektion 5** – gemischt; ein Lehrsatz (L836), aber auch "we would probably have…".
6. **Sektion 2** – überwiegend menschlich (Tippfehler, "How might we end world hunger?").
7. **Sektion 3.1** – Mechanismus-Absätze mit Tippfehlern lesen sich als Studententext.
8. **Sektion 1** – etwas steif, sonst unauffällig.

**Die klassischen LLM-Wörter fehlen komplett** (crucially, notably, robust, leverage,
delve, nuanced, holistic, underscores, highlights: 0 Treffer). Was bleibt, ist
subtiler und trotzdem erkennbar:

| Tic | Anzahl | Beispiele |
|---|---|---|
| "X, not Y" / "rather than" / "instead of"-Umkehrungen | ~28, davon ~15 in Sektion 4 | L748 "met by exclusion, not by verification"; L796 "Used, not consumed"; L808 "for the people at street level, not for cooling performance"; L568 "a benchmark, not an assigned property" |
| Fette Einleitungsabsätze | 35, davon 30 in Sektion 4 | 6 in 4.1, 14 in 4.2, 6 in 4.3, 4 in 4.4 |
| Paradoxe Nominal-Überschriften | 8 | "A benefit without a number", "A balance with one side", "Additive or downtime", "Access or invisibility" |
| Dramatische Ein-Satz-Schlüsse | ~6 | L786; L590 letzter Satz; L604; L818 Schluss |
| Semikolon-Antithesen | ~12 | L482, L590, L658, L740, L756, L786, L798, L802 |
| Verblose Fragment-Öffner | 5 | L790 "Worn by UV…", L796 "Used, not consumed:", L798 "Used, but mobile" |
| Anaphorische "no…no…no"-Listen | 4 | L762 "No water, no refrigerant, no additive and no noise" |
| "remain(s)" als Satzende | 15 | L684 dreimal in fünf Sätzen |
| Meta-Kommentar zur eigenen Redlichkeit | 4 | L604 "Assumptions and untested quantities remain explicit"; L624; L818; L928 |

**Die 15 auffälligsten Stellen** (vollständige Liste mit ~50 Stellen beim KI-Prüfer,
hier die wichtigsten):

- L29 "Fixing one reference city is what makes the constraints and the KPI targets checkable."
- L31/L33 "instead of invented ones" / "instead of intuition" (zwei Zeilen, gleiches Muster)
- L135 "Too broad. No place, no time, no intervention point."
- L520 drei parallele rhetorische Fragen plus Meta-Satz "These questions test the assumptions most likely to change concept selection."
- L590 "Heat released to air remains local heat redistribution." (frei stehender Aphorismus)
- L624 "The flow rates are requirements, not demonstrated circulation."
- L684 fünf Sätze identischer Länge und Rhythmus, eine Hedge-Liste als Absatz getarnt
- L700 "by roughly a factor of 67: the long-coil arrangement must change."
- L740 "The daily cycle is used rather than fought:"
- L748 "The principle is met by exclusion, not by verification."
- L754 "The climate benefit is not what V2 uses but what it replaces: … avoided emissions and avoided waste heat"
- L762 "No water, no refrigerant, no additive and no noise leave the system while it runs."
- L780 "Every square metre that releases heat is a square metre without photovoltaic yield."
- L786 "Under a clear summer sky V2 exports heat from the city at no running cost; the rest of the year it is a visible layer on a listed façade that yields nothing." (auffälligster Satz im Report)
- L836 "Our main lesson from the course is that biological ideas become more useful when calculations and practical constraints shape their technical transfer."

**Was menschlich klingt** (als Kontrast und Ziel-Register): L9–11 Intro, L23–25 ("air
condition", "negative feedback loop"), L135–150 Design-Question-Tabelle ("How might we
end world hunger?"), L208–230 KPI-Prosa ("Therefore we can use the Albedo index…"),
L268–274 Research path ("search engines such as google"), L370 "I needs to be mentioned",
L742 (der eine handgeschriebene Absatz mitten in Sektion 4), L824/L828 Diskussion mit "we".

**Drei Umschreibregeln:**

1. **Umkehrung streichen.** Sagen, was gilt; die "not Y"-Hälfte nur behalten, wenn der
   Leser sonst Y annehmen würde.
   Vorher (L748): "The principle is met by exclusion, not by verification. Two points remain open and unchecked: …"
   Nachher: "We meet this principle mainly by leaving things out (no glycol, no functional additive). We have not verified the materials we do use. The wood treatment of the ribs and the binder and preservatives in the roof coating still have to be checked."
2. **Fette Antithese-Überschriften und Fragment-Öffner durch normale Sätze ersetzen**, die
   Mini-Absätze zu 4–6-Satz-Absätzen zusammenlegen. 4.2 sollte zwei bis drei normale
   Absätze sein, nicht 14 Blöcke.
   Vorher (L796): "**Pipework, carrier plate, supports and fixings.** Used, not consumed: technical cycle, recoverable if specified as separable single materials."
   Nachher: "The pipes, carrier plate, supports and fixings do not wear out in normal use, so they belong to the technical cycle. They can be recovered at end of life if each part is made from a single material and can be unscrewed from the others."
3. **Keine Pointen am Absatzende.** Absätze auf dem nächsten Schritt, einer Zahl oder
   einer Quelle enden lassen. Ein-Satz-Absätze streichen.
   Vorher (L786): siehe oben.
   Nachher (in den Trade-off-Absatz gefaltet): "So the concept only pays off in summer on clear nights. From October to April the loop is drained and the ribs and roof coating just sit on the building, which matters because on a listed façade the visual change is the main objection. We have not calculated whether the summer benefit outweighs this."

Billige Zusatzmassnahmen: "we" in 3.2–4 zulassen (die menschlichen Sektionen tun das
schon); "remain(s) a check" auf eins pro Unterkapitel; von L832/L836 ("supported … but
not demonstrated" / "support … but do not establish") eines streichen; L928 in drei
Sätze teilen.

---

## 5. Totgeredete Inhalte

Ideen, die mehr als zweimal vorkommen. Format: Idee – Stellen – behalten / streichen.

1. **Kein Strom, Auftrieb treibt** – L482, 501, 507, 520, 734, 740, 786, 818, 828 (9×).
   Behalten: 482 (Mechanik), 734 (LP-Claim). Streichen: 786, Klausel in 818, Klausel in 828.
2. **Kein Wasserverbrauch / geschlossener Loop** – L505, 617, 734, 762, 828, 832 (6×).
   Behalten: 617, 734. Streichen: 762 ganz, Klauseln in 828 und 832.
3. **Pumpenlos nicht gezeigt / 300 Pa / Faktor 67** – L564, 624, 700, 702, 715, 736, 770,
   818, 828, 836 (10×). Behalten: 700 (Zahlen), 736 (eine Zeile mit Verweis), eine Klausel
   in 828. Streichen: 702 letzter Satz, 770, Mitte von 818, 836 letzter Satz. Refill-Pumpe
   (708, 736, 828): nur 708.
4. **Entleeren vor Frost / kein Glykol** – L708, 719, 740, 742, 746, 768, 782, 798, 814
   (9×). Behalten: 708, 746. 740+742 zu einem Satz; 768 und 782 zusammenlegen (gleicher
   Trade-off als Limitation und als Trade-off); 814 dupliziert 746 wörtlich.
5. **Reflexion aufs Dach, nicht Fassade, wegen Fussgängern [15]** – L474, 758, 808, 828.
   Behalten: 474. 808 → eine Zeile + "(Section 3.2.2)". Streichen: 758-Klausel, 828-Klausel.
6. **Wand bleibt / Rohre nach aussen / abnehmbare Panels** – L631, 648, 666, 676, 682, 684,
   760, 792, 800, 812, 828, 836 (12×). Behalten: 648, 676. 800 → Verweis, 812 → eine Zeile;
   streichen: 684 erster Satz, 792 zweiter Satz, 682.
7. **Kein LCA** – L684, 772, 818, 836 (4×). Behalten: 772. Rest streichen.
8. **Rippenabstand / Wintersonne** – L60, 684, 742, 778, 723, 832. Behalten: 60, 778.
9. **Abfuhr vs. Umverteilung** – L23, 590, 658, 740, 754, 756, 766, 786. Behalten: 23,
   756, 766. Streichen: 590 letzter Satz, 740-Klausel, 786.
10. **Drei Life's Principles** – Definitionen L254–258 werden in den 4.1-Überschriften
    (732/738/744) nach dem Gedankenstrich wörtlich wiederholt; L810 "which are be resource
    efficient written as constraints" streichen.
11. **Zürich-Kontext / AC-Rückkopplung** – L9 und L23 sind nahezu identisch. Behalten: 23.
    L9 auf eine Klausel, L25 streichen. L642 wiederholt L41.
12. **"Find a solution"** – L11, 15, 17, 25 sagen alle dasselbe. Behalten: 15.
13. **KPIs** – Prosa L206–230 wiederholt Table 2.5 (L232–248) fast wörtlich für KPI 1, 3,
    4, 6. L604 und L637 sagen beide "Einheiten statt °C". Behalten: Tabelle plus je ein
    Satz nur dort, wo die Tabelle etwas nicht sagt.
14. **B ist eine Hypothese** – L437, 486, 490, 509, 511, 513, 520, 635, 642 (8×).
    Behalten: 486, 642.
15. **0.95 Reflexion angenommen** – L572, 609, 658, 832. Behalten: 572, 658.
16. **Fassadenfläche muss reduziert werden** – L564, 590, 633, 688, 717, 832. Behalten:
    590, 688.
17. **Denkmalschutz** – L54, 682, 723, 776, 784, 786, 832. Behalten: 54, 776, 784.
18. **Rohr-Panel-Kontakt kritisch** – L511, 531, 658, 721. Behalten: 531, 721.

**Unterkapitel, die hauptsächlich Früheres wiederholen:**

| Abschnitt | Wiederholungsanteil | wiederholt |
|---|---|---|
| 2.1 Problem Definition | ~80 % | 1.1 (L9) |
| 2.6 KPI-Prosa | ~70 % | Table 2.5 |
| 3.2.6 Critical Engineering Questions | ~100 % | Canvas-Zeilen 509/513 |
| 4.2 Environmental benefits | ~50 % | 4.1 (734/740) und 474 |
| 4.3 Did sustainability change the design | ~85 % | 3.2.2, 3.3.2/3.3.3, 3.3.5 (legitimer Rubrik-Punkt, aber vier Einzeiler mit Verweis statt 190 Wörter) |
| 4.4 Limits of this assessment | ~80 % | 736, 770, 772, 802, 619 |
| 5.2 Strengths and weaknesses | ~70 % | 3.3.3, 3.3.5, 4.1, 474 |
| 5.3 Assessment of challenge and KPIs | ~70 % | Table 3.13, 3.3.1 |
| 5.4 Innovative character | ~60 % | 4.4, Table 3.13 |
| **Sektion 5 gesamt** | **60–70 %** | neu ist nur L824 und "components not new" + "main lesson" |

---

## 6. Sätze, die nichts sagen

Einleitungen, Überschriften-Wiederholungen, Listen-Ankündigungen:

- L11 "To address this problem, the report investigates nature inspired passive cooling mechanisms, also known as biomimicry." (wiederholt den Titel; "also known as biomimicry" ist zudem falsch)
- L17 "This project aims to find a solution which bridges the gap between thermal regulation and sustainable urban infrastructure."
- L25 "To break this cycle a new alternative and sustainable solution needs to be found."
- L29 "Fixing one reference city is what makes the constraints and the KPI targets checkable."
- L41 "Using this building as context for the report allows for a more accurate and realistic project grounded in a realistic setting."
- L45 "These constraints where chosen to keep the project realistic and useful."
- L83 "This is given by the challenge and the defined reference city of Zurich."
- L91 "There are several parallel systems which might need to be involved or considered when finding solutions for the system of interest:"
- L105 "There are several subsystems involved in the system of interest. These subsystems are to be considered when developing a concept."
- L115 "To further scope the project these aspects are scoped in or out:"
- L130 "To define the project several design questions were formulated and evaluated. The table below shows the rejected candidates."
- L150 "This question is not formulated too narrow but also not to wide. It allows some freedom … by narrowing the scope of the project to cities similar to Zurich." (45 Wörter, nichts Prüfbares)
- L156 "Table 2.4 displays the chosen functions and their respective taxonomy link."
- L176 "Using the functions listed in the table 2.4 a couple of flows can be constructed."
- L188 "To ease the search for solutions developed by nature a few biologized questions were formulated:"
- L210 "Therefore we can use the Albedo index as measurement unit to compare the reflective properties of our materials."
- L214 "Therefore the aim of this KPI is to keep a surface under shade for as long as possible. The units of measurement for this KPI will therefore be minutes spent in the shade."
- L218 "This KPI aims at measuring how well heat is dissipated from a surface."
- L222 "This KPI aims at measuring how well heat is transferred from one surface to another using any medium as transfer."
- L230 "This KPI measures the longevity of the solution by using a efficiency factor in percentage. The goal is to keep the factor as high as possible for as long as possible." (zirkulär)
- L252 "The life principles which should reflect the end solution include:"
- L260 "These life principles aim to ensure that the project keeps the solution tuned with the environment and does not introduce new hazards to the environment."
- L274 "Therefore some models were abandoned and not investigated further into." (welche? warum?)
- L428 "The next step combines them into concepts."
- L454 "Choose compatible options for the functions a concept addresses. B covers fewer functions than A, as the KPI comparison shows."
- L472 "Fans and cladding are conventional technical implementations."
- L520 "These questions test the assumptions most likely to change concept selection."
- L544 "Equations use kelvin (K): a difference of 10 K equals a change of 10 °C." und L576 "Fourth powers require absolute temperature: T [K] = T [°C] + 273.15; thus 35 °C = 308.15 K." (Lehrbuchfüller)
- L806 "The design was adjusted in four instances which were documented in sections 3.2 and 3.3."
- L800 "Ecotoxic chemicals (1) and recyclable materials (2) are answered above."

Selbstbezug auf die eigene Redlichkeit oder "nicht gemessen", das schon gesagt wurde:

- L542 "they are not measured site values or comfort targets."
- L568 "This specialised emitter provides a benchmark, not an assigned property of our coating."
- L604 "no surface-temperature reduction has been calculated. Assumptions and untested quantities remain explicit."
- L624 "Missing targets and test data prevent a defensible weighted score; the comparison instead identifies the changes needed for A and the evidence still needed for B."
- L642 "These contrasting results support testing the coating rather than assigning it a cooling value." (schon L635)
- L748 "The principle is met by exclusion, not by verification."
- L770 "A benefit without a number. No cooling figure exists, so … the first open check of Table 3.13." (sagt 604/624/736 nochmal)
- L802 "The result is not clear." und "The pigment is also not the used coating."
- L818 "No life cycle assessment was performed, so nothing in this section is a quantified environmental balance." und "Durability is defined by KPI 6 but has no data" (schon 619)
- L836 "We do not claim that its components are new." und "The estimates support further development, but do not establish measured cooling performance."
- L928 "…are marked as open items rather than left implicit"

Absatzschlüsse, die zusammenfassen oder offene Checks aus Table 3.13 wiederholen:

- L644 "Its greater material and installation needs remain a trade-off. The review in Table 3.11 guides the V2 construction changes and the revised engineering assessment below."
- L658 "Good pipe-to-panel contact is essential." (531, 721)
- L666 "Door operation and remaining pavement width still need checking." (723)
- L676 "Panel fixings and working clearance still need detailing." (721)
- L682 "Heritage protection remains a constraint [19]. Retaining the wall and demonstrating a cooling benefit could support the proposal, but its appearance and attachments still require assessment." (54, 723, 776)
- L684 "Timber treatment, coating durability, chemical safety and glare remain material checks." (723) und "No life-cycle assessment has been performed."
- L702 "The rendered long coils therefore remain a layout to revise, with short parallel circuits and larger connecting pipes." (700, 633)
- L704 "This makes roof loading and winter water storage important checks."
- L708 "Trapped water and pump-assisted refill remain checks [24]." (719)
- L786 "Under a clear summer sky V2 exports heat …" (fasst 4.2 zusammen)
- L796 "Used, not consumed: technical cycle, recoverable if specified as separable single materials." (gilt für jedes Metallteil)
- L824 "Without this process, we would probably have focused on improving existing solutions individually. Conventional engineering could produce a similar concept, but the biological models broadened our search…" (unprüfbar, generisch)
- L828 "Testing must establish whether the revised system delivers the intended cooling."
- L832 "The concept addresses the façade's contribution to urban heat; it does not address all causes of the wider challenge." / "They have therefore supported concept development, but target achievement has not been demonstrated." / "These gaps define the next evaluation steps."
- L836 "Circulation and roof-output tests are the priorities for assessing the concept's potential." (Table 3.13)

---

## 7. Kürzungspotenzial

| Sektion | Wörter | streichbar | Anteil |
|---|---|---|---|
| 1 | 188 | ~35 | 20 % |
| 2 | 1'922 | ~480 | 25 % |
| 3.1 | 1'414 | ~30 | 2 % |
| 3.2 | 1'946 | ~170 | 9 % |
| 3.3 | 1'337 | ~230 | 17 % |
| 4 | 1'499 | ~450 | 30 % |
| 5 | 419 | ~235 | 55 % |
| **gesamt** | **8'725** | **~1'630** | **19 %** |

Grösste Hebel pro Edit: (1) KPI-Prosa L206–230 löschen, Table 2.5 behalten;
(2) 4.3 als vier Einzeiler mit Verweis; (3) 5.2–5.4 auf das Neue reduzieren und für
offene Checks auf Table 3.13 zeigen; (4) "kein LCA", "pumpenlos nicht gezeigt", "Entleeren
statt Glykol" je genau einmal mit Verweis.

---

## 8. Overclaims (Aussagen, die die eigene Evidenz nicht trägt)

- L29/L31/L33: KPI-Targets, Baseline, "measured data" – nichts davon wird gezeigt.
- L150: Design Question "not too narrow, not too wide" – Widerspruch zu L87 und L135.
- L326: Ameise 2 °C plus 5–10 °C gestapelt; Primärquelle sagt 5–10 °C gesamt.
- L412: Bienen-Schwellenwert-Diversität falsch zugeordnet ([14] statt Jones et al. 2004).
- L478/L631/L648: V1 "embedded pipes" – die V1-Zeichnung zeigt sie aussen.
- L564/L736: "use most of the available buoyancy" – per Konstruktion alles.
- L604: KPI-Vergleich "against Section 2 KPIs" – in kW, nicht in den Sektion-2-Einheiten.
- L734: "buoyancy alone" als Fakt; einziger Loop-Check scheitert um Faktor 67.
- L740: "most of its heat to the night sky (Section 3.2.8)" – 3.2.8 rechnet nur den Tag.
- L746: "not through a functional additive" – L802 sagt TiO₂-Pigment.
- L758: "cannot raise heat stress" – [15] untersuchte Wände, nicht Dächer.
- L762: "Nothing emitted in operation" – gegen L794 und L798.
- L802: EuGH-Urteil zitiert mit [28], Eintrag fehlt.
- L806–814: vier "Sustainability changed the design"-Fälle, nur zwei belegt.
- L917: AskNature-Seiten nicht geöffnet, tragen aber die Mechanismus-Claims in 3.1.
- L928: "23 % figure for elephant hair" – kommt im Report nicht vor.
