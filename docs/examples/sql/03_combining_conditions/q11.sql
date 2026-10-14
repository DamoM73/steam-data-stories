SELECT name, developers, price
FROM games
WHERE (developers = 'Valve' OR developers = 'Team Cherry') AND price > 10
