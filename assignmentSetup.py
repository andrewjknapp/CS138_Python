#! /usr/bin/python
# File Name:     zipAssignment.py
# Programmer:    Andrew Knapp
# Date:          June 22, 2021
#
#
# Problem Statement: Automate process of setting up homework assignment
#
#
# Overall Plan:
# 1. Ask user for homework number they want created
# 2. Ask user for number of projects and whether or not there is an extra credit assignment
# 3. create files and folders
#
#
# import the necessary python libraries
import os
from datetime import datetime

def homeworkTemplate(fileName):
    return f"""
#! /usr/bin/python
# File Name:     {fileName}
# Programmer:    Andrew Knapp
# Date:          {datetime.now().strftime("%b %d, %Y")}
#
# Problem Statement: 
#
#
# Overall Plan:
# 1.
#
#
# import the necessary python libraries


def main():
    print("")

main()

"""

def createFile(assignmentName, fileName):
    file = open(f"{assignmentName}/{fileName}", "a")
        
    file.write(homeworkTemplate(fileName))

    file.close()

def main():
    print("Set up assignment")

    STUDENT_NAME = "KnappAndrew"

    assignmentNumber = input("Type number of the homework: ")

    assignmentName = f"hw{assignmentNumber}{STUDENT_NAME}"

    numberOfProjects = eval(input("Enter number of projects in assignment: "))

    hasExtraCredit = input("Is there a extra credit project? (y/n): ")

    os.system(f"mkdir {assignmentName}")
    
    for i in range(1, numberOfProjects + 1):
        fileName = f"hw{assignmentNumber}project{i}.py"
        createFile(assignmentName, fileName)

    if (hasExtraCredit == "y"):
        fileName = f"hw{assignmentNumber}extraCredit.py"
        createFile(assignmentName, fileName)



main()