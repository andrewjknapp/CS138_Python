
#! /usr/bin/python
# File Name:     hw9project1.py
# Programmer:    Andrew Knapp
# Date:          Jun 22, 2021
#
#
# Problem Statement: 
#
#
# Overall Plan:
# 1.
#
#
# import the necessary python libraries
from components.button import Button
from graphics import *

def main():
    WIDTH = 300
    HEIGHT = 300

    win = GraphWin("Height Calculator", WIDTH, HEIGHT)

    motherHeightEntry = Entry(Point(WIDTH / 2, 20), 50)
    
    motherHeightEntry.draw(win)

    submitButton = Button(win, Point(WIDTH / 2, HEIGHT / 2), 100, 50, "Submit")
    submitButton.activate()
    
    win.getMouse()
    win.close()


    print("")

main()

