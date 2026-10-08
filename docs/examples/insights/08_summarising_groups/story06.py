per_year = (
    scored.group_by("Release year")
    .agg(
        pl.len().alias("Games"),
        pl.col("Review score").median().alias("Median review score"),
    )
    .sort("Release year")
)
per_year
