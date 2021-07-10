
#! /usr/bin/python
# File Name:     midtermProject2.py
# Programmer:    Andrew Knapp
# Date:          Jul 9, 2021
#
# Problem Statement: 
#
# Important ASCII Values
# a - 97, z - 122
# A - 65, Z - 90
#
# Overall Plan:
# 1. Prompt user for whether to decode or encode
# 2. Prompt user for phrase
# 3. Prompt user for number of shift
# 4. 
#
# import the necessary python libraries

# Used to check if the new code after applying the shift falls outside
# the bounds of the ascii codes which represent lowercase or uppercase
# characters. If the new code falls outside these bounds that code is 
# wrapped around to the other end of the range
def checkBounds(oldCode, newCode, lower, upper):
    
    if lower <= oldCode <= upper:
        if newCode > upper:
            newCode = lower + (newCode - (upper + 1))
        elif newCode < lower:
            newCode = upper - ((lower - 1) - newCode)

    return newCode

# Translates the character by 'shift' number of steps. If the inputs are
# 'a' and 1 the output will be 'b'. 
def shiftChar(char, shift):
    # Constants for bounds of ascii codes for lowercase and uppercase characters
    LOWER_START = 97
    LOWER_END = 122
    UPPER_START = 65
    UPPER_END = 90

    oldCode = ord(char)

    # Shift code by 'shift' number of steps
    newCode = oldCode + shift

    # Check to make sure the new code is within the correct range for lowercase 
    # or uppercase characters
    if char.islower():
        newCode = checkBounds(oldCode, newCode, LOWER_START, LOWER_END)
    elif char.isupper():
        newCode = checkBounds(oldCode, newCode, UPPER_START, UPPER_END)
    else:
        # This else only runs if the character passed in is not in the uppercase or lowercase 
        # alphabet. We can decide what to do in this case. One option would be to raise an error.
        # Another could be to leave that special character unchanged. I will choose to return the 
        # character unshifted, but will leave my error statement commented out in case raising an 
        # error would be better practice. If raising an error were chosen another elif should be 
        # added before this else to handle characters such as spaces and punctuation to allow those
        # to be included in the input phrase
        #raise ValueError("Characters passed in must be characters from the alphabet.")
        return chr(oldCode)
    
    return chr(newCode)

def ceasarCipher(phrase, shift):
    # Here I am using a list comprehension to generate a list of shifted characters
    # from the original phrase. Then I join these characters together into a string. 
    # I first learned about list comprehension from method 6 on this online article
    # https://waymoot.org/home/python_string/
    return ''.join([shiftChar(char, shift) for char in phrase])

# Prompts user for whether the phrase should be encoded or decoded.
# Function handles error checking to ensure valid input
def getType():
    invalidChoice = True
    while invalidChoice:
        invalidChoice = False
        type = input("Would you like to encode (e) or decode (d) a message? (Answer with e or d): ")
        type = type.lower()
        if not (type == 'e' or type == 'd'):
            print("Please enter either 'e' to encode or 'd' to decode")
            invalidChoice = True
    return type

# Prompts user for the number by which the cipher should shift the phrase
# Handles input to ensure an integer is entered
def getShift():
    invalidInput = True
    while invalidInput:
        try:
            # If a non number value is entered an error is raised
            shift = eval(input("Enter the Cipher Shift (Ex. 5): "))
            
            if not shift == int(shift):
                raise ValueError()
            else:
                invalidInput = False
        except:
            print("Please enter a whole number")
            invalidInput = True
    
    shift = shift % 26
    return shift

# Handles the translating of the phrase by calling the ceasarCipher function
def translate(phrase, shift, type):
    if type == 'e':
        newPhrase = ceasarCipher(phrase, shift)
    else:
        newPhrase = ceasarCipher(phrase, -shift)

    return newPhrase

def main():
    print("Welcome to the Ceasar Cipher Translator")

    anotherRound = True

    while anotherRound:
        # Prompt for information
        type = getType()
        phrase = input("Please enter the phrase: ")
        shift = getShift()

        # Translate phrase
        newPhrase = translate(phrase, shift, type)

        # Print Result
        print(newPhrase)
        print()

        # Prompt to run program again
        anotherRound = input("Do you like to translate another phrase? (y/n) ").strip().lower() == 'y'
        print()

    print("Have a nice day")

main()

