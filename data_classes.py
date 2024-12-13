# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# Description: A collection of classes for managing the application
# Kornel Cieslik, 12/6/2024, Created Script
# Kornel Cieslik, 12/13/2024, Tune Ups, Added Doc Strings, Mark Downs
# ------------------------------------------------------------------------------------------------- #

from typing import List
from datetime import date

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: List["Employee"] = []  # a table of employee data
menu_choice = ''

class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    Methods:
    - __init__: Initializes a new Person object with optional first and last names.
    - __str__: Returns a string representation of the person's data.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Initializes a new instance of the Person class.

        :param first_name: The person's first name (default is an empty string).
        :param last_name: The person's last name (default is an empty string).
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Getter for the first_name property.
        Automatically capitalizes the first name.

        :return: The person's first name in title case.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        Setter for the first_name property.
        Ensures the first name contains only alphabetic characters.

        :param value: The new first name to set.
        :raises ValueError: If the name contains non-alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """
        Getter for the last_name property.
        Automatically capitalizes the last name.

        :return: The person's last name in title case.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        Setter for the last_name property.
        Ensures the last name contains only alphabetic characters.

        :param value: The new last name to set.
        :raises ValueError: If the name contains non-alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """
        String representation of the Person object.

        :return: A string in the format "FirstName,LastName".
        """
        return f"{self.first_name},{self.last_name}"

class Employee(Person):
    """
    A class representing employee data.

    Inherits from:
    - Person

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (str): The date of the employee review (YYYY-MM-DD).
    - review_rating (int): The review rating of the employee's performance (1-5).

    Methods:
    - __init__: Initializes a new Employee object with optional data.
    - __str__: Returns a string representation of the employee's data.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        """
        Initializes a new instance of the Employee class.

        :param first_name: The employee's first name (default is an empty string).
        :param last_name: The employee's last name (default is an empty string).
        :param review_date: The date of the employee's review in YYYY-MM-DD format (default is "1900-01-01").
        :param review_rating: The employee's performance rating (1-5, default is 3).
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        Getter for the review_date property.

        :return: The date of the employee review.
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        Setter for the review_date property.
        Ensures the date is in the format YYYY-MM-DD.

        :param value: The new review date to set.
        :raises ValueError: If the date is not in the correct format.
        """
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        Getter for the review_rating property.

        :return: The review rating of the employee (1-5).
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        """
        Setter for the review_rating property.
        Ensures the rating is an integer between 1 and 5.

        :param value: The new review rating to set.
        :raises ValueError: If the rating is not in the range 1-5.
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        """
        String representation of the Employee object.

        :return: A string in the format "FirstName,LastName,ReviewDate,ReviewRating".
        """
        return f"{super().__str__()},{self.review_date},{self.review_rating}"