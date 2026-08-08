# 🎓 COLLEGE MANAGEMENT SYSTEM

A modular **College Management System** developed in **Python** using **JSON** for data storage. The application allows administrators to manage students, faculty, courses, enrollments, and reports through a menu-driven interface. It also includes a **logging system** that records important events during program execution.

---

## 📌 Features

### 👨‍🎓 Student Management
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

### 👨‍🏫 Faculty Management
- Add Faculty
- View Faculty
- Search Faculty
- Update Faculty
- Delete Faculty

### 📚 Course Management
- Add Course
- View Courses
- Search Course
- Update Course
- Delete Course

### 📝 Enrollment Management
- Enroll Students into Courses
- View Enrollments
- Delete Enrollment

### 📊 Reports
- Total Students
- Total Faculty
- Total Courses
- Total Enrollments

### 🔐 Authentication
- Secure Login System
- Username & Password Verification

### 📝 Logging System
The application automatically creates a log file (`college_management.log`) to record important events during execution.

The log file includes:

- **DEBUG** – Debugging information
- **INFO** – Successful operations
- **WARNING** – Missing records or unusual events
- **ERROR** – Invalid inputs and runtime errors
- **CRITICAL** – Unauthorized login attempts

---

## 🛠️ Technologies Used

- Python 3
- JSON
- File Handling
- Modular Programming
- Logging Module
- Exception Handling

---

## 📁 Project Structure

```
College-Management-System/
│
├── main.py
├── login.py
├── data.py
├── student.py
├── faculty.py
├── course.py
├── enrollment.py
├── reports.py
├── logger_config.py
│
├── students.json
├── faculty.json
├── courses.json
├── enrollment.json
│
├── college_management.log
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/College-Management-System.git
```

2. Navigate to the project folder

```bash
cd College-Management-System
```

3. Run the application

```bash
python main.py
```

---

## 🔑 Default Login Credentials

| Username | Password |
|----------|----------|
| college | college123 |

---

## 📷 Sample Log Entries

```text
2026-08-04 23:46:06 - INFO - User logged in successfully
2026-08-04 23:46:20 - DEBUG - Searching Student ID: S101
2026-08-04 23:46:25 - WARNING - Student S999 not found
2026-08-04 23:46:35 - ERROR - Invalid menu choice entered
2026-08-04 23:47:10 - CRITICAL - Unauthorized login attempt
```

---

## 📚 Concepts Used

- Functions
- Modules
- JSON File Handling
- Exception Handling
- Logging
- CRUD Operations
- Dictionaries & Lists
- Loops
- Conditional Statements

---

## 🚀 Future Enhancements

- Search using Name or Department
- Password Encryption
- Attendance Management
- Marks Management
- Fee Management
- Database Integration (MySQL)
- GUI using Tkinter
- Web Version using Flask/Django

---

## 👩‍💻 Author

Shweta Boraganve

GitHub: https://github.com/shweta-borganve

---

## ⭐ Project Status

✅ Completed

This project demonstrates Python fundamentals including modular programming, CRUD operations, JSON data storage, exception handling, authentication, and professional logging practices.