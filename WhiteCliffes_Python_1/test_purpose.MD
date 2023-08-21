# Test Purpose

The provided unit tests are designed to test various functions within the Python console app. 

## Test show_menu Function:

This test is checking the show_menu function.
It uses @patch to mock the standard output (sys.stdout) and captures the printed output.

The test expects that calling show_menu will print the correct menu to the console.

## Test show_items Function:

This test is checking the show_items function.
Similar to the previous test, it uses @patch to mock the standard output (sys.stdout) and captures the printed output.

The test expects that calling show_items will print the list of available items to the console and checks output matches the expected list.

## Test calculate_total Function:

This test is checking the calculate_total function.
It calls calculate_total with a list of selected items.

The test expects that calculate_total correctly calculates the total price of the selected items and checks the result matches the expected total.

## Test display_bought_items Function:

This test is checking the display_bought_items function.
It calls display_bought_items with a list of selected items.

The test expects that display_bought_items correctly displays the items that were bought in the expected format, and checks the output matches.

The if __name__ == '__main__': block at the end of the script ensures that when you run this script, it will execute the unit tests using unittest.main().
