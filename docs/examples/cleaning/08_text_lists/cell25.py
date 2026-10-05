clean_games = checked.with_columns(
    to_list("Genres"),
    to_list("Tags"),
    to_list("Categories"),
)
clean_games.select("Name", "Genres", "Tags")
