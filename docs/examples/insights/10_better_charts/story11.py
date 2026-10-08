px.box(
    scored,
    x="Group",
    y="Review score",
    color="Group",
    category_orders={"Group": ["Indie", "Not Indie"]},
    labels={"Group": "", "Review score": "Positive reviews (%)"},
    title="Indie games get a higher share of positive reviews",
)
