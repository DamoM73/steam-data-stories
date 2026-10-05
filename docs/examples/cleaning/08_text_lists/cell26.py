genre_counts = clean_games.explode("Genres")["Genres"].value_counts(sort=True)
genre_counts
