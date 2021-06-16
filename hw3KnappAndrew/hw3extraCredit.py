#! /usr/bin/python
# File Name:     hw3extraCredit.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Calculate Gregorian epact given a year
#
#
# Formulas
# C = year // 100
# epact = (8+(C//4) - C + ((8C + 13)//25) + 11(year%19))%30
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the to enter year
# 3. Convert C
# 4. Calculate epact
# 5. Print result
#
#
# import the necessary python libraries

def main():
    # Print welcome message to screen
    print("Epact Calculator")

    # Prompt for height
    year = eval(input("Enter a year (Ex. 1994): "))

    # Calculate C
    C = year // 100

    # Calculate epact
    #epact = (8+(C//4) - C + ((8*C + 13)//25) + 11(year%19))%30
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    # Display length of ladder
    print(f'There were {epact} days between January 1st of {year} and the previous new moon')

main()