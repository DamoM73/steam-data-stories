recent = per_year.filter(pl.col("Release year").is_between(2019, 2024))
average_growth = recent["Games"].diff().mean()
prediction_2025 = recent["Games"][-1] + average_growth
average_growth, prediction_2025
