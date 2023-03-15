-- Create a Database and a Table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select database
USE hbtn_0d_usa;

-- Query to create cities table with constraint
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
