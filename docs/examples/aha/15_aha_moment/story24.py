first_year = monthly.filter(pl.col("Month") <= 11)
aha_chart = px.line(
    first_year,
    x="Month",
    y="Percent of peak",
    color="Name",
    markers=True,
    color_discrete_map={
        "ARC Raiders": "#D62728",
        "Marathon": "#BBBBBB",
        "Escape from Tarkov": "#BBBBBB",
        "Gray Zone Warfare": "#BBBBBB",
        "Arena Breakout: Infinite": "#BBBBBB",
        "Escape from Duckov": "#BBBBBB",
    },
    labels={
        "Month": "Months since launch",
        "Percent of peak": "Players (% of busiest month)",
    },
    title="ARC Raiders kept its players for three months, then lost most of them",
)
aha_chart.add_annotation(
    x=4,
    y=52,
    text="Half its peak after 4 months",
    showarrow=True,
)
aha_chart
