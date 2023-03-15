-- Display the maximum temperature of each state
-- Query to display maximum temperature of each state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state LIMIT 3;
