---
title: "kenangulol.dev"
description: "This site: a logbook drawn on an Aegean chart, with the chart and drawings generated from code."
status: "sea"
years: "2026"
stack: ["Hugo", "Python", "SVG", "Cloudflare Workers"]
repo: "https://github.com/kenanglol/kenangulol.dev"
weight: 2
---

The site you are reading, designed as a logbook for my posts and my route.

- The chart on the home page is an SVG generated with Python that comes out the same on every build. Its coastline, islands and depth contours are traced from a height field.
- The drawings on each page (compass rose, boat on the slip, harbour plan, lighthouse) are also drawn from code and change colour with the light and dark themes.
- Built with Hugo and served from Cloudflare Workers. Comments live in GitHub Discussions, and there is no analytics.
