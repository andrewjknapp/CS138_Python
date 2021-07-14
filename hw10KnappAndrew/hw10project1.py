
#! /usr/bin/python
# File Name:     hw10project1.py
# Programmer:    Andrew Knapp
# Date:          Jul 12, 2021
#
#
# Problem Statement: Count number of occurrences of reserved keywords in a given text file
#
#
# Overall Plan:
# 1. Create list of reserved keywords
# 2. Generate a dictionary for the keyword list setting each value to 0
# 3. Open file 
#
#
# Attribution
# Bee Movie Script transcription found on 
# http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html 
#
# import the necessary python libraries
import re

# Reserved words in python
RESERVED_WORDS = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

def main():
    # Generate dictionary from reserved words.
    # Each key is initially set to zero
    wordMap = { key: 0 for key in RESERVED_WORDS }

    # Open File
    try:
        file = open("./bee_movie_script.txt", 'r')
    except FileNotFoundError as e:
        print("Whoops, that file could not be found.")
        print(e)
        return

    # Read each line from the file
    lines = file.readlines()
    for line in lines:
        words = line.split()
        # For each word in the line check if word is in wordMap
        # if in word map increment the value to keep track of number of times it was found
        for word in words:
            word = re.sub(r'\W+', '', word)
            if word in RESERVED_WORDS:
                wordMap[word] += 1

    print("Reserved Word | Count")
    for key in wordMap:
        print(f"{key:<15} {wordMap[key]}")



    
    


main()

