# Tasks for Claude in VS Code

This site was started in Cowork, which can only create and overwrite files in this folder. It can't delete files, run git, access GitHub or write inside `.github/`. Work on `main`. Check with Damien before each task marked **Confirm first**, and report the output of the checks after each task.

## Context

- **Site generator:** Zensical 0.0.67 (pinned in `requirements.txt`). Config is `zensical.toml`. Pages are in `docs/`.
- **Preview:** `zensical serve`. **Build:** `zensical build --clean` (must report "No issues found").
- **Audience:** Year 9 Digital Technologies students (Year 9/10 writing level) using VS Code on Windows or macOS laptops (instructions that differ use `=== "Windows"` / `=== "macOS"` content tabs, linked across the site). Students know procedural Python and OOP basics, but no Polars, Plotly or notebooks.
- **The unit:** 16 lessons built around the data story arc (Hook, Behind the Scenes, Rising Insights, Aha Moment, Resolution). Everyone uses a classroom copy of the FronkonGames Steam Games Dataset (MIT): games with at least 500 reviews, 13 columns, built by `scripts/build_data.py` and served from the site as `docs/downloads/steam_games.csv` and `docs/downloads/README.txt`. The tutorial works one example question (do Indie games review as well as non-Indie games, and do they cost less?) and students investigate their own question on the same data. Simplified in October 2026 for Year 9: no API, joins or time series.
- **Stack:** Polars 2.0 release candidate (currently 2.0.0rc2; update when stable and recheck examples), Plotly Express (needs NumPy), marimo.
- **Notebooks:** two marimo notebooks. `clean_steam.py` (lessons 2–6: explore, depersonalise, clean, save clean data) and `steam_story.py` (lessons 7–16). Each code block on a page is one marimo cell, titled with its notebook name; `hl_lines` marks new or changed lines in a cell.
- **Structure:** Home; Start (`docs/start/`: introduction, setup); Hook (`docs/hook/01`–`04`); Behind the Scenes (`docs/cleaning/05`–`06`); Rising Insights (`docs/insights/07`–`13`); Aha Moment (`docs/aha/14`); Resolution (`docs/resolution/15`–`16`); Reference (`docs/reference/`).
- **Colour scheme:** espresso `#4E342E` (header, tabs, light-mode links and headings; 11.3:1 with white), espresso light `#7B5E57` (decorative only), latte `#EFDCC9` (active and hovered tab, dark-mode headings and accent; 8.5:1 on espresso), light blue `#8AB4F8` (dark-mode links). Set in `docs/stylesheets/extra.css`. Clearly different from the micro:bit (navy), Lego Spike (magenta), Turtle (teal), Deepest Dungeon (burnt orange), Space Rescue (charcoal slate) and Flask HTMX (crimson) banners.
- **Callouts:** six types, the same on all of Damien's tutorial sites: `!!! learn` (amber, directly under the title), `!!! terms "Terminology"` (grey, straight after `learn`, listing the page's new terms), `!!! primm "PRIMM"` (green), `??? note "Code explanation"` (purple, collapsed), `!!! tip "Title"` (light blue) and `!!! warning "Title"` (hot pink). No videos.
- **Writing style:** Australian English, Year 9/10, Damien's inclusive "we" voice (never "students", "they" or "you" for the reader in prose). Code explanations are `- **line n** → full sentence ending in a full stop.`; ranges use an en dash. No Exercises section; PRIMM **Modify** prompts take their place, and each lesson ends with an "Our data story" task. Error messages are real (made by breaking the code) in ```` ``` { .text .error linenums="1" } ```` blocks followed by a line-by-line breakdown.
- **Dataset currency:** write tutorials against a snapshot taken in October 2026; in May 2027 refresh the snapshot, rerun every example and update outputs; students use the May 2027 snapshot as a fixed classroom copy.
- **Terminology and glossary:** each page's new terms are listed in `scripts/terms.json` (each term on the first page, in nav order, that explains it). `python scripts/build_glossary.py` inserts the Terminology callouts and regenerates `docs/reference/glossary.md`; run it whenever `terms.json` changes, and never edit the callouts or glossary by hand.
- **Screenshots:** spots that need a screenshot from Damien are marked with `<!-- SCREENSHOT: assets/<file> — <description> -->` comments and listed in `todo.md`. Add the same kind of comment (and a `todo.md` line) for any new page that needs one.
- **Plan:** the lesson list is in Damien's Claude project as `claude/Year 9 Data Unit lesson list.md`.

## 1. Deploy workflow (Confirm first)

Create `.github/workflows/deploy.yml` with the workflow below, confirming each action version exists first. Then set **Settings** → **Pages** → **Source** to **GitHub Actions**.

```yaml
name: Deploy site

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v6
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: zensical build --clean
      - uses: actions/upload-pages-artifact@v5
        with:
          path: site
      - uses: actions/deploy-pages@v5
        id: deployment
```

## 2. Final checks

1. `python scripts/check_explanations.py` → `0 issue(s) found`
2. `zensical build --clean` → `No issues found`
3. Check external links. Report broken ones rather than guessing replacements.

## Tasks for Damien (not for Claude)

These are in `todo.md`, which Damien keeps up to date. Don't delete or edit it unless he asks.
