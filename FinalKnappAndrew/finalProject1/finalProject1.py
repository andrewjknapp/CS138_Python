
#! /usr/bin/python
# File Name:     finalProject1.py
# Programmer:    Andrew Knapp
# Date:          Jul 29, 2021
#
#
# Problem Statement: Create an application that spell checks a text file.
#
#
# Overall Plan:
# File list - dashboard, button, page, WordCheckApp
# WordCheckApp
#   1 Main entry point for application
#   2 on initialization opens window for current page
#
# dashboard
#   1 Main page for application
#   2 allows user to enter in path for file to check and file that 
#     contains the dictionary
#   3 Once both are filled out the user can spell check and the list of 
#     misspelled words will be displayed
#
# page
#   1 defines all methods needed for a page
#
#
# import the necessary python libraries
from WordCheckApp import Word_Check_App

def main():
    Word_Check_App()

if __name__ == '__main__':
    main()
