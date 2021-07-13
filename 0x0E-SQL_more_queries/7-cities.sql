-- creates database hbtn_0d_usa and table cities
-- both queries don't fail if db or user exist

-- CREATE DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- CREATE TABLE
CREATE TABLE IF NOT EXISTS cities (id INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
state_id INT NOT NULL,
name VARCHAR(256),
INDEX(state_id),
FOREIGN KEY (state_id) REFERENCES states(id));
