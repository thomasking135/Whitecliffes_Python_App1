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

# Calculate total
    def test_calculate_total(self):
        selected_items = [1, 3, 5]
        total = main.calculate_total(selected_items)
        self.assertEqual(total, 215)  # TV ($100) + Camera ($65) + Ricecooker ($50)

# Display Items bought
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_bought_items(self, mock_stdout):
        selected_items = [1, 1, 2, 3, 4, 5]
        main.display_bought_items(selected_items)
        expected_output = "2 X TV\n1 X Stereo\n1 X Camera\n1 X Laptop\n1 X Ricecooker\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()

## Results  - 1 out of the 4 tests failed. Adjustments were made based on these results



