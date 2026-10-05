per_year = (
    scored.group_by("Release year")
    .agg(
        pl.len().alias("Games"),
        pl.col("Price").median().alias("Median price"),
    )
    .sort("Release year")
)
per_year
