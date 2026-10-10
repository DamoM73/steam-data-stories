# To do

## Decisions

- Replace the placeholder logo (`docs/assets/logo.png`, `logo_header.png`, `favicon.ico`) if you'd like a designed one.
- Where the three-week SQL introduction lives (this site or another) and which tool it uses.
- Which computer hosts the class server (laptop or Raspberry Pi), and check with IT that it can run on the school network. See Reference → Hosting on a Class Server.
- How students hand in `steam_story.py` and `data/clean_games.parquet` for the class server (Publishing Our Data Story says "our teacher will tell us how to hand them in"). Update that page and the Hosting page once decided.
- Test the class server on the chosen computer (it was tested in a Linux sandbox, not yet on Windows or a Pi), including a whole class opening stories at once.

## Screenshots

Each spot is marked in the page source with an HTML comment starting `<!-- SCREENSHOT:` (search the docs folder for `SCREENSHOT`). Save each image in `docs/assets/` with the file name given, then replace the comment with `![description](../assets/<file>)`.

1. `l02_table_viewer.png` — the games table viewer with the sort (column heading), search box and column summaries labelled — Exploring Our Data
2. `l14_controls.png` — the Years slider and Measure dropdown above the explore chart and explore table, all in one cell's output — The Aha Moment
3. `l15_drag_cell.png` — a marimo cell with the drag handle (dots) on its left edge highlighted — Publishing Our Data Story

The chart images (`l09_*.png` to `l14_*.png`), the app view (`l15_app_view.png`) and the class server home page (`class_server_home.png`) are rendered from the real data. Replace them if the data is refreshed. The home page image uses made-up student folder names.

## Housekeeping

- Delete `docs/examples/aha/14_aha_moment/story22.py`. It is no longer used: the explore chart now goes in the same cell as the controls and table (`story21.py`).

## Data

- The classroom data (10,250 games with 500+ reviews, 13 columns, from the 5 Oct 2026 games.json) is served from the site as `docs/downloads/steam_games.csv` and `docs/downloads/README.txt`. Delete the old GitHub release once the site is live.
- May 2027: run `scripts/build_data.py` for a fresh snapshot, have Claude rerun every example and update the numbers and chart images, then commit and push the new `docs/downloads/` files.

## Old files to delete (simplified unit, Oct 2026)

Cowork can't delete files. Delete these in VS Code or File Explorer now. They're no longer in the navigation, and the new lessons reuse some of the same folder names:

- `data/player_history/` (whole folder)
- `docs/cleaning/06_data_types.md`, `07_missing_values.md`, `08_text_lists.md`
- `docs/insights/09_new_columns.md`, `10_summarising_groups.md`, `11_charts_compare.md`, `12_trends_outliers.md`, `13_api.md`, `14_combining.md`
- `docs/aha/15_aha_moment.md`, `docs/resolution/16_publishing.md`
- `docs/examples/cleaning/`, `docs/examples/insights/`, `docs/examples/aha/`, `docs/examples/resolution/`
- `docs/assets/l11_*.png`, `docs/assets/l12_*.png`, `docs/assets/l15_*.png`

## Testing

- Work through the lessons on a school laptop once they're written.
