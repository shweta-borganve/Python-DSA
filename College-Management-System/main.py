import sys

from course import course_management
from enrollment import enrollment_management
from faculty import faculty_management
from logger_config import logger
from login import login
from reports import reports
from student import student_management

logger.info("College Management System Started")

if login():
    logger.info("User logged into the system")
    print("Welcome to this system\n")
else:
    logger.critical("Login failed. Application terminated.")
    print("Access Denied.\n")
    sys.exit()

while True:
    print("*" * 20)
    print("COLLEGE MANAGEMENT SYSTEM")
    print("*" * 20)
    print("1. Student Management")
    print("2. Faculty Management")
    print("3. Course Management")
    print("4. Enrollment")
    print("5. Reports")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
        logger.debug(f"Main menu choice: {choice}")
    except ValueError:
        logger.error("Invalid input entered in Main Menu")
        print("Please enter a valid choice")
        continue

    if choice == 1:
        logger.info("Opened Student Management")
        student_management()

    elif choice == 2:
        logger.info("Opened Faculty Management")
        faculty_management()

    elif choice == 3:
        logger.info("Opened Course Management")
        course_management()

    elif choice == 4:
        logger.info("Opened Enrollment Management")
        enrollment_management()

    elif choice == 5:
        logger.info("Opened Reports")
        reports()

    elif choice == 6:
        logger.info("Application closed by user")
        print("Exiting.....")
        print("Thank you for using this application\n")
        break

    else:
        logger.warning(f"Invalid main menu option selected: {choice}")
        print("Invalid choice") 