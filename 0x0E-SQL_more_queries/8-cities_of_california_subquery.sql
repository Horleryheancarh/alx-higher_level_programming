-- List all Carlfornian cities in the database
SELECT id, name FROM cities WHERE state_id = (
	-- Select Carlifornia id from states
	SELECT id FROM states WHERE name = "Carlifonia"
);
