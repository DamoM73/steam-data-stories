monthly.filter(pl.col("Month") == 6).select(
    "Name", "PvE", "Percent of peak"
).sort("Percent of peak", descending=True)
