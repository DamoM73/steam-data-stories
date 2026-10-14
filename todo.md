# To do

## Decisions

- Which computer hosts the class server (laptop or Raspberry Pi), and check with IT that it can run on the school network. See Reference → Hosting on a Class Server.
- How students hand in `steam_story.py` and `data/clean_games.parquet` for the class server (Publishing Our Data Story says "our teacher will tell us how to hand them in"). Update that page and the Hosting page once decided.
- Test the class server on the chosen computer (it was tested in a Linux sandbox, not yet on Windows or a Pi), including a whole class opening stories at once.

## Screenshots

Each spot is marked in the page source with an HTML comment starting `<!-- SCREENSHOT:` (search the docs folder for `SCREENSHOT`). Save each image in `docs/assets/` with the file name given, then replace the comment with `![description](../assets/<file>)`.

1. `l14_controls.png` — the Years slider and Measure dropdown above the explore chart and explore table, all in one cell's output — The Aha Moment
2. `l15_drag_cell.png` — a marimo cell with the drag handle (dots) on its left edge highlighted — Publishing Our Data Story
3. `s01_sql_button.png` — the buttons under a marimo cell, with the SQL button labelled — Why Databases?
4. `s01_connection.png` — the top of an SQL cell with the connection dropdown open and `conn` selected, with the output variable name `_df` beside it — Why Databases?
5. `s01_first_query.png` — the SQL cell with `SELECT * FROM games LIMIT 5` and its result, five rows starting with Counter-Strike — Why Databases?
6. `s01_table_info.png` — the result of `PRAGMA table_info(games)`: 11 rows, with the name, type and pk columns visible — Why Databases?
7. `s02_no_such_column.png` — the SQL cell with `WHERE developers = Valve` and its red error, `no such column: Valve` — Choosing Columns and Rows in SQL
8. `s05_output_variable.png` — the top of the SQL cell with the output variable changed from `_df` to `top_indie` and `conn` chosen — Summarising Groups in SQL
9. `s06_update_all.png` — the check cell after `UPDATE wishlist SET priority = 1`, all five records with priority 1 — Changing Data
10. `s_duckdb_error.png` — an SQL cell left on the default DuckDB connection, and what it shows when we run `SELECT * FROM games` — Common Errors

All SQL screenshots should be taken in marimo 0.25.1 (now pinned in Setting Up). `s05_top_indie.png` is a chart rendered from the real data.

The chart images (`l09_*.png` to `l14_*.png`), the app view (`l15_app_view.png`) and the class server home page (`class_server_home.png`) are rendered from the real data. Replace them if the data is refreshed. The home page image uses made-up student folder names.

## SQL section checks (in a fresh .venv with only the Setting Up packages)

- The SQL button works, and SQL cells run with `conn`, without installing DuckDB or any other package. Note what happens when the default DuckDB connection is left selected (for Common Errors).
- marimo shows SQLite errors as `OperationalError: …` (Choosing Columns and Rows in SQL, Common Errors). Adjust the page text if the wording differs.
- After an `INSERT INTO`, the check cell (`SELECT * FROM wishlist`) doesn't rerun by itself (Changing Data says to run it again).
- Ctrl+Shift+R after reopening sql_intro.py reruns the change cell (the reason for the "One cell for changes" warning).
- Windows won't let us replace steam.db while marimo has it open (Changing Data → Starting again says to stop marimo first).

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
