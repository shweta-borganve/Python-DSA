import json
import os
import sys

FILE_NAME = "employees.json"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "employee" and password == "employee123":
        print("\nLogin Successful!\n")
        return True
    else:
        print("\nInvalid Username or Password!\n")
        return False


def add_employee():
    try:
        with open(FILE_NAME, "r") as f:
            try:
                employees = json.load(f)
            except json.JSONDecodeError:
                employees = []

        employee = {
            "Employee ID": input("Enter Employee ID: "),
            "Name": input("Enter Employee Name: "),
            "Age": int(input("Enter Employee Age: ")),
            "Gender": input("Enter Employee Gender: "),
            "Department": input("Enter Employee Department: "),
            "Designation": input("Enter Employee Designation: "),
            "Salary": float(input("Enter Employee Salary: ")),
            "Phone": input("Enter Employee Phone Number: "),
        }

        employees.append(employee)

        with open(FILE_NAME, "w") as f:
            json.dump(employees, f, indent=4)

        print("\nEmployee Added Successfully!\n")

    except Exception as e:  # noqa: BLE001
        print("\nError:", e)


def view_employee():
    try:
        with open(FILE_NAME, "r") as f:
            employees = json.load(f)
            if len(employees) == 0:
                print("\nNo employee records found\n")
                return
            print("\n" + "=" * 60)
            print("EMPLOYEE DETAILS")
            print("=" * 60)
            for employee in employees:
                print(f"Employee ID : {employee['Employee ID']}")
                print(f"Name : {employee['Name']}")
                print(f"Age : {employee['Age']}")
                print(f"Gender : {employee['Gender']}")
                print(f"Designation : {employee['Designation']}")
                print(f"Salary : {employee['Salary']}")
                print(f"Phone : {employee['Phone']}")
                print("-" * 60)
    except FileNotFoundError:
        print("\nEmployee file not found!\n")
    except json.JSONDecodeError:
        print("\nEmployee file is empty or corrupted!\n")


def search_employee():
    try:
        with open(FILE_NAME, "r") as f:
            employees = json.load(f)
        search_id = input("Enter Employee ID to search: ")
        found = False
        for employee in employees:
            if employee["Employee ID"] == search_id:
                print("\nEmployee Found!\n")
                print("-" * 20)
                print("Employee ID :", employee["Employee ID"])
                print("Name :", employee["Name"])
                print("Age :", employee["Age"])
                print("Gender :", employee["Gender"])
                print("Department :", employee["Department"])
                print("Designation :", employee["Designation"])
                print("Salary :", employee["Salary"])
                print("Phone :", employee["Phone"])
                print("-" * 50)
                found = True
                break
        if not found:
            print("\nEmployee not found!")
    except FileNotFoundError:
        print("\nEmployee file not found\n")
    except json.JSONDecodeError:
        print("\nEmployee file is empty or corrupted!\n")


def update_employee():
    try:
        with open(FILE_NAME, "r") as f:
            employees = json.load(f)
        employee_id = input("Enter Employee ID to update: ")
        found = False

        for employee in employees:
            if employee["Employee ID"] == employee_id:
                print("\nEnter new Employee Details\n")
                employee["Name"] = input("Enter Employee Name: ")
                employee["Age"] = int(input("Enter Employee Age: "))
                employee["Gender"] = input("Enter Employee Gender: ")
                employee["Department"] = input("Enter Employee Department: ")
                employee["Designation"] = input("Enter Employee Designation: ")
                employee["Salary"] = int(input("Enter Employee Salary: "))
                employee["Phone"] = input("Enter Employee Phone Number: ")

                found = True
                break
        if found:
            with open(FILE_NAME, "w") as f:
                json.dump(employees, f, indent=4)
            print("\nEmployee updated successfully!\n")
        else:
            print("\nEmployee Not Found!\n")
    except ValueError:
        print("Age must be a number and Salary must be a valid number.")
    except FileNotFoundError:
        print("Employee file not found!")
    except json.JSONDecodeError:
        print("Employee file is not found or corrupted!")


def delete_employee():
    try:
        with open(FILE_NAME, "r") as f:
            employees = json.load(f)
        employee_id = input("Enter Employee Id to delete: ")
        found = False

        for employee in employees:
            if employee["Employee ID"] == employee_id:
                employees.remove(employee)
                found = True
                break
        if found:
            with open(FILE_NAME, "w") as f:
                json.dump(employees, f, indent=4)
            print("\nEmployee deleted successfully")
        else:
            print("Employee not found!")
    except FileNotFoundError:
        print("\nEmployee file not exist")
    except json.JSONDecodeError:
        print("\n Employee file is empty or corrupted!\n")


if not login():
    sys.exit()

while True:
    print("=" * 50)
    print("        EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    print("=" * 50)

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employee()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        update_employee()

    elif choice == 5:
        delete_employee()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Feature coming soon.")
