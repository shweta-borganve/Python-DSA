# 📦 INVENTORY MANAGEMENT SYSTEM
# 📦 Inventory Management System

A robust command-line Inventory Management System built in Python that allows admin users to manage products, track stock levels, and generate financial summaries with persistent JSON storage.

---

## ✨ Features

* **Admin Authentication:** Secure login functionality to access the system.
* **Product Management:** Add, view, search, update, and delete product records.
* **Stock Operations:** Streamlined `Stock In` and `Stock Out` quantity tracking with automatic validation against negative or insufficient stock.
* **Low Stock Alerts:** Automatically flags products with a quantity below the threshold.
* **Inventory Summary:** Calculates total products, overall aggregate quantity, and total inventory financial value.
* **Automated CI/CD:** Integrated with GitHub Actions to run unit tests automatically on every push and pull request.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Testing:** `pytest`
* **Linter:** `Ruff`
* **Data Storage:** JSON

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/shweta-borganve/Inventory-Management-System.git](https://github.com/shweta-borganve/Inventory-Management-System.git)
cd Inventory-Management-System 

---

## 📌 Features

* 🔐 Admin Login Authentication
* ➕ Add New Product
* 📋 View All Products
* 🔍 Search Product by Product ID
* ✏️ Update Product Details
* ❌ Delete Product
* 📈 Stock In (Increase Quantity)
* 📉 Stock Out (Decrease Quantity)
* ⚠️ Low Stock Alert
* 📊 Inventory Summary
* 💾 Data Storage Using JSON File
* 🛡️ Exception Handling for Invalid Inputs

---

## 🛠️ Technologies Used

* Python 3
* JSON
* File Handling
* Functions
* Conditional Statements
* Loops
* Dictionaries & Lists
* Exception Handling
* Date & Time (`datetime` module)

---

## 📂 Project Structure

```text
Inventory-Management-System/
│
├── .github/
│   └── workflows/
│       └── main.yml       # GitHub Actions CI workflow
├── tests/
│   └── test_main.py       # Unit tests for core functions
├── .gitignore             # Git ignore file
├── inventory.json         # Local data store (ignored by git)
├── main.py                # Main application entry point
└── README.md              # Project documentation 
```

---

## 🚀 How to Run the Project

1. Clone the repository.

```bash
git clone https://github.com/your-username/Inventory-Management-System.git
```

2. Navigate to the project folder.

```bash
cd Inventory-Management-System
```

3. Run the program.

```bash
python main.py
```

---

## 🔑 Login Credentials

| Username | Password |
| -------- | -------- |
| admin    | admin123 |

---

## 📖 Menu Options

```text
1. Add Product
2. View Product
3. Search Product
4. Update Product
5. Delete Product
6. Stock In
7. Stock Out
8. Low Stock Alert
9. Inventory Summary
10. Exit
```

---

## 📊 Product Information

Each product contains the following details:

* Product ID
* Product Name
* Category
* Price
* Quantity
* Supplier Name
* Date Added

---

## 💡 Concepts Covered

* Python Functions
* JSON File Handling
* CRUD Operations
* Authentication
* Data Validation
* Exception Handling
* Inventory Management Logic
* Date and Time Handling

---

## 🎯 Learning Outcomes

This project demonstrates how to:

* Build a real-world Python console application.
* Perform CRUD operations using JSON files.
* Implement authentication and inventory management.
* Handle exceptions and user input effectively.
* Organize Python code using modular functions.

---

## 🔮 Future Enhancements

* Duplicate Product ID Validation
* Product Sorting
* Category-wise Search
* Sales Report Generation
* Export Inventory to CSV or Excel
* Graphical User Interface (Tkinter)
* Database Integration (MySQL)

---

## 👩‍💻 Author

**Shweta Boraganve**

* GitHub: https://github.com/shweta-borganve
* LinkedIn: https://www.linkedin.com/in/shweta-boraganve-9686ab26a

---

## ⭐ Support

If you found this project helpful, consider giving the repository a ⭐ on GitHub. 