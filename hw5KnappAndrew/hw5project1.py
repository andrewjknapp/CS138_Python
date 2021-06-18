#! /usr/bin/python
# File Name:     hw5project1.py
# Programmer:    Andrew Knapp
# Date:          June 18, 2021
#
# Problem Statement: Convert a phrase to its acronym representation
#
#
# Overall Plan:
# 1. Prompt user for phrase
# 2. Split the string on the spaces
# 3. Loop through resulting list and add capitalized first letter to string
# 4. Display acronym
#
#
# import the necessary python libraries
# No imports needed

def main():
    print("Acronym Generator")

    phrase = input("Please enter a phrase: ").upper()

    wordList = phrase.split()
    acronym = ""

    for word in wordList:
        print(word)

main()