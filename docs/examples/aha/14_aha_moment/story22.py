px.line(
    explore,
    x="Release year",
    y="Median",
    color="Group",
    color_discrete_map={"Indie": "royalblue", "Not Indie": "lightgrey"},
    markers=True,
    title=f"Median {measure.value.lower()} of Indie and other games",
)
