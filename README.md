# 🧾 BILLING SYSTEM

A professional **Billing System** developed using **Python** that helps manage products, generate customer bills, maintain billing history, and track application activities through logging.

This project follows a **modular architecture** by dividing functionalities into separate Python files, making the application clean, organized, maintainable, and scalable.

---

## 🚀 Features

### 🔐 Admin Authentication
- Secure admin login system
- Restricted access to billing operations
- Tracks login activities using logging

### 📦 Product Management
- Add new products
- View available products
- Search products
- Update product details
- Delete products
- Manage product stock

### 🧾 Billing Management
- Generate customer bills
- Add multiple products to a bill
- Automatically calculate the total amount
- Reduce product stock after purchase
- Store billing details permanently

### 📜 Billing History
- View previous bills
- Display customer details
- Display purchased products
- Show total billing amount

### 📝 Logging System
- Creates application log files
- Records:
  - Successful login
  - Failed login attempts
  - Product operations
  - Bill generation
  - System activities

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Storage:** JSON
- **Concepts Implemented:**
  - Functions
  - Modules
  - File Handling
  - JSON Handling
  - Exception Handling
  - CRUD Operations
  - Logging

---

## 📂 Project Structure

```text
Billing-System/
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── data/
│   ├── products.json
│   └── bills.json
│
├── logs/
│   └── billing_system.log
│
├── auth.py
├── billing.py
├── file_handler.py
├── history.py
├── logger_config.py
├── main.py
├── product.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/shweta-borganve/Billing-System.git
cd Billing-System
```

### Run the Project

```bash
python main.py
```

> If you're using Ubuntu or WSL, run:

```bash
python3 main.py
```

---

## 🔑 Default Login Credentials

**Username:** `admin`

**Password:** `1234`

---

## 💻 Application Workflow

- Login using admin credentials
- Add and manage products
- Search, update, or delete products
- Generate customer bills
- View billing history
- Check application logs

---

## 📌 Sample Output

```text
===== Welcome to Billing System =====

Enter Username: admin
Enter Password: 1234

Login Successful!

===== Billing System Menu =====

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Generate Bill
7. View Bill History
8. Exit
```

---

## 🎯 Learning Outcomes

- Developed a real-world Python billing application
- Learned modular programming
- Implemented CRUD operations
- Worked with JSON-based data storage
- Implemented logging for tracking application activities
- Improved code organization and maintainability

---

## 🔮 Future Enhancements

- Add GUI using Tkinter
- Integrate SQL database
- Generate PDF invoices
- Add customer management
- Add multiple payment methods
- Implement user roles and permissions

---

## 👩‍💻 Author

**Shweta Boraganve**

Python Developer

- GitHub: https://github.com/shweta-borganve

---

⭐ **If you like this project, please give it a star!** 