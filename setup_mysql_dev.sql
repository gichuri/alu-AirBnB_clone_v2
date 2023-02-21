--create a new database and user
--grant user priviledges

CREATE DATABASE IF NOT EXISTS 'hbnb_dev_db';
CREATE USER IF NOT EXISTS 'hbnb_dev' IDENTIFIED BY  'hbnb_dev_pwd';
GRANT ALL *.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema* TO 'hbnb_dev'@'localhost';
