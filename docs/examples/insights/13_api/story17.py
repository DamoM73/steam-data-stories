history_frames = []
for app_id in story_games["AppID"]:
    with open(f"data/player_history/{app_id}.json") as file:
        saved = json.load(file)
    history_frames.append(
        pl.DataFrame(saved["history"]).with_columns(
            pl.lit(saved["steamId"]).alias("AppID")
        )
    )
history = pl.concat(history_frames)
history
