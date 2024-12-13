# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# Description: A script to manage employee data, including reading, displaying, adding, and saving data.
# Kornel Cieslik, 12/6/2024, Created Script
# Kornel Cieslik, 12/13/2024, Tune Ups, Added Doc Strings, Mark Downs
# ------------------------------------------------------------------------------------------------- #

import processing_classes as proc
import presentation_classes as pres
import data_classes as data

# Main body of the script
"""
This script manages employee data by leveraging processing, presentation, and data classes.

The following functionalities are implemented:
1. Read employee data from a file.
2. Display employee data to the user.
3. Add new employee data.
4. Save updated employee data to the file.
5. Exit the program.

Modules Used:
- processing_classes: Contains methods for file operations.
- presentation_classes: Handles input/output operations.
- data_classes: Defines data structures and constants.

ChangeLog:
- Kornel Cieslik, 12/6/2024: Created script.
- Kornel Cieslik, 12/13/2024: Added docstrings for clarity and documentation.
"""

# Load employee data from the file
employees = proc.FileProcessor.read_employee_data_from_file(
    file_name=data.FILE_NAME,
    employee_data=data.employees,
    employee_type=data.Employee
)

# Main program loop
while True:
    # Display menu to the user
    pres.IO.output_menu(menu=data.MENU)

    # Get the user's menu choice
    menu_choice = pres.IO.input_menu_choice()

    # Option 1: Display current employee data
    if menu_choice == "1":
        """
        Displays the current employee data stored in memory.
        If an error occurs during data display, an error message is shown to the user.
        """
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    # Option 2: Add new employee data
    elif menu_choice == "2":
        """
        Prompts the user to input new employee data and adds it to the current list.
        The updated employee data is then displayed back to the user.
        """
        try:
            employees = pres.IO.input_employee_data(
                employee_data=employees,
                employee_type=data.Employee
            )
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    # Option 3: Save employee data to a file
    elif menu_choice == "3":
        """
        Saves the current employee data to the file specified in the constants.
        If an error occurs during the save operation, an error message is displayed.
        """
        try:
            proc.FileProcessor.write_employee_data_to_file(
                file_name=data.FILE_NAME,
                employee_data=employees
            )
            print(f"Data was saved to the {data.FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    # Option 4: Exit the program
    elif menu_choice == "4":
        """
        Ends the program by breaking out of the main loop.
        """
        break

