typed.filter(pl.col("Name").is_duplicated()).sort("Name")
