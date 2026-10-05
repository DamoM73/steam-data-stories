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

Hook lessons:

14. `l01_my_data_story.png` — VS Code with my_data_story.md open, editor and Markdown preview side by side — Lesson 1
15. `l02_marimo_cell.png` — empty marimo cell with run and + buttons labelled — Lesson 2
16. `l02_games_table.png` — the games DataFrame in marimo's table viewer — Lesson 2
17. `l02_schema.png` — output of games.schema — Lesson 2
18. `l02_table_viewer.png` — table viewer sort, search and column summaries labelled — Lesson 2
19. `l03_story_games.png` — the story_games DataFrame — Lesson 3
20. `l03_describe.png` — output of games.describe() — Lesson 3
21. `l03_value_counts.png` — value_counts for Estimated owners — Lesson 3

Behind the Scenes lessons:

22. `l05_story_rows.png` — the six story_rows in marimo's table viewer — Lesson 5
23. `l06_dates.png` — typed table with Release date shown as dates — Lesson 6
24. `l06_owners.png` — Release date, Estimated owners, Owners min and Owners max — Lesson 6
25. `l07_null_count.png` — null_count output for typed — Lesson 7
26. `l07_duplicates.png` — duplicated names sorted, showing the two 2048 rows — Lesson 7
27. `l07_checks.png` — output of the checks dictionary — Lesson 7
28. `l08_lists.png` — Name, Genres and Tags shown as lists — Lesson 8

Rising Insights, Aha Moment and Resolution lessons:

29. `l09_nan.png` — Review score showing NaN for a game with no reviews — Lesson 9
30. `l09_scored.png` — scored with Review score, Release year and Price band — Lesson 9
31. `l10_per_year.png` — per_year table scrolled to 2020–2026 — Lesson 10
32. `l10_per_genre.png` — per_genre top 10 table — Lesson 10
33. `l13_two_pages.png` — first_page and second_page joined, 2,000 rows — Lesson 13
34. `l13_history.png` — history with players, added and AppID columns — Lesson 13
35. `l14_clean_history.png` — clean_history with the Time column in AEST — Lesson 14
36. `l14_gaps.png` — the gaps table — Lesson 14
37. `l14_monthly.png` — the monthly table for ARC Raiders — Lesson 14
38. `l15_controls.png` — the multiselect and slider side by side — Lesson 15
39. `l16_md_hook.png` — rendered Markdown hook — Lesson 16
40. `l16_app_view.png` — finished story in app view, code hidden — Lesson 16

Chart images for Lessons 11, 12 and 15 (`l11_*.png`, `l12_*.png`, `l15_*.png`) are already in `docs/assets/`, rendered from the real data. Replace them if the data is refreshed.

## Data

- Download a snapshot of the FronkonGames Steam Games Dataset now (October 2026) for writing the tutorials.
- May 2027: run `scripts/build_data.py` for a fresh snapshot, have Claude rerun every example and update the numbers, chart images and the Lesson 15 and 16 findings, then publish it as the classroom copy.
- Check the school network allows `games-popularity.com` (Lesson 13), and that a class of students can share the 100 requests a day the API allows without a key.

## Testing

- Work through the lessons on a school laptop once they're written.
