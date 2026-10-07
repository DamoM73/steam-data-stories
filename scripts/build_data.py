"""Collect, build and package the data for Steam Data Stories.

Run this once, just before the unit starts. It runs these steps in order:

1. download  Download the latest games.json from the FronkonGames Steam
             Games Dataset on Hugging Face into data/raw/ (about 1 GB).
2. games     Build the classroom games CSV, data/raw/steam_games.csv, from
             games.json: only games with at least MIN_REVIEWS reviews,
             only the CLASSROOM_COLUMNS, and no adult content.
3. audit     Count the data cleaning issues left in steam_games.csv.
4. package   Zip steam_games.csv and a README into
             data/raw/steam_data_stories_data_<date>.zip, ready to attach
             to a GitHub release for students to download.

Games CSV
    The published games.csv merges "Discount" and "DLC count" into one
    header and is missing some games, so the CSV is built from games.json,
    written the way the published CSV writes each value.

    The classroom copy is kept small for Year 9: only games with at least
    MIN_REVIEWS reviews (positive + negative), the columns in
    CLASSROOM_COLUMNS, and no games without genres. Three kinds of mess are
    kept on purpose for the cleaning lessons: release dates stored as text,
    Metacritic scores of 0 meaning "no score", and repeated names.

    Adult content is filtered out (students are aged 13 to 15). A game is
    excluded when it has an "NSFW" tag, notes describing explicit sexual
    content or nudity ("explicit violence", "explicit language" and
    "non-explicit" don't count), Steam's "Sexual Content" or "Nudity"
    genre, or a sexually explicit word or swear word in its name.
    Excluded games are listed in data/raw/excluded_adult.csv. Decisions in
    data/adult_overrides.csv (AppID,Decision with "keep" or "exclude")
    win over the rules.

Everything in data/raw/ is git-ignored. The zip goes on a GitHub release
instead (see the message the package step prints).

Needs the rich library for progress bars:  pip install rich

Run from the repo root:
    python scripts/build_data.py                     all four steps
    python scripts/build_data.py games audit         only the steps named
    python scripts/build_data.py --show 3065800      print one game's raw record
"""

import argparse
import csv
import json
import re
import sys
import urllib.request
import zipfile
from collections import Counter
from datetime import date
from pathlib import Path

try:
    from rich.console import Console
    from rich.progress import (BarColumn, DownloadColumn, Progress,
                               SpinnerColumn, TaskProgressColumn, TextColumn,
                               TimeElapsedColumn, TimeRemainingColumn, TransferSpeedColumn)
except ImportError:
    print("This script needs the rich library. Install it with:  pip install rich")
    sys.exit(1)

console = Console()


def bar_progress():
    """A progress bar for steps with a known total."""
    return Progress(TextColumn("{task.description}"), BarColumn(), TaskProgressColumn(),
                    TimeElapsedColumn(), TimeRemainingColumn(), console=console)


def count_progress():
    """A spinner and running count for steps without a known total."""
    return Progress(SpinnerColumn(), TextColumn("{task.description}"),
                    TextColumn("{task.completed:,} {task.fields[unit]}"), TimeElapsedColumn(),
                    console=console)

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW = DATA / "raw"
JSON_PATH = RAW / "games.json"
OUT = RAW / "steam_games.csv"
EXCLUDED = RAW / "excluded_adult.csv"
OVERRIDES = DATA / "adult_overrides.csv"
TODAY = date.today().isoformat()
PACKAGE = RAW / f"steam_data_stories_data_{TODAY}.zip"
DATASET_URL = "https://huggingface.co/datasets/FronkonGames/steam-games-dataset/resolve/main/games.json"
STEPS = ["download", "games", "audit", "package"]
MIN_REVIEWS = 500

EXPLICIT_NAME = re.compile(
    r"hentai|porn|erotic|eroge|nsfw|netorare|\bntr\b|xxx|\bsex\b|\bsexy\b|\bnude|nudity|naked|"
    r"\blewd|\bmilf|fetish|bdsm|\bboobs?\b|horny|panties|\borgasm|\bslut|cuckold|\bincest",
    re.IGNORECASE)
SWEARING = re.compile(
    r"fuck|\bshit|\bbitch|\bcunt|\bbastard|\basshole|\bass\b|\bpiss|\bwank|\bbollocks|"
    r"\bcock\b|\bdickhead|motherf",
    re.IGNORECASE)
ADULT_GENRES = {"Sexual Content", "Nudity"}
SEXUAL_NEAR_EXPLICIT = re.compile(
    r"sex|nud|naked|genital|porn|erotic|hentai|lewd|breast|nipple|intercourse|masturb|fetish|"
    r"adult (content|themes|material|scenes|represent)|18\+",
    re.IGNORECASE)
NEGATED = re.compile(r"\b(non-?|not|nothing|no|without|never)\s*(sexually\s*)?$", re.IGNORECASE)

csv.field_size_limit(sys.maxsize if sys.maxsize < 2**31 else 2**31 - 1)

# CSV column name -> JSON field name
COLUMNS = {
    "AppID": None,
    "Name": "name",
    "Release date": "release_date",
    "Estimated owners": "estimated_owners",
    "Peak CCU": "peak_ccu",
    "Required age": "required_age",
    "Price": "price",
    "Discount": "discount",
    "DLC count": "dlc_count",
    "About the game": "about_the_game",
    "Supported languages": "supported_languages",
    "Full audio languages": "full_audio_languages",
    "Reviews": "reviews",
    "Header image": "header_image",
    "Website": "website",
    "Support url": "support_url",
    "Support email": "support_email",
    "Windows": "windows",
    "Mac": "mac",
    "Linux": "linux",
    "Metacritic score": "metacritic_score",
    "Metacritic url": "metacritic_url",
    "User score": "user_score",
    "Positive": "positive",
    "Negative": "negative",
    "Score rank": "score_rank",
    "Achievements": "achievements",
    "Recommendations": "recommendations",
    "Notes": "notes",
    "Average playtime forever": "average_playtime_forever",
    "Average playtime two weeks": "average_playtime_2weeks",
    "Median playtime forever": "median_playtime_forever",
    "Median playtime two weeks": "median_playtime_2weeks",
    "Developers": "developers",
    "Publishers": "publishers",
    "Categories": "categories",
    "Genres": "genres",
    "Tags": "tags",
    "Screenshots": "screenshots",
    "Movies": "movies",
}
# the columns in the classroom copy, in this order
CLASSROOM_COLUMNS = [
    "AppID", "Name", "Release date", "Price", "Positive", "Negative",
    "Recommendations", "Metacritic score", "Achievements", "Developers",
    "Publishers", "Genres", "Support email",
]
# list fields the published CSV writes as Python lists: ['English', 'French']
AS_PYTHON_LIST = {"supported_languages", "full_audio_languages"}



# --------------------------------------------------------------- download

def step_download():
    console.rule("download: games.json from Hugging Face")
    RAW.mkdir(parents=True, exist_ok=True)
    part = JSON_PATH.with_suffix(".json.part")
    request = urllib.request.Request(DATASET_URL, headers={"User-Agent": "steam-data-stories (classroom project)"})
    columns = (TextColumn("{task.description}"), BarColumn(), DownloadColumn(),
               TransferSpeedColumn(), TimeRemainingColumn())
    with urllib.request.urlopen(request, timeout=60) as response, part.open("wb") as file, \
            Progress(*columns, console=console) as progress:
        total = int(response.headers.get("Content-Length") or 0) or None
        task = progress.add_task("games.json", total=total)
        done = 0
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            file.write(chunk)
            done += len(chunk)
            progress.update(task, advance=len(chunk))
    if total and done != total:
        console.print(f"[red]Download incomplete ({done} of {total} bytes); games.json not replaced. Run again.")
        sys.exit(1)
    part.replace(JSON_PATH)
    console.print(f"Saved {done // 2**20} MB to {JSON_PATH.relative_to(ROOT)}")


# ------------------------------------------------------------------ games

def records(text):
    """Yield (app_id, record, position) for each game in the top-level JSON object."""
    decoder = json.JSONDecoder()
    index = text.index("{") + 1
    length = len(text)
    while index < length:
        while index < length and text[index] in " \t\r\n,":
            index += 1
        if index >= length or text[index] == "}":
            break
        key, index = decoder.raw_decode(text, index)
        while text[index] in " \t\r\n:":
            index += 1
        value, index = decoder.raw_decode(text, index)
        yield key, value, index


def to_text(field, value):
    """Write one value the way the published CSV does."""
    if value is None:
        return ""
    if isinstance(value, dict):
        return ",".join(value.keys())
    if isinstance(value, list):
        if field in AS_PYTHON_LIST:
            return repr(value)
        return ",".join(str(item) for item in value)
    return str(value)


def tag_names(game):
    tags = game.get("tags") or {}
    return set(tags.keys() if isinstance(tags, dict) else tags)


def adult_reasons(game):
    """Return the reasons a game should be excluded (empty list = keep)."""
    reasons = []
    name = game.get("name") or ""
    tags = game.get("tags") or {}
    if "NSFW" in tags:
        if isinstance(tags, dict):
            ranked = sorted(tags, key=lambda tag: -tags[tag])
            reasons.append(f"tag NSFW (rank {ranked.index('NSFW') + 1} of {len(ranked)}, "
                           f"{tags['NSFW']} votes, top tag {tags[ranked[0]]} votes)")
        else:
            reasons.append("tag NSFW")
    notes = game.get("notes") or ""
    for match in re.finditer(r"explicit", notes, re.IGNORECASE):
        before = notes[max(0, match.start() - 25):match.start()]
        after = notes[match.end():match.end() + 40]
        if NEGATED.search(before):
            continue
        if SEXUAL_NEAR_EXPLICIT.search(before[-15:]) or SEXUAL_NEAR_EXPLICIT.search(after):
            snippet = " ".join(notes[max(0, match.start() - 60):match.end() + 60].split())
            reasons.append(f"notes: ...{snippet}...")
            break
    genres = set(game.get("genres") or []) & ADULT_GENRES
    if genres:
        reasons.append("genre " + "/".join(sorted(genres)))
    match = EXPLICIT_NAME.search(name)
    if match:
        reasons.append("name: " + match.group(0))
    match = SWEARING.search(name)
    if match:
        reasons.append("name swearing: " + match.group(0))
    return reasons


def load_overrides():
    overrides = {}
    if OVERRIDES.exists():
        with OVERRIDES.open(encoding="utf-8", newline="") as file:
            for row in csv.DictReader(file):
                decision = row.get("Decision", "").strip().lower()
                if decision in ("exclude", "keep"):
                    overrides[row["AppID"].strip()] = decision
    return overrides


def build_row(app_id, game):
    return [app_id if COLUMNS[name] is None else to_text(COLUMNS[name], game.get(COLUMNS[name]))
            for name in CLASSROOM_COLUMNS]


def step_games():
    console.rule("games: building the classroom games CSV")
    if not JSON_PATH.exists():
        console.print(f"[red]Missing {JSON_PATH.relative_to(ROOT)}: run the download step first")
        sys.exit(1)
    overrides = load_overrides()
    excluded = []
    skipped = Counter()
    count = 0
    with console.status("Reading games.json"):
        text = JSON_PATH.read_text(encoding="utf-8")
    with OUT.open("w", encoding="utf-8", newline="") as file, bar_progress() as progress:
        task = progress.add_task("Building steam_games.csv", total=len(text))
        writer = csv.writer(file)
        writer.writerow(CLASSROOM_COLUMNS)
        for app_id, game, position in records(text):
            progress.update(task, completed=position)
            reviews = (game.get("positive") or 0) + (game.get("negative") or 0)
            if reviews < MIN_REVIEWS:
                skipped[f"fewer than {MIN_REVIEWS} reviews"] += 1
                continue
            if not game.get("genres"):
                skipped["no genres"] += 1
                continue
            reasons = adult_reasons(game)
            decision = "exclude" if reasons else "keep"
            if app_id in overrides:
                decision = overrides[app_id]
                reasons = reasons + ["override"]
            if decision == "exclude":
                excluded.append([app_id, game.get("name") or "", game.get("recommendations") or 0, "; ".join(reasons)])
                continue
            writer.writerow(build_row(app_id, game))
            count += 1
        progress.update(task, completed=len(text))
    with EXCLUDED.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["AppID", "Name", "Recommendations", "Reasons"])
        writer.writerows(sorted(excluded, key=lambda entry: -int(entry[2])))
    print(f"Wrote {count} games to {OUT.relative_to(ROOT)}")
    for reason, number in skipped.items():
        print(f"Skipped {number} games with {reason}")
    print(f"Excluded {len(excluded)} adult games (list in {EXCLUDED.relative_to(ROOT)})")
    if overrides:
        print(f"Applied {len(overrides)} decisions from {OVERRIDES.relative_to(ROOT)}")


# ------------------------------------------------------------------ audit

FULL_DATE = re.compile(r"^[A-Z][a-z]{2} \d{1,2}, \d{4}$")
EMAIL = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
YEAR = re.compile(r"(\d{4})")


def step_audit():
    console.rule("audit: data cleaning issues in the classroom games CSV")
    if not OUT.exists():
        console.print(f"[red]Missing {OUT.relative_to(ROOT)}: run the games step first")
        sys.exit(1)
    issues = Counter()
    date_shapes = Counter()
    names = Counter()
    years = Counter()
    rows = 0
    with OUT.open(encoding="utf-8", newline="") as file, count_progress() as progress:
        task = progress.add_task("Checking steam_games.csv", total=None, unit="games")
        for row in csv.DictReader(file):
            rows += 1
            progress.advance(task)
            names[row["Name"].strip().lower()] += 1
            date = row["Release date"]
            match = YEAR.search(date)
            years[match.group(1) if match else "none"] += 1
            if not date:
                issues["release date empty"] += 1
            elif not FULL_DATE.match(date):
                issues["release date not 'Mon D, YYYY'"] += 1
                date_shapes[re.sub(r"\d", "9", re.sub(r"[A-Za-z]+", "Aaa", date))] += 1
            if row["Metacritic score"] == "0":
                issues["Metacritic score 0 (means none)"] += 1
            if row["Price"] in ("0", "0.0"):
                issues["price 0 (free)"] += 1
            if "Indie" in row["Genres"].split(","):
                issues["Indie games"] += 1
            if not row["Genres"]:
                issues["genres empty"] += 1
            if EMAIL.search(row["Support email"]):
                issues["support email present (personal information)"] += 1
            if not row["Name"]:
                issues["name empty"] += 1
    issues["games sharing a name with another game"] = sum(count for count in names.values() if count > 1)

    print(f"{OUT.name}: {rows} rows, {len(CLASSROOM_COLUMNS)} columns, {OUT.stat().st_size // 1024} KB")
    for label, count in sorted(issues.items(), key=lambda item: -item[1]):
        print(f"  {count:>7}  {label}")
    if date_shapes:
        print("Release date shapes other than 'Mon D, YYYY':")
        for shape, count in date_shapes.most_common(8):
            print(f"  {count:>7}  {shape!r}")
    print("Games per release year:")
    print("  " + "  ".join(f"{year}: {years[year]}" for year in sorted(years)))


# ---------------------------------------------------------------- package

README = """Steam Data Stories: classroom data ({today})

Files
  steam_games.csv   one row per Steam game ({games} games with at least
                    {min_reviews:,} reviews)

The data is real and has NOT been cleaned. Cleaning it is part of the
course: https://damom73.github.io/steam-data-stories/

Sources
  steam_games.csv is built from the Steam Games Dataset by Fronkon Games
  (https://huggingface.co/datasets/FronkonGames/steam-games-dataset),
  downloaded {today}, which collects data from the Steam store and SteamSpy.
  Changes made for the classroom copy:
    - only games with at least {min_reviews:,} reviews are included
    - only {columns} columns are kept
    - games with no genres are removed
    - games with adult content are removed

Licences
  The Steam Games Dataset is published under the MIT licence:

  Copyright (c) Fronkon Games

  Permission is hereby granted, free of charge, to any person obtaining a
  copy of this software and associated documentation files (the
  "Software"), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to permit
  persons to whom the Software is furnished to do so, subject to the
  following conditions:

  The above copyright notice and this permission notice shall be included
  in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
  NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
  USE OR OTHER DEALINGS IN THE SOFTWARE.

  Steam and game names are trademarks of their owners. This data is for
  classroom use and isn't affiliated with Valve or Steam.
"""


def step_package():
    console.rule("package: zipping the classroom data")
    if not OUT.exists():
        console.print(f"[red]Missing {OUT.relative_to(ROOT)}: run the games step first")
        sys.exit(1)
    with OUT.open(encoding="utf-8", newline="") as file:
        games = sum(1 for _ in csv.reader(file)) - 1
    readme = README.format(today=TODAY, games=games, min_reviews=MIN_REVIEWS,
                           columns=len(CLASSROOM_COLUMNS))
    with zipfile.ZipFile(PACKAGE, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr("README.txt", readme)
        archive.write(OUT, "steam_games.csv")
    size = PACKAGE.stat().st_size // 1024
    print(f"Wrote {PACKAGE.relative_to(ROOT)} ({size} KB)")
    print()
    print("To publish it:")
    print("  1. On GitHub, open DamoM73/steam-data-stories > Releases > Draft a new release.")
    print(f"  2. Tag: data-{TODAY}   Title: Classroom data {TODAY}")
    print(f"  3. Drag {PACKAGE.name} into the release, then Publish release.")


# ------------------------------------------------------------------- show

def show(app_ids):
    """Print the raw games.json record for each app ID, long text skipped."""
    skip = {"detailed_description", "about_the_game", "short_description", "reviews",
            "screenshots", "movies", "header_image", "packages"}
    text = JSON_PATH.read_text(encoding="utf-8")
    decoder = json.JSONDecoder()
    for app_id in app_ids:
        start = text.find(f'"{app_id}":')
        if start == -1:
            print(f"{app_id}: not found")
            continue
        record, _ = decoder.raw_decode(text, text.index("{", start))
        print(f"{app_id}:")
        for field, value in record.items():
            if field not in skip:
                print(f"  {field}: {repr(value)[:120]}")


def main():
    parser = argparse.ArgumentParser(description="Collect and build the Steam Data Stories data.")
    parser.add_argument("steps", nargs="*", choices=STEPS,
                        help="steps to run (default: all four, in order)")
    parser.add_argument("--show", nargs="+", metavar="APP_ID", help="print raw games.json records and stop")
    args = parser.parse_args()
    if args.show:
        show(args.show)
        return
    steps = args.steps or STEPS
    actions = {"download": step_download, "games": step_games,
               "audit": step_audit, "package": step_package}
    for step in STEPS:
        if step in steps:
            actions[step]()


if __name__ == "__main__":
    main()
