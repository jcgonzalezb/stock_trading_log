-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS stock_log_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON stock_log_db.* TO root@localhost;

USE stock_log_db;

--
-- Table structure for table `users`
--
DROP TABLE IF EXISTS trades;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(128) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    name VARCHAR(128),
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Table structure for table `trades`
--
DROP TABLE IF EXISTS trades;
CREATE TABLE trades (
	trade_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	user_id INT UNSIGNED NOT NULL,
	trade_status VARCHAR(60) NOT NULL,
	trade VARCHAR(60) NOT NULL,
    company VARCHAR(128) NOT NULL,
    ticker VARCHAR(60) NOT NULL, 
    quantity int NOT NULL,
    price FLOAT NOT NULL,
	trade_date date NOT NULL,
    PRIMARY KEY (`trade_id`),
	FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;
