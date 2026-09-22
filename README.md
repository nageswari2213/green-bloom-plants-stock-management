# 🌱 Green Bloom Plants Stock Management System

## 📌 Project Description

Green Bloom Plants Stock Management System is a Python and MySQL-based application used to manage plant stock, suppliers, customers, billing, and sales reports.

The project also includes a Streamlit web interface with plant images for easy and user-friendly management.

## 🎯 Objectives

* Manage plant stock
* View plant details
* Search plants
* Add new plants
* Update plant quantity
* Delete plants
* Manage suppliers
* View customer details
* Generate bills
* Automatically update stock after a sale
* View sales reports

## 🛠️ Technologies Used

* Python
* MySQL
* Streamlit
* MySQL Connector
* VS Code
* MySQL Workbench

## 🌿 Features

### Plant Management

* View all plants
* Search plants by name
* Add new plants
* Update plant quantity
* Delete plants
* View plant price and available stock
* View supplier information
* Display plant images

### Supplier Management

* View suppliers
* Add new suppliers
* Update supplier details
* Delete suppliers
* View supplier ID
* View supplier name
* View phone number
* View city

### Customer Management

* View customer details
* View customer ID
* View customer name
* View phone number
* View city
* View customer purchase history
* View total customer purchase amount

### Billing

* Select customer
* Select plant
* Enter quantity
* Calculate total amount
* Save sales information
* Automatically reduce plant stock
* Display generated bill

### Sales Reports

* Total Sales Report
* Available Stock Report
* Low Stock Plants Report
* Customer Purchase History Report
* Sale ID
* Customer name
* Plant name
* Quantity
* Total amount
* Sale date

## 🗄️ Database

Database name:

```text
green_bloom_db
```

### Tables

```text
plants
suppliers
customers
sales
```

## 📂 Project Structure

```text
Green Bloom Project/
│
├── images/
│   ├── aloe_vera.jpg
│   ├── hibiscus.jpg
│   ├── jasmine.jpg
│   ├── lotus.jpg
│   ├── mari_gold.jpg
│   ├── Money_plant.jpg
│   ├── rose.jpg
│   ├── sunflowe.jpg
│   └── Tulip.jpg
│
├── main.py
├── db_connection.py
├── plant_module.py
├── supplier_module.py
├── customer_module.py
├── billing_module.py
├── reports_module.py
├── streamlit_app.py
├── requirements.txt
├── database.sql
└── README.md
```

## ▶️ How to Run the Project

### 1. Open the project folder

```powershell
cd "C:\Users\nages\OneDrive\Desktop\Green Bloom Project"
```

### 2. Run the Streamlit application

```powershell
python -m streamlit run streamlit_app.py
```

The Green Bloom web application will open in the browser.

### 3. Run the console application

```powershell
python main.py
```

## 🔐 Database Configuration

Open `db_connection.py` and enter your MySQL password:

```python
password="YOUR_MYSQL_PASSWORD"
```

The database name must be:

```text
green_bloom_db
```

## 🧪 Testing

The following features were tested successfully:

* ✅ View Plants
* ✅ Search Plant
* ✅ Add Plant
* ✅ Update Quantity
* ✅ Delete Plant
* ✅ View Suppliers
* ✅ Add Supplier
* ✅ Update Supplier
* ✅ Delete Supplier
* ✅ View Customers
* ✅ Customer Purchase History
* ✅ Generate Bill
* ✅ Automatic Stock Update
* ✅ Total Sales Report
* ✅ Available Stock Report
* ✅ Low Stock Plants Report
* ✅ Streamlit Web Interface
* ✅ Plant Images

## 👩‍💻 Developer

**Gonugunta Nageswari**

B.Tech - Electronics and Communication Engineering

## 📌 Conclusion

The Green Bloom Plants Stock Management System provides a simple and efficient way to manage plant inventory, customers, suppliers, billing, and sales.

The project combines Python, MySQL, and Streamlit to provide database management along with a user-friendly web interface.
