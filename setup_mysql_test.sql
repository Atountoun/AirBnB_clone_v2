-- script that prepares a MySQL server for the project

-- create database `hbnb_test_db`
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- add a new user `hbnb_testv` (in localhost) and set password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on `hbnb_test_db` to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privilege on `performance_schema` to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- reload grant tables
FLUSH PRIVILEGES;
