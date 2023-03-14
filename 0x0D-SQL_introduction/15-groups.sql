-- List records with the same score
-- Query to list records with same score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
