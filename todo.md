# To do

## Decisions

- Replace the placeholder logo (`docs/assets/logo.png`, `logo_header.png`, `favicon.ico`) if you'd like a designed one.
- Where the three-week SQL introduction lives (this site or another) and which tool it uses.
- Which computer hosts the class server (laptop or Raspberry Pi), and check with IT that it can run on the school network. See Reference → Hosting on a Class Server.
- How students hand in `steam_story.py` and `data/clean_games.parquet` for the class server (Lesson 15 says "our teacher will tell us how to hand them in"). Update Lesson 15 and the Hosting page once decided.
- Test the class server on the chosen computer (it was tested in a Linux sandbox, not yet on Windows or a Pi), including a whole class opening stories at once.

## Screenshots

Each spot is marked in the page source with an HTML comment starting `<!-- SCREENSHOT:` (search the docs folder for `SCREENSHOT`). Save each image in `docs/assets/` with the file name given, then replace the comment with `![description](../assets/<file>)`.

Setting Up (`docs/start/setup.md`):

1. `setup_python_windows.png` — Windows Python installer with "Add python.exe to PATH" ticked
2. `setup_python_macos.png` — macOS Python installer success screen
3. `setup_python_extension.png` — VS Code Python extension installed
4. `setup_open_folder.png` — Explorer showing the empty STEAM_DATA_STORIES folder
5. `setup_create_environment.png` — Command Palette, Python: Create Environment → Venv
6. `setup_venv_terminal.png` — terminal with the (.venv) prompt
7. `setup_pip_install.png` — "Successfully installed" after pip install
8. `setup_new_folder.png` — VS Code Explorer with the New Folder icon highlighted and the new data folder
9. `setup_data_folder.png` — Explorer with the data folder expanded
10. `setup_marimo_empty.png` — empty clean_steam.py notebook in the browser
11. `setup_marimo_quit.png` — marimo's "Are you sure you want to quit?" prompt
11a. `setup_default_profile.png` — Command Palette list of terminal profiles with Command Prompt highlighted (Windows)
11b. `setup_cmd_venv.png` — VS Code terminal showing Command Prompt with the (.venv) prompt (Windows)

Hook lessons:

12. `l01_my_data_story.png` — VS Code with my_data_story.md open, editor and Markdown preview side by side — Lesson 1
13. `l02_marimo_cell.png` — empty marimo cell with run and + buttons labelled — Lesson 2
14. `l02_games_table.png` — the games DataFrame in marimo's table viewer — Lesson 2
15. `l02_schema.png` — output of games.schema — Lesson 2
16. `l02_table_viewer.png` — table viewer sort, search and column summaries labelled — Lesson 2
17. `l03_describe.png` — output of games.describe() — Lesson 3
18. `l03_value_counts.png` — value_counts for Metacritic score — Lesson 3

Behind the Scenes lessons:

19. `l05_indie_games.png` — the indie_games table in marimo, 6,243 rows — Lesson 5
20. `l06_dates.png` — the dated table with Release date shown as dates — Lesson 6
21. `l06_null_count.png` — null_count output showing 7317 in Metacritic score — Lesson 6
22. `l06_repeated_names.png` — repeated names sorted, showing the two Alpha Protocol rows — Lesson 6

Rising Insights lessons:

23. `l07_review_score.png` — Name, Positive, Negative and Review score columns — Lesson 7
24. `l07_scored.png` — scored with Review score, Release year, Genres and Group columns — Lesson 7
25. `l08_per_year.png` — per_year table scrolled to show 2018 to 2025 — Lesson 8

Chart images for Lessons 9–11 (`l09_*.png`, `l10_*.png`, `l11_*.png`) are already in `docs/assets/`, rendered from the real data. Replace them if the data is refreshed.

Aha Moment and Resolution lessons:

26. `l14_controls.png` — the Years slider and Measure dropdown above the explore chart in marimo — Lesson 14
27. `l15_drag_cell.png` — a marimo cell with the drag handle (dots) on its left edge highlighted — Lesson 15

The Lesson 14 chart images (`l14_*.png`), the Lesson 15 app view (`l15_app_view.png`) and the class server home page (`class_server_home.png`) are already in `docs/assets/`, made from the real data. The home page image uses made-up student folder names.

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
