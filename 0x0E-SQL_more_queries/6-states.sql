-- Create a Database and a Table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select database
USE hbtn_0d_usa;

-- Query to create states table with constraint
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
