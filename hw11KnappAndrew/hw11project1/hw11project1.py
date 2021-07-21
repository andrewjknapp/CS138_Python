
#! /usr/bin/python
# File Name:     hw11project1.py
# Programmer:    Andrew Knapp
# Date:          Jul 13, 2021
#
#
# Problem Statement: Create a splash screen for the GUI poker project and a 
# help popup menu
#
#
# Overall Plan:
# 1.
#
#
# import the necessary python libraries
from guipoker import GraphicsInterface as GamePage
from pokerapp import PokerApp
import time

def main():
    game = GamePage()
    app = PokerApp(game)
    app.run()
    

main()

