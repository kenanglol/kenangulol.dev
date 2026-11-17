# kenangulol.dev

Source of [kenangulol.dev](https://kenangulol.dev), my personal site: posts, projects and my career route, in Turkish and English.

The site is a logbook drawn on an Aegean chart. The home page opens on a nautical chart generated from code, posts are listed like logbook entries, and each section opens with a small drawing from a chart's margin: a compass rose, a boat on the slip, a harbour plan, a lighthouse.

## Stack

- [Hugo](https://gohugo.io) with a small custom theme in `layouts/`, no third-party theme
- Self-hosted fonts: Literata (text) and Barlow Semi Condensed (UI), both under the SIL Open Font License (license texts in `static/fonts/`)
- [Giscus](https://giscus.app) comments, stored in this repository's GitHub Discussions
- Deployed to Cloudflare Workers static assets on every push to `main` (`wrangler.jsonc`)
- No analytics, no third-party requests except Giscus on post pages

## Structure

```
content/            posts and pages; Turkish is the default, English uses the .en.md suffix
layouts/            templates (baseof, home, list, single, rota, projects/, 404) and partials
assets/css/         site styles and syntax highlighting
assets/img/chart.svg   the generated chart on the home page
assets/img/vignettes/  the generated page drawings
i18n/               interface strings per language
static/fonts/       self-hosted font files
tools/make_chart.py    generator for the chart
tools/make_vignettes.py  generator for the page drawings
```

## Local development

```sh
hugo server -D      # http://localhost:1313, drafts included
hugo --gc --minify  # production build into public/
```

## Regenerating the chart

```sh
pip install numpy scikit-image
python tools/make_chart.py            # default sea
python tools/make_chart.py --seed 7   # a different coastline
python tools/make_vignettes.py        # page drawings, no dependencies
```

Setup notes for deployment, comments and the domain are in [KURULUM.md](KURULUM.md) (Turkish).
