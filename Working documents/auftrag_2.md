# Auftrag 2 — Discovering & Abstracting: Funde und Entscheide

Stand 01.09.2026. Grundlage: Auswertung von `Course material/Day 2 Discovering and abstracting/`,
`Course material/Day 1 Intro bionics and scoping part/` und `Course material/Overview of the semester/`.
Aufbereitete Notizen: `../Notes/` (Index in `../Notes/00_index.md`).
Angewandte Prinzipienliste: `lifes_principles_options.md`.
AskNature-Recherche: `asknature_innovation_options.md` (Vorarbeit) und
`asknature_cooling_collection.md` (Modelle).
**Fortsetzung: `auftrag_3.md`** — Vorschläge für die Creating-Phase; dort werden sieben
der neun Entscheide aus Abschnitt 7 beantwortet oder gegenstandslos.

---

## 1. Der wichtigste Fund: Genius of Biome

Das Hintergrunddokument, das im Ordner am unscheinbarsten aussieht: **Genius of Biome**
(178 S., HOK + Biomimicry 3.8) behandelt den *temperate broadleaf forest* — genau die
Biomzone, in der Zürich liegt — und übersetzt dessen Strategien explizit in gebaute Umwelt.
Das ist der „local lens" aus der Vorlesung, als fertiges Dokument.

Drei Stellen sind direkt verwertbar:

### S. 62–65 — Blatt als „passive valve"

Das abstrahierte Designprinzip lautet dort wörtlich, ein Verdunstungssystem zu bauen, bei
dem **ventilartige Poren durch Feuchte- und Wärmeniveau geöffnet und geschlossen werden**.
Das ist F9 als *Ventil* statt als Materialeigenschaft — eine Bauform, die wir bisher nicht
auf dem Radar hatten. S. 65 skizziert sogar eine „bio-adaptive facade" mit
Transpirator-Panel.

Ausserdem liefert die Seite das Gegenargument gegen den Standardeinwand, Verdunstungskühlung
tauge im feuchten Klima nichts: **sie ist die Kühlmethode sämtlicher Vegetation in genau
diesem Biom.**

### S. 41–44 — Flechte

Raue Mehrskalen-Oberfläche plus Hydrophobine ergibt wasserabweisend *und* atmungsaktiv. Die
Anwendungsidee dort verbindet **Wasserernte und Bewuchsschutz in einer Struktur**. Das ist
eine physikalische Antwort auf F10 statt einer chemischen — also genau das, wohin uns die
Biozid-Frage ohnehin drängt.

### S. 53–56 — Moose

Doppelte Schicht plus ruhende Luftgrenzschicht als Feuchtespeicher, inklusive
„Wiederauferstehung" nach Austrocknung. Für unseren Fünf-Tage-Fall interessant: **ein
Material, das Trockenfallen übersteht, versagt graduell statt endgültig.**

---

## 2. Taxonomie → unsere Funktionen

In `../Notes/day2/02_taxonomy_and_function_map.md` steht eine Tabelle, die **F0–F12 auf die
Taxonomie-Pfade abbildet**, mit denen man in AskNature sucht.

F9 fällt dabei auf: es liegt in keinem einzigen Ast, sondern ist die **Paarung von
`SENSE SIGNALS → temperature` mit `PROCESS SIGNALS → respond to signals`**. Dieselbe Paarung
formuliert die Life's-Principles-Checkliste als *„the signal it sends, the antennae it uses
to detect the signal, and its response match"*.

---

## 3. Die Farbwechsel-Idee

Als **„Concept option A"** in `lifes_principles_options.md` ausgearbeitet, mit vier
technischen Routen und fünf Prüfungen.

**Anker:**

- Schneehuhn / Polarfuchs (LP-Folie 18) — saisonaler Fellwechsel
- Photochrome Gläser (LP-Folie 25) — das Menschenbeispiel der Vorlesung für passive,
  reversible optische Änderung
- Vor allem ***Encelia farinosa***, die wir über **Ehleringer 1978 schon in der Bibliografie
  und in der Modelltabelle** haben: eine Wüstenpflanze, die ihre Reflektivität saisonal
  verstellt

**Drei Punkte, die wir kennen müssen, bevor wir uns festlegen:**

1. **Der Schalter ändert die Absorption, nicht die Emission.** Die sichtbare Farbe steuert
   die kurzwellige Seite (F1); die thermische Emission im Langwelligen — der Pfad, der
   nachts F2 trägt — hängt kaum davon ab. Die Idee behebt damit die *Winter*-Schwäche von
   HA 11, nicht dessen *Nacht*-Schwäche. Und die Nacht ist die Lücke, auf die unsere
   Designfrage zielt. **Also Ergänzung zu einem Abfuhrmechanismus, nicht Ersatz dafür.**
2. **Der Schwellwert ist eine Oberflächentemperatur, kein Kalenderdatum.** Wintersonne kann
   eine dunkle Wand über die Schwelle heben und sie weiss schalten; ein Sommermorgen startet
   dunkel und bleibt es, bis die Schwelle überschritten wird. Schalttemperatur und Hysterese
   sind damit Entwurfsparameter, keine Produkteigenschaften.
3. **Für KPI 1 ist es ein Sprung, kein Gradient.** ∂P/∂T_s ist am Schaltpunkt riesig und
   daneben null. Ob F9 mit einer Schwelle erfüllt ist oder eine kontinuierliche Antwort
   verlangt, müssen wir entscheiden — und begründen. Diese Frage sauber zu beantworten
   bringt mehr Punkte als jede der beiden Antworten.

Dazu kommen zwei weitere Prüfungen aus dem Dokument: **wo liegt die Schicht relativ zur
Dämmung** (auf einer gedämmten Fassade kommt der Wintergewinn kaum innen an — auf
ungedämmtem Massivmauerwerk, also dem geschützten Zürcher Bestand, schon), und
**Dauerhaftigkeit** (organische thermochrome Farbstoffe bleichen unter UV aus, was KPI 7
direkt trifft).

---

## 4. AskNature — Innovationen: Vorarbeit und State of the Art

Vollständig in `asknature_innovation_options.md` (13 Einträge, auf F0–F12 abgebildet).
Wichtig zur Einordnung: AskNature trennt *Biological Strategies* von *Innovations*. Unsere
Modelltabelle in §3.1 braucht **Strategies**. Die **Innovations** gehören an zwei andere
Stellen — in die dritte Spalte der Abstraktionstabelle („possible technical interpretation",
`03_bioinspired_design.tex:82`, aktuell leer) und in den **State of the Art**.

Vier davon müssen wir kennen:

- **Kamelfell-Bilayer (MIT)** — Hydrogel innen (Schweissdrüse), Aerogel aussen (Fell). Hielt
  eine Probe **7 °C unter Umgebung über 200 Stunden**, fünfmal länger als das Hydrogel
  allein. Das ist F8 — „Verdunstung dosieren, damit die Reserve die Hitzewelle übersteht" —
  mit einer Zahl dran, und unsere KPI 6 verlangt ≥ 5 Tage Autonomie. Der kontraintuitive Teil
  ist der Hebel: **die isolierende Schicht über der nassen bringt den Faktor fünf.**
- **StoColor Lotusan** — Fassadenfarbe seit 1999, mikrostrukturiert superhydrophob, laut
  Hersteller algen- und pilzresistent **ohne Biozid-Filmschutz**. Das ist genau die
  physikalische statt chemische Antwort auf F10, die unsere Biozid-Analyse fordert — und sie
  ist seit 25 Jahren am Markt, an genau dem Problem, das die Stadt Zürich als Schwäche heller
  Hüllen benennt. **In §2.3 fehlt sie.**
- **HydroCanopy** — Fassadensystem nach Froschhaut-Schleimdrüsen plus Blattdichte-Gradient im
  Kronendach, kombiniert Strahlungsregulation, Lüftung, Speichermasse und
  Verdunstungskühlung. Das ist die **nächstliegende publizierte Vorarbeit zu unserem gesamten
  Konzept.** Wir müssen sie zitieren und sagen können, was wir zusätzlich machen — unsere
  ehrliche Antwort ist **F9 und das Nachtfenster**.
- **Tintenfisch-Decke (UC Irvine, Nature Communications)** — Metallinseln, die beim Dehnen
  auseinandergehen und Infrarot durchlassen; **~36 W/m² geregelt bei ~3 W/m² mechanischem
  Input**. Das ist die **Emissions-Version** unserer Farbwechsel-Idee, also die, die *nachts*
  wirkt. Sie verletzt unseren Energie-Constraint — woraus die vielleicht beste kritische Frage
  des ganzen Projekts wird: **lässt sich derselbe geometrische Schalter passiv betätigen**,
  über Wärmeausdehnung oder eine quellende hygroskopische Schicht?

Nebenbefund für Concept option A: **Cypris Materials** macht paintable Strukturfarbe aus
selbstassemblierenden Blockcopolymeren, ins nahe Infrarot abstimmbar, ARPA-E-gefördert
ausdrücklich für Gebäudekühlung. Strukturfarbe entsteht über einen *Abstand*, und ein Abstand
lässt sich durch Quellen oder Trocknen ändern — ein passiver Schalter ohne den
UV-Ausbleichungsdefekt der Leuko-Farbstoffe, also genau dort, wo unsere thermochrome Route am
ehesten kippt.

---

## 5. AskNature — Sammlung „Cooling Down in the Heat": Modelle

Vollständig in `asknature_cooling_collection.md` (9 Einträge). Diese Sammlung liefert
**Modelle**, also Material für die Modelltabelle.

### Der wichtigste Fund: Bienen beantworten unsere F9-Frage

Bei Honigbienen ist die Temperatur, ab der eine Arbeiterin zu fächeln beginnt,
**individuell verschieden und genetisch bedingt** — ein Volk hat eine Königin, aber viele
Väter, also Patrilinien mit unterschiedlichen Schwellen. Folge: wird es wärmer, fächeln erst
wenige, dann mehr, dann viele. **Jedes Individuum ist ein binärer Schalter, die Antwort des
Volkes ist proportional.**

Das kippt die Bewertung von Concept option A. Unter Punkt 3 steht als Sorge, ein
thermochromer Anstrich liefere nur einen Sprung und erfülle F9 vielleicht nicht. Die Bienen
zeigen die Auflösung: **nicht eine Schaltschwelle, sondern eine Verteilung von
Schaltschwellen.** Ein Anstrich, dessen Domänen bei unterschiedlichen Temperaturen
umschalten, verhält sich makroskopisch proportional. Als übertragbares Prinzip:

> *Verteile eine Population binärer Antwortelemente über einen Bereich von Auslösepunkten;
> die Summenantwort skaliert dann kontinuierlich mit der Last — ohne Regler und ohne ein
> einziges proportionales Element im System.*

Dasselbe gilt für eine Ventil- oder Dochtlösung: viele kleine Poren mit unterschiedlichen
Öffnungspunkten schlagen eine grosse Pore mit einem Punkt. Es ist ausserdem dasselbe Muster,
das der Genius of Biome auf S. 59 **„lots of littles"** nennt — zwei Dokumente, zwei
Richtungen, dieselbe Antwort.

Neue kritische Frage daraus: **lässt sich eine solche Streuung überhaupt formulieren, oder
erzwingt die Chemie eine scharfe Schwelle?**

### Drei Modelle für die Tabelle

- **Wüstenschnecke** *Sphincterochila boissieri* — **95 % Reflexion im nahen Infrarot, 90 % im
  Sichtbaren**, überlebt bis 50 °C. Beim Ästivieren verschliesst sie die Öffnung mit einem
  verkalkten Epiphragma und zieht sich in die zweite Windung zurück; **die Luftschicht
  dahinter** puffert Wärme und Feuchte. Das einzige Modell der Sammlung, das **nicht
  metabolisch** ist: eine passive mineralische Struktur, die genau das tut, was unsere Hülle
  tun muss — und die unseren KPI-2-Zielwert von 0.80 deutlich übertrifft, mit Calciumcarbonat
  statt Pigment. Der Teil, den wir sonst übersehen hätten: **Reflexion allein ist nicht die
  Strategie, Reflexion plus entkoppelnder Luftspalt ist es.** Als geschichteter Aufbau haben
  wir diesen Spalt zur Verfügung, ein Anstrich hat ihn nicht. Dazu existiert eine
  AskNature-Innovation, die Schnecke und **Saharan silver ant** kombiniert — also mit dem
  Modell, das wir über Shi 2015 bereits zitieren.
- **Seestern** — nimmt bei Flut kaltes Wasser auf, und **wie viel er aufnimmt, bestimmt die
  vorangegangene heisse Ebbe**. Das ist unsere Lade-/Entladelogik: Lastfenster = heisse Ebbe,
  Nachtfenster = kalte Flut, Speicher = Coelom. Einschliesslich der ehrlichen Grenze — der
  Mechanismus versagt, sobald das Wasser nicht mehr kälter ist als die Luft, was genau unser
  Reset-Problem über fünf Tage ist. Und er zeigt: **F9 muss nicht sofort wirken.** Heute
  ausgelöst, morgen geliefert, ist immer noch lastgekoppelt.
- **Kaktusrippen** — Spitzen beschatten die Täler; die kühlere Luft in den Tälern nimmt mehr
  Wärme auf, steigt zu den Spitzen und wird vom Wind abgeführt; die gefaltete Fläche
  vergrössert zugleich die abstrahlende Fläche. F5, F3 und F2 aus **reiner Geometrie** — kein
  Material, kein Wasser, keine Chemie, nichts, was ausbleicht oder leerläuft. Der Konflikt ist
  unser Stadtbild-Constraint; die zugehörige Innovation arbeitet mit „unnoticeably small"
  Rippen, die Strukturgrösse ist also verhandelbar.

### Der wasserfreie Weg zu F9

**Hase und Elefant** erreichen F9 durch **Vasodilatation** — sie regeln nicht eine
Materialeigenschaft, sondern den *Transport zu einer abstrahlenden Fläche*, und zwar
ausdrücklich, um **Wasser zu sparen**. Bei etwa 30 °C Lufttemperatur können die Ohren des
Hasen die gesamte Überschusswärme abführen. Das ist der biologische Präzedenzfall für den
zweiten, unabhängigen Abfuhrpfad aus Entscheid 3: wenn der Verdunstungspfad an Tag drei
trockenfällt, ist ein variabler Strahlungspfad das, was noch arbeiten sollte. Passive
Analogien wären ein Thermosiphon, ein Dochtnetz mit temperaturabhängiger Transportrate oder
eine Kontaktfläche, die sich über ein Bimetall vergrössert — ob das einen brauchbaren
∂P/∂T_s ergibt, ist eine Rechnung, keine Annahme.

### Der Satz, der uns Punkte bringt

**Die meiste Kühlungsbiologie ist Stoffwechsel oder Verhalten.** Eine Biene fächelt, ein Hase
weitet Blutgefässe, ein Elefant lenkt Blut um. Eine Fassade hat weder Stoffwechsel noch
Verhalten, also muss die Übertragung auf ein **passives Analogon** zielen — sonst ist es keine
Übertragung. Dass Schnecke und Kaktus die am besten übertragbaren Modelle sind, ist kein
Zufall: es sind die beiden, die **Strukturen statt Prozesse** sind. Zwei Einträge der Sammlung
(Karotis-Rete der Gazelle, Ästivation des Tenreks) lehnen wir aus genau diesem Grund ab — mit
Kriterium, nicht nur mit Urteil.

---

## 6. Ideen aus dem Team

### 6.1 Elefanten-Hotspots: der Radiator muss nicht die ganze Hülle sein

**Der Mechanismus.** Elefanten leiten Blut gezielt an **verstreute Hautflecken** — nicht
gleichmässig über den ganzen Körper. Als fassförmige Tiere können sie sich Schwitzen kaum
leisten, also öffnen sie stattdessen lokale „thermal windows" per Vasodilatation und
verschieben deren Lage und Zahl mit der Last.

**Das übertragbare Prinzip:**

> *Wärme über einen kleinen, veränderlichen Anteil der Fläche abführen — statt schwach über
> die gesamte.*

**Was das für unser Konzept ändert.** Wir haben bisher implizit angenommen, der ganze
Aufbau müsse überall alles können: reflektieren, emittieren, speichern, Wasser führen,
sauber bleiben. Der Elefant sagt: nein. Ein Teil der Fläche wird zum **Wärmefenster**
ausgebaut — hohe Emissivität, benetzt, dort platziert, wo Sky View Factor und Wind am besten
sind (Attika, oberer Fassadenbereich, Dachrand) —, der Rest wird auf Dauerhaftigkeit,
Reflexion und Stadtbildverträglichkeit optimiert. Vier Folgen:

1. **Material und Kosten sinken** — die teure Funktionsschicht liegt nur auf einem Bruchteil
   der Fläche. Das zahlt direkt auf KPI 8 und auf *be resource efficient* ein.
2. **Der Stadtbild-Constraint entspannt sich** — ein Flickenteppich ist weniger sichtbar als
   eine vollflächig neue Hülle, und auf einem geschützten Gebäude eher bewilligungsfähig.
3. **Noch ein Weg zu F9**: der aktive Flächenanteil wächst mit der Last. Das ist Regelung
   über *Fläche* statt über Materialeigenschaft.
4. Der Elefant trägt dann **zwei Funktionen** in unserer Modelltabelle — die Hautrisse
   (Martins 2018, bereits zitiert) für F6–F8 und die Hotspots für F9. Ein Organismus, zwei
   Mechanismen, saubere Begründung.

**Testbar:** welcher Flächenanteil, bei welcher Emissivität oder Benetzung, liefert die
geforderten W/m² bezogen auf die *gesamte* Fassade? Eine saubere Rechnung für §3.2.

### 6.2 Sonnensegel, das sich unter Hitze selbst aufspannt

**Die Idee.** Ein Segel oder Lamellenfeld, das sich bei Hitze von selbst ausbreitet und bei
Kühle wieder zusammenzieht — ohne Motor, ohne Sensor, ohne Strom. Ausgearbeitet als
**„Concept option B"** in `lifes_principles_options.md`.

**Warum das die stärkste Idee bisher sein könnte — vier Gründe:**

1. **Es ist die wörtlichste Antwort auf unsere Designfrage.** Wir fragen, wie die Wärme
   *ihre eigene Abfuhr antreiben* kann. Ein Thermobimetall wird buchstäblich von der Wärme
   angetrieben, die es abwehrt. Die Energie für die Bewegung ist die Last selbst.
2. **Es wirkt im Strassenraum, nicht nur an der Wand.** Seit wir §1.1 auf die Aussenraum-
   Perspektive gedreht haben, ist das entscheidend: eine Beschichtung ändert, was die Wand
   abstrahlt; ein Segel nimmt Fussgängern die direkte Sonne. Das trifft **KPI 4 (PET auf 2 m)**
   — die Grösse, die die Stadt selbst verwendet — direkt statt über Umwege.
3. **Es löst den Nacht-Konflikt, an dem feste Verschattung scheitert.** Eine feste
   Verschattung senkt den Sky View Factor und behindert damit nachts genau die langwellige
   Abstrahlung, die wir brauchen: sie erkauft den Tagesnutzen mit einem Nachtverlust. Ein
   Segel, das sich bei Abkühlung **einzieht**, bekommt beides — Schatten am Tag, freien Himmel
   in der Nacht. Genau die Lücke, die wir bei HA 11 identifiziert haben.
4. **Es löst den Sommer/Winter-Konflikt geometrisch statt chemisch.** Im Winter eingezogen,
   also volle solare Gewinne — dasselbe Ziel wie Concept option A, aber ohne Farbstoff, der
   unter UV ausbleicht.

**Es gibt gebaute Präzedenzfälle, beide energielos:**

- **Thermobimetall** (Doris Sung, System *InVert*): zwei Metalle mit unterschiedlicher
  Wärmeausdehnung; das Element krümmt sich in der Sonne und verschattet — ausdrücklich
  „no energy and no controls", ausgezeichnet u. a. mit einem National Design Award 2021 in
  der Kategorie Climate Action.
- **HygroSkin / HygroScope** (Achim Menges, Krieg, Reichert): Öffnungen aus dünnem Sperrholz,
  die sich allein über die Feuchteaufnahme des Holzes bewegen, Vorbild **Fichtenzapfen** —
  bei 30 % Luftfeuchte geschlossen, bei 75 % vollständig offen, ohne jede Mechanik oder
  Elektronik.
- Dazu auf AskNature die Strategie *Pine Cones Open and Close in Response to Weather* und die
  Innovation *Humidity-Sensitive Hydraulic Actuator Inspired by Pine Cones*.

**Die Prüfung, die alles entscheidet: Wind.** Ein Segel über einem Strassenraum ist ein
Struktur- und Sicherheitsproblem, und ein thermischer Aktuator **spürt keinen Wind**. Ein
heisser Sturmnachmittag spannt das Segel genau dann auf, wenn es eingezogen sein müsste. Es
braucht also eine **zweite, unabhängige und ebenfalls passive Wind-Auslösung** — mechanische
Sollbruchstelle, sich selbst einrollende Geometrie oder Perforation, die Böen durchlässt. Das
ist die kritische Ingenieurfrage dieses Konzepts, und sie ist eine gute.

**Und die ehrliche Einordnung:** Verschattung des gebäudenahen Aussenraums ist bei der Stadt
bereits **HA 12**, also eine Bestandsmassnahme. Neu ist bei uns nicht das Verschatten,
sondern **dass es lastgekoppelt geschieht und sich nachts zurückzieht**. Genau das muss im
Bericht der Unterschied sein.

### 6.3 Farbige Wände, die trotzdem Wärme abweisen — Strukturfarbe

Ausgangspunkt: [Butterflies Hack Light Waves to Produce Brilliant
Color](https://asknature.org/strategy/wing-scales-cause-light-to-diffract-and-interfere/).
Die Flügelschuppen des *Morpho* bestehen aus nano- und mikroskaligen, **transparenten**
Chitin-Luft-Schichten. Auftreffendes Licht wird gebeugt, die Wellen interferieren, bestimmte
Wellenlängen löschen sich aus, andere verstärken sich. Die Farbe steckt in der **Geometrie**,
nicht im Pigment — und die AskNature-Seite nennt als Zweck ausdrücklich Tarnung,
**Thermoregulation** und Signalgebung.

**Warum das unseren härtesten Constraint angreift.** Etwa **45 % der Sonnenenergie, die den
Boden erreicht, liegt im nahen Infrarot** (700–2500 nm) — für das Auge unsichtbar. Eine
Oberfläche kann also im Sichtbaren farbig oder dunkel wirken und trotzdem fast die halbe
solare Last zurückwerfen. Genau daran hängt unser Stadtbild-Constraint: auf einem geschützten
Zürcher Gebäude ist Weiss oft nicht bewilligungsfähig, und die Stadt nennt Blendung als
Haupteinwand gegen helle Hüllen. **Strukturfarbe verwandelt diesen Constraint von einem
Ausschlusskriterium in einen Entwurfsraum:** eine Fassade, die aussieht wie der bestehende
Ocker- oder Grauputz und trotzdem „cool" ist.

**Ehrliche Einordnung — das gibt es schon.** „Cool colored coatings" mit komplexen
anorganischen Pigmenten (Chromoxidgrün, Kobaltblau, Phthalocyaninblau, Hansagelb) sind
Stand der Technik. Das gehört in §2.3, nicht in unsere Neuheitsbehauptung.

**Was der biomimetische Schritt darüber hinaus bringt — drei Dinge:**

1. **Kein Pigment, das ausbleicht.** Struktur altert anders als Farbstoff. Das zahlt direkt
   auf KPI 7 und auf den Dauerhaftigkeits-Constraint ein — und auf die Schwachstelle von
   Concept option A.
2. **Kein bedenkliches Pigment.** Kobalt und Chromoxid sind genau die Stoffe, die unter
   *use life-friendly chemistry* zu rechtfertigen wären. Struktur braucht sie nicht.
   Dieselbe Logik wie beim *Cyphochilus*-Weiss, das TiO₂ ersetzt.
3. **Diffus statt spiegelnd — und das ist der Knackpunkt.** Schichtstapel sind irisierend:
   die Farbe kippt mit dem Blickwinkel, und das wäre an einer Fassade untragbar. Die Antwort
   steckt in unseren eigenen Modellen: *Morpho*-Blau und *Cyphochilus*-Weiss sind
   **ungeordnete** Strukturen und deshalb aus vielen Winkeln gleich und **diffus statt
   spiegelnd**. Damit beantwortet dieselbe Eigenschaft zwei Anforderungen auf einmal —
   Winkelunabhängigkeit und den Blendungs-Constraint der Stadt.

Technische Route: **Cypris Materials** (siehe Abschnitt 4). Zu prüfen ist, ob sich Sichtbares
und NIR wirklich unabhängig einstellen lassen — also ob die Farbe frei wählbar bleibt, während
die NIR-Reflexion hoch bleibt.

### 6.4 UV-Schutz aus dem Auge — die Antwort auf unsere Ausbleich-Frage

Ausgangspunkt: [Sunblock Inspired by Compounds in Our
Eyes](https://asknature.org/innovation/sunblock-inspired-by-compounds-in-our-eyes/).
**Kynurenine** in der Augenlinse schützen die Netzhaut vor UV: trifft UV-Licht auf das
Molekül, wird die Energie durch **wandernde Protonen innerhalb der Molekülstruktur**
abgeführt, statt das Molekül zu zerstören. Die Firma *Sóliome* baut daraus eine nicht toxische,
biologisch abbaubare Sonnencreme, mit angehängten Gruppen, die die Moleküle zu gross zum
Eindringen in die Haut machen.

**Warum das für uns wichtiger ist, als es klingt.** Die Prüfung, an der Concept option A am
ehesten scheitert, ist **UV-Ausbleichung des thermochromen Farbstoffs** — direkt gegen KPI 7.
Die ingenieurmässige Standardantwort ist eine UV-Filterschicht darüber. Was dieses Modell
hinzufügt, ist die *Art* des Filters: ein Molekül, das die UV-Energie **photostabil
wegdissipiert**, statt sie in die eigene Zersetzung zu stecken.

Und es passt zu unserer Biozid-Analyse: ein synthetischer UV-Absorber, der ins gesammelte
Regenwasser auswäscht, das wir auf Fussgängerhöhe verdunsten, wäre derselbe Fehler wie ein
auswaschbares Biozid. Ein biologisch abbaubarer, nicht toxischer Filter ist hier nicht nur
nett, sondern von unserem eigenen Constraint gefordert.

**Was nicht übertragbar ist:** das Produkt. Eine Sonnencreme hält Stunden auf Haut, unsere
Schicht muss zwanzig Jahre an einer Wetterseite halten. Übertragbar ist der **Mechanismus**,
nicht die Formulierung — und genau diese Unterscheidung will die Vorlesung sehen.

Allgemeiner gilt das für F11: **jeder organische Bestandteil unseres Aufbaus** hat ein
UV-Problem, nicht nur ein thermochromer Farbstoff.

### 6.5 Und was ist mit Pflanzen als Schattenspender?

Kurz, weil die Frage im Weltcafé garantiert kommt: Begrünung ist bei der Stadt bereits
**HA 09** (Dachbegrünung) und **HA 10** (Fassadenbegrünung), also Bestandsmassnahme, und
Begrünung im Stadtmassstab liegt laut unserer Systemgrenze **ausserhalb** des Projekts.
Dazu kommt ein handfester Zielkonflikt: eine begrünte Fassade **braucht Wasser** — und zwar
am meisten während der Hitzewelle, also genau dann, wenn unsere Reserve für F8 gebraucht
wird und es nicht regnet.

Übertragbar ist trotzdem etwas: **nicht die Pflanze, sondern die Anordnung des Blattwerks.**
Genius of Biome S. 92 beschreibt Sonnen- und Schattenblätter — dieselbe Art differenziert
ihre Blattform nach Exposition, und Sonnenblätter lassen Licht ins Kroneninnere durch.
HydroCanopy übersetzt genau diesen Dichtegradienten in eine Fassade. Für uns heisst das:
**dasselbe Produkt muss an Süd-, Ost- und Westfassade nicht dieselbe Geometrie haben** — was
die Aussage aus §2 stützt, dass wir uns nicht auf die Fassade allein beschränken.

### 6.6 Die drei Funde zeigen dasselbe Prinzip

Bienen (verteilte Schwellen), Elefant (veränderlicher aktiver Flächenanteil) und Segel
(entfaltete Fläche) laufen auf dieselbe Abstraktion hinaus, und die ist stärker als jedes
Einzelmodell:

> **Nicht regeln, wie stark jedes Element wirkt — sondern wie viele Elemente wirken.**

Das ist ein sauberes, übertragbares Designprinzip für die Abstraktionstabelle, es löst
unsere F9-Schwellenfrage, und es kommt aus drei unabhängigen biologischen Modellen. Genau
so soll die Abstraktionsspalte aussehen.

---

## 7. Was wir besprechen müssen

### Entscheide

Die Reihenfolge ist bewusst: 1 und 2 legen fest, *was* wir bauen, der Rest folgt daraus.

1. **Welche zwei Konzeptvarianten gehen in §3.2?** Die Vorgabe verlangt zwei **technisch
   verschiedene** Konzepte, keine kosmetischen Varianten. Auf dem Tisch liegen inzwischen
   vier Richtungen:
   - **A · Farbwechsel-Beschichtung** — Prävention, wirkt nicht nachts
   - **B · selbstaufspannendes Sonnensegel** — Prävention *plus* freier Nachthimmel, wirkt im
     Strassenraum
   - **C · Verdunstungsaufbau mit Wasserpfad** — Abfuhr, Kamelfell-Bilayer als Dosierprinzip
   - **D · Rippen-/Kaktusgeometrie** — Prävention und Konvektion, ohne Material und ohne Wasser

   Meine Einschätzung: **B und C** sind das beste Paar. Sie sind physikalisch wirklich
   verschieden (Geometrie/Bewegung gegen Phasenwechsel/Wasser), beide decken das Nachtfenster
   ab, und A lässt sich als Modifikator auf beide legen.
2. **Darf F9 eine Schwelle sein?** Nach dem Bienen-Fund lautet die Antwort: **ja, wenn es
   viele Schwellen sind.** Damit wird aus dem bisherigen Einwand eine Entwurfsvorgabe —
   *Verteilung* der Auslösepunkte statt eines einzigen. Zu entscheiden ist nur noch, ob wir
   das so formulieren und ob es sich fertigen lässt.
3. **Wind-Auslösung beim Segel**: verlangen wir eine zweite, unabhängige passive Auslösung?
   Ohne sie ist Konzept B nicht sicherheitsfähig. Das ist die kritische Ingenieurfrage zu B.
4. **Wärmefenster statt Vollfläche?** Nach dem Elefanten-Prinzip: bauen wir die
   Funktionsschicht nur auf einem Teil der Fläche aus, dort wo Sky View Factor und Wind am
   besten sind? Das senkt Kosten, Material und Sichtbarkeit — und ist ein dritter Weg zu F9.
5. **Redundanz als Entwurfsregel**: verlangen wir zwei unabhängige Abfuhrpfade, damit der
   Fünf-Tage-Fall nicht am leeren Wasserspeicher scheitert? Der biologische Präzedenzfall ist
   der Hase: variabler Strahlungspfad, ausdrücklich um Wasser zu sparen.
6. **Farbe statt Weiss?** Wenn ~45 % der Sonnenenergie im NIR liegt, muss unsere Oberfläche
   nicht weiss sein, um kühl zu sein. Setzen wir KPI 2 auf die **solare** Reflexion (was er
   ohnehin tut) und lassen die sichtbare Farbe frei — dann wird der Stadtbild-Constraint
   erfüllbar statt blockierend.
7. **Zielbestand**: gedämmt oder ungedämmt? Betrifft nur A — die Winterhälfte des Arguments
   funktioniert nur ungedämmt.
8. **Selbstreinigung**: darf sie überhaupt chemisch sein? Ein Biozid, das ins gesammelte
   Regenwasser gelangt, das wir auf Fussgängerhöhe verdunsten, setzt es genau dort frei, wo
   wir die Lage verbessern wollen. Lotusan zeigt, dass die physikalische Antwort seit 25
   Jahren marktfähig ist.
9. **F9 als Ventil oder als Material?** Genius of Biome S. 63 macht die Ventil-Variante
   plausibel; unser bisheriges Denken war materialbasiert. Konzept B ist die dritte Antwort:
   F9 als **Bewegung**.

### Anpassungen am Bericht, die sich aus der Auswertung ergeben

- **§2.7 mischt Ebenen.** „Use low energy processes" und „maintain integrity through
  self-renewal" sind im Handbuch Unterprinzipien von *Be resource efficient* bzw. *Adapt to
  changing conditions*. Neu strukturieren: sechs Prinzipien → beanspruchtes Unterprinzip →
  Funktion → KPI.
- **Drei Prinzipien fehlen ganz** (*Evolve to survive*, *Integrate development with growth*,
  Dach-Prinzip *Create conditions conducive to life*). Zwei davon sollten wir **begründet
  ablehnen** — die Rubrik belohnt eine begründete Abwahl und straft eine blosse Liste ab.
- **8 KPIs statt der geforderten 4–7.** Sowohl die Aufgabenstellung (Scoping-Folie 28) als
  auch die Rubrik nennen 4–7. Zusammenlegen.
- **Leitfrage 3 der Challenge unbeantwortet.** Die Aufgabenstellung fragt ausdrücklich: *„What
  can we learn from desert plants or animals about passive cooling?"* Unsere Modelltabelle
  ist voller Wüstenorganismen, aber wir sagen nirgends, dass die Wüste der Ort ist, an dem
  die Champion-Adapter für dieses Problem leben. Ein Satz behebt das und begründet zugleich
  die Modellauswahl.
- **Kein einziger AskNature-Eintrag zitiert**, obwohl beide Vorgabedokumente ihn als
  erwarteten Quellentyp nennen.
- **`helms2009` ist unzitiert** — es ist eine der beiden Quellen der Vorlesung und gehört in
  den Methodikteil.
- **Widerspruch in §2**: `02_scoping.tex:438` nennt das Abendfenster 20:00–24:00, die
  Fenstertabelle und ihre Begründung nennen 18:00–24:00.

### Was der Weltcafé-Auftritt liefern muss

Der Weltcafé ist laut Rubrik **die Peer-Review-Evidenz für §3.3**. Fünf Minuten Pitch, dann
vier Runden à zehn Minuten Feedback. Das funktioniert nur, wenn jemand pro Runde mitschreibt:
**wer welchen Einwand gebracht hat und ob wir ihn akzeptieren.** Als „open questions" für den
Pitch eignen sich genau die Entscheide oben.

---

## 8. Postfertig — neun Modelle, auf die Stadt bezogen

Gefiltert nach dem, was in **unserer** Stadt tatsächlich funktioniert: passiv, übersteht Frost
und UV über zwanzig Jahre, lebt in einer Oberfläche, verbraucht kein Wasser, das wir während
der Hitzewelle nicht haben — und wirkt möglichst *nachts*, weil das die grössere Hälfte des
Problems ist. **Kamel und Fasskaktus sind von den anderen schon gepostet**; Nr. 5 nimmt
deshalb die technische Umsetzung des Kamels statt die Biologie zu wiederholen. Alles unter der
Linie ist zum Kopieren.

-------------------------

**1 · Move the heat to where the sky is — jackrabbit ears and elephant skin**

*What it is:* A jackrabbit sheds heat through thin, heavily vascularised ears and controls how much by widening or narrowing the vessels. At around 30 °C air temperature the ears alone carry all of its excess heat, and it costs no water. Elephants do the same in patches: small cooling windows scattered over the skin, opened as needed.

*Links:* https://asknature.org/strategy/how-blood-flow-keeps-jackrabbits-cool/ · https://asknature.org/strategy/skin-fine-tunes-internal-temperature/

*Why this is interesting for us:* The animal separates the place where heat is picked up from the place where it is released, and it regulates the transport instead of changing the surface. It does this specifically to avoid spending water.

*How we could apply it to the city:* In a street canyon, a wall at eye level can barely see the sky, and that blocked view is the physical cause of the night-time heat island. A roof or parapet two floors higher sees it well. A closed liquid loop needs no pump if it is driven by density differences alone, and its circulation strengthens as the temperature difference grows — so heat picked up on the hot canyon face could be released at roof level after sunset. Following the elephant, that radiator does not have to cover the whole envelope, only the fraction with the best sky view and the most wind. Open question: how the loop survives a Swiss winter.

-------------------------

**2 · Reflect it, then decouple it — desert snail**

*What it is:* The desert snail *Sphincterochila boissieri* survives on sun-exposed ground at up to 50 °C. Its shell reflects about 90 % of visible light and about 95 % in the near infrared, and when conditions get extreme the animal seals the opening with a calcified plate and withdraws deeper in, leaving a layer of air between itself and the hot ground.

*Link:* https://asknature.org/strategy/shell-protects-from-heat/

*Why this is interesting for us:* Reflection alone is not the strategy. Reflection plus a decoupling air gap is. And unlike almost every other cooling model, this one is a passive mineral structure rather than a living process — which is exactly what a wall is.

*How we could apply it to the city:* The heat that makes a city 7 K warmer at night is heat that was stored in mass during the day. A reflective outer skin in front of a ventilated cavity does two things at once: it reflects, and it stops what is still absorbed from charging the masonry behind it. Less charge means less released into the street after sunset. This is not exotic construction — a rear-ventilated façade is a standard system that ordinary trades already install, which matters more in a retrofit than any material novelty.

-------------------------

**3 · Colour is free — Morpho butterfly**

*What it is:* A Morpho wing is brilliantly blue and contains no blue pigment. Transparent layers of chitin and air, a few hundred nanometres apart, bend the light and recombine it so that some wavelengths cancel out and others are reinforced. The colour sits in the geometry.

*Link:* https://asknature.org/strategy/wing-scales-cause-light-to-diffract-and-interfere/

*Why this is interesting for us:* About half of the sun's energy arrives as invisible near-infrared light, so how a surface looks and how much heat it takes up are separable problems. And because the Morpho's structure is disordered rather than a regular mirror stack, the colour holds from many angles and the surface stays diffuse.

*How we could apply it to the city:* In an old town a white façade is often not permitted, and the city names glare as its main objection to bright envelopes. A surface that looks like the ochre or grey plaster already on the building and still rejects the near infrared turns the heritage rule from a dead end into a design space. To be fair: "cool colour" pigments already exist commercially. What the structural route adds is that there is no dye to bleach and no cobalt or chromium to justify.

-------------------------

**4 · Put the control into the opening — leaf stomata**

*What it is:* A leaf cools itself by more than 10 K through pores whose two guard cells swell and shrink with their water content, opening and closing the pore as they do. The water is pulled up from the roots by the evaporation itself. There is no pump anywhere in the system.

*Link:* Genius of Biome, pp. 62–65 (`Course material/Day 2 Discovering and abstracting/`)

*Why this is interesting for us:* The valve responds directly to heat and dryness, so the cooling effort rises with the load without a sensor and without a controller. That is our design question, already solved.

*How we could apply it to the city:* Evaporation is the only mechanism on this list that cools the air people actually breathe at street level, rather than only the surface they walk past. The binding constraint is water: during a heat wave it does not rain, so the reserve has to be collected beforehand and released slowly — which is the next entry.

-------------------------

**5 · Meter the water, and insulate it — camel-inspired bilayer**

*What it is:* A two-layer passive cooler built at MIT: a hydrogel layer that evaporates, like a sweat gland, underneath an aerogel layer that blocks incoming heat but lets vapour through, like camel fur. It held a sample 7 K below ambient for 200 hours — five times longer than the hydrogel on its own.

*Link:* https://asknature.org/innovation/passive-cooling-system-inspired-by-camels/

*Why this is interesting for us:* The counter-intuitive part is the lever. Putting insulation *over* the wet layer instead of exposing it to the air multiplies how long the reserve lasts by five. Our target is five days of autonomy; 200 hours is more than eight.

*How we could apply it to the city:* Zurich gets plenty of rain over a year and almost none during a heat wave, so our problem is storage and metering, not collection. That also rules out the most-cited water model in biomimicry for our climate: the Namib desert beetle harvests fog, and fog in Zurich is a winter phenomenon.

-------------------------

**6 · Shade the people, then get out of the way — pine cone**

*What it is:* A pine cone opens and closes with the weather years after the tree stopped feeding it. Each scale is two bonded layers that swell differently with moisture, so the scale bends. The cone is dead tissue; all the movement comes from the surrounding climate. The same principle is already built: HygroSkin, whose wooden apertures are closed at 30 % humidity and open at 75 %, and thermobimetal shutters that curl in the sun, explicitly with "no energy and no controls".

*Link:* https://asknature.org/strategy/pine-cones-open-and-close-in-response-to-weather/

*Why this is interesting for us:* The actuator is powered by the very load it counteracts. That is the most literal possible reading of our design question.

*How we could apply it to the city:* A coating changes what a wall radiates; a shade takes the sun off the person standing underneath it, which is the effect the city measures. But permanent shading also blocks the night sky, and the night is the larger half of the problem — so the element has to retract as it cools. The risk is wind: a thermal actuator cannot feel a storm, so a second, independent and equally passive release is needed before this is safe over a street.

-------------------------

**7 · Many switches beat one — honeybee fanning thresholds**

*What it is:* Every worker bee starts fanning at a slightly different temperature, and the spread is genetic — one queen, many fathers, therefore many thresholds in one colony. As the nest warms, a few bees fan, then more, then many, and the nest stays below about 36 °C without any central control.

*Link:* https://asknature.org/strategy/varying-response-thresholds-aid-hive-thermoregulation/

*Why this is interesting for us:* Every individual is an on/off switch, yet the colony's response is smooth and proportional to the load. That removes the standard objection to switchable materials, which is that they are all-or-nothing.

*How we could apply it to the city:* Whatever we build, build it as many small units with a deliberate spread of trigger temperatures — thermochromic domains, shading elements, valves. Shading or cooling then grows through the course of a hot afternoon instead of snapping on at one temperature, and no controller is needed to achieve it.

-------------------------

**8 · Stay clean without chemistry — lichen**

*What it is:* The lichen *Lecanora* keeps water out and air in through roughness on several size scales at once. Droplets perch on the peaks and roll off, while the channels between them are coated so they stay dry and air still reaches the algae inside. The surface is waterproof and breathable at the same time, and gives dirt and biofilm very little to hold on to.

*Links:* Genius of Biome, pp. 41–44 · https://asknature.org/innovation/paint-inspired-by-lotus-leaves-creates-self-cleaning-and-antifouling-surfaces/

*Why this is interesting for us:* The city itself names soiling as the specific weakness of bright envelopes, and a lotus-effect façade paint has been on the market since 1999 with no biocide in the film. The physical route is not speculative, it is sold.

*How we could apply it to the city:* A bright surface that greys within three years has solved nothing. And if we collect the rain running off it and evaporate that rain at head height, then whatever leaches out of the coating ends up in the air people breathe. That rules out a biocide — and by the same argument any UV stabiliser we would not want in the run-off, which is why the kynurenine filter from the eye lens is worth a look for the durability problem.

-------------------------

**9 · Charge the store before the load arrives — sea star**

*What it is:* After a hot low tide, a sea star takes up more cold water into its body cavity during the next high tide, and the extra cold fluid keeps it cooler through the following low tide. The heat of one cycle sets how much it charges up for the next.

*Link:* https://asknature.org/strategy/body-buffers-thermal-variations/

*Why this is interesting for us:* Self-regulation does not have to be instantaneous — cued today and delivered tomorrow is still coupled to the load. And the researchers name the failure mode themselves: the strategy only works while the sea is colder than the air.

*How we could apply it to the city:* Charge at night, spend by day. That is also precisely what a multi-day heat wave with tropical nights attacks, so whatever we build has to be shown not to drift upward from one morning to the next. A design that cools well on day one and saturates by day three has failed the case, even if every single-day number looks good.

-------------------------

**What we looked at and left out, and why**

The termite mound, because the Eastgate building that made it famous uses fans and the chimney explanation is contested in the literature (Turner 2008) — it is not the passive system it is sold as. Fog harvesting, because Zurich's fog is a winter phenomenon and there is none during a heat wave. Green façades, because they are already the city's own measures HA 09 and HA 10, and because they need the most water exactly when we have the least. And the gazelle's carotid rete and the tenrec's summer dormancy, because they are internal physiology and behaviour, and a wall has neither. The criterion throughout: it has to be passive, survive frost and UV for twenty years, and live in a surface.
