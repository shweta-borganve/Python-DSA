# 🏥 Hospital Management System

A Python-based command-line Hospital Management System designed to efficiently manage patient records, doctor details, appointments, and credentials with persistent JSON storage and automated unit testing.

---

## 🚀 Features

* **Secure Authentication**: Username and password login verification.
* **Patient Management**: Add, view, search, update, discharge, and track total patient counts.
* **Appointment Scheduling**: Book and view appointments mapped to specific patients.
* **Doctor Directory**: View a distinct list of doctors managing patients.
* **Data Persistence**: Automatically loads and saves data locally using `patients.json`.
* **Automated CI/CD**: Integrated with GitHub Actions to run pytest automatically on every push and pull request.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Testing Framework**: `pytest`
* **Storage**: JSON
* **CI/CD**: GitHub Actions

---

## 📁 Project Structure

```text
Hospital-Management-System/
│
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions CI pipeline configuration
├── test/
│   └── test_main.py        # Pytest unit test suite
├── main.py                 # Core application logic and CLI menu
├── patients.json           # Local database (auto-generated)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

Clone the repository:

```bash
git clone https://github.com/shweta-borganve/Hospital-Management-System.git
```

Navigate to the project directory:

```bash
cd Hospital-Management-System
```

Run the application:

```bash
python main.py
```

---

## 🔑 Login Credentials

| Username | Password |
|----------|----------|
| hospital | hospital123 |

---

## 📋 Available Operations

- Add Patient
- View Patient Records
- Search Patient
- Update Patient Details
- Delete Patient Record
- View Doctor Details
- Book Appointment
- View Appointment
- Discharge Patient
- Patient Count
- Exit Application

---

## 💾 Data Storage

The application stores all patient records in a **patients.json** file.

Patient data is automatically:
- Saved after every modification
- Loaded when the application starts
- Preserved between program executions

---

## 📸 Sample Menu

```text
********************
Hospital Management System Menu
********************

1. Add Patient
2. View Patient
3. Search Patient
4. Update Patient Details
5. Delete Patient Record
6. View Doctor Details
7. Book Appointment
8. View Appointment
9. Discharge Patient
10. Patient Count
11. Exit
```

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Functions
- Conditional Statements
- Loops
- Lists and Dictionaries
- JSON File Handling
- Exception Handling
- CRUD Operations
- Modular Programming
- User Authentication
- Console-Based Application Development

---

## 🔮 Future Enhancements

- Database Integration (MySQL/SQLite)
- Graphical User Interface (Tkinter)
- Doctor Management Module
- Billing & Payment System
- Prescription Management
- Patient Report Generation
- Role-Based Access Control
- Email/SMS Notifications

---

## 👩‍💻 Author

**Shweta Boraganve**

**GitHub:** https://github.com/shweta-borganve

**LinkedIn:** https://www.linkedin.com/in/shweta-boraganve-9686ab26a

---

## 📄 License

This project is developed for educational and learning purposes.

---

⭐ **If you found this project helpful, please consider giving it a Star on GitHub!**