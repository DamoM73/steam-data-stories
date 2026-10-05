game_picker = mo.ui.multiselect(
    options=story_games["Name"].to_list(),
    value=["ARC Raiders", "Escape from Tarkov"],
    label="Games",
)
month_slider = mo.ui.slider(1, 11, value=11, label="Months since launch")
mo.hstack([game_picker, month_slider])
