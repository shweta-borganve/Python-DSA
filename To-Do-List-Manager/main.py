import json
import os
import sys

if os.path.exists("task.json"):
    try:
        with open("task.json", "r") as file:
            task = json.load(file)
    except json.JSONDecodeError:
        task = []
else:
    task = []


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "task" and password == "task123":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False


if login():
    print("\nWelcome to the To-Do List Manager!\n")
else:
    print("Access denied. Exiting the system.")
    sys.exit()


def add_task():
    print("-" * 20)
    print("\nAdd Task Details: \n")
    print("-" * 20)
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    status = input("Enter Task Status (Pending/Completed): ")

    task_details = {
        "task_id": task_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": status,
    }
    task.append(task_details)

    with open("task.json", "w") as file:
        json.dump(task, file, indent=4)

    print("\nTask details added successfully!\n")


def view_tasks():
    if not task:
        print("\nNo tasks found.\n")
        return

    print("-" * 20)
    print("\nTask List: \n")
    print("-" * 20)
    for task_details in task:
        print(f"Task ID: {task_details['task_id']}")
        print(f"Title: {task_details['title']}")
        print(f"Description: {task_details['description']}")
        print(f"Due Date: {task_details['due_date']}")
        print(f"Status: {task_details['status']}")
        print("-" * 20)


def update_task():
    task_id = input("Enter Task ID to update: ")
    for task_details in task:
        if task_details["task_id"] == task_id:
            print("\nUpdate Task Details: \n")
            print("-" * 20)
            task_details["title"] = input("Enter new Task Title: ")
            task_details["description"] = input("Enter new Task Description: ")
            task_details["due_date"] = input("Enter new Due Date (YYYY-MM-DD): ")
            task_details["status"] = input(
                "Enter new Task Status (Pending/Completed): "
            )

            with open("task.json", "w") as file:
                json.dump(task, file, indent=4)

            print("\nTask details updated successfully!\n")
            return

    print("\nTask ID not found. Please try again.\n")


def task_completed():
    task_id = input("Enter Task ID to mark as completed: ")
    for task_details in task:
        if task_details["task_id"] == task_id:
            task_details["status"] = "Completed"

            with open("task.json", "w") as file:
                json.dump(task, file, indent=4)

            print("\nTask marked as completed successfully!\n")
            return

    print("\nTask ID not found. Please try again.\n")


def delete_task():
    task_id = input("Enter Task ID to delete: ")
    for task_details in task:
        if task_details["task_id"] == task_id:
            task.remove(task_details)

            with open("task.json", "w") as file:
                json.dump(task, file, indent=4)

            print("\nTask deleted successfully!\n")
            return

    print("\nTask ID not found. Please try again.\n")


def search_task():
    search_term = input("Enter Task Title or Description to search: ")
    found_tasks = []

    for task_details in task:
        if (
            search_term.lower() in task_details["title"].lower()
            or search_term.lower() in task_details["description"].lower()
        ):
            found_tasks.append(task_details)

    if not found_tasks:
        print("\nNo tasks found matching the search term.\n")
        return

    print("-" * 20)
    print("\nSearch Results: \n")
    print("-" * 20)
    for task_details in found_tasks:
        print(f"Task ID: {task_details['task_id']}")
        print(f"Title: {task_details['title']}")
        print(f"Description: {task_details['description']}")
        print(f"Due Date: {task_details['due_date']}")
        print(f"Status: {task_details['status']}")
        print("-" * 20)


while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Search Task")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice (1-7): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue

    if choice == 1:
        add_task()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        update_task()

    elif choice == 4:
        task_completed()

    elif choice == 5:
        delete_task()

    elif choice == 6:
        search_task()

    elif choice == 7:
        print("Exiting....")
        print("Thank you for using the To-Do List Manager!\n")
        break

    else:
        print("Invalid choice. Please try again.\n")
