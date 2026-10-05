px.box(
    scored.filter(pl.col("Recommendations") >= 100),
    x="Price band",
    y="Review score",
    category_orders={
        "Price band": ["Free", "Under $10", "$10 to $30", "$30 and over"]
    },
    title="Review scores are similar at every price",
)
