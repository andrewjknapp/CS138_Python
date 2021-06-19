#! /usr/bin/python
# File Name:     hw5project2.py
# Programmer:    Andrew Knapp
# Date:          June 18, 2021
#
# Problem Statement: Read in numbers from file and write sums
# of numbers to separate file
#
#
# Overall Plan:
# 1. Open input file and output file
# 2. For each line of the input file
#   2a. Split the string into two expected numbers
#   2b. Add numbers together
#   2c. Store sum into string to be written
# 3. Write list of sums out to file
# 4. Close connection to files
#
#
# import the necessary python libraries
import os

def main():
    # Constants for file names
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "output.txt"

    print("Bulk Summation Starting")

    print("Opening Files")
    inputFile = open(INPUT_FILE, "r")

    # If file already exists, delete then create new one
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    outputFile = open(OUTPUT_FILE, "a")

    print("Processing file")
    sumList = ""
    for line in inputFile:
        num1, num2 = line.split()
        sum = eval(num1) + eval(num2)
        sumList += (str(sum) + "\n")

    print("Writing result to file")
    outputFile.write(sumList)

    print("Closing connection for files")
    inputFile.close()
    outputFile.close()

main()