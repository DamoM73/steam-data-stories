years = mo.ui.range_slider(
    start=2010,
    stop=2024,
    value=[2010, 2024],
    label="Years",
    show_value=True,
)
measure = mo.ui.dropdown(
    options=["Review score", "Price"],
    value="Review score",
    label="Measure",
)
