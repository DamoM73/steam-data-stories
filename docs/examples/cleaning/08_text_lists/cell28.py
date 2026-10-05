clean_games.filter(
    pl.col("Name").str.to_lowercase() == "escape from duckov"
).select("AppID", "Name")
