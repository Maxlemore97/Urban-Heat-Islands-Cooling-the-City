#!/usr/bin/env python3
"""
Transient 1-D wall model — baseline façade against a concept façade,
over the five-day design heat wave of Section 2.

Produces four figures and one animated time-lapse for the presentation.

    python3 wall_model.py

WHAT THIS IS: an explicit finite-difference solution of heat conduction through
a layered wall, with a surface energy balance that carries absorbed short-wave
radiation, long-wave exchange with the sky, and convection to outdoor air.

WHAT THIS IS NOT: a validated model. Until real weather is loaded it runs on a
synthetic drive, and every figure is stamped accordingly. Do not put an unstamped
figure in the report without saying where the weather came from.

To use real data, set USE_REAL_DATA = True and supply:
  weather.csv  with columns  timestamp, T_air_C, G_facade_Wm2
    T_air  — Stadtklima Zürich, meteoblue network, nearest station
             data.stadt-zuerich.ch/dataset/ugz_stadtklima_zuerich_temperaturmessungen_messnetz_meteoblue
    G      — irradiance on the façade surface, sonnenfassade.ch
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.colors import Normalize
from pathlib import Path

OUT = Path(__file__).parent / "wall_model"
OUT.mkdir(exist_ok=True)

# ----------------------------------------------------------------- settings
USE_REAL_DATA = False          # ← flip once weather.csv exists
WEATHER_CSV   = Path(__file__).parent / "weather.csv"

DAYS      = 5                  # the design heat wave, Section 2
DT        = 60.0               # s, time step
T_INDOOR  = 26.0               # °C, assumed and not modelled further
H_OUT     = 12.0               # W/m²K, low wind speed in a street canyon
H_IN      = 8.0                # W/m²K, indoor surface
H_CAVITY  = 25.0               # W/m²K, faces of a ventilated cavity to outdoor air
H_RAD_CAV = 5.0                # W/m²K, linearised radiation across the cavity
SIGMA     = 5.670374419e-8

# Layers, outside → inside: (name, thickness m, k W/mK, rho kg/m³, cp J/kgK, cavity?)
WALL_BASELINE = [
    ("Aussenputz",   0.020, 0.80, 1600,  1000, False),
    ("Mauerwerk",    0.380, 0.60, 1600,   900, False),
    ("Innenputz",    0.015, 0.70, 1400,  1000, False),
]
WALL_CONCEPT = [
    ("Aussenschale", 0.012, 0.35, 1600,  1000, False),
    ("Luftspalt",    0.040, 0.025,  1.2, 1005, True),   # ventilated
    ("Aussenputz",   0.020, 0.80, 1600,  1000, False),
    ("Mauerwerk",    0.380, 0.60, 1600,   900, False),
    ("Innenputz",    0.015, 0.70, 1400,  1000, False),
]

# Optical properties of the outermost surface
OPT_BASELINE = dict(alpha_sol=0.30, eps=0.90)   # city value for an un-greened façade
OPT_CONCEPT  = dict(alpha_sol=0.80, eps=0.90)   # KPI 2 target

TARGET_DX = 0.020              # m, aimed node size


# ------------------------------------------------------------------ weather
def synthetic_weather(days, dt):
    """Placeholder drive. Shape is right, provenance is not. Clearly stamped."""
    t = np.arange(0, days * 86400, dt)
    hour = (t / 3600.0) % 24
    # air temperature: 22 °C before dawn to 35 °C at 15:00 (Section 2: 33-36 °C)
    T_air = 28.5 + 6.5 * np.cos(2 * np.pi * (hour - 15.0) / 24.0)   # Maximum um 15:00
    # irradiance on a vertical façade, peaking early afternoon
    G = np.where((hour > 6) & (hour < 20),
                 450.0 * np.clip(np.sin(np.pi * (hour - 6) / 14.0), 0, None) ** 1.3,
                 0.0)
    return t, T_air, G


def load_weather(path, dt):
    import csv
    ts, Ta, G = [], [], []
    with open(path) as f:
        for row in csv.DictReader(f):
            Ta.append(float(row["T_air_C"])); G.append(float(row["G_facade_Wm2"]))
    Ta, G = np.array(Ta), np.array(G)
    t_src = np.arange(len(Ta)) * (86400 * DAYS / len(Ta))
    t = np.arange(0, DAYS * 86400, dt)
    return t, np.interp(t, t_src, Ta), np.interp(t, t_src, G)


# -------------------------------------------------------------------- model
def build_nodes(layers):
    """Control-volume grid.

    A ventilated cavity is not discretised. Air has almost no heat capacity, so
    an air node would force an impractically small time step and would model a
    ventilated gap badly anyway. Instead the cavity becomes an *interface*: the
    two faces bounding it each exchange convectively with outdoor air, which is
    the standard assumption for a well-ventilated rear-ventilated façade, plus a
    linearised radiative exchange between the two faces. No conduction crosses it.
    """
    dx, k, rc, lid, gaps = [], [], [], [], []
    for i, (_, th, kk, rho, cp, is_cav) in enumerate(layers):
        if is_cav:
            gaps.append(len(dx) - 1)          # cavity sits after the last node built
            continue
        n = max(1, int(round(th / TARGET_DX)))
        for _ in range(n):
            dx.append(th / n); k.append(kk); rc.append(rho * cp); lid.append(i)
    return (np.array(dx), np.array(k), np.array(rc),
            np.array(lid), np.array(gaps, dtype=int))


def sky_temperature(T_air_C):
    """Swinbank (1963), clear sky. T in kelvin."""
    Ta = T_air_C + 273.15
    return 0.0552 * Ta ** 1.5


def simulate(layers, opt, t, T_air, G, dt=DT):
    dx, k, rc, lid, gaps = build_nodes(layers)
    n = len(dx)
    T = np.full(n, 24.0)                       # start of the first hot day

    # inter-node conductance, harmonic mean of the two half-resistances.
    # Zero across a ventilated cavity — nothing conducts through moving air.
    Uint = np.zeros(n - 1)
    for i in range(n - 1):
        Uint[i] = 0.0 if i in gaps else \
            1.0 / (dx[i] / (2 * k[i]) + dx[i + 1] / (2 * k[i + 1]))

    C = rc * dx                                 # J/m²K per node
    steps = len(t)
    Ts   = np.empty(steps)                      # outer surface temperature
    Qout = np.empty(steps)                      # outward release, W/m²
    field = np.empty((steps, n))

    Tsky = sky_temperature(T_air) - 273.15

    for s in range(steps):
        q = np.zeros(n)

        # --- outer surface node
        solar = (1.0 - opt["alpha_sol"]) * G[s]
        lw    = opt["eps"] * SIGMA * ((Tsky[s] + 273.15) ** 4 - (T[0] + 273.15) ** 4)
        conv  = H_OUT * (T_air[s] - T[0])
        q[0] += solar + lw + conv

        # --- the two faces of a ventilated cavity
        for g in gaps:
            q[g]     += H_CAVITY * (T_air[s] - T[g])
            q[g + 1] += H_CAVITY * (T_air[s] - T[g + 1])
            rad = H_RAD_CAV * (T[g] - T[g + 1])
            q[g] -= rad; q[g + 1] += rad

        # --- conduction between nodes
        flux = Uint * (T[:-1] - T[1:])
        q[:-1] -= flux
        q[1:]  += flux

        # --- indoor surface
        q[-1] += H_IN * (T_INDOOR - T[-1])

        Ts[s] = T[0]
        Qout[s] = -(lw + conv)                  # positive = leaving the surface
        field[s] = T
        T = T + dt * q / C

    if not np.all(np.isfinite(field)):
        raise RuntimeError("Loesung divergiert — Zeitschritt DT verkleinern.")
    return dict(Ts=Ts, Qout=Qout, field=field, dx=dx, lid=lid, layers=layers,
                gaps=gaps)


# ------------------------------------------------------------------ figures
STAMP = None if USE_REAL_DATA else \
    "SYNTHETIC WEATHER — shape only, not a result. Replace with meteoblue + sonnenfassade data."

C_BASE, C_CONC, C_AIR = "#AE3B2E", "#15709F", "#86867C"


def stamp(fig):
    if STAMP:
        fig.text(0.5, 0.012, STAMP, ha="center", fontsize=7.5,
                 color="#AE3B2E", style="italic")


def fig_surface(t, T_air, base, conc):
    h = t / 3600.0
    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.plot(h, T_air, color=C_AIR, lw=1.2, label="Aussenluft")
    ax.plot(h, base["Ts"], color=C_BASE, lw=1.8, label="Bestand, $\\alpha_{sol}=0.30$")
    ax.plot(h, conc["Ts"], color=C_CONC, lw=1.8, label="Konzept, $\\alpha_{sol}=0.80$")
    for d in range(DAYS):
        ax.axvspan(d * 24, d * 24 + 6, color="#15709F", alpha=0.05)
    ax.set_xlabel("Stunden ab Beginn der Hitzewelle")
    ax.set_ylabel("Temperatur [°C]")
    ax.set_title("Oberflächentemperatur der Fassade über fünf Tage "
                 "(blau hinterlegt: Nachtfenster 00–06 Uhr)")
    ax.legend(frameon=False); ax.grid(alpha=.25)
    stamp(fig); fig.tight_layout(rect=(0, .03, 1, 1))
    fig.savefig(OUT / "01_oberflaechentemperatur.png", dpi=160); plt.close(fig)


def fig_depthtime(t, base, conc):
    fig, axes = plt.subplots(2, 1, figsize=(11, 6), sharex=True)
    vmin = min(base["field"].min(), conc["field"].min())
    vmax = max(base["field"].max(), conc["field"].max())
    for ax, r, name in zip(axes, (base, conc), ("Bestand", "Konzept")):
        depth = np.cumsum(r["dx"]) - r["dx"] / 2
        im = ax.pcolormesh(t / 3600.0, depth * 1000, r["field"].T,
                           cmap="inferno", vmin=vmin, vmax=vmax, shading="auto")
        ax.invert_yaxis(); ax.set_ylabel(f"{name}\nTiefe [mm]")
        fig.colorbar(im, ax=ax, label="°C", pad=0.01)
    axes[-1].set_xlabel("Stunden ab Beginn der Hitzewelle")
    axes[0].set_title("Wärme im Wandquerschnitt — Eindringen am Tag, Abgabe in der Nacht")
    stamp(fig); fig.tight_layout(rect=(0, .03, 1, 1))
    fig.savefig(OUT / "02_tiefe_zeit.png", dpi=160); plt.close(fig)


def fig_release(t, base, conc):
    h = t / 3600.0
    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.plot(h, base["Qout"], color=C_BASE, lw=1.4, label="Bestand")
    ax.plot(h, conc["Qout"], color=C_CONC, lw=1.4, label="Konzept")
    ax.axhline(0, color="#333", lw=.8)
    for d in range(DAYS):
        ax.axvspan(d * 24, d * 24 + 6, color="#15709F", alpha=0.05)
    ax.set_xlabel("Stunden ab Beginn der Hitzewelle")
    ax.set_ylabel("Abgabe an Luft und Himmel [W/m²]")
    ax.set_title("Wärmeabgabe der Oberfläche — positiv heisst, die Wand gibt ab")
    ax.legend(frameon=False); ax.grid(alpha=.25)
    stamp(fig); fig.tight_layout(rect=(0, .03, 1, 1))
    fig.savefig(OUT / "03_abgabe.png", dpi=160); plt.close(fig)


def fig_reset(t, base, conc):
    """The reset condition of Section 2: does the wall drift upward day by day?"""
    h = t / 3600.0
    fig, ax = plt.subplots(figsize=(8, 4.2))
    for r, c, name in ((base, C_BASE, "Bestand"), (conc, C_CONC, "Konzept")):
        mid = r["field"].shape[1] // 2
        vals = [r["field"][np.argmin(np.abs(h - (d * 24 + 6))), mid] for d in range(DAYS)]
        ax.plot(range(1, DAYS + 1), vals, "o-", color=c, lw=1.8, label=name)
    ax.set_xticks(range(1, DAYS + 1))
    ax.set_xlabel("Tag der Hitzewelle"); ax.set_ylabel("Temperatur Wandmitte um 06:00 [°C]")
    ax.set_title("Reset-Bedingung: driftet der Speicher von Tag zu Tag nach oben?")
    ax.legend(frameon=False); ax.grid(alpha=.25)
    stamp(fig); fig.tight_layout(rect=(0, .04, 1, 1))
    fig.savefig(OUT / "04_reset.png", dpi=160); plt.close(fig)


def animate(t, T_air, base, conc, every_minutes=30, fps=20):
    """The time-lapse: both wall sections side by side, colour = temperature."""
    step = int(every_minutes * 60 / DT)
    idx = np.arange(0, len(t), step)
    vmin = min(base["field"].min(), conc["field"].min())
    vmax = max(base["field"].max(), conc["field"].max())
    norm, cmap = Normalize(vmin, vmax), plt.get_cmap("inferno")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4))
    bars = []
    for ax, r, name in zip(axes, (base, conc), ("Bestand", "Konzept")):
        depth = np.concatenate([[0], np.cumsum(r["dx"])]) * 1000
        b = ax.bar(x=0, height=np.diff(depth), bottom=depth[:-1], width=1.0,
                   align="center", edgecolor="none")
        bars.append(b)
        ax.set_xlim(-.7, .7); ax.set_ylim(depth[-1], 0)
        ax.set_xticks([]); ax.set_ylabel("Tiefe [mm]" if name == "Bestand" else "")
        ax.set_title(name, fontsize=12, fontweight="bold",
                     color=C_BASE if name == "Bestand" else C_CONC)
        # layer boundaries
        for e in np.cumsum([l[1] for l in r["layers"] if not l[5]]) * 1000:
            ax.axhline(e, color="w", lw=1.1)
        for g in r["gaps"]:                    # ventilated cavity
            ax.axhline(depth[g + 1], color="#15709F", lw=2.4)
    fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap),
                 ax=axes, label="Temperatur [°C]", pad=.02, fraction=.05)
    clock = fig.text(.5, .955, "", ha="center", fontsize=13, fontweight="bold")
    sub = fig.text(.5, .915, "", ha="center", fontsize=9.5, color="#4A4B45")
    if STAMP:
        fig.text(.5, .015, STAMP, ha="center", fontsize=7.5, color=C_BASE, style="italic")

    def draw(i):
        s = idx[i]
        for b, r in zip(bars, (base, conc)):
            for rect, temp in zip(b, r["field"][s]):
                rect.set_facecolor(cmap(norm(temp)))
        hh = t[s] / 3600.0
        clock.set_text(f"Tag {int(hh // 24) + 1} · {int(hh % 24):02d}:{int((hh % 1) * 60):02d} Uhr")
        sub.set_text(f"Aussenluft {T_air[s]:.1f} °C   ·   "
                     f"Oberfläche Bestand {base['Ts'][s]:.1f} °C   ·   "
                     f"Konzept {conc['Ts'][s]:.1f} °C")
        return []

    anim = FuncAnimation(fig, draw, frames=len(idx), blit=False)
    anim.save(OUT / "wall_timelapse.gif", writer=PillowWriter(fps=fps))
    plt.close(fig)


# --------------------------------------------------------------------- main
if __name__ == "__main__":
    if USE_REAL_DATA and WEATHER_CSV.exists():
        t, T_air, G = load_weather(WEATHER_CSV, DT)
        print(f"Wetter aus {WEATHER_CSV.name}")
    else:
        t, T_air, G = synthetic_weather(DAYS, DT)
        print("!" * 74)
        print("!  SYNTHETISCHES WETTER. Die Form stimmt, die Herkunft nicht.")
        print("!  Vor jeder Verwendung im Bericht: weather.csv mit meteoblue- und")
        print("!  sonnenfassade-Daten fuellen und USE_REAL_DATA = True setzen.")
        print("!" * 74)

    base = simulate(WALL_BASELINE, OPT_BASELINE, t, T_air, G)
    conc = simulate(WALL_CONCEPT,  OPT_CONCEPT,  t, T_air, G)

    fig_surface(t, T_air, base, conc)
    fig_depthtime(t, base, conc)
    fig_release(t, base, conc)
    fig_reset(t, base, conc)
    animate(t, T_air, base, conc)

    peak_b, peak_c = base["Ts"].max(), conc["Ts"].max()
    night = (t / 3600.0 % 24 < 6)
    print(f"\nSpitzen-Oberflaechentemperatur   Bestand {peak_b:5.1f} °C   "
          f"Konzept {peak_c:5.1f} °C   Differenz {peak_b - peak_c:4.1f} K")
    print(f"Mittlere naechtliche Abgabe      Bestand {base['Qout'][night].mean():5.1f} W/m²  "
          f"Konzept {conc['Qout'][night].mean():5.1f} W/m²")
    print(f"\nAusgabe in {OUT}")
