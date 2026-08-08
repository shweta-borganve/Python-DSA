from data import courses, enrollment, faculty, students
from logger_config import logger


def reports():
    while True:
        print("\n" + "-" * 30)
        print("REPORTS")
        print("-" * 30)
        print("1. Total Students")
        print("2. Total Faculty")
        print("3. Total Courses")
        print("4. Total Enrollments")
        print("5. Back")

        try:
            choice = int(input("Enter your choice (1-5): "))
            logger.debug(f"Reports menu choice: {choice}")

        except ValueError:
            logger.error("Invalid menu choice entered in reports")
            print("Please enter a valid choice")
            continue

        if choice == 1:
            logger.info("Viewed total students report")
            print(f"\nTotal Students: {len(students)}")

        elif choice == 2:
            logger.info("Viewed total faculty report")
            print(f"\nTotal Faculty: {len(faculty)}")

        elif choice == 3:
            logger.info("Viewed total courses report")
            print(f"\nTotal Courses: {len(courses)}")

        elif choice == 4:
            logger.info("Viewed total enrollments report")
            print(f"\nTotal Enrollments: {len(enrollment)}")

        elif choice == 5:
            logger.info("Exited Reports Menu")
            break

        else:
            logger.warning(f"Invalid reports menu choice: {choice}")
            print("Invalid choice")
