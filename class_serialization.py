# ****************************************************************************************************
#
# File name:  Classes_serialization.py
# Description:
#               This is a program that saves the employee information.
#
#
# ****************************************************************************************************

import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = 'employee.dat'

# ****************************************************************************************************

class Employee:
    def __init__(self, name, emp_id, department, job_title):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title


# ****************************************************************************************************

def load_employees():
    try:
        with open(FILENAME, "rb") as file:
            employee_dict = pickle.load(file)
        return employee_dict
    except IOError:
        return {}


# ****************************************************************************************************

def save_employees(employee_dict):
    with open(FILENAME, "wb") as file:
        pickle.dump(employee_dict, file)


# ****************************************************************************************************

def get_user_choice():
    while True:
        try:
            print("Menu")
            print("=" * 50)
            print("1. Look up employee")
            print("2. Add employee")
            print("3. Change employee")
            print("4. Delete employee")
            print("5. Quit")
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# ****************************************************************************************************

def look_up(employee_dict):
    emp_id = input("Enter employee ID number: ")
    employee = employee_dict.get(emp_id)
    if employee:

        print(f"Employee found:\n"
              f"Name: {employee.name}\n"
              f"ID : {employee.emp_id}\n"
              f"Department: {employee.department}\n"
              f"Job Title: {employee.job_title}")
    else:
        print("The specified ID number was not found.")


# ****************************************************************************************************

def add(employee_dict):
    emp_id = input("Enter employee ID number: ")
    if emp_id in employee_dict:
        print("An employee with that ID already exists.")
    else:
        name = input("Enter employee name: ")
        department = input("Enter employee department: ")
        job_title = input("Enter employee job title: ")
        new_employee = Employee(name, emp_id, department, job_title)
        employee_dict[emp_id] = new_employee
        print("Employee added successfully.")


# ****************************************************************************************************

def change(employee_dict):
    emp_id = input("Enter employee ID number: ")
    if emp_id in employee_dict:
        name = input("Enter new employee name: ")
        department = input("Enter new employee department: ")
        job_title = input("Enter new employee job title: ")
        employee_dict[emp_id].name = name
        employee_dict[emp_id].department = department
        employee_dict[emp_id].job_title = job_title
        print("Employee information updated successfully.")
    else:
        print("The specified ID number was not found.")


# ****************************************************************************************************

def delete(employee_dict):
    emp_id = input("Enter employee ID number: ")
    if emp_id in employee_dict:
        del employee_dict[emp_id]
        print("Employee deleted successfully.")
    else:
        print("The specified ID number was not found.")


# ****************************************************************************************************

def main():
    employee_dict = load_employees()

    while True:
        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(employee_dict)
        elif choice == ADD:
            add(employee_dict)
        elif choice == CHANGE:
            change(employee_dict)
        elif choice == DELETE:
            delete(employee_dict)
        elif choice == QUIT:
            break

    save_employees(employee_dict)


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************
