try:
    username = input("Enter your UserId: ")
    Password = input("Enter your Password: ")

    if username == "Shweta" and Password == "Python123":
        print("Login Successful")
    else:
        print("Incorrect username or Password")
except Exception:
    print("Something went wrong.")
finally:
    print("Thank yoouu") 