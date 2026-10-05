"""Download the full hourly player history for Steam games.

Uses the Games Popularity API (https://games-popularity.com/api-docs),
which returns up to 1,000 hourly records per request, newest first,
with a nextCursor value for the next (older) page. This script keeps
requesting older pages until there are none left, then saves every
record, unchanged, for each game to data/player_history/<app_id>.json.

Without an API key the limit is 100 requests per day per IP address,
so the script waits between requests and stops at MAX_REQUESTS. With a
free key the limit is 1 request per second and there's no daily cap.
To use a key, set it as an environment variable before running the
script (it's never saved in the repo):
    PowerShell:  $env:GAMES_POPULARITY_KEY = "your-key"

Run from the repo root:
    python scripts/fetch_player_history.py 1808500
    python scripts/fetch_player_history.py 1808500 3932890
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "player_history"
URL = "https://games-popularity.com/swagger/api/game/players/{app_id}"
API_KEY = os.environ.get("GAMES_POPULARITY_KEY", "").strip()
WAIT_SECONDS = 1.2 if API_KEY else 2
MAX_REQUESTS = 500 if API_KEY else 60


def fetch_page(app_id, cursor=None):
    """Return one page of history as a dict."""
    url = URL.format(app_id=app_id)
    params = {}
    if cursor:
        params["cursor"] = cursor
    if API_KEY:
        params["apiKey"] = API_KEY
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": "steam-data-stories (classroom project)"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_history(app_id, budget):
    """Fetch every page for one game. Returns (records, requests used)."""
    records = []
    cursor = None
    used = 0
    while used < budget:
        page = fetch_page(app_id, cursor)
        used += 1
        history = page.get("history", [])
        records.extend(history)
        oldest = history[-1]["added"] if history else "none"
        print(f"  page {used}: {len(history)} records, oldest {oldest}")
        cursor = page.get("nextCursor")
        if not history or not cursor:
            break
        time.sleep(WAIT_SECONDS)
    else:
        print(f"  stopped at the request limit ({budget}); history may be incomplete")
    return records, used


def main():
    app_ids = sys.argv[1:]
    if not app_ids:
        print("Give at least one Steam app ID, for example: python scripts/fetch_player_history.py 1808500")
        sys.exit(1)
    OUT.mkdir(parents=True, exist_ok=True)
    print("Using API key" if API_KEY else "No API key: limited to 100 requests per day")
    remaining = MAX_REQUESTS
    for app_id in app_ids:
        print(f"Game {app_id}")
        records, used = fetch_history(app_id, remaining)
        remaining -= used
        # saved raw (newest first, repeats and gaps kept) so the
        # cleaning lessons have the real data to work with
        path = OUT / f"{app_id}.json"
        path.write_text(json.dumps({"steamId": app_id, "history": records}, indent=1), encoding="utf-8")
        if records:
            print(f"  saved {len(records)} records ({records[-1]['added']} to {records[0]['added']}) to {path.relative_to(ROOT)}")
        if remaining <= 0:
            print("Request limit reached; run again tomorrow for the remaining games.")
            break


if __name__ == "__main__":
    main()
