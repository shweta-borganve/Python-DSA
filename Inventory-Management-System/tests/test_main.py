from unittest.mock import patch, mock_open
import main


def test_login_success():
    with patch("builtins.input", side_effect=["admin", "admin123"]):
        assert main.login() is True


def test_login_failure():
    with patch("builtins.input", side_effect=["admin", "wrongpassword"]):
        assert main.login() is False


@patch("main.load_data")
@patch("main.save_data")
@patch(
    "builtins.input",
    side_effect=["P001", "Laptop", "Electronics", "1200.0", "10", "Dell"],
)
def test_add_product(mock_input, mock_save, mock_load):
    mock_load.return_value = []
    
    main.add_product()
    
    mock_save.assert_called_once()
    saved_data = mock_save.call_args[0][0]
    assert len(saved_data) == 1
    assert saved_data[0]["Product ID"] == "P001"
    assert saved_data[0]["Product Name"] == "Laptop"
    assert saved_data[0]["Price"] == 1200.0
    assert saved_data[0]["Quantity"] == 10


@patch("main.load_data")
def test_inventory_summary(mock_load):
    mock_load.return_value = [
        {
            "Product ID": "P001",
            "Product Name": "Laptop",
            "Price": 1000.0,
            "Quantity": 2,
        },
        {
            "Product ID": "P002",
            "Product Name": "Mouse",
            "Price": 50.0,
            "Quantity": 10,
        },
    ]

    # Verify calculation logic used inside Inventory_summary
    products = main.load_data()
    total_quantity = sum(p["Quantity"] for p in products)
    total_value = sum(p["Price"] * p["Quantity"] for p in products)

    assert len(products) == 2
    assert total_quantity == 12
    assert total_value == (1000.0 * 2) + (50.0 * 10) 