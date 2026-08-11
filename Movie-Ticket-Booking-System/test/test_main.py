import json
import os

import pytest


# Mocking the JSON database files for testing
@pytest.fixture(autouse=True)
def clean_test_files():
    # Setup: remove any existing test files before running
    for file in ["users.json", "movies.json", "bookings.json"]:
        if os.path.exists(file):
            os.remove(file)
    yield
    # Teardown: clean up after test
    for file in ["users.json", "movies.json", "bookings.json"]:
        if os.path.exists(file):
            os.remove(file)


def test_user_registration_and_persistence():
    from main import save_users, users

    # Clear out any leftover data from previous tests
    users.clear()

    # Simulate adding user data directly or testing functions
    users.append({"username": "testuser", "password": "password123"})
    save_users()

    assert os.path.exists("users.json")
    with open("users.json", "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["username"] == "testuser"


def test_movie_addition_and_availability():
    from main import movies, save_movies

    # Clear out any leftover data from previous tests
    movies.clear()

    movies.append({"title": "Avatar", "showtime": "6:00 PM", "available_seats": 20})
    save_movies()

    with open("movies.json", "r") as f:
        data = json.load(f)
    assert data[0]["title"] == "Avatar"
    assert data[0]["available_seats"] == 20


def test_ticket_booking_seat_reduction():
    from main import bookings, movies, save_bookings, save_movies

    # Clear out any leftover data from previous tests
    movies.clear()
    bookings.clear()

    # Setup initial movie state
    movies.append({"title": "Matrix", "showtime": "9:00 PM", "available_seats": 10})

    # Simulate a successful booking logic check
    movie_title = "Matrix"
    tickets = 3

    for movie in movies:
        if (
            movie["title"].lower() == movie_title.lower()
            and tickets <= movie["available_seats"]
        ):
            movie["available_seats"] -= tickets
            bookings.append(
                {"username": "neo", "movie_title": movie["title"], "tickets": tickets}
            )
            save_movies()
            save_bookings()

    assert movies[0]["available_seats"] == 7
    assert len(bookings) == 1
    assert bookings[0]["tickets"] == 3
