# kenangulol.dev

Source of [kenangulol.dev](https://kenangulol.dev), my personal site: posts and CV, in Turkish and English.

The site is a logbook drawn on an Aegean chart. The home page opens on a nautical chart generated from code, and posts are listed like logbook entries.

## Stack

- [Hugo](https://gohugo.io) with a small custom theme in `layouts/`, no third-party theme
- Self-hosted fonts: Literata (text) and Barlow Semi Condensed (UI), both under the SIL Open Font License (license texts in `static/fonts/`)
- [Giscus](https://giscus.app) comments, stored in this repository's GitHub Discussions
- Deployed to Cloudflare Workers static assets on every push to `main` (`wrangler.jsonc`)
- No analytics, no third-party requests except Giscus on post pages

## Structure

```
content/            posts and pages; Turkish is the default, English uses the .en.md suffix
layouts/            templates (baseof, home, list, single, cv, 404) and partials
assets/css/         site styles and syntax highlighting
assets/img/chart.svg   the generated chart on the home page
i18n/               interface strings per language
static/fonts/       self-hosted font files
tools/make_chart.py    generator for the chart
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
```

Setup notes for deployment, comments and the domain are in [KURULUM.md](KURULUM.md) (Turkish).
