scored = games.with_columns(
    (pl.col("Positive") / (pl.col("Positive") + pl.col("Negative")) * 100)
    .round(1)
    .fill_nan(None)
    .alias("Review score"),
)
scored.select("Name", "Positive", "Negative", "Review score")
