aha_chart = px.line(
    per_year_group,
    x="Release year",
    y="Median review score",
    color="Group",
    color_discrete_map={"Indie": "royalblue", "Not Indie": "lightgrey"},
    markers=True,
    labels={"Release year": "", "Median review score": "Positive reviews (%)"},
    title="Since 2017, Indie games have reviewed better every year",
)
aha_chart.add_annotation(
    x=2018,
    y=87.05,
    text="From 2018, Indie games stay about 4 to 8 points ahead",
    ax=-120,
    ay=-40,
)
aha_chart
