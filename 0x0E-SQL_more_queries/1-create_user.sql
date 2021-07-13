-- creates user user_0d_1 with password user_0d_1_pwd
-- with all privileges.
-- does not fail if user exists

CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL
ON *.*
TO user_0d_1@localhost
