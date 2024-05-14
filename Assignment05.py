# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Rachel Hostetler, 05/13/24, Assignment05
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  
students: list = []  # a table of student data


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data to dictionary
        row_data = row.split(',')
        student_data = {"FirstName": row_data[0], "LastName": row_data[1], "Class": row_data[2].strip()}
        # Load it into our collection (list of lists)
        students.append(student_data)
except FileNotFoundError as e:
    print("File not found\n")
    print("-- More Info: Error -- ")
    print(e, e.__doc__, type(e), sep="\n")
except Exception as e:
    print("Other Error\n")
    print("-- More Info: Error -- ")
    print(e, e.__doc__, type(e), sep="\n")
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        if not student_first_name.isalpha():
            raise ValueError("First name should not include numbers.")
        
        student_last_name = input("Enter the student's last name: ")
        if not student_last_name.isalpha():
            raise ValueError("Last name should not include numbers.")
        
        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "Class": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["Class"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        
        try:      
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student["FirstName"]}, {student["LastName"]}, {student["Class"]}\n"
                file.write(csv_data)
            file.close()
            print("Data was saved to file!")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["Class"]}")

        except FileNotFoundError as e:
            print("File not found\n")
            print("-- More info: error -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            print("Other error\n")
            print("-- More info: error -- ")
            print(e, e.__doc__, type(e), sep="\n")
        finally:
            if not file.closed:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
