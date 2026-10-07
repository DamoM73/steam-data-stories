# To do

## Decisions

- Replace the placeholder logo (`docs/assets/logo.png`, `logo_header.png`, `favicon.ico`) if you'd like a designed one.
- Where the three-week SQL introduction lives (this site or another) and which tool it uses.

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
8. `setup_release_download.png` — GitHub release page with the data zip
9. `setup_extract_windows.png` — Windows Extract All dialog ending in \data
10. `setup_extract_macos.png` — Finder with the unzipped folder renamed to data
11. `setup_data_folder.png` — Explorer with the data folder expanded
12. `setup_marimo_empty.png` — empty clean_steam.py notebook in the browser
13. `setup_marimo_quit.png` — marimo's "Are you sure you want to quit?" prompt
13a. `setup_default_profile.png` — Command Palette list of terminal profiles with Command Prompt highlighted (Windows)
13b. `setup_cmd_venv.png` — VS Code terminal showing Command Prompt with the (.venv) prompt (Windows)

Hook lessons:

14. `l01_my_data_story.png` — VS Code with my_data_story.md open, editor and Markdown preview side by side — Lesson 1
15. `l02_marimo_cell.png` — empty marimo cell with run and + buttons labelled — Lesson 2
16. `l02_games_table.png` — the games DataFrame in marimo's table viewer — Lesson 2
17. `l02_schema.png` — output of games.schema — Lesson 2
18. `l02_table_viewer.png` — table viewer sort, search and column summaries labelled — Lesson 2
19. `l03_describe.png` — output of games.describe() — Lesson 3
20. `l03_value_counts.png` — value_counts for Metacritic score — Lesson 3

Screenshots for Lessons 5–16 will be listed here as those lessons are rewritten.

## Data

- Publish the classroom data release built on 7 Oct 2026 (`steam_data_stories_data_2026-10-07.zip`: 10,250 games with 500+ reviews, 13 columns, from the 5 Oct 2026 games.json).
- May 2027: run `scripts/build_data.py` for a fresh snapshot, have Claude rerun every example and update the numbers and chart images, then publish it as the classroom copy.

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
