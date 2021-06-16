#! /usr/bin/python
# Exercise No.   1
# File Name:     hw2project1.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Ask user to enter a temperature in Fahrenheit and convert
# it to celsius
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the to enter temp in Fahrenheit
# 3. Convert temp into Celsius
# 4. Print temp in Celsius
#
#
# import the necessary python libraries
# for this example none are needed

def main():
    # Print welcome message to screen
    print("Welcome to the Fahrenheit to Celsius temperature converter")

    # Prompt for temperature
    userTempF = eval(input("Enter a temperature in Fahrenheit: "))

    # Convert temperature from Fahrenheit to Celsius
    tempInCelsius = 5 * (userTempF - 32) / 9

    # Display temp in Celsius
    print(f'{userTempF:.1f}\u00B0F is {tempInCelsius:.1f}\u00B0C')

main()