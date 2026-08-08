import json
import os

# Load users
if os.path.exists("users.json"):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = []
else:
    users = []


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login Successful!")
            return True

    print("Invalid Username or Password.")
    return False


def add_products():
    if os.path.exists("products.json"):
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except json.JSONDecodeError:
            products = []
    else:
        products = []

    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    product_price = float(input("Enter Product Price: "))
    product_stock = int(input("Enter Product Stock: "))

    product = {
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "stock": product_stock,
    }

    products.append(product)

    with open("products.json", "w") as f:
        json.dump(products, f, indent=4)

    print("Product Added Successfully!")


def view_products():
    if os.path.exists("products.json"):
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except json.JSONDecodeError:
            products = []
    else:
        products = []

    if len(products) == 0:
        print("No Products Available")
    else:
        print("\n===== Available Products =====")
        for product in products:
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ₹{product['price']}")
            print(f"Stock: {product['stock']}")
            print("------------------------")


def search_product():
    if os.path.exists("products.json"):
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except json.JSONDecodeError:
            products = []
    else:
        products = []
    if len(products) == 0:
        print("No products found")
        return
    search = input("Enter product name to search: ").lower()
    found = False
    for product in products:
        if product["name"].lower() == search:
            print("\nProduct found")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Stock: {product['stock']}")
            found = True
            break
    if not found:
        print("Product not found")


def add_to_cart():
    if os.path.exists("products.json"):
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except json.JSONDecodeError:
            products = []
    else:
        products = []

    if os.path.exists("cart.json"):
        try:
            with open("cart.json", "r") as f:
                cart = json.load(f)
        except json.JSONDecodeError:
            cart = []
    else:
        cart = []

    product_id = input("Enter Product ID: ")
    quantity = int(input("Enter Quantity: "))

    for product in products:
        if product["id"] == product_id:

            if quantity > product["stock"]:
                print("Insufficient Stock")
                return

            cart_item = {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity,
            }

            cart.append(cart_item)

            product["stock"] -= quantity

            with open("products.json", "w") as f:
                json.dump(products, f, indent=4)

            with open("cart.json", "w") as f:
                json.dump(cart, f, indent=4)

            print("Product Added to Cart Successfully!")
            return

    print("Product Not Found")


def view_cart():
    if os.path.exists("cart.json"):
        try:
            with open("cart.json", "r") as f:
                cart = json.load(f)
        except json.JSONDecodeError:
            cart = []
    else:
        cart = []

    if len(cart) == 0:
        print("Cart is Empty")
    else:
        print("\n===== Cart =====")

        total = 0

        for item in cart:
            amount = item["price"] * item["quantity"]
            total += amount

            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ₹{item['price']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Amount: ₹{amount}")
            print("--------------------------")

        print(f"Total Bill: ₹{total}")


def update_cart():
    if os.path.exists("cart.json"):
        try:
            with open("cart.json", "r") as f:
                cart = json.load(f)
        except json.JSONDecodeError:
            cart = []
    else:
        cart = []

    if len(cart) == 0:
        print("Cart is Empty")
        return

    product_id = input("Enter Product ID to Update: ")
    new_quantity = int(input("Enter New Quantity: "))

    found = False

    for item in cart:
        if item["id"] == product_id:
            item["quantity"] = new_quantity
            found = True
            break

    if found:
        with open("cart.json", "w") as f:
            json.dump(cart, f, indent=4)
        print("Cart Updated Successfully!")
    else:
        print("Product Not Found in Cart")


def remove_from_cart():
    if os.path.exists("cart.json"):
        try:
            with open("cart.json", "r") as f:
                cart = json.load(f)
        except json.JSONDecodeError:
            cart = []
    else:
        cart = []

    if len(cart) == 0:
        print("Cart is Empty")
        return

    product_id = input("Enter Product ID to Remove: ")

    found = False

    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            found = True
            break

    if found:
        with open("cart.json", "w") as f:
            json.dump(cart, f, indent=4)
        print("Product Removed from Cart Successfully!")
    else:
        print("Product Not Found in Cart")


def checkout():
    if os.path.exists("cart.json"):
        try:
            with open("cart.json", "r") as f:
                cart = json.load(f)
        except json.JSONDecodeError:
            cart = []
    else:
        cart = []

    if len(cart) == 0:
        print("Cart is Empty")
        return

    total = 0

    print("\n========== BILL ==========")

    for item in cart:
        amount = item["price"] * item["quantity"]
        total += amount

        print(f"Product : {item['name']}")
        print(f"Price   : ₹{item['price']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Amount  : ₹{amount}")
        print("---------------------------")

    print(f"Total Bill: ₹{total}")

    confirm = input("Confirm Checkout? (yes/no): ").lower()

    if confirm == "yes":
        with open("cart.json", "w") as f:
            json.dump([], f, indent=4)

        print("Checkout Successful!")
        print("Thank you for shopping with us.")
    else:
        print("Checkout Cancelled.")


def shopping_menu():
    while True:
        print("\n===== Shopping Menu =====")
        print("1. Add Products")
        print("2. View Products")
        print("3. Search Products")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Update Cart")
        print("7. Remove from Cart")
        print("8. Checkout")
        print("9. Logout")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid choice.")
            continue

        if choice == 1:
            add_products()

        elif choice == 2:
            view_products()

        elif choice == 3:
            search_product()

        elif choice == 4:
            add_to_cart()

        elif choice == 5:
            view_cart()

        elif choice == 6:
            update_cart()

        elif choice == 7:
            remove_from_cart()

        elif choice == 8:
            checkout()

        elif choice == 9:
            print("Logged Out Successfully.")
            break

        else:
            print("Invalid Choice.")


while True:
    print("\n===== Online Shopping Cart System =====")
    print("1. Login")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:
        if login():
            shopping_menu()

    elif choice == 2:
        print("Thank You for using the Online Shopping Cart System!")
        break

    else:
        print("Invalid Choice.")
