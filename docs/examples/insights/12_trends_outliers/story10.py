full_years = per_year.filter(pl.col("Release year").is_between(2006, 2025))
px.line(
    full_years,
    x="Release year",
    y="Games",
    markers=True,
    title="Steam releases have boomed since 2013",
)
