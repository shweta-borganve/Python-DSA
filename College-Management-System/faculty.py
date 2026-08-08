import json

from data import faculty
from logger_config import logger


def add_faculty():
    faculty_id = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")
    department = input("Enter Department: ")
    subject = input("Enter Subject: ")
    phone = input("Enter Phone Number: ")

    faculty_member = {
        "Faculty ID": faculty_id,
        "Name": name,
        "Department": department,
        "Subject": subject,
        "Phone": phone,
    }

    faculty.append(faculty_member)
    logger.info(f"Faculty {faculty_id} added successfully")

    with open("faculty.json", "w") as f:
        json.dump(faculty, f, indent=4)

    print("\nFaculty added successfully!\n")


def view_faculty():
    if not faculty:
        print("\nNo faculty records found.\n")
        return

    print("\n" + "-" * 60)
    print("FACULTY RECORDS")
    print("-" * 60)

    for member in faculty:
        print(f"Faculty ID : {member['Faculty ID']}")
        print(f"Name       : {member['Name']}")
        print(f"Department : {member['Department']}")
        print(f"Subject    : {member['Subject']}")
        print(f"Phone      : {member['Phone']}")
        print("-" * 60)


def search_faculty():
    faculty_id = input("Enter Faculty ID to search: ")
    logger.debug(f"Searching Faculty Id: {faculty_id}")

    for member in faculty:
        if member["Faculty ID"] == faculty_id:
            logger.info(f"Faculty{faculty_id} found")
            print("\nFaculty Found")
            print("-" * 30)
            print(f"Faculty ID : {member['Faculty ID']}")
            print(f"Name       : {member['Name']}")
            print(f"Department : {member['Department']}")
            print(f"Subject    : {member['Subject']}")
            print(f"Phone      : {member['Phone']}")
            return

    logger.warning(f"Faculty{faculty_id} not found")
    print("\nFaculty not found.\n")


def update_faculty():
    faculty_id = input("Enter Faculty ID to update: ")

    for member in faculty:
        if member["Faculty ID"] == faculty_id:
            logger.info(f"Faculty{faculty_id} updated successfully")
            print("\nEnter New Faculty Details")

            member["Name"] = input("Enter Faculty Name: ")
            member["Department"] = input("Enter Department: ")
            member["Subject"] = input("Enter Subject: ")
            member["Phone"] = input("Enter Phone Number: ")

            with open("faculty.json", "w") as f:
                json.dump(faculty, f, indent=4)

            print("\nFaculty updated successfully!\n")
            return

    logger.warning(f"Faculty{faculty_id} not found for update")
    print("\nFaculty not found.\n")


def delete_faculty():
    faculty_id = input("Enter Faculty ID to delete: ")

    for member in faculty:
        if member["Faculty ID"] == faculty_id:
            faculty.remove(member)

            with open("faculty.json", "w") as f:
                json.dump(faculty, f, indent=4)

            logger.info(f"Faculty {faculty_id} deleted successfully")
            print("\nFaculty deleted successfully!\n")
            return

    logger.warning(f"Faculty {faculty_id} not found for deletion")
    print("\nFaculty not found.\n")


def faculty_management():
    while True:
        print("\n" + "-" * 30)
        print("FACULTY MANAGEMENT SYSTEM")
        print("-" * 30)

        print("1. Add Faculty")
        print("2. View Faculty")
        print("3. Search Faculty")
        print("4. Update Faculty")
        print("5. Delete Faculty")
        print("6. Back")

        try:
            choice = int(input("Enter your choice (1-6): "))
            logger.debug(f"Faculty menu choice:{choice}")
        except ValueError:
            logger.error("Invalid menu choice entered in faculty management")
            print("Please enter a valid choice")
            continue

        if choice == 1:
            add_faculty()

        elif choice == 2:
            view_faculty()

        elif choice == 3:
            search_faculty()

        elif choice == 4:
            update_faculty()

        elif choice == 5:
            delete_faculty()

        elif choice == 6:
            break

        else:
            print("Invalid choice")
