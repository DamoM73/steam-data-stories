scored = games.with_columns(
    (pl.col("Positive") / (pl.col("Positive") + pl.col("Negative")) * 100)
    .round(1)
    .fill_nan(None)
    .alias("Review score"),
    pl.col("Release date").dt.year().alias("Release year"),
    pl.when(pl.col("Price") == 0)
    .then(pl.lit("Free"))
    .when(pl.col("Price") < 10)
    .then(pl.lit("Under $10"))
    .when(pl.col("Price") < 30)
    .then(pl.lit("$10 to $30"))
    .otherwise(pl.lit("$30 and over"))
    .alias("Price band"),
)
scored.select(
    "Name", "Review score", "Release date", "Release year", "Price", "Price band"
)
