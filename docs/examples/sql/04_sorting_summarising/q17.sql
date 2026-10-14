SELECT name, review_score, positive
FROM games
ORDER BY review_score DESC, positive DESC
LIMIT 10
