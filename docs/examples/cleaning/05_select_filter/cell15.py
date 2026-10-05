popular_paid = selected.filter(
    (pl.col("Price") > 0) & (pl.col("Recommendations") > 1000)
)
popular_paid.height
