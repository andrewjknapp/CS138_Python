
#! /usr/bin/python
# File Name:     hw8project1.py
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
from graphics import *

def main():
    print("Grayscale Converter")

    # Prompt for image
    filePath = input("Please enter the name of the file you wish to convert: ")

    # Check to ensure image exists
    try:
        image = Image(Point(0,0), filePath)
    except:
        print("Could not find file, please make sure the image exists")
        return
    
    # Create the window for the image
    WIDTH = image.getWidth()
    HEIGHT = image.getHeight()
    win = GraphWin("Picture Greyscale Converter", WIDTH, HEIGHT)

    # Display Image
    image.draw(win)
    image.move(WIDTH / 2, HEIGHT / 2)

    win.getMouse()

    # Manipulate image
    for i in range(WIDTH):
        for j in range(HEIGHT):
            r, g, b = image.getPixel(i, j)
            gValue = int(0.299*r + 0.587*g + 0.114*b)
            image.setPixel(i, j, color_rgb(gValue, gValue, gValue))
        image.undraw()
        image.draw(win)

    # Prompt for new file name
    print("Finished converting to greyscale")
    newFileName = input("Enter name of file to save: ")

    # Save modified image
    image.save(newFileName)

    win.close()

main()

