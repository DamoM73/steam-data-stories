recent = full_years.filter(pl.col("Release year") >= 2020)
average_growth = recent["Games"].diff().mean()
prediction_2026 = recent["Games"][-1] + average_growth
round(average_growth), round(prediction_2026)
