import sys

username = input("Enter Username: ")
password = input("Enter password: ")

if username == "json" and password == "json123":
    print("Login Successfull")

    while True:
        print("=" * 50)
        print("CONTACT BOOK MANAGEMENT SYSTEM")
        print("=" * 50)
        break
else:
    print("Invalid Usrename or Password")
    sys.exit()

import json


def add_contacts():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {"name": name, "phone": phone, "email": email}

    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

    contacts.append(contact)

    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

    print("Contact Added Successfully!!")


def view_contact():
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)

        if len(contacts) == 0:
            print("No contacts available")
        else:
            print("\n--- Contact List ---")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("--------------------")

    except FileNotFoundError:
        print("No contacts available")


def search_contact():
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact found")
                print("Name: ", contact["name"])
                print("Phone:", contact["phone"])
                print("Email: ", contact["email"])

                found = True
                break
        if not found:
            print("Contact not found.")

    except FileNotFoundError:
        print("No contacts available")


def update_contact():
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
            search_name = input("Enter contact name to update: ")
            found = False

            for contact in contacts:
                if contact["name"].lower() == search_name.lower():
                    print("\nContact found")
                    contact["name"] = input("Enter new name: ")
                    contact["phone"] = input("Enter new phone number: ")
                    contact["email"] = input("Enter new mail id: ")

                    found = True
                    break
            if found:
                with open("contacts.json", "w") as f:
                    json.dump(contacts, f, indent=4)
                    print("Contact updated Successfully!!")
            else:
                print("Contact not found.")
    except FileNotFoundError:
        print("No contacts available")


def Delete_contact():
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
            delete_name = input("Enter a name you want to delete: ")
            found = False

            for contact in contacts:
                if contact["name"].lower() == delete_name.lower():
                    contacts.remove(contact)
                    found = True
                    break
            if found:
                with open("contacts.json", "w") as f:
                    json.dump(contacts, f, indent=4)
                print("Contact deleted Successfully!!")
            else:
                print("Contact not found.")
    except FileNotFoundError:
        print("No contacts available.")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your Choice: "))

        if choice == 1:
            add_contacts()

        elif choice == 2:
            view_contact()

        elif choice == 3:
            search_contact()

        elif choice == 4:
            update_contact()

        elif choice == 5:
            Delete_contact()

        elif choice == 6:
            print("Exiting... Thank you for using this Application")
            break

        else:
            print("Feature not implemented yet")

    except ValueError:
        print("Invalid Input! Please enter a valid number(1-6).")
