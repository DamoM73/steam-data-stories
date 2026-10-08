prices = (
    scored.group_by("Group")
    .agg(
        pl.col("Price").median().alias("Median price"),
        pl.col("Price").mean().round(2).alias("Mean price"),
    )
    .sort("Group")
)
prices
