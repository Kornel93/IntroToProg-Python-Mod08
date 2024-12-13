# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# Description: Unit tests for FileProcessor class methods to ensure proper file operations.
# Kornel Cieslik, 12/6/2024, Created Script
# Kornel Cieslik, 12/13/2024, Tune Ups, Added Doc Strings, Mark Downs
# ------------------------------------------------------------------------------------------------- #

import unittest
import json
from data_classes import Employee
from processing_classes import FileProcessor  # Assuming your class is in file_processor.py


class TestFileProcessor(unittest.TestCase):
    """
    A class for testing the functionality of the FileProcessor class methods.

    Methods:
    - setUp: Prepares a test file with predefined content before each test.
    - test_read_employee_data_from_file: Tests reading employee data from a file.
    - test_write_employee_data_to_file: Tests writing employee data to a file.
    - tearDown: Cleans up the test file after each test.

    ChangeLog:
    - Kornel Cieslik, 12/6/2024: Created script.
    - Kornel Cieslik, 12/13/2024: Added detailed docstrings and enhancements.
    """

    test_file = "test_employee_data.json"  # File used for testing

    def setUp(self):
        """
        Create a test file with predefined employee data before each test.

        This method is executed before each test case to ensure consistent testing conditions.
        """
        employee_data = [
            {"FirstName": "Kornel", "LastName": "Cieslik", "ReviewDate": "2024-12-06", "ReviewRating": 5},
            {"FirstName": "Cieslik", "LastName": "Kornel", "ReviewDate": "2024-12-05", "ReviewRating": 4}
        ]
        with open(self.test_file, "w") as file:
            json.dump(employee_data, file)

    def test_read_employee_data_from_file(self):
        """
        Test the functionality of reading employee data from a file.

        This method verifies that the `read_employee_data_from_file` method:
        - Loads the correct number of employee records.
        - Maps file data to Employee objects correctly.
        """
        employee_data = []  # Initialize an empty list to store data to be read and processed
        FileProcessor.read_employee_data_from_file(self.test_file, employee_data, Employee)

        # Validate that the data has been loaded correctly
        self.assertEqual(len(employee_data), 2)  # Check that there are two entries in the list
        self.assertEqual(employee_data[0].first_name, "Kornel")  # Verify the first employee's first name
        self.assertEqual(employee_data[1].review_rating, 4)  # Verify the second employee's review rating

    def test_write_employee_data_to_file(self):
        """
        Test the functionality of writing employee data to a file.

        This method verifies that the `write_employee_data_to_file` method:
        - Correctly writes employee data to a file.
        - Saves the data in a JSON format that can be read back accurately.
        """
        # Create a new employee to write to the file
        employee_data = [Employee("Cieslik", "Cieslik", "2024-12-03", 5)]

        # Write to the test file
        FileProcessor.write_employee_data_to_file(self.test_file, employee_data)

        # Read the file content back
        with open(self.test_file, "r") as file:
            content = json.load(file)

        # Validate that the file contains the new employee data
        self.assertEqual(len(content), 1)  # Check that there is one entry in the test file
        self.assertEqual(content[0]["FirstName"], "Cieslik")  # Verify the first name
        self.assertEqual(content[0]["ReviewRating"], 5)  # Verify the review rating

    def tearDown(self):
        """
        Clean up the test file after each test case.

        This method is executed after each test case to remove the test file and ensure no residual data remains.
        """
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
