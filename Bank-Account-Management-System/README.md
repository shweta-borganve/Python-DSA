# Bank Account Management System

A Python-based command-line Bank Account Management System that allows users to securely manage bank accounts, perform transactions (deposits, withdrawals, transfers), and track transaction history with data persistence using JSON.

## Features

- **Secure Login Authentication**: Simple credential check before accessing the system.
- **Account Management**: Create, view, search, update, and delete bank accounts.
- **Transaction Operations**: Deposit funds, withdraw money with balance validation, and transfer money between accounts.
- **Record Keeping**: Check current balances and view detailed transaction histories.
- **JSON Data Persistence**: Automatically saves all accounts and transactional data locally.
- **Automated Testing & CI/CD**: Fully tested using `pytest` with automated continuous integration pipelines via GitHub Actions.

---

## Project Structure

```text
Bank-Account-Management-System/
│
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions CI/CD configuration
│
├── tests/
│   └── test_main.py        # Pytest suite for unit testing core functions
│
├── main.py                 # Core application script
├── accounts.json           # Local database for accounts (auto-generated)
├── .gitignore              # Ignored files/folders (caches, temp files)
└── README.md               # Project documentation 
```

---

# ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/shweta-borganve/Bank-Account-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Bank-Account-Management-System
```

### 3. Run the Application

```bash
python main.py
```

---

# 🔑 Login Credentials

| Username | Password   |
| -------- | ---------- |
| account  | account123 |

---

# 💾 Account Information Stored

Each account stores the following information:

* Account Number
* Account Holder Name
* Phone Number
* Account Type (Savings/Current)
* Account Balance
* Transaction History

---

# 📋 Sample Menu

```text
--------------------
BANK MANAGEMENT SYSTEM
--------------------
1. Create New Account
2. View All Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Transfer Money
7. Update Account Details
8. Delete Account
9. Check Balance
10. Transaction History
11. Exit
--------------------
```

---

# 📚 Python Concepts Used

* Functions
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* Exception Handling (`try`, `except`)
* JSON File Handling
* Lists
* Dictionaries
* CRUD Operations
* Menu-Driven Programming

---

# 🎯 Learning Outcomes

This project helped me learn:

* Python programming fundamentals
* File handling using JSON
* Data storage and retrieval
* Creating menu-driven applications
* CRUD operations
* Input validation
* Error handling
* Problem-solving using Python

---

# 🚀 Future Enhancements

* Database integration (SQLite/MySQL)
* User authentication with encrypted passwords
* Interest calculation
* Account statements
* GUI using Tkinter
* Email/SMS notifications
* Admin dashboard

---

# 👩‍💻 Author

**Shweta Boraganve**

* GitHub: https://github.com/shweta-borganve
* LinkedIn: https://www.linkedin.com/in/shweta-boraganve-9686ab26a

---

# ⭐ If you like this project

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub 