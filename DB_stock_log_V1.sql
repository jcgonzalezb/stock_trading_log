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
	user_id VARCHAR(60) NOT NULL, 
    email VARCHAR(128) UNIQUE NOT NULL,
    hashed_password VARCHAR(128) NOT NULL,
    session_id VARCHAR(128) NOT NULL,
    PRIMARY KEY (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--
INSERT INTO user(user_id, user_name, email, hashed_password, session_id) VALUES ("1", "John Doe", "123@gmail.com", "ABCDE", "qeqweqw");
UNLOCK TABLES;


--
-- Table structure for table `trade`
--
DROP TABLE IF EXISTS trade;
CREATE TABLE trade (
	trade_id VARCHAR(60) NOT NULL,
	user_id VARCHAR(60) NOT NULL, 
	trade_status VARCHAR(60) NOT NULL,
	trade VARCHAR(60) NOT NULL,
    company VARCHAR(128) NOT NULL,
    ticker VARCHAR(60) NOT NULL, 
    quantity int NOT NULL,
    price FLOAT NOT NULL,
	trade_date date NOT NULL,
    PRIMARY KEY (`trade_id`),
	FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `trade`
--
INSERT INTO trade(trade_id, trade_status, user_id, trade, company, ticker, quantity, price, trade_date) VALUES ("AB", "enable", "1", "Buy","Tesla", "TSLA",5, 134.5, "2022-03-21");
UNLOCK TABLES;