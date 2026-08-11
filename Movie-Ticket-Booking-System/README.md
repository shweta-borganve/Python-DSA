# MOVIE TICKET BOOKING SYSTEM

A robust console-based Python application designed to manage user authentication, movie listings, seat availability, and ticket bookings, complete with persistent JSON storage and automated CI/CD testing.

## Features

* **Admin Portal**:
  * Secure administrator login.
  * Add new movies, view active listings, and update movie details (titles, showtimes, and available seats).
  * View all user bookings across the system.
* **User Management**:
  * User registration with duplicate username checking.
  * Secure user login validation.
* **Booking System**:
  * Browse available movies and real-time seat counts.
  * Book tickets with automatic seat reduction and persistence.
  * View personal booking history.
* **Data Persistence**:
  * Automatic data storage and recovery using local JSON files (`users.json`, `movies.json`, `bookings.json`).

---

## Project Structure

```text
Movie-Ticket-Booking-System/
│
├── .github/
│   └── workflows/
│       └── pytest.yml       # GitHub Actions CI workflow
├── test/
│   └── test_main.py         # Automated pytest suite
├── main.py                  # Main application source code
├── users.json               # Persistent user data store
├── movies.json              # Persistent movie data store
└── bookings.json            # Persistent booking data store

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/Movie-Ticket-Booking-System.git
```

2. Navigate to the project folder:

```bash
cd Movie-Ticket-Booking-System
```

3. Run the program:

```bash
python main.py
```

---

## 📋 Main Menu

```
======= Movie Ticket Booking System =======

1. Admin Login
2. User Registration
3. User Login
4. Exit
```

---

## 📊 Project Workflow

### Admin

* Login using admin credentials
* Add movies
* View movies
* Update movie details

### User

* Register a new account
* Login
* View available movies
* Book movie tickets
* View booking history

---

## 📁 JSON Files

### users.json

Stores registered user information.

### movies.json

Stores movie details including:

* Movie Title
* Show Time
* Available Seats

### bookings.json

Stores booking information including:

* Username
* Movie Title
* Number of Tickets

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Python Programming
* File Handling
* JSON Data Storage
* User Authentication
* CRUD Operations
* Data Management
* Menu-Driven Applications
* Problem Solving

---

## 🔮 Future Enhancements

* Delete Movie
* Cancel Booking
* Search Movies
* Seat Selection
* Ticket Price Management
* Booking Date & Time
* Admin Dashboard
* User Dashboard
* Booking Receipt Generation

---

## 👩‍💻 Developer

**Shweta Boraganve**

GitHub: https://github.com/shweta-borganve

LinkedIn: https://www.linkedin.com/in/shweta-boraganve-9686ab26a

---

## ⭐ Support


# 🎬 MOVIE TICKET BOOKING SYSTEM

A **Python-based Movie Ticket Booking System** that allows administrators to manage movie details and users to register, log in, and book movie tickets. The project uses **JSON files** for persistent data storage, making it simple, lightweight, and easy to understand for beginners.

---

## 📌 Features

### 👨‍💼 Admin

* Secure Admin Login
* Add New Movies
* View Available Movies
* Update Movie Details

### 👤 User

* User Registration
* User Login
* View Available Movies
* Book Movie Tickets
* View Personal Booking History

### 💾 Data Storage

* Stores user information in `users.json`
* Stores movie information in `movies.json`
* Stores booking details in `bookings.json`

---

## 🛠️ Technologies Used

* Python 3
* JSON
* File Handling
* Functions
* Conditional Statements
* Loops
* Exception Handling
* VS Code

---

## 📂 Project Structure

```
Movie-Ticket-Booking-System/
│── main.py
│── users.json
│── movies.json
│── bookings.json
│── README.md
```

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/Movie-Ticket-Booking-System.git
```

2. Navigate to the project folder:

```bash
cd Movie-Ticket-Booking-System
```

3. Run the program:

```bash
python main.py
```

---

## 📋 Main Menu

```
======= Movie Ticket Booking System =======

1. Admin Login
2. User Registration
3. User Login
4. Exit
```

---

## 📊 Project Workflow

### Admin

* Login using admin credentials
* Add movies
* View movies
* Update movie details

### User

* Register a new account
* Login
* View available movies
* Book movie tickets
* View booking history

---

## 📁 JSON Files

### users.json

Stores registered user information.

### movies.json

Stores movie details including:

* Movie Title
* Show Time
* Available Seats

### bookings.json

Stores booking information including:

* Username
* Movie Title
* Number of Tickets

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Python Programming
* File Handling
* JSON Data Storage
* User Authentication
* CRUD Operations
* Data Management
* Menu-Driven Applications
* Problem Solving

---

## 🔮 Future Enhancements

* Delete Movie
* Cancel Booking
* Search Movies
* Seat Selection
* Ticket Price Management
* Booking Date & Time
* Admin Dashboard
* User Dashboard
* Booking Receipt Generation

---

## 👩‍💻 Developer

**Shweta Boraganve**

GitHub: https://github.com/shweta-borganve

LinkedIn: https://www.linkedin.com/in/shweta-boraganve-9686ab26a

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.