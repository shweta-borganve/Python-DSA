import json
import os
from datetime import datetime

FILE_NAME = "inventory.json"

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "admin123":
        print("\nLogin Successful!\n")
        return True
    else:
        print("\nInvalid Username or Password!")
        return False


def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(products):
    with open(FILE_NAME, "w") as file:
        json.dump(products, file, indent=4)


def add_product():
    products = load_data()

    product = {
        "Product ID": input("Enter Product ID: "),
        "Product Name": input("Enter Product Name: "),
        "Category": input("Enter Category: "),
        "Price": float(input("Enter Product Price: ")),
        "Quantity": int(input("Enter Product Quantity: ")),
        "Supplier": input("Enter Supplier Name: "),
        "Date Added": datetime.now().strftime("%d-%m-%Y")
    }

    products.append(product)
    save_data(products)

    print("\nProduct Added Successfully!\n")

def view_product():
    products = load_data()

    if len(products) == 0:
        print("\nNo products found!")
        return
    print("\n" + "=" * 50)
    for product in products:
        print("Product ID: ", product["Product ID"])
        print("Product Name: ", product["Product Name"])
        print("Category: ", product["Category"])
        print("Price: ", product["Price"])
        print("Quantity: ", product["Quantity"])
        print("Supplier: ", product["Supplier"])
        print("Date Added: ", product["Date Added"])
        print("-" * 50)

def search_product():
    products = load_data()
    product_id = input("Enter Product ID to search: ")
    found = False
    for product in products:
        if product["Product ID"] == product_id:
            print("\nProduct found!")
            print("-" * 50)
            print("Product ID: ", product["Product ID"])
            print("Product Name: ", product["Product Name"])
            print("Category: ", product["Category"])
            print("Price: ", product["Price"])
            print("Quantity: ", product["Quantity"])
            print("Supplier: ", product["Supplier"])
            print("Date Added: ", product["Date Added"])
            print("-" * 50)

            found = True
            break
        if not found:
            print("\nProduct not found!") 

def update_product():
    products = load_data()
    product_id = input("Enter product ID to update: ")
    found = False
    for product in products:
        if product["Product ID"] == product_id:
            print("\nEnter New Details")
            product["Product Name"] = input("Enter Product Name: ")
            product["Price"] = input("Enter product Price: ")
            product["Quantity"] = input("Enter product Quantity: ")
            product["Supplier"] = input("Enter Supplier Name: ")
            save_data(products)
            print("\nProduct Updated Successfully!") 
            found = True
            break
        if not found:
            print("\nProduct Not Found!") 

def delete_contact():
    products = load_data()
    product_id = input("Enter product ID to delete: ")
    found = False
    for product in products:
        if product["Product ID"] == product_id:
            products.remove(product)
            save_data(products) 
            print("\nProduct deleted Successfully!")
            found = True
            break
        if not found:
            print("\nProduct not found!") 

def stock_in():
    products = load_data()
    product_id = input("Enter Product ID: ")
    found = False
    for product in products:
        if product["Product ID"] == product_id:
            quantity = int(input("Enter Quantity to Add: "))
            product["Quantity"] += quantity
            save_data(products)
            print("\nStock updated Successfully!")
            print("Current Quantity:", product["Quantity"])
            found = True
            break
        if not found:
            print("\nProduct not Found!")

def stock_out():
    products = load_data()
    product_id = input("Enter product ID: ") 
    found = False
    for product in products:
        if product["Product ID"] == product_id:
            quantity = int(input("Enter Quantity to remove: "))
            if quantity <= product["Quantity"]:
                product["Quantity"] -= quantity
                save_data(products)
                print("\nStock updated successfully!")
                print("Current Quantity:", product["Quantity"])
            else:
                print("\nInsufficient Stock!")
                found = True
                break
    if not found:
        print("\nProduct not Found!") 

def low_stock_alert():
    products = load_data()
    found = False
    for product in products:
        if product["Quantity"] < 5:
            print("Product ID: ", product["Product ID"])
            print("Product Name: ", product["Product Name"])
            print("Category: ", product["Category"])
            print("Quantity: ", product["Quantity"])
            found = True
        if not found:
            print("No low stock products found!") 

def Inventory_summary():
    products = load_data()
    total_products = len(products)
    total_quantity = 0
    total_value = 0

    for product in products:
        total_quantity += product["Quantity"]
        total_value += product["Price"] * product["Quantity"]

        print("-" * 20)
        print("INVENTORY SUMMARY")
        print("=" * 20)
        print("Total Products: ", total_products)
        print("Total Quantity: ", total_quantity)
        print("Total Value: ", total_value)

# -------------------- Main Program --------------------

if login():

    while True:
        print("\n" + "=" * 50)
        print("      INVENTORY MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Product")
        print("2. View Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Stock In")
        print("7. Stock Out")
        print("8. Low Stock Alert")
        print("9. Inventory Summary")
        print("10. Exit")

        try:
            choice = int(input("\nEnter your Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_product()

        elif choice == 2:
            view_product() 

        elif choice == 3:
            search_product() 

        elif choice == 4:
            update_product() 

        elif choice == 5:
            delete_contact() 

        elif choice == 6:
            stock_in() 

        elif choice == 7:
            stock_out() 

        elif choice == 8:
            low_stock_alert() 

        elif choice == 9:
            Inventory_summary() 

        elif choice == 10:
            print("\nThank you for using Inventory Management System.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Access Denied.")