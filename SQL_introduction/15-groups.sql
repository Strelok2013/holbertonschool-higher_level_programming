-- Returns a table with score and the amount of entries with the same score
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;