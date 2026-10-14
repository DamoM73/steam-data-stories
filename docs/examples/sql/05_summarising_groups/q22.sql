SELECT indie, COUNT(*) AS games, ROUND(AVG(price), 2) AS mean_price
FROM games
GROUP BY indie
