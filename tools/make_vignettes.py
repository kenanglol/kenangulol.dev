#!/usr/bin/env python3
"""Draw the page vignettes as SVG line art in the style of the home chart.

Old charts carry small coastal views and plans in their margins; each page
gets one:

  posts.svg       a plotted track with fixes, dividers and a compass rose
  projects.svg    a sailboat on the slip, half planked
  route.svg       a harbour plan with breakwaters, lights and a course in
  lighthouse.svg  a lighthouse on a rock, flashing twice every ten seconds

Colours come from CSS classes (see .vignette in assets/css/main.css), so the
drawings follow the light and dark themes. Run from the repository root:

    python tools/make_vignettes.py
"""
import math
from pathlib import Path

OUT = Path("assets/img/vignettes")
W, H = 600, 200


def svg(body, h=H):
    return (
        f'<svg class="vignette" viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'aria-hidden="true" focusable="false">\n{body}\n</svg>\n'
    )


def bez(p0, p1, p2, p3, n=200):
    pts = []
    for i in range(n + 1):
        t = i / n
        a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
        pts.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0],
                    a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return pts


def y_at(pts, x):
    best = min(pts, key=lambda p: abs(p[0] - x))
    return best[1]


def fmt(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def waves(x0, x1, ys, step=34, seed=0):
    out = []
    for j, y in enumerate(ys):
        x = x0 + (j * 13 + seed) % step
        while x + 14 < x1:
            out.append(f'M{fmt(x)},{y} q4,-3 8,0 t8,0')
            x += step
    return '<path class="ink water thin" d="' + " ".join(out) + '"/>'


# ---------- posts: track, fixes, dividers, compass rose ----------
def posts():
    parts = []
    cx, cy = 482, 100
    # rose rings and degree ticks
    parts.append(f'<circle class="ink thin" cx="{cx}" cy="{cy}" r="82"/>')
    parts.append(f'<circle class="ink thin" cx="{cx}" cy="{cy}" r="72"/>')
    ticks = []
    for deg in range(0, 360, 5):
        a = math.radians(deg - 90)
        r1 = 72 if deg % 10 == 0 else 76
        r1 = 66 if deg % 30 == 0 else r1
        ticks.append(f"M{fmt(cx + r1 * math.cos(a))},{fmt(cy + r1 * math.sin(a))} "
                     f"L{fmt(cx + 82 * math.cos(a))},{fmt(cy + 82 * math.sin(a))}")
    parts.append('<path class="ink thin" d="' + " ".join(ticks) + '"/>')
    # eight-point star, each point half shaded as on printed roses
    for deg in range(0, 360, 45):
        long = deg % 90 == 0
        r = 60 if long else 34
        w = 9 if long else 6
        a = math.radians(deg - 90)
        tip = (cx + r * math.cos(a), cy + r * math.sin(a))
        left = (cx + w * math.cos(a - math.pi / 2), cy + w * math.sin(a - math.pi / 2))
        right = (cx + w * math.cos(a + math.pi / 2), cy + w * math.sin(a + math.pi / 2))
        north = deg == 0
        shade = "light" if north else "inkfill"
        parts.append(f'<path class="paper ink thin" d="M{fmt(cx)},{fmt(cy)} L{fmt(left[0])},{fmt(left[1])} L{fmt(tip[0])},{fmt(tip[1])} Z"/>')
        parts.append(f'<path class="{shade}" d="M{fmt(cx)},{fmt(cy)} L{fmt(right[0])},{fmt(right[1])} L{fmt(tip[0])},{fmt(tip[1])} Z"/>')
    parts.append(f'<circle class="paper ink thin" cx="{cx}" cy="{cy}" r="3.5"/>')

    # plotted track with four fixes and times
    fixes = [(34, 160, "0600"), (150, 132, "0900"), (272, 124, "1200"), (378, 92, "1500")]
    d = "M" + " L".join(f"{x},{y}" for x, y, _ in fixes)
    parts.append(f'<path class="ink" d="{d}"/>')
    for x, y, t in fixes:
        parts.append(f'<circle class="paper ink thin" cx="{x}" cy="{y}" r="5"/>')
        parts.append(f'<circle class="inkfill" cx="{x}" cy="{y}" r="1.4"/>')
        parts.append(f'<text class="label" x="{x}" y="{y + 22}" text-anchor="middle">{t}</text>')
    # arrow on the last leg, pointing on to the rose
    parts.append('<path class="ink" d="M386,95 L398,87 L384,85"/>')

    # dividers stepping off the distance between two fixes
    hx, hy = 211, 44
    parts.append(f'<path class="ink" d="M{hx},{hy} L150,129 M{hx},{hy} L272,121"/>')
    parts.append(f'<path class="ink thin" d="M{hx},{hy - 4} L{hx},{hy - 16}"/>')
    parts.append(f'<circle class="paper ink thin" cx="{hx}" cy="{hy}" r="4"/>')
    return svg("\n".join(parts))


# ---------- projects: sailboat on the slip ----------
def projects():
    parts = []
    ground = 176
    # ground with engineering hatch, then the slip running into the water
    parts.append(f'<path class="ink" d="M24,{ground} H462"/>')
    hatch = " ".join(f"M{x},{ground} l-7,9" for x in range(36, 462, 12))
    parts.append(f'<path class="ink thin" d="{hatch}"/>')
    parts.append(f'<path class="ink" d="M462,{ground} L590,194"/>')
    parts.append(f'<path class="ink water thin" d="M470,182 H600"/>')
    parts.append(waves(480, 600, [190, 198], step=30, seed=4))

    # hull: sheer and underbody as cubic curves, sampled for ribs and posts
    deck = bez((166, 96), (260, 101), (380, 97), (452, 82))
    under1 = bez((452, 82), (442, 110), (410, 131), (360, 137))
    under2 = bez((360, 137), (300, 141), (220, 135), (184, 120))
    under3 = bez((184, 120), (176, 112), (170, 104), (166, 96))
    underbody = under1 + under2 + under3
    hull = ("M166,96 C260,101 380,97 452,82 C442,110 410,131 360,137 "
            "C300,141 220,135 184,120 C176,112 170,104 166,96 Z")

    # cradle posts and keel block, drawn before the hull so the hull sits on them
    for x in (232, 392):
        yb = y_at(underbody, x)
        parts.append(f'<path class="ink" d="M{x},{fmt(yb)} V{ground} M{x - 10},{ground} H{x + 10}"/>')
    parts.append('<path class="ink thin" d="M232,160 L392,170 M232,170 L392,160"/>')
    parts.append(f'<rect class="paper ink" x="282" y="{ground - 8}" width="62" height="8"/>')

    # keel and rudder
    parts.append(f'<path class="paper ink" d="M302,139 L294,{ground - 8} L334,{ground - 8} L342,137 Z"/>')
    parts.append('<path class="paper ink" d="M204,128 L198,160 L216,160 L222,132 Z"/>')
    parts.append(f'<path class="paper ink" d="{hull}"/>')

    # planking on the bow half, bare frames on the stern half
    parts.append('<path class="ink thin" d="M300,108 C360,108 410,103 446,91 M318,122 C364,122 404,116 434,105"/>')
    frames = []
    for x in range(194, 296, 14):
        yt = y_at(deck, x)
        yb = y_at(underbody[len(under1):], x)
        frames.append(f"M{x},{fmt(yt + 1)} Q{x - 4},{fmt((yt + yb) / 2)} {x},{fmt(yb - 1)}")
    parts.append('<path class="ink thin" d="' + " ".join(frames) + '"/>')

    # mast and standing rigging, no sails yet
    mx = 332
    yd = y_at(deck, mx)
    parts.append(f'<path class="ink" d="M{mx},{fmt(yd)} V16"/>')
    parts.append(f'<path class="ink thin" d="M{mx - 14},52 H{mx + 14} M{mx},18 L450,84 M{mx},18 L168,95"/>')
    parts.append(f'<circle class="light" cx="{mx}" cy="14" r="2.6"/>')

    # ladder against the stern
    rails = "M136,176 L176,102 M150,176 L190,104"
    rungs = " ".join(
        f"M{fmt(136 + 40 * t)},{fmt(176 - 74 * t)} L{fmt(150 + 40 * t)},{fmt(176 - 72 * t)}"
        for t in (0.15, 0.32, 0.49, 0.66, 0.83)
    )
    parts.append(f'<path class="ink thin" d="{rails} {rungs}"/>')
    return svg("\n".join(parts))


# ---------- route: harbour plan ----------
def route():
    parts = []
    # land and quay along the top
    land = ("M0,0 H600 V52 C560,56 520,44 470,46 L428,46 L420,40 L180,40 L172,46 "
            "C120,48 60,40 0,56 Z")
    parts.append(f'<path class="land ink" d="{land}"/>')
    # depth contours outside the harbour
    parts.append('<path class="ink water thin" d="M0,118 C120,128 186,168 300,166 C414,164 480,126 600,116"/>')
    parts.append('<path class="ink water thin" d="M0,160 C140,172 220,198 300,196 C380,194 470,166 600,156"/>')
    for x, y, s in [(64, 98, "4"), (110, 146, "7"), (520, 98, "5"), (556, 142, "9"),
                    (472, 184, "14"), (214, 194, "12"), (300, 182, "11")]:
        parts.append(f'<text class="label" x="{x}" y="{y}" text-anchor="middle">{s}</text>')
    # breakwaters
    parts.append('<path class="ink mole" d="M184,44 C180,82 202,118 250,134"/>')
    parts.append('<path class="ink mole" d="M416,44 C422,84 402,116 352,132"/>')

    def flare(x, y, rot):
        return (f'<g transform="translate({x} {y}) rotate({rot})">'
                f'<path class="light" d="M0,0 C-3.2,-7 -2.4,-14 0,-19 C2.4,-14 3.2,-7 0,0 Z"/>'
                f'<circle class="inkfill" r="1.8"/></g>')
    parts.append(flare(252, 135, -40))
    parts.append(flare(350, 133, 40))

    # boats moored stern-to along the quay
    boats = []
    for x in (214, 236, 258, 364, 386):
        boats.append(f"M{x},44 C{x - 5},52 {x - 5},62 {x},72 C{x + 5},62 {x + 5},52 {x},44 Z")
    parts.append('<path class="paper ink thin" d="' + " ".join(boats) + '"/>')

    # anchorage symbol
    parts.append('<path class="ink" d="M300,82 V104 M293,89 H307 M290,96 Q291,106 300,106 Q309,106 310,96"/>')
    parts.append('<circle class="paper ink" cx="300" cy="79" r="3"/>')

    # the course in, with its bearing
    parts.append('<path class="ink course" d="M30,198 L236,170 L298,146 L300,118"/>')
    parts.append('<path class="ink" d="M295.5,127 L300,116 L304.5,127"/>')
    parts.append('<text class="label" x="132" y="174" transform="rotate(-7.7 132 174)">072°</text>')
    return svg("\n".join(parts))


# ---------- 404: lighthouse on a rock ----------
def lighthouse():
    parts = []
    h = 220
    # beams first, behind everything
    parts.append('<g class="beams">'
                 '<path class="beam" d="M300,42 L20,14 L20,74 Z"/>'
                 '<path class="beam" d="M300,42 L580,12 L580,76 Z"/></g>')
    # sea
    parts.append('<path class="ink water thin" d="M0,172 H600"/>')
    parts.append(waves(0, 600, [184, 196, 208], step=38, seed=9))
    # rock
    parts.append('<path class="land ink" d="M218,174 L230,160 L242,156 L252,146 L266,144 L274,148 '
                 'L326,148 L338,140 L350,146 L356,156 L370,160 L384,174 Z"/>')
    parts.append('<path class="ink thin" d="M240,166 l10,-6 M352,160 l9,6 M262,158 l6,-4"/>')
    # tower with two day-mark bands
    parts.append('<path class="paper ink" d="M276,148 L285,64 L315,64 L324,148 Z"/>')

    def xl(y):
        return 276 + (148 - y) / 84 * 9

    for y0, y1 in ((92, 104), (120, 132)):
        parts.append(f'<path class="inkfill" d="M{fmt(xl(y1))},{y1} L{fmt(xl(y0))},{y0} '
                     f'L{fmt(600 - xl(y0))},{y0} L{fmt(600 - xl(y1))},{y1} Z"/>')
    parts.append('<path class="paper ink thin" d="M294,148 V137 A6,6 0 0 1 306,137 V148"/>')
    parts.append('<rect class="paper ink thin" x="297" y="74" width="6" height="10"/>')
    # gallery, lantern, dome
    parts.append('<path class="ink thin" d="M280,58 V50 H320 V58 M290,50 V58 M300,50 V58 M310,50 V58"/>')
    parts.append('<rect class="paper ink" x="279" y="58" width="42" height="6"/>')
    parts.append('<rect class="paper ink" x="288" y="34" width="24" height="16"/>')
    parts.append('<path class="ink thin" d="M296,34 V50 M304,34 V50"/>')
    parts.append('<path class="paper ink" d="M286,34 Q300,16 314,34 Z"/>')
    parts.append('<path class="ink" d="M300,23 V13"/>')
    parts.append('<circle class="light lamp" cx="300" cy="42" r="4.5"/>')
    # the light's characteristic as printed beside it on a chart
    parts.append('<text class="label label-light" x="336" y="96">Fl(2) 10s</text>')
    parts.append('<text class="label" x="336" y="113">24m 15M</text>')
    return svg("\n".join(parts), h=h)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [("posts", posts), ("projects", projects), ("route", route), ("lighthouse", lighthouse)]:
        text = fn()
        (OUT / f"{name}.svg").write_text(text)
        print(f"wrote {OUT / name}.svg ({len(text) // 1024 + 1} KB)")
