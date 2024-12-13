# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# Kornel Cieslik, 12/6/2024, Created Script
# Kornel Cieslik, 12/13/2024, Tune Ups, Added Doc Strings, Mark Downs
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):
    """
    Unit tests for the Person class to ensure correct behavior of
    attributes like first name, last name, and string representation.
    """

    def test_first_name_setter_valid(self):
        """Test that the first_name setter accepts valid input."""
        person = Person()  # initializing
        person.first_name = "Kornel"
        self.assertEqual(person.first_name, "Kornel")

    def test_first_name_setter_invalid(self):
        """Test that the first_name setter raises a ValueError for invalid input."""
        person = Person()  # initializing
        with self.assertRaises(ValueError):
            person.first_name = "Kornel123"

    def test_last_name_setter_valid(self):
        """Test that the last_name setter accepts valid input."""
        person = Person()
        person.last_name = "Cieslik"
        self.assertEqual(person.last_name, "Cieslik")

    def test_last_name_setter_invalid(self):
        """Test that the last_name setter raises a ValueError for invalid input."""
        person = Person()
        with self.assertRaises(ValueError):
            person.last_name = "Cieslik123"

    def test_string_representation(self):
        """Test the string representation of a Person object."""
        person = Person("Kornel", "Cieslik")
        self.assertEqual(str(person), "Kornel,Cieslik")

class TestEmployee(unittest.TestCase):
    """
    Unit tests for the Employee class to ensure correct behavior of
    attributes like review_date, review_rating, and inheritance from Person.
    """

    def test_review_date_setter_valid(self):
        """Test that the review_date setter accepts a valid date in YYYY-MM-DD format."""
        employee = Employee()
        employee.review_date = "2024-12-06"
        self.assertEqual(employee.review_date, "2024-12-06")

    def test_review_date_setter_invalid(self):
        """Test that the review_date setter raises a ValueError for an invalid date format."""
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_date = "06-12-2024"  # invalid date format, should be YYYY-MM-DD

    def test_review_rating_setter_valid(self):
        """Test that the review_rating setter accepts a valid rating (e.g., within allowed range)."""
        employee = Employee()
        employee.review_rating = 5
        self.assertEqual(employee.review_rating, 5)

    def test_review_rating_setter_invalid(self):
        """Test that the review_rating setter raises a ValueError for an invalid rating."""
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_rating = 6  # invalid rating, assuming allowed range is 1-5

    def test_string_representation(self):
        """Test the string representation of an Employee object."""
        employee = Employee("Kornel", "Cieslik", "2024-12-06", 5)
        self.assertEqual(str(employee), "Kornel,Cieslik,2024-12-06,5")

    def test_employee_inheritance(self):
        """Test that Employee correctly inherits from Person."""
        employee = Employee("Kornel", "Cieslik", "2024-12-06", 5)
        self.assertIsInstance(employee, Person)

if __name__ == '__main__':
    unittest.main()

