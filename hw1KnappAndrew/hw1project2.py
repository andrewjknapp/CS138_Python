#! /usr/bin/python
# Exercise No.   1
# File Name:     hw1project2.py
# Programmer:    Andrew Knapp
# Date:          June 15, 2021
#
# Problem Statement: Calculate the percentage of correct answers based on 
# number of questions answered correctly and total questions
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for total number of questions
# 3. Prompt the user for number answered correctly
# 4. Calculate the percent correct
# 5. Print the percent correct to the screen
#
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print welcome message to screen
    print("Welcome to the percent calculator!")

    # Prompt for total questions and questions answered correctly
    totalQuestions = eval(input("Enter the total number of questions: "))
    answeredCorrectly = eval(input("Enter the number of questions answered correctly: "))

    # Calculate percent correct
    percentCorrect = (answeredCorrectly / totalQuestions) * 100

    # Display percent correct to screen
    print("You score in percent is " + str(percentCorrect) + "%")


main()