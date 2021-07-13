
#! /usr/bin/python
# File Name:     hw10project2.py
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
# import the necessary python libraries
from components import Card
from graphics import *


def main():
    # Constants
    WIDTH = 600
    CENTER_X = WIDTH / 2
    HEIGHT = 600

    # Create window object
    win = GraphWin("Height Calculator", WIDTH, HEIGHT)

    card = Card(win, Point(CENTER_X, 100), "Heart", 5)

    win.getMouse()

main()

