#! /usr/bin/python
# Exercise No.   1
# File Name:     hw1project1.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Ask the user to enter three numbers, calculate the sum of 
# these three numbers, and display the sum and quotient to the screen
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two integers
# 3. Calculate the sum of the integers
# 4. Calculate the quotient of the integers
# 5. Print the sum and quotient of the integers to the screen
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("I can add three numbers for you")

    # Variables are declared dynamically no need to pre-define
    num1 = eval(input("Enter one whole number (Ex. 52): "))
    num2 = eval(input("Enter another whole number (Ex. 41): "))
    num3 = eval(input("Enter another whole number (Ex. 42): "))

    #Here is the processing that is needed
    sum = num1 + num2 + num3
    #Here is the multiplying 
    quotient = num1 * num2 * num3

    # Output the results
    print("The sum of the the numbers is ", sum)
    print("The quotient of the numbers is ", quotient)


main()

