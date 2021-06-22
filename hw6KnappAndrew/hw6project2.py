#! /usr/bin/python
# File Name:     hw5project2.py
# Programmer:    Andrew Knapp
# Date:          June 18, 2021
#
# Problem Statement: Create program to display verses of 
# "The Ants go Marching"
#
#
# Overall Plan:
# 1. create function as template for repeated phrases in verses
# 2. Create list of numbers of ants and phrases
# 3. Loop over list calling function on each
#
#
# import the necessary python libraries
# No imports needed

def verse(number, phrase):
    print(f"""
        The ants go marching {number} by {number}, hurrah! hurrah!
        The ants go marching {number} by {number}, hurrah! hurrah!
        The ants go marching {number} by {number},
        The Little one stopped to {phrase},
        And they all go marching down...
        In the ground...
        To get out...
        Of the rain.
        Boom! Boom! Boom!
    """)

def main():
    phrases = {
        "one": "have some fun",
        "two": "eat some stew",
        "three": "chase a bee",
        "four": "knock down a door",
        "five": "stay alive",
        "six": "pick up sticks",
        "seven": "go to heaven",
        "eight": "stand up straight",
        "nine": "earn a dime",
        "ten": "steal a stem"
    }

    for number, phrase in phrases.items():
        verse(number, phrase)

main()