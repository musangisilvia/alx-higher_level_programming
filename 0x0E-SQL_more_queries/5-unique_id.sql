-- create the table unique_id
-- id has default value of 1 and is unique
-- database name is passed in the command line

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
