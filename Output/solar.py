#!/usr/bin/env python3
"""
Solar geometry for Zurich, and the step from a horizontal measurement to the
irradiance actually striking an oriented façade.

The city measures global radiation on a horizontal plane at one station. A wall
is vertical, so the measurement has to be decomposed and re-projected:

    GHI  --Erbs-->  direct + diffuse  --geometry-->  irradiance on the façade

Sources
  Duffie & Beckman, Solar Engineering of Thermal Processes — declination,
    equation of time, hour angle, incidence angle.
  Erbs, Klein & Duffie (1982), Estimation of the diffuse radiation fraction,
    Solar Energy 28(4). The correlation used in `diffuse_fraction`.
"""

import numpy as np

LAT_ZURICH = 47.3769          # degrees north
LON_ZURICH = 8.5417           # degrees east
ALBEDO_GROUND = 0.20          # asphalt and stone, city value for asphalt


def sun_position(times_utc, lat=LAT_ZURICH, lon=LON_ZURICH):
    """Altitude and azimuth of the sun. Azimuth measured from north, clockwise."""
    doy = times_utc.dayofyear.to_numpy()
    hour = (times_utc.hour + times_utc.minute / 60.0).to_numpy()

    B = 2 * np.pi * (doy - 81) / 364.0
    eot = 9.87 * np.sin(2 * B) - 7.53 * np.cos(B) - 1.5 * np.sin(B)   # minutes
    solar_hour = hour + lon / 15.0 + eot / 60.0
    omega = np.radians(15.0 * (solar_hour - 12.0))                    # hour angle
    delta = np.radians(23.45 * np.sin(2 * np.pi * (284 + doy) / 365.0))
    phi = np.radians(lat)

    sin_alt = np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta) * np.cos(omega)
    alt = np.arcsin(np.clip(sin_alt, -1, 1))
    az = np.arctan2(np.sin(omega),
                    np.cos(omega) * np.sin(phi) - np.tan(delta) * np.cos(phi))
    return np.degrees(alt), (np.degrees(az) + 180.0) % 360.0


def diffuse_fraction(kt):
    """Erbs et al. (1982)."""
    kd = np.where(kt <= 0.22, 1.0 - 0.09 * kt,
         np.where(kt <= 0.80,
                  0.9511 - 0.1604 * kt + 4.388 * kt**2
                  - 16.638 * kt**3 + 12.336 * kt**4,
                  0.165))
    return np.clip(kd, 0.0, 1.0)


MIN_ALT = 5.0                 # degrees; below this the split is not trustworthy


def clear_sky_dni(alt_deg, i0):
    """Upper bound on direct normal irradiance from air mass.

    Without it the split below divides by a vanishing sin(altitude) at sunrise
    and returns direct beams that the atmosphere cannot deliver — which then
    lands on an east-facing wall as a spurious morning peak.
    """
    am = 1.0 / np.sin(np.radians(np.clip(alt_deg, MIN_ALT, None)))
    return i0 * 0.7 ** (am ** 0.678)


def split_ghi(ghi, alt_deg, doy):
    """Global horizontal → direct normal and diffuse horizontal."""
    sin_alt = np.sin(np.radians(np.clip(alt_deg, MIN_ALT, None)))
    i0 = 1367.0 * (1 + 0.033 * np.cos(2 * np.pi * doy / 365.0))
    up = alt_deg > MIN_ALT
    with np.errstate(divide="ignore", invalid="ignore"):
        kt = np.where(up, ghi / (i0 * sin_alt), 0.0)
    kt = np.clip(np.nan_to_num(kt), 0.0, 1.0)
    dhi = np.where(up, ghi * diffuse_fraction(kt), ghi)     # low sun: all diffuse
    dni = np.where(up, (ghi - dhi) / sin_alt, 0.0)
    dni = np.minimum(np.clip(dni, 0, None), clear_sky_dni(alt_deg, i0))
    return dni, np.clip(dhi, 0, None)


def surface_irradiance(ghi, alt_deg, az_deg, surface_azimuth, tilt=90.0,
                       albedo=ALBEDO_GROUND, doy=None):
    """Irradiance on a plane of given azimuth (from north) and tilt (90 = wall)."""
    dni, dhi = split_ghi(ghi, alt_deg, doy)
    b, a = np.radians(tilt), np.radians(alt_deg)
    cos_theta = (np.cos(b) * np.sin(a)
                 + np.sin(b) * np.cos(a) * np.cos(np.radians(az_deg - surface_azimuth)))
    beam    = dni * np.clip(cos_theta, 0, None) * (alt_deg > 0)
    sky     = dhi * (1 + np.cos(b)) / 2.0
    ground  = albedo * ghi * (1 - np.cos(b)) / 2.0
    return beam + sky + ground


ORIENTATIONS = {"Süd": 180.0, "West": 270.0, "Ost": 90.0, "Nord": 0.0}
