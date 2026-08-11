import json
import os

import pytest

import main


@pytest.fixture(autouse=True)
def reset_hospital_state():
    """Reset the patients list and clean up json file before/after each test."""
    main.patients = []  # Clear the global list in memory
    if os.path.exists("patients.json"):
        os.remove("patients.json")
    yield
    main.patients = []
    if os.path.exists("patients.json"):
        os.remove("patients.json")


def test_login_success(monkeypatch):
    inputs = iter(["hospital", "hospital123"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert main.login() is True


def test_login_failure(monkeypatch):
    inputs = iter(["wronguser", "wrongpass"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert main.login() is False


def test_add_patient(monkeypatch):
    inputs = iter(
        [
            "P001",
            "John Doe",
            "30",
            "Male",
            "Fever",
            "Dr. Smith",
            "1234567890",
            "123 Main St",
            "2026-06-06",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.add_patient()

    assert os.path.exists("patients.json")
    with open("patients.json", "r") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["patient_id"] == "P001"
    assert data[0]["name"] == "John Doe"
    assert data[0]["age"] == 30
