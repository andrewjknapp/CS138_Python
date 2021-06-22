
#! /usr/bin/python
# File Name:     hw7project1.py
# Programmer:    Andrew Knapp
# Date:          Jun 22, 2021
#
# Problem Statement: Estimate a child's adult height given the height of 
# the father and mother as well as the child's gender
#
#
# FORMULAS
# 1.  Height (male) = ((Hmother * 13/12) + Hfather ) / 2
# 2.  Height (female) = ((Hfather * 12/13) + Hmother ) / 2
#
# Overall Plan:
# 1. Prompt user for height of mother and father as well as gender of child
# 2. If child is male use FORMULA 1
# 3. else use FORMULA 2
# 4. display the child's height
#
#
# import the necessary python libraries

# Converts a number representing inches into
# a string formatted as feet and inches
def inchesToFeetAndInches(height):
    feet = height // 12
    inches = height % 12
    return f"{feet:.0f}'{inches:.0f}\""

def main():
    print("Predict your child's height!")

    # Prompt for user input
    heightMother = eval(input("What is the height of the child's mother in inches (Ex. 62): "))
    heightFather = eval(input("What is the height of the child's father in inches (Ex. 62): "))
    gender = input("Enter the child's biological gender (male/female): ").lower()

    # Calculate height based on correct formula for specified gender
    if (gender == "male"):
        height = ((heightMother * 13/12) + heightFather ) / 2
    elif (gender == "female"):
        height = ((heightFather * 12/13) + heightMother ) / 2
    else:
        print("Please choose one of the gender options")
        return

    # Display result
    print(f"This child's estimated adult height is {inchesToFeetAndInches(height)}")

main()

