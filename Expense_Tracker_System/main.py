def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "expense" and password == "expense123":
        print("Login Successful")
        return True
    else:
        print("Invalid Username or Password")
        return False


def menu():
    print("\n" + "-" * 50)
    print("         EXPENSE TRACKER SYSTEM")
    print("-" * 50)

    print("1. Add Expense")
    print("2. View Expense")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Total Expense")
    print("7. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Please enter a valid number.")


def add_expense():
    print("\nADD EXPENSE")
    print("-" * 30)

    try:
        date = input("Enter Date(DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        description = input("Enter description: ")

        with open("expenses.txt", "a") as f:
            f.write(f"{date}, {category}, {amount}, {description}\n")

        print("\nExpense Added Successfully!")
    except ValueError:
        print("Amount must be a number.")


def view_expense():
    print("\nVIEW EXPENSE")

    try:
        with open("expenses.txt", "r") as f:
            expenses = f.readlines()
        if len(expenses) == 0:
            print("No expenses available")
        else:
            for expense in expenses:
                data = expense.strip().split(",")

                print("Date       :", data[0])
                print("Category   :", data[1])
                print("Amount     :", data[2])
                print("Description:", data[3])
                print("----------------------")

    except FileNotFoundError:
        print("No Expenses available")


def search_expense():
    print("\nSEARCH EXPENSE")
    print("-" * 30)

    search_category = input("Enter Category to Search: ")
    found = False
    try:
        with open("expenses.txt", "r") as f:
            expenses = f.readlines()
        for expense in expenses:
            data = expense.strip().split(",")
            if data[1].strip().lower() == search_category.lower():
                print("\nExpense Found")
                print("Date :", data[0].strip())
                print("Category :", data[1].strip())
                print("Amount :", data[2].strip())
                print("Description :", data[3].strip())
                print("-" * 30)

                found = True
        if not found:
            print("No expenses found for this category.")

    except FileNotFoundError:
        print("No expenses available")


def update_expense():
    print("\nUPDATE  EXPENSE")
    print("-" * 30)
    search_category = input("Enter a category to update: ")
    updated = False

    try:
        with open("expenses.txt", "r") as f:
            expenses = f.readlines()
        with open("expenses.txt", "w") as f:
            for expense in expenses:
                data = expense.strip().split(",")
                if data[1].strip().lower() == search_category.lower():
                    print("\nExpense Found.")
                    date = input("Enter New Date: ")
                    category = input("Enter New Category: ")
                    amount = float(input("Enter New Amount: "))
                    description = input("Enter New Category: ")

                    f.write(f"{date},{category},{amount},{description}\n")
                    updated = True
                else:
                    f.write(expense)
        if updated:
            print("Expense updated successfully!!!")
        else:
            print("Expense not found")
    except ValueError:
        print("Amount must be a number.")


def delete_expense():
    print("\nDELETE EXPENSE")
    print("-" * 30)
    search_category = input("Enter category to delete: ")
    deleted = False

    try:
        with open("expenses.txt", "r") as f:
            expenses = f.readlines()
        with open("expenses.txt", "w") as f:
            for expense in expenses:
                data = expense.strip().split(",")
                if data[1].strip().lower() == search_category.lower():
                    deleted = True
                    continue
                else:
                    f.write(expense)
            if deleted:
                print("Expense deleted successfully!")
            else:
                print("Expense not found.")
    except FileNotFoundError:
        print("No expenses found")


def total_expense():
    print("\nTOTAL EXPENSE")
    print("-" * 30)

    total = 0
    try:
        with open("expenses.txt", "r") as f:
            expenses = f.readlines()
        if len(expenses) == 0:
            print("No expenses available.")
            return
        for expense in expenses:
            data = expense.strip().split(",")
            total += float(data[2].strip())
        print(f"Total Expense: ₹ {total}")

    except FileNotFoundError:
        print("No expenses available.")
    except ValueError:
        print("Invalid amount found in the file.")


def main():

    if login():

        while True:

            choice = menu()

            if choice == 1:
                add_expense()

            elif choice == 2:
                view_expense()

            elif choice == 3:
                search_expense()

            elif choice == 4:
                update_expense()

            elif choice == 5:
                delete_expense()

            elif choice == 6:
                total_expense()

            elif choice == 7:
                print("\nThank you for using Expense Tracker System.")
                break

            else:
                print("Invalid Choice.")


main()
