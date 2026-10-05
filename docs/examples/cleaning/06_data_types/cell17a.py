typed = selected.with_columns(
    pl.col("Release date").str.to_date(),
)
typed
