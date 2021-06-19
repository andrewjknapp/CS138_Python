#! /usr/bin/python
# File Name:     zipAssignment.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
#
# Description: For this course (Python 138) each of the homework assignments
# follow the structure
# hw [homework number] student name
# And they should be submitted as a zipped file
# hw [homework number] student name .zip
# This program asks the user which homework they are on and then compresses
# that folder and puts the zip into the Submissions folder
# This is accomplished with the tar command
# To customize this you should replace the STUDENT_NAME constant with your name
#
#
# Problem Statement: Automate process of zipping homework assignment
#
#
# Overall Plan:
# 1. Ask user for homework number they want zipped
# 2. Compress corresponding folder and place in Submissions folder
#
#
# import the necessary python libraries
import os

def main():
    print("Zip your assignment here")

    STUDENT_NAME = "KnappAndrew"

    assignmentNumber = input("Type number of the homework: ")

    assignmentName = f"hw{assignmentNumber}{STUDENT_NAME}"

    os.system(f"tar -cf Submissions/{assignmentName}.zip {assignmentName}")

    print(f"{assignmentName}.zip created")

main()