import plotly.express as px

px.bar(
    top_indie,
    x="mean_score",
    y="developers",
    orientation="h",
    title="The top 10 Indie developers all average over 93% positive reviews",
    labels={"mean_score": "Mean review score (%)", "developers": "Developer"},
)
