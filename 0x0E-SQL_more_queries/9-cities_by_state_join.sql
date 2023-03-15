-- List all cities in the database
SELECT cities.id, cities.name, states.name FROM cities
-- Join cities and states
JOIN states ON cities.state_id = states.id;
