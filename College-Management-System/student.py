import json

from data import students
from logger_config import logger


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    department = input("Enter Department: ")
    year = input("Enter Year: ")
    phone = input("Enter Phone Number: ")

    student = {
        "Student ID": student_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Department": department,
        "Year": year,
        "Phone": phone,
    }

    students.append(student)

    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

    logger.info(f"Student {student_id} added successfully")
    print("\nStudent added successfully!\n")


def view_students():
    if not students:
        logger.warning("No student records found")
        print("\nNo student records found.\n")
        return

    print("\n" + "-" * 70)
    print("STUDENT RECORDS")
    print("-" * 70)

    for student in students:
        print(f"Student ID : {student['Student ID']}")
        print(f"Name       : {student['Name']}")
        print(f"Age        : {student['Age']}")
        print(f"Gender     : {student['Gender']}")
        print(f"Department : {student['Department']}")
        print(f"Year       : {student['Year']}")
        print(f"Phone      : {student['Phone']}")
        print("-" * 70)


def search_student():
    student_id = input("Enter Student ID to search: ")
    logger.debug(f"Searching Student ID: {student_id}")

    for student in students:
        if student["Student ID"] == student_id:
            logger.info(f"Student {student_id} found")

            print("\nStudent Found")
            print("-" * 30)
            print(f"Student ID : {student['Student ID']}")
            print(f"Name       : {student['Name']}")
            print(f"Age        : {student['Age']}")
            print(f"Gender     : {student['Gender']}")
            print(f"Department : {student['Department']}")
            print(f"Year       : {student['Year']}")
            print(f"Phone      : {student['Phone']}")
            return

    logger.warning(f"Student {student_id} not found")
    print("\nStudent not found.\n")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["Student ID"] == student_id:

            print("\nEnter New Student Details")

            student["Name"] = input("Enter Name: ")
            student["Age"] = input("Enter Age: ")
            student["Gender"] = input("Enter Gender: ")
            student["Department"] = input("Enter Department: ")
            student["Year"] = input("Enter Year: ")
            student["Phone"] = input("Enter Phone Number: ")

            with open("students.json", "w") as f:
                json.dump(students, f, indent=4)

            logger.info(f"Student {student_id} updated successfully")
            print("\nStudent updated successfully!\n")
            return

    logger.warning(f"Student {student_id} not found for update")
    print("\nStudent not found.\n")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["Student ID"] == student_id:
            students.remove(student)

            with open("students.json", "w") as f:
                json.dump(students, f, indent=4)

            logger.info(f"Student {student_id} deleted successfully")
            print("\nStudent deleted successfully!\n")
            return

    logger.warning(f"Student {student_id} not found for deletion")
    print("\nStudent not found.\n")


def student_management():
    while True:
        print("-" * 30)
        print("STUDENT MANAGEMENT SYSTEM")
        print("-" * 30)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        try:
            choice = int(input("Enter your choice (1-6): "))
            logger.debug(f"Student menu choice: {choice}")
        except ValueError:
            logger.error("Invalid menu choice entered in student management")
            print("Please enter a valid choice")
            continue

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            break

        else:
            logger.warning(f"Invalid student menu choice: {choice}")
            print("Invalid choice")
