# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# Kornel Cieslik, 12/6/2024, Created Script
# Kornel Cieslik, 12/13/2024, Tune Ups, Added Doc Strings, Mark Downs
# ------------------------------------------------------------------------------------------------- #

import unittest
import data_classes as data
from presentation_classes import IO

class TestIO(unittest.TestCase):

    def test_output_error_messages(self):
        """Testing error message outputs"""
        IO.out_error_messages("An error occurred", Exception("Test exception"))

    def test_output_menu(self):
        menu: str = '''
        ---- Employee Ratings ------------------------------
          Select from the following menu:
            1. Show current employee rating data.
            2. Enter new employee rating data.
            3. Save data to a file.
            4. Exit the program.
        --------------------------------------------------
        '''
        IO.output_menu(menu)

    def test_input_menu_choice_valid(self):
            """ Test valid menu choice """
            print("Testing valid menu choice. Enter '1' when prompted.")
            choice = IO.input_menu_choice()  # Manually input '1' during test
            self.assertEqual(choice, '1')

    def test_input_menu_choice_invalid(self):
            """ Test invalid menu choice """
            print("Testing invalid menu choice. Enter '5' when prompted.")
            choice = IO.input_menu_choice()  # Manually input '5' during test
            self.assertEqual(choice, '5')

if __name__ == '__main__':
    unittest.main()