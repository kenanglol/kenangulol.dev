"""Generate the nautical-chart SVG used on the home page.

A deterministic height field (a coast on the right, a few islands, gentle
noise) is contoured into a coastline, depth lines and spot soundings, the way
an Aegean chart is drawn. Run from the repo root:

    python tools/make_chart.py            # writes assets/img/chart.svg
    python tools/make_chart.py --seed 7   # a different sea
"""

import argparse
import math
from pathlib import Path

import numpy as np
from skimage import measure

W, H = 1200, 520          # SVG viewBox
NX, NY = 300, 130         # grid resolution
SCALE = W / NX


def height_field(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    y, x = np.mgrid[0:NY, 0:NX].astype(float)
    u, v = x / NX, y / NY

    # Mainland rising toward the right, with a bay cut into it.
    z = 3.2 * (u - 0.78) - 0.25 * np.sin(v * math.pi * 1.4)
    z -= 0.55 * np.exp(-(((u - 0.86) / 0.07) ** 2 + ((v - 0.55) / 0.16) ** 2))

    # Islands
    for cx, cy, r, h in [(0.62, 0.30, 0.045, 1.0), (0.58, 0.14, 0.03, 0.95),
                         (0.70, 0.88, 0.03, 0.95), (0.47, 0.42, 0.02, 0.9)]:
        z += h * np.exp(-(((u - cx) / r) ** 2 + ((v - cy) / (r * 2.3)) ** 2))

    # Smooth pseudo-noise from a handful of random waves
    for _ in range(14):
        kx, ky = rng.uniform(1.2, 4.5, 2)
        ph = rng.uniform(0, 2 * math.pi)
        z += rng.uniform(0.02, 0.06) * np.sin(kx * u * 2 * math.pi + ky * v * 2 * math.pi + ph)
    return z


def path_d(contour: np.ndarray, step: int = 2, close: bool = False) -> str:
    pts = contour[::step]
    if len(pts) < 3:
        return ""
    coords = " ".join(f"{c * SCALE:.1f},{r * SCALE:.1f}" for r, c in pts)
    return f"M{coords}{' Z' if close else ''}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=1923)
    ap.add_argument("--out", default="assets/img/chart.svg")
    args = ap.parse_args()

    z = height_field(args.seed)
    padded = np.pad(z, 1, constant_values=z.min() - 1)

    land = [path_d(c - 1, step=1, close=True) for c in measure.find_contours(padded, 0.0)]
    land = [d for d in land if d]

    depth_levels = [-0.12, -0.3, -0.55, -0.85, -1.2, -1.6]
    depths = []
    for i, lvl in enumerate(depth_levels):
        for c in measure.find_contours(z, lvl):
            if len(c) > 25:
                depths.append((i, path_d(c, step=2)))

    # Spot soundings: depth in metres, only in open water, kept apart
    rng = np.random.default_rng(args.seed + 1)
    soundings, placed = [], []
    for _ in range(600):
        gx, gy = rng.integers(6, NX - 6), rng.integers(6, NY - 6)
        val = z[gy, gx]
        if val > -0.08:
            continue
        # Keep the lower-left open water clear: the name is lettered there
        if gx < NX * 0.74 and gy > NY * 0.55:
            continue
        sx, sy = gx * SCALE, gy * SCALE
        if any((sx - px) ** 2 + (sy - py) ** 2 < 70 ** 2 for px, py in placed):
            continue
        placed.append((sx, sy))
        metres = int(round(-val * 38 + rng.uniform(-2, 2)))
        soundings.append(f'<text x="{sx:.0f}" y="{sy:.0f}">{max(metres, 2)}</text>')
        if len(soundings) >= 34:
            break

    parts = [
        f'<svg class="chart" viewBox="0 0 {W} {H}" preserveAspectRatio="xMinYMid slice" '
        'xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">',
        '<g class="chart-depths">',
        *[f'<path class="d{i}" pathLength="1" d="{d}"/>' for i, d in depths],
        "</g>",
        '<g class="chart-soundings">', *soundings, "</g>",
        '<g class="chart-land">', *[f'<path d="{d}"/>' for d in land], "</g>",
        "</svg>",
    ]
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB, {len(depths)} depth lines, "
          f"{len(land)} land shapes, {len(soundings)} soundings)")


if __name__ == "__main__":
    main()
