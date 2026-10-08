price_outliers.group_by("Group").agg(pl.len().alias("Games")).sort("Group")
