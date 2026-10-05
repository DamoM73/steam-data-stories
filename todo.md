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

## Data

- Download a snapshot of the FronkonGames Steam Games Dataset now (October 2026) for writing the tutorials.
- May 2027: download a fresh snapshot, have Claude rerun every example and update outputs, then use it as the classroom copy.
- Check the school network allows `api.steampowered.com` (Lesson 13).

## Testing

- Work through the lessons on a school laptop once they're written.
