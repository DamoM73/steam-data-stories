paid_games = selected.filter(pl.col("Price") > 0)
paid_games.height
