CREATE DATABASE IF NOT EXISTS green_bloom_db;

USE green_bloom_db;


-- =========================
-- PLANTS TABLE
-- =========================

CREATE TABLE IF NOT EXISTS plants(
    plant_id INT PRIMARY KEY,
    plant_name VARCHAR(100),
    category VARCHAR(50),
    price FLOAT,
    quantity INT,
    supplier_name VARCHAR(100)
);


-- =========================
-- SUPPLIERS TABLE
-- =========================

CREATE TABLE IF NOT EXISTS suppliers(
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50)
);


-- =========================
-- CUSTOMERS TABLE
-- =========================

CREATE TABLE IF NOT EXISTS customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50)
);


-- =========================
-- SALES TABLE
-- =========================

CREATE TABLE IF NOT EXISTS sales(
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    plant_name VARCHAR(100),
    quantity INT,
    total_amount FLOAT,
    sale_date DATE
);


-- =========================
-- PLANT DATA
-- =========================

INSERT INTO plants VALUES
(1, 'Rose', 'Flower', 50, 20, 'Green Nursery'),
(2, 'Jasmine', 'Flower', 40, 15, 'Nature Plants'),
(3, 'Aloe Vera', 'Medicinal', 80, 10, 'Green Nursery'),
(4, 'Money Plant', 'Indoor', 100, 25, 'Plant World');


-- =========================
-- SUPPLIER DATA
-- =========================

INSERT INTO suppliers VALUES
('S001', 'Green Nursery', '9876543210', 'Hyderabad'),
('S002', 'Nature Plants', '9876501234', 'Bangalore'),
('S003', 'Plant World', '9876512345', 'Chennai');


-- =========================
-- CUSTOMER DATA
-- =========================

INSERT INTO customers VALUES
(1, 'Ravi', '9876543211', 'Hyderabad'),
(2, 'Priya', '9876543212', 'Bangalore');