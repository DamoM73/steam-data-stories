explore = (
    scored.filter(
        pl.col("Release year").is_between(years.value[0], years.value[1])
    )
    .group_by("Release year", "Group")
    .agg(pl.col(measure.value).median().alias("Median"))
    .sort("Release year", "Group")
)
explore_chart = px.line(
    explore,
    x="Release year",
    y="Median",
    color="Group",
    color_discrete_map={"Indie": "royalblue", "Not Indie": "lightgrey"},
    markers=True,
    title=f"Median {measure.value.lower()} of Indie and other games",
)
mo.vstack([mo.hstack([years, measure]), explore_chart, explore])
