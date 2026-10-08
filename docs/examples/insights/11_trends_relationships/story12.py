per_year_group = (
    scored.filter(pl.col("Release year").is_between(2010, 2024))
    .group_by("Release year", "Group")
    .agg(pl.col("Review score").median().alias("Median review score"))
    .sort("Release year", "Group")
)
per_year_group
