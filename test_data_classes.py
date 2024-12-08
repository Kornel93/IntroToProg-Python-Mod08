# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# Kornel Cieslik, 12/6/2024, Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from Module08.data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_first_name_setter_valid(self):
        person = Person() #initializing
        person.first_name = "Kornel"
        self.assertEqual(person.first_name, "Kornel")

    def test_first_name_setter_invalid(self):
        person = Person() #initializing
        with self.assertRaises(ValueError):
            person.first_name = "Kornel123"

    def test_last_name_setter_valid(self):
        person = Person()
        person.last_name = "Cieslik"
        self.assertEqual(person.last_name,"Cieslik")

    def test_last_name_setter_invalid(self):
        person = Person()
        with self.assertRaises(ValueError):
            person.last_name = "Cieslik123"

    def test_string_representation(self):
        person = Person("Kornel", "Cieslik")
        self.assertEqual(str(person), "Kornel,Cieslik")

class TestEmployee(unittest.TestCase):
    def test_review_date_setter_valid(self):
        employee = Employee()
        employee.review_date = "2024-12-06"
        self.assertEqual(employee.review_date, "2024-12-06")

    def test_review_date_setter_invalid(self):
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_date = "06-12-2024" #invalid date format, YYYY/MM/DD

    def test_review_rating_setter_valid(self):
        employee = Employee()
        employee.review_rating = 5
        self.assertEqual(employee.review_rating, 5)

    def test_review_rating_setter_invalid(self):
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_rating = 6

    def test_string_representation(self):
        employee = Employee("Kornel", "Cieslik", "2024-12-06", 5)
        self.assertEqual(str(employee), "Kornel,Cieslik,2024-12-06,5")

    def test_employee_inheritance(self):
        employee = Employee("Kornel", "Cieslik", "2024-12-06", 5)

if __name__ == '__main__':
    unittest.main()

