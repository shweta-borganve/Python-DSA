import json

from data import enrollment
from logger_config import logger


def add_enrollment():
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")

    enroll = {"Student ID": student_id, "Course ID": course_id}

    enrollment.append(enroll)

    with open("enrollment.json", "w") as f:
        json.dump(enrollment, f, indent=4)

    logger.info(f"Enrollment added: Student {student_id} -> Course {course_id}")
    print("\nEnrollment added successfully!\n")


def view_enrollments():
    if not enrollment:
        logger.warning("No enrollment records found")
        print("\nNo enrollment records found.\n")
        return

    print("\n" + "-" * 40)
    print("ENROLLMENT RECORDS")
    print("-" * 40)

    for enroll in enrollment:
        print(f"Student ID : {enroll['Student ID']}")
        print(f"Course ID  : {enroll['Course ID']}")
        print("-" * 40)


def delete_enrollment():
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")

    logger.debug(f"Deleting enrollment: Student {student_id}, Course {course_id}")

    for enroll in enrollment:
        if enroll["Student ID"] == student_id and enroll["Course ID"] == course_id:

            enrollment.remove(enroll)

            with open("enrollment.json", "w") as f:
                json.dump(enrollment, f, indent=4)

            logger.info(
                f"Enrollment deleted: Student {student_id} -> Course {course_id}"
            )
            print("\nEnrollment deleted successfully!\n")
            return

    logger.warning(f"Enrollment not found: Student {student_id}, Course {course_id}")
    print("\nEnrollment record not found.\n")


def enrollment_management():
    while True:
        print("\n" + "-" * 30)
        print("ENROLLMENT MANAGEMENT")
        print("-" * 30)

        print("1. Add Enrollment")
        print("2. View Enrollments")
        print("3. Delete Enrollment")
        print("4. Back")

        try:
            choice = int(input("Enter your choice (1-4): "))
            logger.debug(f"Enrollment menu choice: {choice}")

        except ValueError:
            logger.error("Invalid menu choice entered in enrollment management")
            print("Please enter a valid choice")
            continue

        if choice == 1:
            add_enrollment()

        elif choice == 2:
            view_enrollments()

        elif choice == 3:
            delete_enrollment()

        elif choice == 4:
            break

        else:
            logger.warning(f"Invalid enrollment menu choice: {choice}")
            print("Invalid choice")
