

CREATE DATABASE IF NOT EXISTS madb;
CREATE USER IF NOT EXISTS 'dba'@'%' IDENTIFIED BY 'Password123$';

GRANT ALL PRIVILEGES ON madb.* TO 'dba'@'%';
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%';

grant all on *. * to 'dba'@'%' ;


FLUSH PRIVILEGES;
FLUSH PRIVILEGES;



CREATE TABLE users ( id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), email VARCHAR(100) );
INSERT INTO users (name, email) VALUES ('ali', 'ali@example.com');
INSERT INTO users (name, email) VALUES ('haldun', 'haldun@techniaa.com');
INSERT INTO users (name, email) VALUES ('haldun1', 'haldun@techniaa.com');
INSERT INTO users (name, email) VALUES ('omar', 'haldun@techniaa.com');
USE madb ; 

-- Debugging lines
SELECT User, Host FROM mysql.user;
SHOW GRANTS FOR 'dba'@'%';
