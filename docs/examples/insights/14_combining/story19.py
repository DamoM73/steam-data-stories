clean_history = (
    history.with_columns(
        pl.col("AppID").cast(pl.Int64),
        pl.col("added")
        .str.to_datetime()
        .dt.replace_time_zone("UTC")
        .dt.convert_time_zone("Australia/Brisbane")
        .alias("Time"),
    )
    .unique(subset=["AppID", "Time"])
    .sort("AppID", "Time")
)
clean_history
