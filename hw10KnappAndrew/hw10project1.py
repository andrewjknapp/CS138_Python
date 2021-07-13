
#! /usr/bin/python
# File Name:     hw10project1.py
# Programmer:    Andrew Knapp
# Date:          Jul 12, 2021
#
#
# Problem Statement: 
#
#
# Overall Plan:
# 1.
#
#
# Attribution
# Bee Movie Script transcription found on 
# http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html 
#
# import the necessary python libraries


RESERVED_WORDS = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

def main():
    wordMap = { key: 0 for key in RESERVED_WORDS }
    file = open("./bee_movie_script.txt", 'r')

    lines = file.readlines()

    for line in lines:
        words = line.split()
        for word in words:
            if word in RESERVED_WORDS:
                wordMap[word] += 1

    print("Reserved Word | Count")
    for key in wordMap:
        print(f"{key:<15} {wordMap[key]}")



    
    


main()

