#! /usr/bin/python
# File Name:     finalProject2.py
# Programmer:    Andrew Knapp
# Date:          Aug 1, 2021
#
#
# Problem Statement: Create program to check the popularity of girl and boy names.
#
#
# Overall Plan:
# 1. Create three functions, readFile, generateDict, and checkName
#   readFile
#   1. For a given filename read in contents of file
#   2. Split contents on the newline characters and return list
#
#   generateDict
#   1. Call readFile for appropriate file
#   2. For each name, naimings pair of the file add to new dict
#   dict = {
#       name: {
#           namings: number,
#           rank: number
#       },
#   }
#   3. return dictionary
#
#   checkName
#   1. If name is not in dictionary display according message
#   2. If name is in dictionary show rank and number of namings
#
# In main
# 2. Generate both dictionaries
# 3. Prompt user for a name
# 4. display corresponding stats
# 5. ask user if they want to enter another name
#
#
# import the necessary python libraries
import os

def main():
    # Boy and Girl name files
    BOY_NAMES_FILE = os.path.join(os.path.dirname(__file__), 'boynames.txt')
    GIRL_NAMES_FILE = os.path.join(os.path.dirname(__file__), 'girlnames.txt')

    # Read files and generate dictionaries
    boysDict = generateDict(BOY_NAMES_FILE)
    girlsDict = generateDict(GIRL_NAMES_FILE)

    # Prompt user for name
    enterAnother = True
    while enterAnother:
        userInput = input("Please enter a name: ")

        # Check and display message
        checkName(userInput, boysDict, "boy")
        checkName(userInput, girlsDict, "girl")

        enterAnother = input("Would you like to enter another name? (y/n) ") == "y"


# Displays if name is in the dictionary
def checkName(name, dict, type):
    if not name in dict:
        print(f"{name} is not ranked among the top 1000 {type} names.")
    else:
        print(f"{name} is ranked {dict[name]['rank']} in popularity among {type}s with {dict[name]['namings']} namings.")


# Reads file and creates data structure to hold names
def generateDict(fileName):
    fileContents = readFile(fileName)

    namesDict = {}
    rank = 1
    for data in fileContents:
        try:
            name, number = data.split()
        except ValueError:
            break

        namesDict[name] = {"namings": int(number), "rank": rank}
        rank += 1

    return namesDict


# Reads given file and returns a list contianing each line
def readFile(fileName):
    try:
        with open(fileName, "r") as f:
            userFile = f.read()
            return userFile.split('\n')
    except:
        print("Trouble reading file", fileName)


if __name__ == '__main__':
    main()

