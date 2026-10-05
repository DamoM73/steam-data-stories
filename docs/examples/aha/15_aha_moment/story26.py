picked = monthly.filter(
    pl.col("Name").is_in(game_picker.value),
    pl.col("Month") <= month_slider.value,
)
px.line(
    picked,
    x="Month",
    y="Percent of peak",
    color="Name",
    line_dash="PvE",
    markers=True,
    title="Compare any of our games",
)
