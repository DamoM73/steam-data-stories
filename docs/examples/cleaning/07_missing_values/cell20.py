missing = typed.with_columns(
    pl.col("Peak CCU").replace(0, None),
    pl.col("Metacritic score").replace(0, None),
    pl.col("Owners max").replace(0, None),
)
missing.null_count()
