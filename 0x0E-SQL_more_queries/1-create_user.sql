-- Create a new user
-- Query to create a new user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
-- Set user password
IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
