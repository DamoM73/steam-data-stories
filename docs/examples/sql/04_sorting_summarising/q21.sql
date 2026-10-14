SELECT COUNT(*) AS games, ROUND(AVG(review_score), 1) AS mean_score
FROM games
WHERE release_date BETWEEN '2024-01-01' AND '2024-12-31'
