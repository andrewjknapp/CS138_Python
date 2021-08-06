
#! /usr/bin/python
# File Name:     hw14project3.py
# Programmer:    Andrew Knapp
# Date:          Aug 1, 2021
#
#
# Problem Statement: Create an employee management system to track how employee
# pay information
#
#
# Overall Plan:
# 1. Create a class to perform logic of asking for user input (ManagementSystem)
# 2. Create class to hold employee name and id, use as parent class (Employee)
# 3. Create child classes that inherit Employee to represent different types of employees (Hourly, Salary, PartTime)
# 4. In Management System display menu and allow user to pick aciton
#   Menu Options
#   1 View all Employees - display id, first, and last name of all employees
#   2 Add Employee - Prompt for employee info and add to list (do not write to DB)
#   3 Remove Employee - Prompt for employee id and remove from list (do not write to DB)
#   4 Save Changes - Write all changes to DB
#   5 Load other Employee Database - Prompt for new DB path. Read and store employee info in list. If 
#     DB does not exist exit out and retain previous DB
#   6 Calculate Pay for All Employees - Display id, first, last name, and calculated pay for each employee
#   7 Exit - End program
#
#
# import the necessary python libraries
from managementSystem import ManagementSystem


def main():
    ManagementSystem()

if __name__ == "__main__":
    main()

