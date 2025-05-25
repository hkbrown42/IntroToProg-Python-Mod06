# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions, classes, and structured error handling
# Change Log:
#   Hannah Brown, 5/24/2025, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# -- Data -- #

# Define the data constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a student for a course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Define the data variables
menu_choice: str = ""       # holds the menu selection made by the user
students: list = []         # a table of student data; a list of dictionaries

# -- Processing -- #

class FileProcessor:
    """A collection of processing functions that work with JSON files.

    Change Log:
    Hannah Brown, 5/24/2025, Created class.
    Hannah Brown, 5/25/2025, Added read and write functions.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This function loads the existing JSON data and stores
        it in a list of dictionaries.

        Change Log:
        Hannah Brown, 5/25/2025, Created function.

        :return: currently saved data (list)
        """

        try:
            file = open(file_name, 'r')
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(
                "Please make sure the file you are trying to open exists!", e)
        except Exception as e:
            IO.output_error_messages(
                "Unspecified error. Please try again.", e)
        finally:
            if not file.closed:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function takes the course registration data currently stored
        and writes it to a designated JSON file.

        Change Log:
        Hannah Brown, 5/25/2025, Created function.

        :return: None
        """

        try:
            file = open(file_name, 'w')
            json.dump(student_data, file, indent=2)
            file.close()
            print("Here is the data you just saved!:")
            for student in student_data:
                print(f"Student {student["FirstName"]} "
                      f"{student["LastName"]} is enrolled in {student["CourseName"]}")
        except TypeError as e:
            IO.output_error_messages(
                "Please make sure the data is a valid JSON format!", e)
        except Exception as e:
            IO.output_error_messages(
                "Unspecified error. Please try again.", e)
        finally:
            if not file.closed:
                file.close()


# -- Presentation -- #

class IO:
    """A collection of presentation functions that manage user input and output.

    Change Log:
    Hannah Brown, 5/24/2025, Created class.
    Hannah Brown, 5/25/2025, Added menu output/input functions.
    Added data display functions.
    Added function to display custom error messages.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """This function displays custom error messages to the user.

        Change Log:
        Hannah Brown, 5/25/2025, Created function.

        :param message:  The error message to be displayed.
        :param error: The current exception. 
        :return: None
        """

        print(message, end='\n')
        if error is not None:
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """This function displays the menu to the user.

        Change Log:
        Hannah Brown, 5/25/2025, Created function.

        :param menu: The menu to be displayed.
        :return: None
        """

        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """This function prompts the user to select from the menu
        and stores the user's selection.

        Change Log:
        Hannah Brown, 5/25/2025, Created function.

        :return: user's menu selection (str)
        """

        choice = ""
        try:
            choice = input("Please enter your menu selection: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please choose a valid option!")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice


    @staticmethod
    def input_student_data(student_data: list):
        """This function registers a student for a course by taking in user
        input of a student's name and the course name and storing it in a
        table.

        Change Log:
        Hannah Brown, 5/25/2025, Created function

        :return: students' names and courses (str)
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            student_registration = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_registration)
            print()
            print(f"You have registered {student_first_name} "
                  f"{student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(
                "Please make sure you have entered the correct information.", e)
        except Exception as e:
            IO.output_error_messages(
                "Unspecified error. Please try again.", e)
        return student_data


    @staticmethod
    def output_student_courses(student_data: list):
        """This function displays the current student registrations.

        Change Log:
        Hannah Brown, 5/25/2025, Created function.

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f"Student {student["FirstName"]} {student["LastName"]} "
                  f"is enrolled in {student["CourseName"]}")
        print("-" * 50)

# End of function definitions

# Start of program's main body
# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                             student_data=students)

while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME,
                                         student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

print("Program complete. Have a nice day! :)")