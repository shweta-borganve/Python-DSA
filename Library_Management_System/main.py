def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "library" and password == "library123":
        print("\nLogin Successful!\n")
        return True
    else:
        print("\nInvalid username or password\n")
        return False
if not login():
    exit() 
print("Welcome to Library Management System")

def add_book():
    book_id = input("Enter a Book ID: ")
    book_name = input("Enter Book name: ")
    author = input("Enter Author name: ")
    category = input("Enter Category: ")
    quantity = int(input("Enter Quantity: "))

    with open("books.txt", "a") as f:
        f.write(f"{book_id},{book_name},{author},{category},{quantity}\n")
        print("\nBook added Successfully!")

def view_books():
    try:
        with open("books.txt", "r") as f:
            data = f.read()

            if data.strip() == "":
                print("\nNo books found!\n")
            else:
                print("\n======= BOOK LIST==========")
                print(data)
    except FileNotFoundError:
        print("\nbooks.txt file not found!\n") 

def search_book():
    search_id = input("Enter a book id to search: ")
    found = False

    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",") 
            if data[0] == search_id:
                print("\nBook Found!")
                print(f"book id : {data[0]}")
                print(f"book name : {data[1]}")
                print(f"author name : {data[2]}")
                print(f"category : {data[3]}")
                print(f"quantity : {data[4]}")
                found = True
                break
    if not found:
        print("\nBook not found!")

def issue_book():
    book_id = input("Enter Book ID to issue: ")

    updated_books = []
    found = False

    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == book_id:
                found = True

                if int(data[4]) > 0:
                    data[4] = str(int(data[4]) - 1)
                    print("\nBook Issued Successfully!")
                else:
                    print("\nBook is Out of stock!")
            updated_books.append(",".join(data))
    if found:
        with open("books.txt", "w") as f:
            for book in updated_books:
                f.write(book + "\n")
    else:
        print("\nBook not found!")

def return_book():
    book_id = input("Enter Book ID to return: ")
    updated_books = []
    found = False
    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == book_id:
                found = True
                data[4] = str(int(data[4]) + 1)
                print("\nBook Returned Successfully!")
            updated_books.append(",".join(data))
    if found:
        with open("books.txt", "w") as f:
            for book in updated_books:
                f.write(book + "\n")
    else:
        print("\nBook not found!") 

def update_book():
    book_id = input("Enter Book ID to update: ")

    updated_books = []
    found = False

    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == book_id:
                found = True

                data[1] = input("Enter New Book Name: ")
                data[2] = input("Enter New Author Name: ")
                data[3] = input("Enter New Category: ")
                data[4] = input("Enter New Quantity: ")

                print("\nBook Updated Successfully!")

            updated_books.append(",".join(data))

    if found:
        with open("books.txt", "w") as f:
            for book in updated_books:
                f.write(book + "\n")
    else:
        print("\nBook not found!") 

def delete_book():
    book_id = input("Enter your Book ID: ")
    updated_books = []
    found = False

    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == book_id:
                found = True
                print("\nBook deleted Successfully!")
                continue
            updated_books.append(",".join(data))
    if found:
        with open("books.txt", "w") as f:
            for book in updated_books:
                f.write(book + "\n")
    else:
        print("\nBook not found!") 

def count_book():
    count = 0

    with open("books.txt", "r") as f:
        for line in f:
            if line.strip():
                count = count + 1
    print(f"\nTotal Books: {count}") 
        
while True:
    print("-" * 50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("-" * 50)

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")   
    print("6. Update Book")
    print("7. Delete Book")
    print("8. Count Books")
    print("9. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nPlease enter a valid number.")
        continue

    if choice == 1:
        add_book()

    elif choice == 2:
        view_books()

    elif choice == 3:
        search_book() 

    elif choice == 4:
        issue_book() 

    elif choice == 5:
        return_book()

    elif choice == 6:
        update_book()

    elif choice == 7:
        delete_book()

    elif choice == 8:
        count_book() 

    elif choice == 9:
        print("\nThank you for using Library Management System!")
        break
    else:
        print("\nThis feature will be implemented next.\n") 