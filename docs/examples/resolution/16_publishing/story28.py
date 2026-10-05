arc_month_6 = monthly.filter(
    pl.col("Name") == "ARC Raiders", pl.col("Month") == 6
)["Percent of peak"][0]
mo.md(
    f"""
    ## What we found

    Six months after launch, ARC Raiders still had **{arc_month_6}%**
    of its peak players. Escape from Tarkov and Arena Breakout: Infinite
    kept more than half of theirs, but Marathon, Gray Zone Warfare and
    Escape from Duckov had all fallen below 5%.
    """
)
