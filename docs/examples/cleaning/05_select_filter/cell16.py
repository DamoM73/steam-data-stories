indie_games = selected.filter(pl.col("Genres").str.contains("Indie"))
indie_games
