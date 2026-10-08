scored = games.with_columns(
    (pl.col("Positive") / (pl.col("Positive") + pl.col("Negative")) * 100)
    .round(1)
    .alias("Review score"),
    pl.col("Release date").dt.year().alias("Release year"),
    pl.when(pl.col("Genres").str.contains("Indie"))
    .then(pl.lit("Indie"))
    .otherwise(pl.lit("Not Indie"))
    .alias("Group"),
)
scored.select("Name", "Review score", "Release year", "Genres", "Group")
