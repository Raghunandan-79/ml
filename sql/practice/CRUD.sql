CREATE DATABASE IF NOT EXISTS ShopDB;

USE ShopDB;

CREATE TABLE Customers (
	CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    City VARCHAR(200)
);

INSERT INTO Customers (Name, Email, City)
VALUES
('Amit Kumar', 'amit@email.com', 'Delhi, India'),
('Neha Verma', 'neha@email.com', 'Bangalore, India'),
('Rahul Sharma', 'rahul@email.com', 'Bangalore, India');

SELECT * FROM Customers;

UPDATE Customers
SET City = 'Pune, India'
WHERE Name = 'Rahul Sharma';

SELECT * FROM Customers;

DELETE FROM Customers
WHERE NAME = 'Neha Verma';