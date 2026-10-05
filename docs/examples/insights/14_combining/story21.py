monthly = (
    clean_history.with_columns(
        (
            (pl.col("Time") - pl.col("Time").min().over("AppID")).dt.total_days()
            // 30
        ).alias("Month")
    )
    .group_by("AppID", "Month")
    .agg(pl.col("players").max().alias("Peak players"))
    .with_columns(
        (pl.col("Peak players") / pl.col("Peak players").max().over("AppID") * 100)
        .round(1)
        .alias("Percent of peak")
    )
    .join(story_games, on="AppID")
    .sort("AppID", "Month")
)
monthly
