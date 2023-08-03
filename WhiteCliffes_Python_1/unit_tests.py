# To run tests enter python unit_tests.py in the console

# App unit tests
import unittest
from io import StringIO
from unittest.mock import patch

import main  # Import the module containing the code to be tested

# Test case menu unit test
class TestShoppingApp(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_menu(self, mock_stdout):
        main.show_menu()
        expected_output = "Menu:\n1) Start\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

# Item unit test

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_items(self, mock_stdout):
        main.show_items()
        expected_output = "Available items:\n1) TV $100\n2) Stereo $75\n3) Camera $65\n4) Laptop $90\n5) Ricecooker $50\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()

## Results  - 1 out of the 2 tests failed. Adjustments were made based on these results
