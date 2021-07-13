-- creates database hbtn_0d_2 and user user_0d_2
-- user_0d_2 only has SELECT privilege in the database
-- user_0d_2 has password.
-- both queries don't fail if db or user exist

-- CREATE DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- CREATE USER
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';

-- GRANT USER privileges
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
