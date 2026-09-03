#!/usr/bin/env python3
"""
The building, not the diagram.

Runs the transient wall model once per façade orientation, driven by measured
Zurich weather, and renders two identical buildings side by side — the existing
one and the same one with the concept façade — coloured by the surface
temperature the model computes. Animated over two days of the heat wave.

    python3 fetch_weather.py     # once, builds weather.csv from open data
    python3 house_render.py

The roof is deliberately identical in both. Section 2 narrows the system of
interest to the façade and leaves the roof as the release interface, so the
picture should show the façades changing and the roof not.
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from matplotlib.colors import Normalize
from pathlib import Path

import solar
import wall_model as wm

HERE = Path(__file__).parent
OUT  = HERE / "wall_model"
OUT.mkdir(exist_ok=True)

ANIM_DAYS = 2          # of the five in weather.csv
FPS       = 18


# --------------------------------------------------------------- simulation
def run_all(weather, dt=60.0):
    """Measured weather comes on a 15-minute grid; the solver needs a step small
    enough to stay stable, so everything is interpolated onto a `dt` grid first."""
    t_src = (weather.index - weather.index[0]).total_seconds().to_numpy()
    t = np.arange(0.0, t_src[-1] + dt, dt)
    times = weather.index[0] + pd.to_timedelta(t, unit="s")

    Ta  = np.interp(t, t_src, weather.T_air_C.to_numpy())
    ghi = np.interp(t, t_src, weather.GHI_Wm2.to_numpy())
    utc = times.tz_convert("UTC")
    alt, az = solar.sun_position(utc)
    doy = utc.dayofyear.to_numpy()
    surfaces = {}
    for name, s_az in solar.ORIENTATIONS.items():
        surfaces[name] = solar.surface_irradiance(ghi, alt, az, s_az, 90.0, doy=doy)
    surfaces["Dach"] = solar.surface_irradiance(ghi, alt, az, 180.0, 0.0, doy=doy)

    res = {"baseline": {}, "concept": {}}
    for name, G in surfaces.items():
        res["baseline"][name] = wm.simulate(wm.WALL_BASELINE, wm.OPT_BASELINE,
                                            t, Ta, G, dt=dt)
        # the concept treats façades only; the roof stays as built
        if name == "Dach":
            res["concept"][name] = res["baseline"][name]
        else:
            res["concept"][name] = wm.simulate(wm.WALL_CONCEPT, wm.OPT_CONCEPT,
                                               t, Ta, G, dt=dt)
    return t, times, Ta, alt, az, surfaces, res


# ------------------------------------------------------------------ drawing
W, D, H = 18.0, 14.0, 16.0        # m, five storeys plus roof structure
C30, S30 = np.cos(np.radians(30)), np.sin(np.radians(30))


def iso(x, y, z):
    return (x - y) * C30, (x + y) * S30 + z


def faces():
    """South (y=0), west (x=0) and roof, in an isometric that shows all three."""
    return {
        "Süd":  [(0, 0, 0), (W, 0, 0), (W, 0, H), (0, 0, H)],
        "West": [(0, 0, 0), (0, D, 0), (0, D, H), (0, 0, H)],
        "Dach": [(0, 0, H), (W, 0, H), (W, D, H), (0, D, H)],
    }


def sky_colour(alt):
    if alt <= -6:  return "#141b2e"
    if alt <= 0:   return "#3a3f5c"
    f = min(alt / 45.0, 1.0)
    top = np.array([0.36, 0.44, 0.62]) * (1 - f) + np.array([0.55, 0.71, 0.88]) * f
    return tuple(top)


def build_figure(res, t, Ta, alt, surfaces):
    vals = np.concatenate([r["Ts"] for v in res.values() for r in v.values()])
    norm = Normalize(np.floor(vals.min()), np.ceil(vals.max()))
    cmap = plt.get_cmap("inferno")

    fig, axes = plt.subplots(1, 2, figsize=(12.5, 6.4))
    fig.subplots_adjust(left=.02, right=.88, top=.84, bottom=.06, wspace=.05)
    polys, labels = {}, {}

    for ax, key, title, colour in zip(
            axes, ("baseline", "concept"),
            ("Bestand  ·  $\\alpha_{sol}=0.30$", "Konzept  ·  $\\alpha_{sol}=0.80$ + Hinterlüftung"),
            ("#AE3B2E", "#15709F")):
        ax.set_aspect("equal")
        # not axis("off") — that hides the axes patch, and the patch is the sky
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(title, fontsize=12.5, fontweight="bold", color=colour, pad=14)
        # ground
        g = [iso(x, y, 0) for x, y in [(-6, -6), (W + 6, -6), (W + 6, D + 6), (-6, D + 6)]]
        ax.add_patch(Polygon(g, closed=True, facecolor="#8d8a83", edgecolor="none", zorder=0))
        polys[key], labels[key] = {}, {}
        for fname, pts in faces().items():
            xy = [iso(*p) for p in pts]
            poly = Polygon(xy, closed=True, edgecolor="#2b2b28", lw=1.1, zorder=2)
            ax.add_patch(poly); polys[key][fname] = poly
            cx = np.mean([p[0] for p in xy]); cy = np.mean([p[1] for p in xy])
            labels[key][fname] = ax.text(cx, cy, "", ha="center", va="center",
                                         fontsize=10.5, fontweight="bold", zorder=3)
        ax.set_xlim(-22, 22); ax.set_ylim(-4, 34)

    cax = fig.add_axes([0.90, 0.12, 0.018, 0.66])
    fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax,
                 label="Oberflächentemperatur [°C]")
    clock = fig.text(.45, .945, "", ha="center", fontsize=15, fontweight="bold")
    info  = fig.text(.45, .900, "", ha="center", fontsize=10, color="#4A4B45")
    src   = fig.text(.02, .015,
                     "Antrieb: gemessene Lufttemperatur Station I11 Röntgenstrasse und "
                     "Globalstrahlung Zch_Stampfenbachstrasse, Open Data Zürich, "
                     "10.–14.08.2024. Fassadeneinstrahlung aus Sonnenstand und "
                     "Erbs-Zerlegung. Dach in beiden Varianten unverändert.",
                     fontsize=7, color="#6b6b62")
    return fig, axes, polys, labels, norm, cmap, clock, info


def animate(times, t, Ta, alt, az, surfaces, res, every_minutes=15):
    fig, axes, polys, labels, norm, cmap, clock, info = build_figure(res, t, Ta, alt, surfaces)
    step = max(1, int(every_minutes * 60 / (t[1] - t[0])))
    idx = np.arange(0, min(len(t), int(ANIM_DAYS * 86400 / (t[1] - t[0]))), step)

    def draw(f):
        i = idx[f]
        for ax in axes:
            ax.set_facecolor(sky_colour(alt[i]))
        for key in ("baseline", "concept"):
            for fname, poly in polys[key].items():
                T = res[key][fname]["Ts"][i]
                poly.set_facecolor(cmap(norm(T)))
                shade = "white" if norm(T) > .55 else "#f2f2ee"
                labels[key][fname].set_text(f"{fname}\n{T:.1f} °C")
                labels[key][fname].set_color(shade)
        ts = times[i]
        clock.set_text(ts.strftime("%d.%m.%Y  ·  %H:%M"))
        sun = f"Sonne {alt[i]:.0f}° über dem Horizont" if alt[i] > 0 else "Sonne unter dem Horizont"
        info.set_text(f"Aussenluft {Ta[i]:.1f} °C   ·   {sun}   ·   "
                      f"Einstrahlung Südfassade {surfaces['Süd'][i]:.0f} W/m²")
        return []

    anim = FuncAnimation(fig, draw, frames=len(idx), blit=False)
    anim.save(OUT / "haus_zeitraffer.gif", writer=PillowWriter(fps=FPS))
    plt.close(fig)
    print(f"  haus_zeitraffer.gif  ({len(idx)} Bilder)")


def figure_orientations(times, t, Ta, ghi, surfaces, res):
    """Which façade is the problem, and when."""
    h = t / 3600.0
    fig, axes = plt.subplots(2, 1, figsize=(11.5, 6.6), sharex=True)
    cols = {"Süd": "#A8871A", "West": "#AE3B2E", "Ost": "#15709F", "Nord": "#6b6b62"}
    for name, c in cols.items():
        axes[0].plot(h, surfaces[name], color=c, lw=1.3, label=name)
        axes[1].plot(h, res["baseline"][name]["Ts"], color=c, lw=1.3, label=f"{name} Bestand")
        axes[1].plot(h, res["concept"][name]["Ts"], color=c, lw=1.1, ls=":",
                     label=f"{name} Konzept")
    axes[0].plot(h, ghi, color="#2b2b28", lw=1.0, ls="--", label="horizontal (Messung)")
    axes[0].set_ylabel("Einstrahlung [W/m²]"); axes[0].legend(ncol=5, frameon=False, fontsize=8.5)
    axes[1].plot(h, Ta, color="#2b2b28", lw=1.2, label="Aussenluft")
    axes[1].set_ylabel("Oberfläche [°C]"); axes[1].set_xlabel("Stunden ab 10.08.2024 00:00")
    axes[1].legend(ncol=5, frameon=False, fontsize=7.5)
    for ax in axes:
        ax.grid(alpha=.25)
        for d in range(6):
            ax.axvspan(d * 24, d * 24 + 6, color="#15709F", alpha=.05)
    axes[0].set_title("Einstrahlung und Oberflächentemperatur je Orientierung — "
                      "durchgezogen Bestand, gepunktet Konzept")
    fig.tight_layout()
    fig.savefig(OUT / "05_orientierungen.png", dpi=160); plt.close(fig)
    print("  05_orientierungen.png")


if __name__ == "__main__":
    csv = HERE / "weather.csv"
    if not csv.exists():
        raise SystemExit("weather.csv fehlt — zuerst  python3 fetch_weather.py")
    weather = pd.read_csv(csv, parse_dates=["timestamp"], index_col="timestamp")
    print(f"Wetter: {len(weather)} Werte, {weather.index[0]:%d.%m.%Y} bis {weather.index[-1]:%d.%m.%Y}")

    t, times, Ta, alt, az, surfaces, res = run_all(weather)
    ghi = np.interp(t, (weather.index - weather.index[0]).total_seconds().to_numpy(),
                    weather.GHI_Wm2.to_numpy())

    print("\nSpitzen-Oberflächentemperatur je Orientierung:")
    for name in list(solar.ORIENTATIONS) + ["Dach"]:
        b, c = res["baseline"][name]["Ts"].max(), res["concept"][name]["Ts"].max()
        tag = "  (unverändert, ausserhalb der Systemgrenze)" if name == "Dach" else ""
        print(f"  {name:5s}  Bestand {b:5.1f} °C   Konzept {c:5.1f} °C   "
              f"Differenz {b - c:4.1f} K{tag}")

    print("\nErzeuge:")
    figure_orientations(times, t, Ta, ghi, surfaces, res)
    animate(times, t, Ta, alt, az, surfaces, res)
    print(f"\nAusgabe in {OUT}")
