px.histogram(
    scored.filter(pl.col("Price").is_between(0.01, 60)),
    x="Price",
    nbins=60,
    title="Most paid games cost less than $10",
)
