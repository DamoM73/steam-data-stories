px.scatter(
    scored.filter(pl.col("Recommendations") >= 1000),
    x="Price",
    y="Review score",
    hover_name="Name",
    opacity=0.4,
    title="Expensive games don't get better reviews",
)
