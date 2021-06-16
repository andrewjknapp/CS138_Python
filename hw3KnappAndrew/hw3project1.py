#! /usr/bin/python
# File Name:     hw3project1.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Ask user for price and diameter then calculate
# the cost per square inch
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the to enter price and diameter
# 3. Calculate area of pizza using A=pi(r^2)
# 4. Calculate cost per area using costPerArea = price / Area
# 5. Print result
#
#
# import the necessary python libraries
import math

def main():
    # Print welcome message to screen
    print("Pizza Price per Square inch Calculator")

    # Prompt for price
    price = eval(input("Enter the price of the Pizza: "))

    # Prompt for diameter
    diameter = eval(input("Enter the diameter of the Pizza (in inches): "))

    # Calculate area
    area = math.pi * ((diameter / 2) ** 2)

    # Calculate price per area
    pricePerArea = price / area

    # Display cost per square inch
    print(f'Price per square inch is ${pricePerArea:.2f}/in')

main()