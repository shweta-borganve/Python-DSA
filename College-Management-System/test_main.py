import unittest
from unittest.mock import patch, sys
import os

class TestMainApplication(unittest.TestCase):

    @patch.dict(os.environ, {"CI": "true"})
    @patch("main.login")
    def test_ci_environment_startup(self, mock_login):
        """Test that setting CI=true bypasses login and safely exits the menu loop."""
        # Remove main from sys.modules if it was previously imported, 
        # so it re-runs the top-level execution script safely during the test
        if "main" in sys.modules:
            del sys.modules["main"]

        # Importing main will execute the top-level code and the CI check block
        import main
        
        # Verify login was never called because CI=true bypassed it
        mock_login.assert_not_called()
        self.assertTrue(main.is_ci)

    @patch("main.is_ci", False)
    @patch("main.login", return_value=True)
    @patch("builtins.input", side_effect=["6"])  # Simulate user selecting option 6 (Exit)
    def test_main_menu_exit(self, mock_input, mock_login):
        """Test that selecting option '6' breaks the main menu loop gracefully."""
        if "main" in sys.modules:
            del sys.modules["main"]

        # Import main to run the script loop with mocked input
        import main
        
        mock_login.assert_called_once()
        mock_input.assert_called()

    @patch("main.is_ci", False)
    @patch("main.login", return_value=True)
    @patch("main.student_management")
    @patch("builtins.input", side_effect=["1", "6"])  # Select option 1 (Student Mgmt), then 6 (Exit)
    def test_menu_student_management_option(self, mock_input, mock_student_mgmt, mock_login):
        """Test that choosing option 1 successfully triggers student_management()."""
        if "main" in sys.modules:
            del sys.modules["main"]

        import main
        
        # Verify that student_management function was called
        mock_student_mgmt.assert_called_once()


if __name__ == "__main__":
    unittest.main() 