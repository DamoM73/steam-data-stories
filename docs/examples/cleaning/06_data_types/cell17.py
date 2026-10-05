typed = selected.with_columns(
    pl.col("Release date").str.to_date("%b %d, %Y"),
    pl.col("Estimated owners")
    .str.split(" - ")
    .list.first()
    .cast(pl.Int64)
    .alias("Owners min"),
    pl.col("Estimated owners")
    .str.split(" - ")
    .list.last()
    .cast(pl.Int64)
    .alias("Owners max"),
)
typed
