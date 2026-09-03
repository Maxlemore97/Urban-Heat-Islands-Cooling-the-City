# Real data for a Zurich building, and which simulation tool to use

Stand 02.09.2026. Antwort auf drei Fragen: gibt es ein Haus in Zürich, für das wir echte
Messwerte bekommen? Taugt Unity dafür? Und was wäre besser?

**Jede Quelle unten ist verlinkt.** Bibliografie-Einträge zum direkten Einfügen in
`references.bib` stehen am Ende. Wo ich ein Feld nicht verifizieren konnte, steht das dabei
— bitte vor dem Zitieren prüfen.

---

## 1. Die kurzen Antworten

**Gibt es ein Haus mit allen Messwerten?** Ein öffentlich instrumentiertes Einzelgebäude
mit publizierten Messreihen: nein, das existiert nicht. Aber für **jedes** Gebäude in Zürich
lassen sich Geometrie, Baujahr, Einstrahlung pro Fassadenfläche und — der eigentliche Fund —
**gemessene Lufttemperatur aus einem Netz von rund 90 Stationen im Stadtgebiet, im
15-Minuten-Takt seit August 2019** zusammentragen. Was fehlt, ist genau eine Grösse: die
Oberflächentemperatur der Wand. Die kostet ein IR-Thermometer und einen Nachmittag.

**Unity?** Für Zahlen nein, für Bilder ja. Begründung in Abschnitt 4.

**Besser?** Für unsere zwei kritischen Fragen: Python oder eine Tabellenkalkulation, sonst
nichts. Begründung und die Alternativen in Abschnitt 5.

---

## 2. Was öffentlich verfügbar ist

| Quelle | Was sie liefert | Link |
|---|---|---|
| **Stadtklima Zürich — Temperaturmessungen Messnetz meteoblue** | **~90 Stationen im Stadtgebiet, 15-Minuten-Mittelwerte, seit August 2019**, Jahres-CSV plus Gesamtdatensatz als Parquet. Zeitstempel in UTC, Wert = Mittel der vorangegangenen 15 Minuten | [data.stadt-zuerich.ch](https://data.stadt-zuerich.ch/dataset/ugz_stadtklima_zuerich_temperaturmessungen_messnetz_meteoblue) · [opendata.swiss](https://opendata.swiss/de/dataset/stadtklima-zurich-bereinigte-temperaturmessungen-messnetz-meteoblue) |
| **Standorte der Messstationen** | Koordinaten in WGS84 und CH1903+, Stationsname, Höhe ü. M. | [data.stadt-zuerich.ch](https://data.stadt-zuerich.ch/dataset/ugz_stadtklima_zuerich_messorte_messnetz_meteoblue) |
| **Starter-Code der Stadt** | fertige R-Markdown-Beispiele, wie man genau diese Datensätze einliest | [github.com/opendatazurich/starter-code](https://github.com/opendatazurich/starter-code) |
| **sonnenfassade.ch** | Einstrahlung und Solarpotenzial **pro Fassadenfläche, gebäudescharf**; berechnet aus MeteoSchweiz-Strahlungsdaten und dem 3D-Gebäudemodell von swisstopo. Rund 50 % des Gebäudebestands abgedeckt, Schwerpunkt Zentral- und Nordostschweiz | [sonnenfassade.ch](https://www.sonnenfassade.ch/) · [Datensatz auf opendata.swiss](https://opendata.swiss/de/dataset/eignung-von-hausfassaden-fur-die-nutzung-von-sonnenenergie) |
| **sonnendach.ch** | dasselbe für Dachflächen | [sonnendach.ch](https://www.sonnendach.ch/) |
| **Klimadaten Stadt Zürich (Geodatensatz)** | Klimaanalysekarten als Shapefile, WFS, WMS, WMTS; CH1903+/LV95 | [data.stadt-zuerich.ch](https://data.stadt-zuerich.ch/dataset/geo_klimadaten) · [Download](https://www.stadt-zuerich.ch/geodaten/download/Klimadaten) |
| **Klimakarten Kanton Zürich** | Klimaanalyse auf Kantonsebene | [zh.ch](https://www.zh.ch/de/umwelt-tiere/klima/klimakarte-daten.html) |
| **Luftbild- und Höhenprodukte Kanton Zürich** | Orthofotos und Höhenmodelle als Open Government Data | [zh.ch](https://www.zh.ch/de/planen-bauen/geoinformation/luftbild-und-hoehenprodukte.html) |
| **Eidg. Gebäude- und Wohnungsregister (GWR)** | Adresse, Koordinaten, **Baujahr, Geschosszahl**, Gebäudeart. Daten der Stufe A sind öffentlich | [housing-stat.ch](https://www.housing-stat.ch/de/madd/public.html) · [gwr.admin.ch](https://www.gwr.admin.ch/de/home.html) · [Gebäudestatus auf opendata.swiss](https://opendata.swiss/de/dataset/eidg-gebaude-und-wohnungsregister-gebaudestatus) |
| **MeteoSchweiz Stundendaten** | Globalstrahlung, Lufttemperatur, Wind, seit 1992 | [opendata.swiss](https://opendata.swiss/de/dataset/stundlich-aktualisierte-meteodaten-seit-1992) |
| **Landsat 8/9 Thermalband** | **gemessene** Oberflächentemperatur, ca. 100 m Auflösung | USGS, siehe `usgs_landsat` in unserer Bibliografie |

### Der Fund, der das Vorgehen ändert

Das **meteoblue-Messnetz** ist der Grund, warum diese Idee funktioniert. Rund 90 Stationen
im Stadtgebiet, viertelstündlich, seit 2019 — das heisst, für praktisch jedes Gebäude in
Zürich gibt es eine **gemessene Lufttemperatur in wenigen hundert Metern Entfernung**, und
nicht nur den Flughafenwert. Für einen Vergleich Ist-Zustand gegen Konzept ist das der
entscheidende Eingangswert: die Randbedingung ist gemessen, nicht angenommen.

### Zwei Fallstricke bei den Daten

**sonnenfassade.ch ist für Photovoltaik gebaut.** Die Kennzahl, die die Anwendung
prominent zeigt, ist ein PV-Ertrag in kWh pro Jahr, und dieser Ertrag hängt an einer
Modulwirkungsgrad-Annahme, die per 1. Januar 2023 von 17 % auf 20 % geändert wurde. Wir
brauchen die **Einstrahlung**, nicht den Ertrag — beim Datenbezug also die Strahlungsgrösse
ziehen und die Annahme nennen.

**Die Abdeckung ist nicht vollständig.** Rund die Hälfte des Schweizer Gebäudebestands ist
auf sonnenfassade.ch erfasst, Schwerpunkt Zentral- und Nordostschweiz. Zürich liegt in
diesem Schwerpunkt, aber die Abdeckung für die konkrete Adresse muss geprüft werden, bevor
das Gebäude gewählt wird.

## 3. Was es nicht gibt — und wie wir es ersetzen

**Es gibt keine öffentliche Thermografie von Zürcher Fassaden.** Die Suche liefert
ausschliesslich kommerzielle Anbieter für Gebäudethermografie an Privathäusern. Solche
Aufnahmen entstehen ausserdem **im Winter und nachts**, bei mindestens 15 K
Innen-Aussen-Differenz — sie zeigen Wärmeverluste von innen nach aussen und damit genau das
Gegenteil unseres Sommerproblems. Selbst wenn wir eine Aufnahme bekämen, wäre sie für unsere
Frage unbrauchbar.

Damit bleibt die Wandtemperatur die eine Grösse, die wir selbst messen müssen:

- **IR-Thermometer**, Gerät ab etwa 30 Franken. Messreihe an derselben Fassade, besonnter
  und beschatteter Teil, um 14:00 und um 22:00. Das gibt einen realen Tagesgang und eine
  reale Hell-Dunkel-Differenz.
- **Den angenommenen Emissionsgrad protokollieren.** Die meisten Geräte stehen fest auf
  0.95; für Putz ist das brauchbar, für eine metallische oder glänzende Fläche falsch. Ohne
  diese Angabe ist die Messung nicht nachvollziehbar.
- Die Vorlesung nennt „a simple experiment" ausdrücklich als zulässigen Engineering Check.

## 4. Welches Gebäude — und ein Auswahlkriterium, das viel spart

Nicht irgendeines im Modellierungsgebiet 03, sondern:

1. In der **Klimaanalysekarte** eine Strasse der geschlossenen Randbebauung mit hoher
   Wärmebelastung suchen.
2. Dort ein Gebäude wählen, das **möglichst nahe an einer meteoblue-Station** steht — die
   Standortliste ist verlinkt. Dann ist die antreibende Lufttemperatur real gemessen, wenige
   hundert Meter entfernt, statt aus einer entfernten Station interpoliert. **Das ist das
   wichtigste Auswahlkriterium**, und es kostet nichts ausser einem Blick auf zwei Karten.
3. Abdeckung auf **sonnenfassade.ch** für diese Adresse prüfen.
4. **Baujahr und Geschosszahl aus dem GWR** ziehen.
5. Hingehen, messen, fotografieren.

Damit ist zugleich der offene `\todo` in §2 erledigt, ein konkretes Gebäude zu benennen —
und der Bericht bekommt seine ersten eigenen Fotos.

---

## 5. Unity

**Für Zahlen: nein.** Unity ist eine Spiele-Engine. Ihr Beleuchtungsmodell ist auf
wahrnehmungsmässige Plausibilität ausgelegt, nicht auf eine Energiebilanz. Es fehlen
sämtliche Grössen, um die es bei uns geht:

- keine **Wärmeleitung** und keine Speichermasse im Bauteil,
- kein **konvektiver Übergangskoeffizient** $h_c$,
- kein **langwelliger Strahlungsaustausch** mit einem Himmel effektiver Temperatur — und
  genau der trägt unser Nachtfenster,
- keine **latente Wärme**, also kein Verdunstungspfad,
- die gerenderte Helligkeit ist nicht die absorbierte Strahlungsleistung im Solarspektrum.

Man könnte in Unity HDRP mit physikalisch basierter Beleuchtung die *Einstrahlung* auf
Flächen annähern — aber genau das liefert sonnenfassade.ch bereits, gerechnet aus
MeteoSchweiz-Daten und dem swisstopo-Gebäudemodell, und es beantwortet trotzdem keine
thermische Frage. Wer den Wärmelöser ohnehin selbst schreiben muss, schreibt ihn besser dort,
wo man ihn plotten und prüfen kann.

**Für Bilder: ja, und das ist kein Trostpreis.** Der Bericht hat null Abbildungen, und die
Rubrik bewertet, ob Figuren gut integriert und lesbar sind. Ein begehbarer Strassenraum mit
dem entfalteten Schirm, aus zwei Tageszeiten, ist eine gute Abbildung — und wenn jemand im
Team Unity ohnehin beherrscht, ist das ein realer Beitrag. Nur muss die Bildunterschrift
sagen, dass es eine **Visualisierung** ist und keine Simulation.

---

## 6. Simulationssoftware, sortiert nach der Frage, die sie beantwortet

| Frage | Werkzeug | Aufwand | Referenz |
|---|---|---|---|
| Oberflächentemperatur um 14:00, Ist gegen Konzept | **Energiebilanz von Hand**, Gl. `eq:energybalance`, Python oder Tabelle | Stunden | im Bericht bereits hergeleitet |
| Nächtliche Abgabe, Reset über fünf Tage | **transientes 1-D-Modell** des Aufbaus, Python | 1–2 Tage | Standardverfahren, kein eigenes Zitat nötig |
| Effektive Himmelstemperatur für den Strahlungsterm | **Korrelation**, nicht simulieren | Minuten | Swinbank (1963); Berdahl & Martin (1984) |
| Ganzes Gebäude, Jahressimulation | **EnergyPlus**, meist über OpenStudio oder Ladybug/Honeybee in Rhino Grasshopper | Wochen zum Lernen | Crawley et al. (2001); Roudsari & Pak (2013) |
| PET auf 2 m in der Strassenschlucht | **ENVI-met** | Wochen | Bruse & Fleer (1998) |
| Quartier, städtische Wärmeinsel | **CitySim** (EPFL) oder Dragonfly mit dem Urban Weather Generator | Wochen | Robinson et al. (2009); Bueno et al. (2013) |
| Gemessene Oberflächentemperatur des Quartiers | **Landsat 8/9 Level-2** | 1 Tag, wenn bekannt | USGS |

### Empfehlung

**Python für beide Checks, sonst nichts.** Die zwei kritischen Fragen aus `auftrag_3.md` —
reicht der Auftrieb, reicht das Wasser — sind Rechnungen von unter hundert Zeilen. Das
transiente 1-D-Modell für die Reset-Bedingung ist die einzige Erweiterung, die sich lohnt,
und es ist die einzige Rechnung, die die Fünf-Tage-Frage überhaupt beantworten kann.

**ENVI-met nicht.** Das ist der Weg, auf dem GEO-NET die Zahlen erzeugt hat, die in der
Fachplanung stehen — wir übernehmen deren Ergebnis für die Fussgängerebene, statt es in
einer Woche schlecht nachzubauen.

**Und das Argument, das die Werkzeugwahl eigentlich entscheidet:** die Rubrik verlangt ein
bis zwei Engineering Checks mit einer quantitativen Abschätzung. **Eine sauber
durchgeführte, gegen eine eigene Messung geprüfte Handrechnung schneidet besser ab als eine
grosse Simulation, die niemand verteidigen kann.** Ein schwer zu bedienendes Werkzeug
schlecht einzusetzen ist ein Risiko für die Note, kein Gewinn.

---

## 7. Bibliografie-Einträge zum Einfügen

```bibtex
@misc{ugz_stadtklima,
  author       = {{Umwelt- und Gesundheitsschutz Z\"urich}},
  title        = {Stadtklima Z\"urich --- bereinigte Temperaturmessungen
                  Messnetz meteoblue},
  howpublished = {Open Data Z\"urich},
  url          = {https://data.stadt-zuerich.ch/dataset/ugz_stadtklima_zuerich_temperaturmessungen_messnetz_meteoblue},
  urldate      = {2026-09-02},
  note         = {Ca. 90 Stationen im Stadtgebiet, 15-Minuten-Mittelwerte seit
                  August 2019; Zeitangaben in UTC. Stationsstandorte im
                  Datensatz \texttt{ugz\_stadtklima\_zuerich\_messorte\_messnetz\_meteoblue}}
}

@misc{sonnenfassade,
  author       = {{Bundesamt f\"ur Energie}},
  title        = {sonnenfassade.ch --- Eignung von Hausfassaden f\"ur die
                  Nutzung von Sonnenenergie},
  url          = {https://www.sonnenfassade.ch/},
  urldate      = {2026-09-02},
  note         = {Berechnet aus Strahlungsdaten der MeteoSchweiz und dem
                  3D-Geb\"audemodell von swisstopo. Datensatz auf
                  opendata.swiss. \todo{Deckung f\"ur die gew\"ahlte Adresse
                  pr\"ufen; Einstrahlung beziehen, nicht PV-Ertrag}}
}

@misc{gwr,
  author       = {{Bundesamt f\"ur Statistik}},
  title        = {Eidgen\"ossisches Geb\"aude- und Wohnungsregister (GWR)},
  url          = {https://www.housing-stat.ch/de/madd/public.html},
  urldate      = {2026-09-02},
  note         = {Adresse, Koordinaten, Baujahr, Geschosszahl; Daten der
                  Stufe A \"offentlich}
}

@article{swinbank1963,
  author  = {Swinbank, W. C.},
  title   = {Long-wave radiation from clear skies},
  journal = {Quarterly Journal of the Royal Meteorological Society},
  year    = {1963},
  note    = {\todo{Band, Heft und Seiten pr\"ufen (89(381), 339--348)}}
}

@article{berdahl1984,
  author  = {Berdahl, Paul and Martin, Marlo},
  title   = {Emissivity of clear skies},
  journal = {Solar Energy},
  year    = {1984},
  note    = {\todo{Band und Seiten pr\"ufen}}
}

@article{crawley2001,
  author  = {Crawley, Drury B. and others},
  title   = {{EnergyPlus}: creating a new-generation building energy
             simulation program},
  journal = {Energy and Buildings},
  year    = {2001},
  note    = {\todo{vollst\"andige Autorenliste, Band und Seiten erg\"anzen}}
}

@article{bruse1998,
  author  = {Bruse, Michael and Fleer, Heribert},
  title   = {Simulating surface--plant--air interactions inside urban
             environments with a three dimensional numerical model},
  journal = {Environmental Modelling \& Software},
  year    = {1998},
  note    = {Referenzpublikation zu ENVI-met.
             \todo{Band und Seiten pr\"ufen}}
}

@inproceedings{robinson2009,
  author    = {Robinson, Darren and others},
  title     = {{CitySim}: Comprehensive micro-simulation of resource flows
               for sustainable urban planning},
  booktitle = {Proceedings of Building Simulation (IBPSA)},
  year      = {2009},
  note      = {EPFL. \todo{Autorenliste und Seiten erg\"anzen}}
}

@article{bueno2013,
  author  = {Bueno, Bruno and Norford, Leslie and Hidalgo, Julia and
             Pigeon, Gr\'egoire},
  title   = {The urban weather generator},
  journal = {Journal of Building Performance Simulation},
  year    = {2013},
  note    = {\todo{Band und Seiten pr\"ufen}}
}

@inproceedings{roudsari2013,
  author    = {Roudsari, Mostapha Sadeghipour and Pak, Michelle},
  title     = {Ladybug: a parametric environmental plugin for {Grasshopper}
               to help designers create an environmentally-conscious design},
  booktitle = {Proceedings of Building Simulation (IBPSA)},
  year      = {2013},
  note      = {\todo{Seiten erg\"anzen}}
}
```

**Zu allen Einträgen mit `\todo`:** ich habe Titel, Autoren und Jahr, aber nicht in jedem
Fall Band und Seiten verifizieren können. Vor dem Zitieren nachschlagen — eine falsche
Seitenzahl fällt in Kriterium 6 auf.

## 8. Angebot

Das transiente 1-D-Modell kann ich schreiben: explizites Differenzenverfahren über den
Wandaufbau, angetrieben mit den meteoblue-Stundenwerten und der Einstrahlung aus
sonnenfassade, mit dem Strahlungsterm gegen eine Himmelstemperatur nach Swinbank. Ausgabe
wären Oberflächentemperatur und nächtliche Abgabe über fünf aufeinanderfolgende Tage, für
Ist-Zustand und Konzept. Sagt Bescheid, dann liegt es im `Output`-Ordner.
