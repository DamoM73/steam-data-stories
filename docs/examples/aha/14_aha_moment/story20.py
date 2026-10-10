explore = (
    scored.filter(
        pl.col("Release year").is_between(years.value[0], years.value[1])
    )
    .group_by("Release year", "Group")
    .agg(pl.col(measure.value).median().alias("Median"))
    .sort("Release year", "Group")
)
mo.vstack([mo.hstack([years, measure]), explore])
