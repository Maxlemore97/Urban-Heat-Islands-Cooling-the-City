#!/usr/bin/env python3
"""
Build weather.csv for the wall model from City of Zurich open data.

    python3 fetch_weather.py

Two sources, deliberately split:

  AIR TEMPERATURE  Stadtklima Zürich, meteoblue network, 15-minute means.
                   93 stations inside the city, so the driving temperature is
                   measured a few hundred metres from the building instead of
                   interpolated from an airport.
                   data.stadt-zuerich.ch/dataset/ugz_stadtklima_zuerich_temperaturmessungen_messnetz_meteoblue

  GLOBAL RADIATION UGZ hourly meteo data, station Zch_Stampfenbachstrasse —
                   the only one of the four that carries a pyranometer.
                   data.stadt-zuerich.ch/dataset/ugz_meteodaten_stundenmittelwerte

That split is not a compromise, it is the physics: radiation over a city of this
size is close to uniform, air temperature is not. The city measures temperature
at 93 points and radiation at one for exactly that reason.

The downloads are cached in /tmp because the temperature file is ~137 MB.
"""

import io
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

CACHE = Path("/tmp")
OUT   = Path(__file__).parent / "weather.csv"

YEAR    = 2024
STATION = "I11"                 # Röntgenstrasse, Kreis 5, closed perimeter block
RAD_ST  = "Zch_Stampfenbachstrasse"
START   = "2024-08-10"          # hottest five-day stretch of 2024, see below
END     = "2024-08-14"
TZ      = "Europe/Zurich"

BASE = "https://data.stadt-zuerich.ch/dataset"
URL_T   = (f"{BASE}/ugz_stadtklima_zuerich_temperaturmessungen_messnetz_meteoblue/"
           f"download/ugz_stadtklima_zuerich_temperaturmessungen_messnetz_meteoblue_{YEAR}.csv")
URL_MET = f"{BASE}/ugz_meteodaten_stundenmittelwerte/download/ugz_ogd_meteo_h1_{YEAR}.csv"
URL_SITE = (f"{BASE}/ugz_stadtklima_zuerich_messorte_messnetz_meteoblue/"
            f"download/ugz_stadtklima_zuerich_messorte_messnetz_meteoblue.csv")


def cached(url, name):
    p = CACHE / name
    if not p.exists():
        print(f"  laden: {name}")
        urllib.request.urlretrieve(url, p)
    return p


def main():
    print("Open Data Zürich")
    p_t   = cached(URL_T,    f"mb{YEAR}.csv")
    p_met = cached(URL_MET,  f"ugz_meteo{YEAR}.csv")
    p_st  = cached(URL_SITE, "mb_sites.csv")

    # ---------------------------------------------------------- temperature
    lo = pd.Timestamp(START, tz=TZ)
    hi = pd.Timestamp(END,   tz=TZ) + pd.Timedelta(days=1)

    rows = []
    with open(p_t, encoding="utf-8-sig") as f:
        next(f)
        want = f'"{STATION}","T"'
        for line in f:
            if want in line:
                rows.append(line)
    T = pd.read_csv(io.StringIO("".join(rows)),
                    names=["timestamp", "locationID", "parameter", "value", "qc", "rc"])
    T["timestamp"] = pd.to_datetime(T.timestamp, utc=True).dt.tz_convert(TZ)
    T = T[(T.qc == 0)].set_index("timestamp").value.sort_index().loc[lo:hi]

    site = pd.read_csv(p_st, encoding="utf-8-sig").set_index("locationID").loc[STATION]
    print(f"\nTemperatur: Station {STATION} — {site.streetName}, "
          f"{site.latDecimal:.5f} N {site.lonDecimal:.5f} E, {site.masl} m")
    print(f"  {len(T)} Werte, {T.min():.1f} bis {T.max():.1f} °C")

    # ------------------------------------------------------------ radiation
    M = pd.read_csv(p_met, encoding="utf-8-sig")
    M = M[(M.Standort == RAD_ST) & (M.Parameter == "StrGlo")]
    M["Datum"] = pd.to_datetime(M.Datum, utc=True, format="mixed").dt.tz_convert(TZ)
    G = M.set_index("Datum").Wert.sort_index().loc[lo:hi]
    print(f"Strahlung:  {RAD_ST}, {len(G)} Stundenwerte, max {G.max():.0f} W/m²")

    # --------------------------------------------------- common 15-min grid
    grid = pd.date_range(lo, hi, freq="15min", tz=TZ, inclusive="left")
    out = pd.DataFrame(index=grid)
    out["T_air_C"]  = T.reindex(grid).interpolate(limit_direction="both")
    out["GHI_Wm2"]  = G.reindex(grid).interpolate(limit_direction="both").clip(lower=0)
    out.index.name = "timestamp"
    out.round(2).to_csv(OUT)

    print(f"\n{OUT.name}: {len(out)} Zeilen, {START} bis {END}")
    print(f"  Lufttemperatur {out.T_air_C.min():.1f} … {out.T_air_C.max():.1f} °C")
    print(f"  Globalstrahlung bis {out.GHI_Wm2.max():.0f} W/m², "
          f"Tagessumme im Mittel {out.GHI_Wm2.resample('D').sum().mean()*0.25/1000:.1f} kWh/m²")
    print("\nQuellen im Bericht als ugz_stadtklima und ugz_meteo zitieren.")


if __name__ == "__main__":
    main()
