SELECT name, positive + negative AS reviews
FROM games
ORDER BY reviews DESC
LIMIT 10
