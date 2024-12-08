# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# Kornel Cieslik, 12/6/2024, Created Script
# ------------------------------------------------------------------------------------------------- #
import unittest
import json
from data_classes import Employee
from processing_classes import FileProcessor  # Assuming your class is in file_processor.py


class TestFileProcessor(unittest.TestCase):
    test_file = "test_employee_data.json"  # File used for testing

    def setUp(self):
        """Create a file with known content before each test."""
        employee_data = [
            {"FirstName": "Kornel", "LastName": "Cieslik", "ReviewDate": "2024-12-06", "ReviewRating": 5},
            {"FirstName": "Cieslik", "LastName": "Kornel", "ReviewDate": "2024-12-05", "ReviewRating": 4}
        ]
        with open(self.test_file, "w") as file:
            json.dump(employee_data, file)

    def test_read_employee_data_from_file(self):
        """Test reading employee data from an actual file."""

        employee_data = []
        FileProcessor.read_employee_data_from_file(self.test_file, employee_data, Employee)

        # Check that data has been loaded correctly
        self.assertEqual(len(employee_data), 2)
        self.assertEqual(employee_data[0].first_name, "Kornel")
        self.assertEqual(employee_data[1].review_rating, 4)

    def test_write_employee_data_to_file(self):
        """Test writing employee data to a file."""

        # Create a new employee to write to file
        employee_data = [Employee("Cieslik", "Cieslik", "2024-12-03", 5)]

        # Write to the test file
        FileProcessor.write_employee_data_to_file(self.test_file, employee_data)

        # Read the file content back
        with open(self.test_file, "r") as file:
            content = json.load(file)

        # Check that the file contains the new employee data
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]["FirstName"], "Cieslik")
        self.assertEqual(content[0]["ReviewRating"], 5)

    def tearDown(self):
        """Clean up the test file after each test."""
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()

