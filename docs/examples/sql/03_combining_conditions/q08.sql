SELECT name, price, review_score
FROM games
WHERE indie = 1 AND review_score >= 98
