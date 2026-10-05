per_band = (
    scored.group_by("Price band")
    .agg(
        pl.len().alias("Games"),
        pl.col("Recommendations").median().alias("Median recommendations"),
        pl.col("Recommendations").mean().round(0).alias("Mean recommendations"),
    )
    .sort("Games", descending=True)
)
per_band
