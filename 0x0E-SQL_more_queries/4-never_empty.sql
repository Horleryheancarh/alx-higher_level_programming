-- Create a table thats never empty
-- Query to Table a table with a default value
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
