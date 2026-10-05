gaps = clean_history.with_columns(
    pl.col("Time").diff().over("AppID").alias("Gap")
).filter(pl.col("Gap") > pl.duration(hours=3))
gaps.select("AppID", "Time", "Gap")
