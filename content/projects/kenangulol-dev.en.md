---
title: "kenangulol.dev"
description: "This site: a logbook drawn on an Aegean chart. The chart and drawings are generated from code, and there is no analytics or tracking."
status: "sea"
years: "2026"
role: "Design and development"
stack: ["Hugo", "Python (NumPy, scikit-image)", "SVG", "CSS", "Cloudflare Workers", "Giscus"]
repo: "https://github.com/kenanglol/kenangulol.dev"
weight: 2
---

The site you are reading, designed as a logbook for my posts, my projects and my career route. I designed and built it together with Claude.

## The idea

The site will mostly hold long posts, so I didn't want a plain blog template. The theme comes from my long-term plan to learn sailing and live aboard a boat in the Aegean: every page is drawn like part of a nautical chart.

- **The home page** opens on an Aegean chart, with a coastline, islands, depth contours and soundings. My name is lettered like a sea name on a chart, in widely spaced italics.
- **Posts** are listed like entries in a logbook: date on the left, title on the right.
- **Projects** are marked by their state: on the slip (in progress), at sea (live), in harbour (finished).
- **Route** shows my career and education as a course plotted on a chart: each workplace is a port, and the current position is lit.

## Design

- **Colours:** cool chart paper, the teal from my CV for deep water, olive green, and the magenta that real nautical charts use for lights and buoys.
- **Type:** Literata for text, a typeface designed for long reading, and Barlow Semi Condensed for menus and labels. Both are served from the site itself.
- **Drawings:** each section opens with a small drawing, like the coastal views in the margins of old charts. Posts have a compass rose and a plotted track, projects a sailboat on the slip, the route a harbour plan, and the not-found page a lighthouse. The lighthouse flashes on the "Fl(2) 10s" rhythm, two flashes every ten seconds, as printed on charts.
- **Light and dark themes:** the site follows the device setting and can be switched with the button at the top right. The light background is slightly dimmed so long reading is easier on the eyes.

## Technical

- **The chart and drawings are generated from code.** For the chart, Python builds a height field, and scikit-image traces the coastlines and depth contours from it. A fixed seed means every build produces the same chart. The drawings are also written as SVG from Python. They take their colours from CSS, so they change with the theme.
- **Hugo** builds the site. Turkish is the default language and English lives under `/en/`. Translations are paired by file name, so the language switch goes straight to the translated page.
- **Cloudflare Workers** serves it. Every push to `main` republishes the site, and other branches get their own preview addresses.
- **Comments** are handled by Giscus and stored in this repository's GitHub Discussions, so there is no server or database to run.
- **Privacy:** no analytics, cookies or tracking. Everything, fonts included, is served from the site itself. The only outside request is the comment box on post pages.
