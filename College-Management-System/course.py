import json

from data import courses
from logger_config import logger


def add_course():
    course_id = input("Enter Course ID: ")
    course_name = input("Enter Course Name: ")
    department = input("Enter Department: ")
    credits = input("Enter Credits: ")

    course = {
        "Course ID": course_id,
        "Course Name": course_name,
        "Department": department,
        "Credits": credits,
    }

    courses.append(course)

    with open("courses.json", "w") as f:
        json.dump(courses, f, indent=4)

    logger.info(f"Course {course_id} added successfully")
    print("\nCourse added successfully!\n")


def view_courses():
    if not courses:
        logger.warning("No course records found")
        print("\nNo course records found.\n")
        return

    print("\n" + "-" * 60)
    print("COURSE RECORDS")
    print("-" * 60)

    for course in courses:
        print(f"Course ID   : {course['Course ID']}")
        print(f"Course Name : {course['Course Name']}")
        print(f"Department  : {course['Department']}")
        print(f"Credits     : {course['Credits']}")
        print("-" * 60)


def search_course():
    course_id = input("Enter Course ID to search: ")
    logger.debug(f"Searching Course ID: {course_id}")

    for course in courses:
        if course["Course ID"] == course_id:
            logger.info(f"Course {course_id} found")

            print("\nCourse Found")
            print("-" * 30)
            print(f"Course ID   : {course['Course ID']}")
            print(f"Course Name : {course['Course Name']}")
            print(f"Department  : {course['Department']}")
            print(f"Credits     : {course['Credits']}")
            return

    logger.warning(f"Course {course_id} not found")
    print("\nCourse not found.\n")


def update_course():
    course_id = input("Enter Course ID to update: ")

    for course in courses:
        if course["Course ID"] == course_id:

            print("\nEnter New Course Details")

            course["Course Name"] = input("Enter Course Name: ")
            course["Department"] = input("Enter Department: ")
            course["Credits"] = input("Enter Credits: ")

            with open("courses.json", "w") as f:
                json.dump(courses, f, indent=4)

            logger.info(f"Course {course_id} updated successfully")
            print("\nCourse updated successfully!\n")
            return

    logger.warning(f"Course {course_id} not found for update")
    print("\nCourse not found.\n")


def delete_course():
    course_id = input("Enter Course ID to delete: ")

    for course in courses:
        if course["Course ID"] == course_id:
            courses.remove(course)

            with open("courses.json", "w") as f:
                json.dump(courses, f, indent=4)

            logger.info(f"Course {course_id} deleted successfully")
            print("\nCourse deleted successfully!\n")
            return

    logger.warning(f"Course {course_id} not found for deletion")
    print("\nCourse not found.\n")


def course_management():
    while True:
        print("\n" + "-" * 30)
        print("COURSE MANAGEMENT SYSTEM")
        print("-" * 30)

        print("1. Add Course")
        print("2. View Courses")
        print("3. Search Course")
        print("4. Update Course")
        print("5. Delete Course")
        print("6. Back")

        try:
            choice = int(input("Enter your choice (1-6): "))
            logger.debug(f"Course menu choice: {choice}")
        except ValueError:
            logger.error("Invalid menu choice entered in course management")
            print("Please enter a valid choice")
            continue

        if choice == 1:
            add_course()

        elif choice == 2:
            view_courses()

        elif choice == 3:
            search_course()

        elif choice == 4:
            update_course()

        elif choice == 5:
            delete_course()

        elif choice == 6:
            break

        else:
            logger.warning(f"Invalid course menu choice: {choice}")
            print("Invalid choice")
