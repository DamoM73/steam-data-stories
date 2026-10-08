clean_games = dated.with_columns(
    pl.col("Metacritic score").replace(0, None),
)
clean_games.null_count()
