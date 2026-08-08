from logger_config import logger


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "college" and password == "college123":
        logger.info("User logged in successfully")
        print("\nLogin Successful\n")
        return True
    else:
        logger.critical("Unauthorized login attempt")
        print("\nInvalid Username or Password\n")
        return False
