# Auftrag 3 — Creating & Evaluating: Vorschläge

Stand 02.09.2026. Grundlage: `Notes/day3/01_creating_evaluating.md` (44 Folien),
die Abstraktionen aus `../Report_LaTeX/sections/03_bioinspired_design.tex` §3.1.

**Alles hier sind Vorschläge, keine Entscheide.** Jeder Punkt hat eine Empfehlung und
mindestens eine Alternative, damit ihr annehmen, ändern oder verwerfen könnt. Was das Team
beschliesst, geht danach in §3.2 und §3.3 — dort steht aktuell nur das Gerüst.

Die Reihenfolge folgt der Pipeline von Folie 13: **Crazy 8s → Matrix → 2 Konzepte →
Canvas → kritische Fragen → Checks → Bewertung → V2.**

---

## 1. Crazy 8s — Vorschlag für die acht Ideen

Regel von Folie 18: **den Mechanismus variieren, nicht die Form.** Die acht unten stammen
alle aus *unseren* Abstraktionen, nicht aus dem Vorlesungsbeispiel — das ist wichtig, weil
vier der acht Ideen des Dozenten (Nachtspülung, Verdunstungseinlass, Speichermasse,
Verschattungshaut) zufällig unsere Funktionen treffen. Wenn unsere Liste so aussieht wie
seine, haben wir abgeschrieben.

| # | Idee | Mechanismus | Aus welchem Modell |
|---|---|---|---|
| 1 | **Hinterlüftete Reflexhaut** | Reflexion plus entkoppelnder Luftspalt, keine beweglichen Teile | Wüstenschnecke |
| 2 | **NIR-selektive Farbfläche** | sichtbare Farbe bleibt, nahes Infrarot wird zurückgeworfen | Morpho |
| 3 | **Rippenprofil** | Selbstverschattung, grössere Abstrahlfläche, Auftriebsströmung in den Tälern | Kaktus |
| 4 | **Millimeter-Textur** | Grenzschicht aufbrechen, damit bewegte Luft die Fläche erreicht | Elefantenhärchen |
| 5 | **Parapet-Radiator mit Schwerkraftkreislauf** | Wärme dorthin transportieren, wo der Himmel sichtbar ist | Hasenohr + Elefanten-Hotspots |
| 6 | **Verdunstungsmatte unter poröser Decke** | Wasser dosieren, indem die nasse Schicht abgedeckt wird | Kamel-Bilayer |
| 7 | **Porenfeld mit Schwellenstreuung** | viele kleine Öffnungen, die lastabhängig aufgehen | Stomata + Bienen |
| 8 | **Selbstentfaltendes Lamellenfeld** | Bimetall- oder Quellschicht-Aktuator, kein Motor | Kiefernzapfen |

**Vorschlag zum Vorgehen:** die acht in 8 Minuten skizzieren lassen (Folie 42), *danach*
zwei bis drei Elemente einkreisen. Nicht währenddessen bewerten.

---

## 2. Morphologische Matrix — Vorschlag

Fünf Zeilen, gefiltert nach dem Kriterium von Folie 22: nur Funktionen, bei denen
alternative Prinzipien zu wirklich anderen Konzepten führen. F0 raus (Hauptfunktion), F10
und F11 raus (Anforderung bzw. Engineering Check), F12 nur bei Bedarf.

| Funktion | Option A | Option B | Option C |
|---|---|---|---|
| **F1, F5** Eintrag senken | NIR-selektive Strukturfarbe | Rippengeometrie | entfaltbare Verschattung |
| **F2, F3** Wärme abführen | Breitbandemitter mit gutem Himmelsblick | Grenzschicht-Textur | Schwerkraftkreislauf zum Parapet-Radiator |
| **F4** Speichern | Masse im Aufbau | Latentspeicher | kein Speicher, nur Entkopplung |
| **F6–F8** Wasser | Saugschicht unter dampfdurchlässiger Decke | Docht mit lastgesteuerter Abgabe | kein Wasserpfad |
| **F9** Last koppeln | Schaltmaterial, viele Einheiten, gestreute Schwellen | lastgetriebenes Ventil | Bilayer, der sich mit Wärme entfaltet |

Diese Matrix steht bereits als `tab:morph` im Bericht.

### Drei Kombinationen, die physikalisch zusammenpassen

| | **K1 · Radiatorfassade** | **K2 · Atmende Haut** | **K3 · Entfaltender Schirm** |
|---|---|---|---|
| F1/F5 | NIR-selektive Strukturfarbe | helles Strukturweiss + flache Rippen | helle Lamellen |
| F2/F3 | **Schwerkraftkreislauf zum Parapet** | Grenzschicht-Textur | Rückzug bei Abkühlung gibt den Himmel frei |
| F4 | kleiner Puffer im Fluid | Masse der feuchten Schicht | keiner |
| F6–F8 | keiner | **Saugschicht unter poröser Decke** | keiner |
| F9 | **Auftrieb ∝ ΔT** | **Dampfdruck ∝ T** plus Porenventil | Bilayer mit Schwellenstreuung |

---

## 3. Der wichtigste Vorschlag: K1 und K2 als Konzept A und B

**Begründung.** Die Vorgabe verlangt zwei **technisch verschiedene** Konzepte. K1 und K2
sind maximal verschieden: trockener Fluidtransport gegen nassen Phasenwechsel. Beide wirken
im Nachtfenster, beide haben eine Rechnung, die in einer Woche machbar ist, und beide
erfüllen die harten Constraints.

**Und der Punkt, der mir beim Durchrechnen aufgefallen ist:** bei beiden ist **F9
kontinuierlich, ohne jede Schwelle.**

- Beim Thermosiphon wächst der Auftriebsdruck **linear mit der Temperaturdifferenz** — der
  Kreislauf zirkuliert stärker, je heisser die Fassade ist. Kein Regler, kein Schaltpunkt.
- Bei der Verdunstung wächst der Sättigungsdampfdruck **überproportional mit der
  Temperatur** — genau der steile Gradient, den §2 als den steilsten identifiziert hat.

Damit löst sich die Schwellendebatte aus `auftrag_2.md` auf: **die zwei besten Konzepte
brauchen das Bienen-Prinzip gar nicht**, weil ihre Lastkopplung physikalisch ohnehin
stetig ist. Das Bienen-Prinzip bleibt die Antwort für die *schaltenden* Optionen — die
thermochrome Beschichtung und das Lamellenfeld — und wird damit vom Rettungsanker zum
Argument bei der Abwahl.

**Die ehrliche Gegenrede für K3.** Der entfaltende Schirm ist die einzige Option, die
Fussgängern direkt die Sonne nimmt und damit KPI 4 unmittelbar trifft, und er ist die
wörtlichste Antwort auf die Designfrage. Ich schlage ihn trotzdem nicht als Konzept B vor,
weil seine kritische Frage — bei welcher Windgeschwindigkeit er sich einziehen muss und was
ihn einzieht — in einer Woche nicht glaubwürdig zu beantworten ist. **Vorschlag:** K3 als
dritte Kombination dokumentieren, nicht ausarbeiten, und in §5 als das nennen, was man als
Nächstes entwickeln würde.

---

## 4. Engineering Canvas — Vorschlag für beide Konzepte

### Konzept A · Radiatorfassade

| Feld | Vorschlag |
|---|---|
| Funktion | F0 über F2/F3: Wärme von der Canyon-Fassade abführen und dort abgeben, wo der Himmel sichtbar ist |
| Biologischer Mechanismus | Hase: Vasodilatation regelt den Blutstrom zu einer dünnen, gut exponierten Abstrahlfläche. Elefant: nur ein Teil der Haut ist aktiv |
| Abstrahiertes Prinzip | Regeln über den **Transport** zu einer Abstrahlfläche, und die Fläche dort platzieren, wo die Bedingungen am besten sind |
| Technisches Prinzip | Geschlossener, pumpenloser Kreislauf; Auftrieb durch Dichteunterschied treibt die Zirkulation |
| Architektur | Absorberfläche auf der besonnten Fassade · Steigleitung · Finnenradiator auf Attikahöhe · Rücklauf · Ausdehnungsgefäss |
| Ein-/Ausgänge | Ein: absorbierte Strahlung an der Fassade. Aus: langwellige Abstrahlung am Radiator, vor allem nachts |
| Anforderungen/KPIs | KPI 1 (Gradient), KPI 5 (Nachtleistung), KPI 4 (PET), Constraint: keine Hilfsenergie |
| Annahmen | Höhendifferenz ≥ 10 m verfügbar · Sky View Factor am Parapet deutlich besser als auf 2 m Höhe · Kreislauf frostsicher ausführbar |
| Unsicherheiten | Reicht der Auftrieb gegen den Rohrwiderstand? Frost. Eingriff in eine womöglich geschützte Fassade |
| Nächster Check | Auftriebshöhe gegen erforderlichen Massenstrom — siehe Abschnitt 5 |

### Konzept B · Atmende Haut

| Feld | Vorschlag |
|---|---|
| Funktion | F0 über F6–F8: gespeichertes Regenwasser dosiert verdunsten und damit die Luft auf Fussgängerhöhe kühlen |
| Biologischer Mechanismus | Blatt: Schliesszellen öffnen die Pore lastabhängig, Verdunstung selbst zieht das Wasser. Kamel: Isolation **über** der nassen Schicht |
| Abstrahiertes Prinzip | Regelung in die Öffnung legen; Last zuerst senken, dann wenig Wasser auf den Rest — und die nasse Schicht abdecken |
| Technisches Prinzip | Saugfähige, regengeladene Schicht unter einer dampfdurchlässigen, wärmedämmenden Decke |
| Architektur | Poröse Deckschicht · Saugschicht · Regenwasserzuführung von der Dachfläche · Sperrschicht zum Bestand |
| Ein-/Ausgänge | Ein: Regen vor der Hitzewelle, Strahlung während. Aus: Wasserdampf auf Fussgängerhöhe |
| Anforderungen/KPIs | KPI 6 (kein Trinkwasser, ≥ 5 Tage Autonomie), KPI 3, KPI 4 |
| Annahmen | Speichervolumen im Aufbau unterzubringen · Regen vor der Hitzewelle · Bestand bleibt trocken |
| Unsicherheiten | Frost in der nassen Schicht · Algenwachstum · Wasser reicht nicht bis Tag fünf |
| Nächster Check | Wasserbilanz — siehe Abschnitt 5 |

---

## 5. Zwei Engineering Checks, die in einer Woche machbar sind

Formate nach Folie 32: **Frage → Annahme → Methode → Ergebnis → Konsequenz**, bei Rechnungen
**Formel · Annahmen · Einheiten · Ergebnis · Bedeutung**.

Die Zahlen unten sind **Grössenordnungs-Skizzen von mir, damit ihr seht, ob sich der Check
lohnt** — nicht das Ergebnis. Rechnet sie mit euren eigenen Annahmen nach.

### Check 1 — Reicht der Auftrieb? (Konzept A)

Treibender Druck im Schwerkraftkreislauf:

$$\Delta p = \rho \, g \, \beta \, \Delta T \, H$$

mit ρ ≈ 1000 kg/m³ (Wasser), g = 9.81 m/s², β ≈ 2·10⁻⁴ K⁻¹ (Volumenausdehnung),
ΔT = Temperaturdifferenz zwischen Steig- und Fallstrang, H = Höhendifferenz.

Für H = 12 m (vier Geschosse) und ΔT = 10 K ergibt das **rund 235 Pa**. Die Anschlussfrage
ist, welchen Massenstrom dieser Druck gegen den Rohrwiderstand treibt und welche
Wärmeleistung daraus folgt:

$$\dot{Q} = \dot{m} \, c_p \, \Delta T$$

**Was der Check entscheidet:** die Fassade nimmt in der Lastphase grob 400–500 W/m² auf.
Wenn der Kreislauf davon nur wenige Prozent transportiert, ist Konzept A ein hübsches Bild
ohne Wirkung. Kommt er in den zweistelligen Prozentbereich, trägt es.

**Empfehlung:** zuerst H und ΔT aus dem Referenzgebäude bestimmen (fünf Geschosse plus
Dachaufbau, §2), dann den Rohrdurchmesser so wählen, dass der Widerstand nicht dominiert —
und genau diesen Zusammenhang als Ergebnis berichten, nicht eine Einzelzahl.

### Check 2 — Reicht das Wasser fünf Tage? (Konzept B)

Latente Verdampfungswärme 2.45 MJ/kg. Für eine gewünschte Kühlleistung *X* über das
Lastfenster von 7 h:

$$m_{\text{Wasser}} = \frac{X \cdot t}{h_{fg}}$$

Für X = 100 W/m² und t = 7 h = 25 200 s: 2.52 MJ/m² → **rund 1.0 l/m² und Tag**, über fünf
Tage **rund 5 l/m²**.

Gegenprobe zum Bauteil: eine 20 mm starke Saugschicht mit 30 % nutzbarem Porenanteil fasst
6 l/m². **Das passt** — und genau deshalb lohnt sich der Check: die Grössenordnung sagt,
dass Konzept B an der Speichermenge *nicht* scheitert, sondern an der Dosierung, am Frost
und an der Frage, ob vor der Hitzewelle überhaupt Regen fällt.

**Empfehlung:** dieselbe Rechnung zusätzlich für X = 50 und X = 200 W/m² durchziehen und
als Kurve berichten. Eine Bandbreite ist ehrlicher als ein Punkt, und sie zeigt, wo die
Grenze liegt.

### Optionaler dritter Check — die Reset-Bedingung

Für beide Konzepte: driftet der Zustand um 06:00 über fünf Tage nach oben? Das ist die
Bedingung aus §2, es ist der Seestern-Mechanismus und sein Versagensmodus, und es ist die
einzige Grösse, die ein Konzept aushebelt, das an Tag eins gut aussieht.

---

## 6. Idee aus dem Team: zwei Gebäude vergleichen

**Der Vorschlag.** Ein real existierendes Gebäude als Referenz nehmen und ihm ein
theoretisches gegenüberstellen, das wir simulieren — also nicht nur eine Zahl für unser
Konzept ausrechnen, sondern eine **Differenz** gegen einen dokumentierten Ausgangszustand.

Das ist der Rahmen, in dem die beiden Checks aus Abschnitt 5 erst aussagekräftig werden.
Eine absolute Zahl wie „Oberflächentemperatur 42 °C" sagt für sich genommen nichts; „14 K
kühler als dieselbe Wand ohne Aufbau, gleiches Wetter, gleicher Tag" ist ein Ergebnis.

### 6.1 Eine Schärfung: dasselbe Gebäude zweimal, nicht zwei Gebäude

Zwei *verschiedene* Gebäude zu vergleichen wäre verführerisch, aber methodisch schwach:
Orientierung, Strassenbreite, Höhe, Speichermasse und Baujahr unterscheiden sich mit, und
jede gemessene Differenz liesse sich auf ein halbes Dutzend Ursachen schieben.

**Stärker ist dasselbe Gebäude, zweimal modelliert** — einmal im Ist-Zustand, einmal mit
unserem Aufbau. Geometrie, Orientierung, Strassenschlucht und Wetterdatensatz sind dann
identisch, und die einzige Variable ist die Hülle. Damit ist die Differenz dem Konzept
**zurechenbar**, und genau das verlangt ein Engineering Check.

Das reale Gebäude bleibt dabei zentral: es liefert Geometrie, Orientierungen, Dachfläche und
Baujahr. Der `\todo` in §2 verlangt ohnehin, ein konkretes Gebäude im
Modellierungsgebiet 03 zu benennen — **diese Idee schliesst ihn.**

### 6.2 Der eigentliche Gewinn: es gibt eine dritte Spalte

Die Fachplanung veröffentlicht für Modellierungsgebiet 03 **bereits modellierte Ergebnisse,
im Ist-Zustand und in einer klimaoptimierten Variante**, und HA 11 ist mit −1.0 K PET
(Fassade), −1.2 K (Dach) und −0.1 K nachts beziffert. Damit wird aus dem Zweiervergleich ein
Dreiervergleich:

| Spalte | Was es ist | Woher die Zahlen kommen |
|---|---|---|
| **Ist-Zustand** | das Gebäude, wie es heute dasteht | unser Modell — und zur Plausibilitätsprüfung die Fachplanung |
| **HA 11** | helle Hülle, die Massnahme des Kunden | **von der Stadt publiziert** |
| **Konzept A / B** | unsere Varianten | unser Modell |

Die mittlere Spalte ist der Grund, warum sich der Aufwand lohnt. KPI 4 verlangt wörtlich,
den Amtsbestand zu schlagen — mit dieser Anordnung ist „schlagen wir HA 11?" keine
Behauptung mehr, sondern eine ablesbare Zeile.

### 6.3 Was wir realistisch simulieren können — und was nicht

| Ebene | Werkzeug | Aufwand | Liefert |
|---|---|---|---|
| Oberfläche, stationär | Energiebilanz Gl. `eq:energybalance`, Tabellenkalkulation oder ein paar Zeilen Python | Stunden | $T_s$ um 14:00 für Ist und Konzept → **KPI 3** |
| Aufbau, transient 1-D | explizites Differenzenverfahren über den Tagesgang, fünf Tage hintereinander | ein bis zwei Tage | nächtliche Abgabe, **Reset-Bedingung**, KPI 5 |
| Strassenraum, Mikroklima | ENVI-met o. ä. | Wochen | PET auf 2 m — **KPI 4** |

**Vorschlag:** die ersten beiden Ebenen selbst rechnen, die dritte **nicht**. Für die
Fussgängerwirkung verankern wir uns an den publizierten Zahlen der Stadt, statt ein
Mikroklimamodell zu simulieren, das wir in einer Woche weder aufsetzen noch validieren
können. Diese Grenze offen zu benennen ist keine Schwäche — Kriterium 4 belohnt ausdrücklich,
dass man sagt, was ein Ergebnis nicht zeigt.

Die transiente 1-D-Rechnung ist dabei die interessantere der beiden: sie ist die **einzige**,
die die Reset-Bedingung über fünf Tage prüfen kann, und damit die einzige, die den
Seestern-Versagensmodus sichtbar macht.

### 6.4 Die methodische Falle, die im Bericht benannt werden muss

Unsere modellierte Zahl neben die modellierte Zahl der Stadt zu stellen heisst, **zwei
verschiedene Modelle** zu vergleichen — anderes Werkzeug, andere Randbedingungen, andere
Auflösung. Sauber vergleichbar ist nur, was **innerhalb unseres eigenen Modells** gerechnet
wurde: Ist-Zustand gegen Konzept, identisch parametriert.

**Vorschlag für die Formulierung:** die Differenz Ist → Konzept als unser Ergebnis
berichten, die Zahlen der Stadt als *Grössenordnungs-Kontrolle* danebenstellen und explizit
schreiben, dass es nicht dieselbe Grösse aus derselben Quelle ist. Wer das offen sagt, sieht
sorgfältig aus; wer es verschweigt und erwischt wird, sieht schlampig aus.

### 6.5 Was dafür beschafft werden muss

1. **Ein konkretes Gebäude** im Modellierungsgebiet 03: Adresse, Fassadenorientierungen,
   Höhe, Strassenbreite, Dachfläche, Baujahr, Wandaufbau soweit erkennbar. Aus dem GIS-Browser
   der Stadt und einer Ortsbegehung — das ist auch das Fotomaterial, das dem Bericht fehlt.
2. **Ein Wetterdatensatz** für die Auslegungs-Hitzewelle: fünf aufeinanderfolgende heisse
   Tage, stündlich, Globalstrahlung und Lufttemperatur. MeteoSwiss, Station benennen.
3. **Die publizierten Werte der Stadt** für dieses Modellierungsgebiet, mit Seitenzahl.

Punkt 1 und 2 sind ohnehin zwei offene `\todo` im Bericht. Die Idee erledigt beide neben dem
eigentlichen Zweck.

### 6.6 Erweiterung: mit echten Daten **validieren**, nicht nur vergleichen

Wenn wir für das reale Gebäude an gemessene Daten kommen, ändert sich die Qualität des
Checks grundlegend. Bisher wäre es ein Vergleich zweier Modellläufe — beide von uns, beide
mit unseren Annahmen. Mit echten Daten wird daraus eine **Validierung**: wir zeigen zuerst,
dass unser Modell den Ist-Zustand trifft, und erst dann rechnen wir die Variante.

Der Unterschied im Bericht ist der zwischen

> „Wir haben \qty{42}{\celsius} Oberflächentemperatur gerechnet."

und

> „Unser Modell reproduziert die gemessene Oberflächentemperatur auf X K genau; mit dem
> Konzept rechnet dasselbe Modell Y K weniger."

Der zweite Satz trägt die Unsicherheit mit, statt sie zu verschweigen. Genau das unterscheidet
in Kriterium 4 die Stufe „technisches Prüfen versucht" von „Annahmen mit geeigneten
Methoden getestet".

#### Welche echten Daten wir realistisch bekommen

| Quelle | Was sie liefert | Massstab | Im Literaturverzeichnis |
|---|---|---|---|
| **MeteoSwiss** | Lufttemperatur, Globalstrahlung, Wind, stündlich, reale Hitzewelle | Station | `meteoswiss` ✓ |
| **sonnendach.ch / sonnenfassade.ch** | modellierte Einstrahlung **pro Dach- und Fassadenfläche, gebäudescharf** | Bauteil | `sonnendach` ✓ |
| **GIS-Browser / Open Data Stadt Zürich** | Gebäudegeometrie, Höhen, Strassenbreite, Klimaanalyse | Quartier | `stadtzuerich_opendata` ✓ |
| **Landsat 8/9 Thermalband (USGS)** | **gemessene** Oberflächentemperatur der Stadt | ca. 100 m | `usgs_landsat` — **liegt ungenutzt in der Bibliografie** |
| **Eigene IR-Messung** | Wandtemperatur an unserem Gebäude, besonnt und beschattet | Fassade | — |

Die letzte Zeile ist die wichtigste und wird am leichtesten übersehen: **ein
Infrarot-Thermometer ist das Einzige, was uns eine echte Zahl für eine echte Wand liefert.**
Gerät für rund 30 Franken, eine Messreihe am besonnten und am beschatteten Teil derselben
Fassade um 14:00 und noch einmal um 22:00 — und wir haben einen realen Tagesgang und eine
reale Differenz zwischen heller und dunkler Fläche. Die Vorlesung nennt „a simple
experiment" ausdrücklich als zulässigen Engineering Check.

#### Die Anordnung

1. Modell für das reale Gebäude aufbauen: Geometrie aus dem GIS, Einstrahlung pro
   Fassadenfläche aus sonnenfassade.ch.
2. Mit MeteoSwiss-Stundenwerten einer **dokumentierten Hitzewelle** antreiben, Station und
   Zeitraum benennen.
3. **Validieren:** modellierte gegen gemessene Oberflächentemperatur — unsere IR-Messung für
   die Wand, das Landsat-Thermalbild für das Quartier.
4. Den Validierungsfehler berichten. Er ist das Ergebnis, nicht die Fussnote.
5. Dasselbe Modell mit der Konzepthülle erneut rechnen.
6. Die Differenz berichten, mit dem Validierungsfehler als Unsicherheitsband.

#### Was dabei ehrlich gesagt werden muss

- **Landsat löst keine Fassade auf.** Rund 100 m Pixel mischen Dächer, Strassen, Bäume und
  Bäume-dazwischen. Es validiert das **Quartier**, nicht die Wand — und das ist trotzdem
  wertvoll, weil unsere KPI 4 ohnehin eine Quartiersgrösse ist.
- **Der Überflug liegt am Vormittag**, nicht um 14:00. Landsat sieht also nicht unsere
  Lastspitze. Das schliesst die Nutzung nicht aus, verbietet aber, die Zahl als
  Spitzentemperatur zu verkaufen.
- **Satelliten-LST ist eine Skin-Temperatur** der gemischten Oberfläche, keine Wandtemperatur.
- **Ein Messtag ist keine Validierung im ingenieurmässigen Sinn**, sondern eine
  Plausibilitätsprüfung. Genau so sollten wir es nennen.
- **Das IR-Thermometer braucht einen Emissionsgrad.** Die meisten Geräte stehen fest auf
  0.95; für Putz ist das brauchbar, für eine metallische oder glänzende Fläche falsch. Der
  angenommene Wert gehört in die Annahmenliste, sonst ist die Messung nicht nachvollziehbar.

#### Empfehlung zum Aufwand

**Die IR-Messung auf jeden Fall** — ein Nachmittag, minimales Risiko, und sie liefert das
einzige Wand-Datum, das wir je haben werden. Sie erledigt zugleich das Fotomaterial, das dem
Bericht fehlt, und den `\todo` in §2, ein konkretes Gebäude zu benennen.

**Landsat nur, wenn jemand im Team das Werkzeug schon kennt.** Eine Szene herunterzuladen,
zu entwolken und in Oberflächentemperatur umzurechnen ist an einem Tag machbar, wenn man es
schon einmal gemacht hat, und ein Zeitfresser, wenn nicht. Falls nicht: die Klimaanalyse der
Stadt liefert die Quartiersebene bereits ausgewertet, und `usgs_landsat` bleibt dann als
Datenquelle unzitiert — was kein Verlust ist, solange wir nicht behaupten, sie benutzt zu
haben.

---

### 6.7 Fokus: Fassade

**Entscheid des Teams:** das System of Interest ist die **Fassade**, nicht die Hülle
allgemein.

Das widerspricht einer Stelle in §2, die aus der Sonnengeometrie hergeleitet ist und heute
das Gegenteil sagt: bei \ang{47.38} Breite trifft der Mittagsstrahl das Flachdach mit
$\sin h \approx 0.91$, die Südfassade nur mit $\cos h \approx 0.41$, das Dach bekommt also
mehr als doppelt so viel — und §2 schliesst daraus, die Hülle *nicht* auf die Fassade zu
beschränken.

**Die Geometrie bleibt richtig, die Schlussfolgerung dreht sich.** Das Dach bekommt mehr
Sonne, aber die Wärme, die ein Dach speichert, wird **nach oben** abgegeben, an einen
Himmel, den das Dach sieht. Die Wärme, die eine Fassade speichert, wird **seitwärts**
abgegeben, in die Schlucht, auf Kopfhöhe der Leute darin. Seit §1 den Aussenraum als den Ort
festlegt, an dem die Wirkung auftreten muss, ist die Fassade die richtige Fläche — nicht
obwohl sie weniger Strahlung bekommt, sondern weil ihre Wärme dorthin geht, wo sie stört.

Zwei Nebeneffekte, die den Entscheid stützen: die Fassade steht **nicht in Konkurrenz zu
Photovoltaik** um die Dachfläche, was unser weicher Constraint verlangt; und ein Systemblick
soll das Projekt laut Tag 1 **fokussierter machen, nicht grösser**.

**Das Dach verschwindet damit nicht, es wechselt die Rolle.** Es ist nicht mehr eine zweite
zu behandelnde Fläche, sondern die **Schnittstelle mit dem guten Himmelsblick** — also genau
das, was Konzept K1 braucht: gesammelt wird an der Fassade, abgegeben am Parapet. Der
Fokusentscheid macht K1 schärfer, statt ihn zu beschädigen.

#### Was das im Bericht ändert

| Stelle | Änderung |
|---|---|
| §2.2 „Where on the envelope?" | Schlussfolgerung umdrehen: Fassade als System of Interest, Dach als Abgabeschnittstelle. Der offene `\todo` dort wird damit beantwortet |
| KPI 4 | Benchmark ist die **Fassadenzahl** von HA 11, also \qty{-1.0}{\kelvin} PET; die Dachzahl \qty{-1.2}{\kelvin} bleibt als Kontext stehen |
| KPI 5 | dito für den Nachtwert |
| §3.2 K1 | unverändert — der Radiator am Parapet ist jetzt ausdrücklich eine Schnittstelle, kein zweites System |
| Bildprompts 17, 21 | zeigen bereits Parapet und Fassade; passen |

Der Rest des Berichts spricht ohnehin von der Fassade im Strassenraum. Die einzige Stelle,
die wirklich widerspricht, ist die Sonnengeometrie-Passage.

---

### 6.8 Empfehlung

Aufnehmen, und zwar als **Rahmen für beide Engineering Checks** aus Abschnitt 5 statt als
dritten Check. Mit der IR-Messung aus 6.6 als Validierungsschritt davor. Die Auftriebsrechnung und die Wasserbilanz bleiben, was sie sind; der
Gebäudevergleich ist die Anordnung, in der ihre Ergebnisse eine Bedeutung bekommen. Im
Bericht gehört er an den Anfang von §3.2 als Beschreibung der Prüfanordnung, nicht in die
Modellliste von §3.1.

---

## 7. Drei kritische Fragen — Vorschlag

Nach Folie 33 nennt eine gute Frage **Grösse, Schwelle und Massstab**.

1. **Ist der Auftrieb in einem 12-m-Kreislauf gross genug, um einen nennenswerten Anteil
   der 400–500 W/m² abzuführen — und übersteht der Kreislauf einen Schweizer Winter?**
2. **Passen 5 l/m² Regenwasser in einen Aufbau, der die Auflast- und Dickenbeschränkung des
   Bestands einhält, und was passiert mit der nassen Schicht bei −10 °C?**
3. **Halten beide Konzepte die Reset-Bedingung über fünf Tage, oder sättigen sie?**

Die Skalenfrage aus Folie 40 ist bewusst nicht dabei: sie betrifft die Modelle
(*Cyphochilus*, Morpho, Flechte, Stomata) und gehört als eigener Absatz in §3.2, nicht in
die kritischen Fragen zum Konzept.

---

## 8. Bewertung — Vorschlag für Gewichte

Die Matrix hat neben den KPIs drei Zeilen, die keine KPIs sind (Machbarkeit,
Transferqualität, Evidenz). Vorschlag für die Gewichtung, zur Diskussion:

| Kriterium | Gewicht | Begründung |
|---|---|---|
| KPI 1 Selbstregelungsgradient | **3** | die definierende Grösse des Projekts |
| KPI 5 Nachtleistung | **3** | die Lücke, die wir bei HA 11 gefunden haben |
| KPI 4 PET auf 2 m | 2 | die Metrik des Kunden |
| KPI 6 Wasserpfad | 2 | harter Constraint dahinter |
| KPI 2, 3, 7 | 1 | wichtig, aber abgeleitet |
| Machbarkeit | 2 | |
| Transferqualität | 2 | wird in der Rubrik separat benotet |
| Evidenz und Unsicherheit | **3** | verhindert, dass geschätzte Zeilen wie gerechnete aussehen |

**Wichtig nach Folie 36:** jede Bewertung braucht eine Begründung durch Rechnung oder
begründete Schätzung. Eine Zeile ohne Beleg bekommt in der Spalte „Evidenz" eine schlechte
Note — auch wenn das Konzept dort gut wäre.

---

## 9. Iteration zu V2 — was vermutlich passiert

Verlangt ist mindestens **eine benannte Schwäche und eine dokumentierte Antwort darauf**.
Die wahrscheinlichste Kette lässt sich heute schon absehen:

- **Wenn Check 1 zu schwach ausfällt**, ist die naheliegende Antwort nicht, Konzept A zu
  verwerfen, sondern die Temperaturdifferenz zu vergrössern — indem der Radiator am Parapet
  eine Verdunstungsschicht aus Konzept B bekommt. Das ist ein **begründeter Hybrid**, und
  die Vorgabe erlaubt ihn ausdrücklich.
- **Wenn Check 2 an der Dosierung scheitert**, kommt das Bienen-Prinzip zurück: viele kleine
  Poren mit gestreuten Öffnungspunkten statt einer gleichmässig verdunstenden Fläche.
- **Wenn die Reset-Bedingung reisst**, ist die Antwort die Redundanz aus `auftrag_2.md`:
  ein zweiter, wasserfreier Abfuhrpfad, der noch arbeitet, wenn der Speicher leer ist.

Alle drei sind Antworten, die aus unseren eigenen Modellen kommen. Das ist der Punkt, den
§3.3 zeigen muss.

---

## 10. Was diese Vorschläge an offenen Entscheiden schliessen

Bezogen auf die neun Entscheide in `auftrag_2.md`:

| Nr. | Entscheid | Vorschlag |
|---|---|---|
| 1 | Welche zwei Konzepte? | **K1 Radiatorfassade und K2 Atmende Haut.** K3 dokumentieren, nicht ausarbeiten |
| 2 | Darf F9 eine Schwelle sein? | **Frage entfällt für A und B** — deren Lastkopplung ist physikalisch stetig. Bleibt relevant für die schaltenden Optionen |
| 3 | Windauslösung beim Segel | **vertagt** mit K3 |
| 4 | Wärmefenster statt Vollfläche? | **ja**, in K1 eingebaut: der Radiator sitzt nur am Parapet |
| 5 | Redundanz als Regel? | **ja**, aber als Antwort in V2 statt als Vorgabe in V1 |
| 6 | Farbe statt Weiss? | **ja**, in beiden Konzepten als NIR-selektive Fläche |
| 7 | Zielbestand gedämmt/ungedämmt? | betrifft nur die thermochrome Option, **entfällt** mit dieser Auswahl |
| 8 | Selbstreinigung chemisch? | **nein** — Flechten-/Lotus-Route, in beiden Konzepten gleich |
| 9 | F9 als Ventil, Material oder Bewegung? | **als Strömung** in K1, **als Ventil** in K2 |

Von neun Entscheiden werden damit sieben beantwortet oder gegenstandslos. Die zwei
verbleibenden — Windauslösung und Redundanz — hängen an Ergebnissen, die wir noch nicht
haben, und das ist der richtige Zeitpunkt, sie offen zu lassen.

---

## 11. Nachfrage: gibt es das Kamel als Pflanze?

Ja — und zwar zweimal, und eine davon steht bereits in unserer Modelltabelle.

### 11.1 Das botanische Kamel: Blatthaare

Das Kamelprinzip ist **Isolation über der verdunstenden Schicht**. Pflanzen bauen genau das
als **Trichome**, also einen dichten Haarfilz über der Blattoberfläche. Er reflektiert einen
Teil der Strahlung, hält eine ruhende Luftschicht fest und senkt damit den Wasserverlust —
während die Stomata darunter weiter transpirieren. Fell über Schweissdrüse, nur botanisch.

**Wir zitieren das bereits:** *Encelia farinosa* steht über Ehleringer 1978 in
`references.bib` und in der Modelltabelle, mit dem Vermerk, dass die Behaarung die
Reflektivität erhöht und **saisonal verstellt** wird. Bisher haben wir sie nur als Beleg für
den saisonalen Wechsel benutzt. Sie ist aber zusätzlich der pflanzliche Beleg für die
Kamel-Schichtung — und ein zweites Modell für dieselbe Aussage ist in §3.1 mehr wert als ein
neues.

Gartenmassstab, dieselbe Struktur: die grau-silbrigen Mittelmeerpflanzen. *Stachys
byzantina*, *Artemisia*, *Salvia officinalis*, *Verbascum*, *Phlomis*, Ölbaum, *Elaeagnus*.
**Das Silber *ist* die Haarschicht** — es ist keine Pigmentfarbe, sondern Streuung an den
Trichomen. Wer eine solche Pflanze anfasst, fasst die Abstraktion an.

Zweites pflanzliches Vorbild, ebenfalls schon in unseren Notizen: die **Moose** (Genius of
Biome S. 53–56) — lebende Schicht über toter Schicht, geschützt von einer ruhenden
Luftgrenzschicht. Auch das ist ein Bilayer mit geschützter Nassschicht.

### 11.2 Und Bepflanzung ums Haus herum?

Hier muss ich bremsen, und zwar mit unseren eigenen Entscheiden:

- Begrünung ist bei der Stadt bereits **HA 09, HA 10 und HA 12** — Bestandsmassnahme, nicht
  Neuheit.
- Unsere Systemgrenze legt Begrünung im Quartiersmassstab ausdrücklich **nach draussen**
  (Tabelle `tab:inout`).
- Und die unbequeme Wahrheit, die wir besser selbst aussprechen: **ein Baum in der
  Strassenschlucht senkt die PET stärker als jede Fassadenmassnahme.** Wenn das Ziel allein
  Fussgängerkomfort wäre, lautete die Antwort „pflanzt Bäume" und nicht „baut eine Fassade".
  Unsere Rechtfertigung steht in §2: wir bearbeiten den Bestand, weil die Stadt dort einen
  Handlungsbedarf hat, den Begrünung nicht deckt — versiegelte, geschützte, nicht
  bepflanzbare Fassadenflächen.

### 11.3 Wo es trotzdem hineingehört: die Schnittstelle

Es gibt eine Verbindung, die unsere eigene Systemanalyse nahelegt und die den Konflikt
auflöst statt ihn zu verwalten.

Unser Wasserpfad sammelt Regen **vor** der Hitzewelle und verbraucht ihn dosiert. Ausserhalb
der Hitzewelle fällt mehr Regen an, als die Saugschicht fasst — und dieser Überschuss läuft
heute in die Kanalisation, also genau in das Parallelsystem, das §2.4 als *verworfene
Kühlreserve* identifiziert hat.

**Vorschlag: der Überschuss geht an die Bepflanzung am Fuss der Fassade.** Damit
konkurrieren die beiden Systeme nicht mehr um Wasser, sondern der eine speist den anderen.
Für uns bleibt die Bepflanzung ausserhalb der Systemgrenze — sie ist eine **Schnittstelle**,
kein Bauteil unseres Konzepts. Genau so gehört sie in den Bericht: ein Absatz in §2.4 bei
den Parallelsystemen, und ein Satz in §5 als das, was ein nächster Schritt verbinden würde.

**Empfehlung:** 11.1 aufnehmen, das kostet zwei Sätze in §3.1 und stärkt ein bestehendes
Modell. 11.2 nicht aufnehmen, aber die unbequeme Wahrheit über Bäume in §5 selbst
aussprechen — wer sie verschweigt und gefragt wird, steht schlechter da. 11.3 als
Schnittstellen-Absatz, nicht als Erweiterung des Konzepts.

---

## 12. Was ich bewusst nicht vorgeschlagen habe

Keine Materialwahl. Kein Hersteller, kein Produkt, keine Schichtdicke ausser der einen
Gegenprobe in Check 2. Der Grund steht auf Folie 28: verlangt ist ein **Konzept**, nicht ein
Prototyp — die Leitfrage lautet *was könnte funktionieren*, nicht *funktioniert dieses
Bauteil*. Eine Materialliste würde Präzision vortäuschen, die wir nicht haben, und genau
davor warnt die Vorlesung mit dem Hinweis, dass Konzeptzeichnungen den Transfer erklären
sollen und nicht beweisen, dass das Konzept funktioniert.
