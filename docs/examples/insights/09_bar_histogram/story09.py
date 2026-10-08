px.histogram(
    scored,
    x="Review score",
    color="Group",
    barmode="overlay",
    histnorm="percent",
    nbins=45,
    title="Review scores of Indie and other games",
)
