import os
import json
import pytest
import main

@pytest.fixture(autouse=True)
def setup_teardown_file():
    """Setup a temporary accounts file for each test and clean it up afterward."""
    main.FILE_NAME = "test_accounts.json"
    # Initialize empty accounts list
    with open(main.FILE_NAME, "w") as f:
        json.dump([], f)
    yield
    if os.path.exists(main.FILE_NAME):
        os.remove(main.FILE_NAME)

def test_create_account(monkeypatch):
    """Test creating a new bank account."""
    # Simulate user inputs for: account_no, name, phone, account_type, balance
    inputs = iter(["101", "John Doe", "9876543210", "savings", "5000"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.create_account()

    # Verify account was saved in JSON file
    with open(main.FILE_NAME, "r") as f:
        accounts = json.load(f)

    assert len(accounts) == 1
    assert accounts[0]["account_no"] == "101"
    assert accounts[0]["name"] == "John Doe"
    assert accounts[0]["balance"] == 5000.0

def test_deposit_money(monkeypatch):
    """Test depositing money into an account."""
    # Pre-populate an account
    initial_data = [{
        "account_no": "102",
        "name": "Jane Doe",
        "phone": "1234567890",
        "account_type": "savings",
        "balance": 1000.0,
        "transactions": []
    }]
    with open(main.FILE_NAME, "w") as f:
        json.dump(initial_data, f)

    # Simulate user inputs for: account_no, deposit amount
    inputs = iter(["102", "500"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.deposit_money()

    # Verify balance update
    with open(main.FILE_NAME, "r") as f:
        accounts = json.load(f)

    assert accounts[0]["balance"] == 1500.0
    assert "Deposited500.0" in accounts[0]["transactions"]

def test_withdraw_money_insufficient(monkeypatch):
    """Test withdrawal failure due to insufficient balance."""
    initial_data = [{
        "account_no": "103",
        "name": "Bob Smith",
        "phone": "5555555555",
        "account_type": "current",
        "balance": 200.0,
        "transactions": []
    }]
    with open(main.FILE_NAME, "w") as f:
        json.dump(initial_data, f)

    # Try to withdraw more than available balance
    inputs = iter(["103", "500"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Should print "Insufficient Balance!" and return without changing balance
    main.withdraw_money()

    with open(main.FILE_NAME, "r") as f:
        accounts = json.load(f)

    assert accounts[0]["balance"] == 200.0 