import json
import os 

if os.path.exists("users.json"):
    try: 
        with open("users.json", "r") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = []  
else:
    users = [] 

if os.path.exists("movies.json"):
    try:
        with open("movies.json", "r") as f:
            movies = json.load(f)
    except json.JSONDecodeError:
        movies = []
else:
    movies = [] 

if os.path.exists("bookings.json"):
    try:
        with open("bookings.json", "r") as f:
            bookings = json.load(f)
    except json.JSONDecodeError:
        bookings = [] 
else:
    bookings = [] 

def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4) 

def save_movies():
    with open("movies.json", "w") as f:
        json.dump(movies, f, indent=4) 

def save_bookings():
    with open("bookings.json", "w") as f:
        json.dump(bookings, f, indent=4) 

def register_user():
    username = input("Enter a Username: ") 
    for user in users:
        if user["username"] == username:
            print("Username already exists. Please choose a different username.")
            return
    password = input("Enter a Password: ") 
    users.append({"username": username, "password": password}) 
    save_users() 
    print("User registered successfully!") 

def user_login():
    username = input("Enter your Username: ") 
    password = input("Enter your Password: ") 
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!") 
            return True
    print("Invalid username or password. Please try again.") 
    return False 

def admin_login():
    admin_username = "admin" 
    admin_password = "admin123" 
    username = input("Enter Admin Username: ") 
    password = input("Enter Admin Password: ") 
    if username == admin_username and password == admin_password:
        print("Admin login successful!") 
        return True
    else:
        print("Invalid admin credentials. Please try again.") 
        return False
    
def add_movie():
    title = input("Enter Movie Title: ") 
    showtime = input("Enter Show Time (e.g., 7:00 PM): ") 
    available_seats = int(input("Enter Number of Available Seats: ")) 
    movies.append({"title": title, "showtime": showtime, "available_seats": available_seats}) 
    save_movies() 
    print(f"Movie '{title}' added successfully!") 

def view_movies(): 
    if not movies:
        print("No movies available at the moment.") 
        return
    print("\nAvailable Movies:")
    for idx, movie in enumerate(movies, start=1):
        print(f"{idx}. {movie['title']} - Showtime: {movie['showtime']} - Available Seats: {movie['available_seats']}") 

def update_movie(): 
    print("\nUpdate Movie Details") 
    movie_title = input("Enter the title of the movie to update: ")
    for movie in movies: 
        if movie["title"].lower() == movie_title.lower():
            new_title = input("Enter new title (leave blank to keep current): ") 
            new_showtime = input("Enter new showtime (leave blank to keep current): ") 
            new_available_seats = input("Enter new available seats (leave blank to keep current): ") 

            if new_title:
                movie["title"] = new_title
            if new_showtime:
                movie["showtime"] = new_showtime
            if new_available_seats:
                try:
                    movie["available_seats"] = int(new_available_seats)
                except ValueError:
                    print("Invalid input for available seats. Keeping current value.")

            save_movies() 
            print(f"Movie '{movie['title']}' updated successfully!") 
            return 

def book_movie(username): 
    print("\nBook a Movie Ticket") 

    if not movies:
        print("No movies available for booking at the moment.") 
        return 
    print("Available Movies:") 
    for movie in movies: 
        print(f"Title: {movie['title']}") 
        print(f"Showtime: {movie['showtime']}") 
        print(f"Available Seats: {movie['available_seats']}") 
        print("-" * 30) 
    movie_title = input("Enter the title of the movie you want to book: ") 
    tickets = int(input("Enter the number of tickets you want to book: ")) 
    for movie in movies:  
        if movie["title"].lower() == movie_title.lower(): 
            if tickets <= movie["available_seats"]: 
                movie["available_seats"] -= tickets 
                bookings.append({"username": username, "movie_title": movie["title"], "tickets": tickets}) 
                save_movies() 
                save_bookings() 
                print(f"Successfully booked {tickets} tickets for '{movie['title']}'!") 
                return 
def view_bookings(username): 
    print("\nYour Bookings:") 
    user_bookings = [booking for booking in bookings if booking["username"] == username] 
    if not user_bookings: 
        print("You have no bookings.") 
        return 
    for booking in user_bookings: 
        print(f"Movie: {booking['movie_title']} - Tickets: {booking['tickets']}") 


while True: 
    print("\n======= Movie Ticket Booking System =======")
    print("1. Admin Login") 
    print("2. User Registration")
    print("3. User Login")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): ")) 
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1: 
        if admin_login():  
            view_bookings("admin")   

    elif choice == 2: 
        register_user() 

    elif choice == 3: 
        if user_login():  
            username = input("Enter your Username: ") 
            password = input("Enter your Password: ")
            book_movie(username) 

    elif choice == 4:
        print("Exiting the Movie Ticket Booking System!\n")  
        print("Thank you for using the Movie Ticket Booking System!\n") 
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.") 