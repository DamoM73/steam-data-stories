q1 = scored["Price"].quantile(0.25)
q3 = scored["Price"].quantile(0.75)
upper_fence = q3 + 1.5 * (q3 - q1)
price_outliers = scored.filter(pl.col("Price") > upper_fence)
upper_fence, price_outliers.height
