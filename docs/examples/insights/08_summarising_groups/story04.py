per_group = (
    scored.group_by("Group")
    .agg(
        pl.len().alias("Games"),
        pl.col("Review score").median().alias("Median review score"),
    )
    .sort("Group")
)
per_group
