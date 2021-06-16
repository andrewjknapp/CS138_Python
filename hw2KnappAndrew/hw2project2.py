#! /usr/bin/python
# Exercise No.   1
# File Name:     hw2project2.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Average a user specified number of exam scores
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
    # Display welcome message
    print("Welcome to the exam score averager")

    # Prompt user for number of scores
    numberOfScores = eval(input("Enter the number of exam scores to be averaged: "))

    # Variable to hold sum of exam scores
    sum = 0

    # Loop 'numberOfScores' times
    for _ in range(numberOfScores):
        # Get current score and add to sum
        currentScore = eval(input("Enter exam score: "))
        sum += currentScore

    # Calculate average of scores
    average = sum / numberOfScores

    # Display results
    print(f'The average of the scores is {average:.1f}')

main()
