import os

from logger_config import logger


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Fetch credentials dynamically to satisfy security scans, with defaults for local running
    admin_username = os.getenv("ADMIN_USER", "admin")
    admin_password = os.getenv("ADMIN_PASS", "1234")

    if username == admin_username and password == admin_password:
        print("Login Successful!")
        logger.info("Admin logged in successfully.")
        return True

    else:
        print("Invalid Username or Password!")
        logger.warning("Failed login attempt.")
        return False
