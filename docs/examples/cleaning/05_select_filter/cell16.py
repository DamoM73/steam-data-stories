story_rows = selected.filter(
    pl.col("AppID").is_in(story_games["AppID"].to_list())
)
story_rows
