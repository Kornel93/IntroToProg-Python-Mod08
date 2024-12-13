# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# Description: A collection of classes for managing the application
# Kornel Cieslik, 12/6/2024, Created Script
# Kornel Cieslik, 12/13/2024, Tune Ups, Added Doc Strings, Mark Downs
# ------------------------------------------------------------------------------------------------- #
import data_classes as data


class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Methods:
    - output_error_messages: Displays custom error messages with optional technical details.
    - output_menu: Displays a menu of choices to the user.
    - input_menu_choice: Gets and validates a menu choice from the user.
    - output_employee_data: Displays formatted employee data.
    - input_employee_data: Collects and appends employee data from user input.
    - out_error_messages: Demonstrates error output handling.

    ChangeLog:
    - RRoot, 1.1.2030: Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays a custom error message with optional technical details.

        :param message: Custom message to display to the user.
        :param error: Optional exception object for technical details.
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays a menu of choices to the user.

        :param menu: A formatted string representing the menu options.
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        Gets and validates a menu choice from the user.

        :return: A string representing the user's menu choice.
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Displays formatted employee data.

        :param employee_data: A list of employee objects to display.
        :return: None
        """
        message: str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations)"

            print(message.format(employee.first_name, employee.last_name))
        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: data.Employee):
        """
        Collects and appends employee data from user input.

        :param employee_data: A list to which the new employee data will be appended.
        :param employee_type: An instance of the Employee class.
        :return: Updated list with new employee data.
        """
        try:
            employee_object = employee_type
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data

    @classmethod
    def out_error_messages(cls, param, param1):
        """
        Demonstrates handling of error output using predefined methods.

        :param param: Placeholder parameter.
        :param param1: Placeholder parameter.
        :return: None
        """
        IO.output_error_messages("An error occurred", Exception("Test exception"))

