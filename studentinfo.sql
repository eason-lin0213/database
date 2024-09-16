CREATE DATABASE IF NOT EXISTS testdb;

USE testdb;


CREATE TABLE studentinfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);
