-- Display top 3 cities in July and August
-- Query to display average top cities
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
