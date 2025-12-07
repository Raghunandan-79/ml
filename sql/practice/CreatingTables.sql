CREATE DATABASE IF NOT EXISTS CollegeDB;
USE CollegeDB;
SELECT DATABASE();

CREATE TABLE Students (
	StudentID INT AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(100),
    Age TINYINT,
    Email VARCHAR(100),
    JoinDate DATE
);

SELECT * FROM Students;

INSERT INTO Students(Name, Age, Email, JoinDate)
VALUES 
('Amit Gupta', 22, 'amit@email.com', '2025-02-19'),
('Aditi Sharma', 22, 'aditi@email.com', '2025-01-20');

ALTER TABLE Students ADD COLUMN City VARCHAR(50);
ALTER TABLE Students MODIFY Age SMALLINT;
ALTER TABLE Students RENAME COLUMN Email TO StudentEmail;

TRUNCATE TABLE Students;

SELECT * FROM Students;