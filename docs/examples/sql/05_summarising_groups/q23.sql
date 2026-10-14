SELECT developers, COUNT(*) AS games
FROM games
GROUP BY developers
ORDER BY games DESC
LIMIT 10
