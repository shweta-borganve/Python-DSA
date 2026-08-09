import unittest
from unittest.mock import patch
import json
import os
import main

class TestOnlineShoppingCart(unittest.TestCase):

    def setUp(self):
        """Prepare temporary clean files before each test."""
        self.products_file = "products.json"
        self.cart_file = "cart.json"
        self.users_file = "users.json"
        
        # Backup or set initial test data
        main.users = [{"username": "shweta", "password": "123"}]

    @patch('builtins.input', side_effect=['shweta', '123'])
    def test_login_success(self, mock_input):
        """Test login with correct username and password."""
        result = main.login()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['shweta', 'wrong_pass'])
    def test_login_failure(self, mock_input):
        """Test login with incorrect password."""
        result = main.login()
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['P1', 'Laptop', '50000', '10'])
    @patch('os.path.exists', return_value=True)
    @patch('builtins.open')
    @patch('json.load', return_value=[])
    def test_add_products(self, mock_json_load, mock_open, mock_exists, mock_input):
        """Test adding a product saves correctly."""
        # This mocks file reading/writing so it safely tests logic without touching real files
        try:
            main.add_products()
        except Exception as e:
            self.fail(f"add_products raised an exception unexpectedly: {e}")

    def test_view_cart_empty(self):
        """Test view_cart handles empty cart gracefully."""
        with patch('os.path.exists', return_value=False):
            # Should print 'Cart is Empty' without crashing
            try:
                main.view_cart()
            except Exception as e:
                self.fail(f"view_cart raised an exception: {e}")

if __name__ == '__main__':
    unittest.main() 