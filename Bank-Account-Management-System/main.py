import json
import os
import sys

FILE_NAME = "accounts.json"
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "account" and password == "account123":
        print("\nLogin Successful.")
        return True
    else:
        print("\nInvalid Username or Password")
        return False


def create_account():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    account_no = input("Enter account number: ")

    for account in accounts:
        if account["account_no"] == account_no:
            print("Account Number already exists!")
            return
    name = input("Enter account holder name: ")
    phone = input("Enter phone number: ")
    account_type = input("Enter account type(savings/current): ")

    try:
        balance = float(input("Enter Initial balance: "))
    except ValueError:
        print("Invalid Balance!")
        return
    new_account = {
        "account_no": account_no,
        "name": name,
        "phone": phone,
        "account_type": account_type,
        "balance": balance,
        "transactions": [],
    }
    accounts.append(new_account)
    with open(FILE_NAME, "w") as f:
        json.dump(accounts, f, indent=4)
    print("Account Created Successfully!")


def view_account():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    if not accounts:
        print("\nNo accounts found!")
        return
    print("-" * 20)
    print("ALL BANK ACCOUNTS")
    print("-" * 20)

    for account in accounts:
        print(f"Account Number : {account['account_no']}")
        print(f"Name : {account['name']}")
        print(f"Phone : {account['phone']}")
        print(f"Account Type : {account['account_type']}")
        print(f"Balance : {account['balance']}")
        print("-" * 20)


def search_account():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    account_no = input("Enter account number to search: ")
    for account in accounts:
        if account["account_no"] == account_no:
            print("\nAccount found successfully!")
            print("-" * 20)
            print(f"Account Number : {account['account_no']}")
            print(f"Name : {account['name']}")
            print(f"Phone : {account['phone']}")
            print(f"Account Type : {account['account_type']}")
            print(f"Balance : {account['balance']}")
            print("-" * 20)
            return
    print("Account not found!")


def deposit_money():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    account_no = input("Enter Account Number: ")
    for account in accounts:
        if account["account_no"] == account_no:
            try:
                amount = float(input("Enter Deposit amount: "))
            except ValueError:
                print("Invalid amount!")
                return
            if amount <= 0:
                print("Amount must be greater than zero!")
                return
            account["balance"] += amount
            account["transactions"].append(f"Deposited{amount}")
            with open(FILE_NAME, "w") as f:
                json.dump(accounts, f, indent=4)
            print("Amount Deposited Successfully!")
            print("Updated Balance:", account["balance"])
            return

    print("Account not found!")


def withdraw_money():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)

    account_no = input("Enter Account Number: ")

    for account in accounts:
        if account["account_no"] == account_no:

            try:
                amount = float(input("Enter Withdraw Amount: "))
            except ValueError:
                print("Invalid Amount!")
                return

            if amount <= 0:
                print("Amount must be greater than zero!")
                return

            if amount > account["balance"]:
                print("Insufficient Balance!")
                return

            account["balance"] -= amount
            account["transactions"].append(f"Withdrawn ₹{amount}")

            with open(FILE_NAME, "w") as f:
                json.dump(accounts, f, indent=4)

            print("Amount Withdrawn Successfully!")
            print(f"Updated Balance: ₹{account['balance']}")
            return

    print("Account Not Found!")


def transfer_money():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    sender_acc = input("Enter sender acc number: ")
    receiver_acc = input("Enter receiver acc numver: ")
    sender = None
    receiver = None
    for account in accounts:
        if account["account_no"] == sender_acc:
            sender = account
        elif account["account_no"] == receiver_acc:
            receiver = account
    if sender is None:
        print("Sender Account not found!")
        return

    if receiver is None:
        print("Receiver Account not found!")
        return
    try:
        amount = float(input("Enter Transfer amount: "))
    except ValueError:
        print("Invalid Amount!")
        return

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    if sender["balance"] < amount:
        print("Insufficient Balance!")
        return

    sender["balance"] -= amount
    receiver["balance"] += amount

    sender["transactions"].append(f"Transferred {amount} to Account {receiver_acc}")
    receiver["transactions"].append(f"Received {amount} from Account {sender_acc}")
    with open(FILE_NAME, "w") as f:
        json.dump(accounts, f, indent=4)
    print("Money Transferred Successfully!")
    print(f"Sender Balance: {sender['balance']}")
    print(f"Receiver Balance: {receiver['balance']}")


def update_account():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    account_no = input("Enter account number to update: ")

    for account in accounts:
        if account["account_no"] == account_no:
            account["name"] = input("Enter New Name: ")
            account["phone"] = input("Enter new phone number: ")
            account["account_type"] = input("Enter new account type(savings/current): ")
            with open(FILE_NAME, "w") as f:
                json.dump(accounts, f, indent=4)
            print("Account updated successfully!")
            return
    print("Account Not Found!")


def delete_account():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    account_no = input("Enter Account Number to delete: ")
    for account in accounts:
        if account["account_no"] == account_no:
            accounts.remove(account)
            with open(FILE_NAME, "w") as f:
                json.dump(accounts, f, indent=4)
            print("Account Deleted Successfully!")
            return

    print("Account not Found!")


def check_balance():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)
    account_no = input("Enter Account Number: ")
    for account in accounts:
        if account["account_no"] == account_no:
            print("\nAccount found successfully!")
            print("-" * 20)
            print(f"Account Number : {account['account_no']}")
            print(f"Account holder: {account['name']}")
            print(f"Current Balance: {account['balance']}")
            print("-" * 20)
            return
    print("Account not found!")


def transaction_history():
    with open(FILE_NAME, "r") as f:
        accounts = json.load(f)

    account_no = input("Enter Account Number: ")

    for account in accounts:
        if account["account_no"] == account_no:
            print("\nTransaction History")
            print("-" * 30)

            if not account["transactions"]:
                print("No Transactions Found!")
                return

            for transaction in account["transactions"]:
                print(transaction)

            print("-" * 30)
            return

    print("Account Not Found!")


def main_app():
    if login():
        print("\nWelcome to Bank Management System")
    else:
        print("\nPlease enter correct Username or Password")
        sys.exit()

    while True:
        print("-" * 20)
        print("BANK MANAGEMENT SYSTEM")
        print("-" * 20)
        print("1. Create New Account")
        print("2. View All Accounts")
        print("3. Search Account")
        print("4. Deposit Account")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. Update Account Details")
        print("8. Delete Account")
        print("9. Check Balance")
        print("10. Transaction History")
        print("11. Exit")
        print("-" * 20)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please Enter a valid Choice.")
            continue

        if choice == 1:
            create_account()

        elif choice == 2:
            view_account()

        elif choice == 3:
            search_account()

        elif choice == 4:
            deposit_money()

        elif choice == 5:
            withdraw_money()

        elif choice == 6:
            transfer_money()

        elif choice == 7:
            update_account()

        elif choice == 8:
            delete_account()

        elif choice == 9:
            check_balance()

        elif choice == 10:
            transaction_history()

        elif choice == 11:
            print("Exiting....")
            print("\nThank you for using this application\n")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_app()
