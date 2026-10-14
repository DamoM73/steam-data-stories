SELECT developers, COUNT(*) AS games, ROUND(AVG(review_score), 1) AS mean_score
FROM games
GROUP BY developers
HAVING COUNT(*) >= 5
ORDER BY mean_score DESC
LIMIT 10
