
#! /usr/bin/python
# File Name:     hw11project2.py
# Programmer:    Andrew Knapp
# Date:          Jul 22, 2021
#
#
# Problem Statement: Create an ATM application where users can sign in and see their account balances
#
#
# Overall Plan:
# For this assignment I decided to implement a GUI application using ideas 
# from the Model View Controller style. 
# ATM_App is both the Model and the Controller
# Page, LoginPage, and Dashboard are the Views
# 
# ATM_App - This class handles the starting of the application, changing views, tracking who is logged in,
# and getting data from the faux database. 
#
# Page - Abstract parent class that contains the methods necessary to display a view
#
# LoginPage - This defines the layout and actions of the login page
#
# Dashobard = This defines the layout and actions of the dashobard page
#
#
# import the necessary python libraries
from graphics import *
from atmApp import ATM_App

def main():
    ATM_App()


main()

