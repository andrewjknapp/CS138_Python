
#! /usr/bin/python
# File Name:     hw12project2.py
# Programmer:    Andrew Knapp
# Date:          Jul 26, 2021
#
#
# Problem Statement: Create a recursive function that determines if a string is a pallindrome
#
#
# Overall Plan:
# 1. If the phrase has only 1 or 0 characters it is a pallindrome
# 2. If the first or last character is not a letter, remove that character and recurse
# 3. If the first and last character are the same remove both and recurse
# 4. If the first and last character are not the same the phrase is not a pallindrome
#
#
# import the necessary python libraries


def main():
    
    promptAgain = True

    while promptAgain:

        phrase = input("Please enter a phrase: ")

        if isPalindrome(phrase):
            print(phrase, "is a palindrome.")
        else:
            print(phrase, "is not a palindrome.")

        promptAgain = input("Enter another phrase? (y/n) ").lower() == 'y'
    
    print("Thank you for using the Palindrome checker!")

def isPalindrome(phrase):
    # If there is one or no characters left in the phrase then it means
    # the original phrase is a palindrome
    if len(phrase) <= 1:
        return True

    # If the first character is not a letter then remove first character
    # and call recursive function
    if not phrase[0].isalpha():
        phrase = phrase[1:]
        return isPalindrome(phrase)

    # If the last character is not a letter then remove last character
    # and call recursive function
    if not phrase[len(phrase) - 1].isalpha():
        phrase = phrase[0:len(phrase) - 1]
        return isPalindrome(phrase)

    # If the first and last characters are equal, remove them and call 
    # recursive function. Otherwise return false as the phrase is not a 
    # palindrome
    firstAndLastEqual = phrase[0].lower() == phrase[len(phrase) - 1].lower() 
    if firstAndLastEqual:
        return isPalindrome(phrase[1:(len(phrase) - 1)])
    else:
        return False

main()

