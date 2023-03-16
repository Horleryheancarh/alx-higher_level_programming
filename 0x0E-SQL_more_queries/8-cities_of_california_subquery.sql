-- List all Californian cities in the database
SELECT id, name FROM cities WHERE state_id = (
	-- Select California id from states
	SELECT id FROM states WHERE name = 'California'
);
