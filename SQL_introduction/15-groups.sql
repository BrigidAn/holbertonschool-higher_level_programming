-- Select the score and the number of occurrences from second_table, grouped by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;