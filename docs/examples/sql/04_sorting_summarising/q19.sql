SELECT COUNT(*) AS games, MIN(price) AS lowest, MAX(price) AS highest, ROUND(AVG(price), 2) AS mean_price
FROM games
