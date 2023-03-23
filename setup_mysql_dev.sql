-- script that prepares a MySQL server for the project

-- create database `hbnb_dev_db`
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- add a new user `hbnb_dev` (in localhost) and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on `hbnb_dev_db` to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant select privilege on `performance_schema` to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- reload grant tables
FLUSH PRIVILEGES;
