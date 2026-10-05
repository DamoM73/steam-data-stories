per_genre = (
    scored.explode("Genres")
    .group_by("Genres")
    .agg(
        pl.len().alias("Games"),
        pl.col("Review score").median().alias("Median review score"),
    )
    .sort("Games", descending=True)
    .head(10)
)
per_genre
