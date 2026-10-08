clean_games.filter(pl.col("Name").is_duplicated()).sort("Name")
