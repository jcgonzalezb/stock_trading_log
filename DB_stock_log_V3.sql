-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS stock_log_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON stock_log_db.* TO root@localhost;

USE stock_log_db;

--
-- Table structure for table `user`
--
DROP TABLE IF EXISTS trade;
DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(128) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    name VARCHAR(128),
    PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Table structure for table `trade`
--
DROP TABLE IF EXISTS trade;
CREATE TABLE trade (
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
	FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;
