#! /usr/bin/python
# File Name:     hw3project2.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Calculate length of ladder when given
# the height of the building and angle (radians) of ladder with 
# respect to the ground
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the to enter height of building and angle of ladder
# 3. Convert angle to degrees
# 4. Calculate length of ladder
# 5. Print result
#
#
# import the necessary python libraries
import math

def main():
    # Print welcome message to screen
    print("Ladder Length Calculator")

    # Prompt for height
    height = eval(input("Enter the height of the building (in feet): "))

    # Prompt for angle
    radiansAngle = eval(input("Enter the angle of the ladder (in radians): "))

    # Convert angle to degrees
    degreesAngle = (math.pi / 180) * radiansAngle

    # Calculate length of ladder
    ladderLength = height / math.sin(degreesAngle)

    # Display length of ladder
    print(f'Length of ladder must be at least {ladderLength:.1f} ft')

main()