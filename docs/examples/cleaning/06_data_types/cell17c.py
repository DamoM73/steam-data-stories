typed = selected.with_columns(
    pl.col("Release date").str.to_date("%b %d, %Y"),
    pl.col("Estimated owners").cast(pl.Int64),
)
typed
