
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
# 1. 
#
# import the necessary python libraries

def checkBounds(oldCode, newCode, lower, upper):
    
    if lower <= oldCode <= upper:
        if newCode > upper:
            newCode = lower + (newCode - (upper + 1))
        elif newCode < lower:
            newCode = upper - ((lower - 1) - newCode)

    return newCode

def shiftChar(char, shift):
    LOWER_START = 97
    LOWER_END = 122
    UPPER_START = 65
    UPPER_END = 90

    oldCode = ord(char)
    newCode = oldCode + shift

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

def getShift():
    invalidInput = True
    while invalidInput:
        try:
            shift = eval(input("Enter the Cipher Shift (Ex. 5): "))
            
            if not shift == int(shift):
                raise ValueError()
            else:
                invalidInput = False
        except:
            print("Please enter a whole number")
            invalidInput = True
            
    return shift


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
        type = getType()

        phrase = input("Please enter the phrase: ")

        shift = getShift()

        newPhrase = translate(phrase, shift, type)

        print(newPhrase)

        print()
        anotherRound = input("Do you like to translate another phrase? (y/n) ").strip().lower() == 'y'
        print()

    print("Have a nice day")

main()

