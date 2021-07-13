-- creates database hbtn_0d_usa and table states
-- both queries don't fail if db or user exist

-- CREATE DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- CREATE TABLE
CREATE TABLE IF NOT EXISTS states (id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
name VARCHAR(256) NOT NULL);
