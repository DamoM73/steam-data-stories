story_games.join(games.select("Name", "Release date"), on="Name", how="left")
