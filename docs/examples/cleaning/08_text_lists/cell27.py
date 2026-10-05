extraction_shooters = clean_games.filter(
    pl.col("Tags").list.contains("Extraction Shooter")
)
extraction_shooters.select("AppID", "Name", "Release date")
