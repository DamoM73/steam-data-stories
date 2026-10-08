indie_score = per_group["Median review score"][0]
other_score = per_group["Median review score"][1]
mo.md(
    f"""
    ## Players like Indie games more

    The typical Indie game gets **{indie_score}%** positive reviews,
    compared with **{other_score}%** for other games.
    """
)
