#! /usr/bin/python
# File Name:     hw6project1.py
# Programmer:    Andrew Knapp
# Date:          June 22, 2021
#
# Problem Statement: Create definitions for the functions sphereArea and sphereVolume
#
#
# Functions
# Area of Sphere = 4 pi radius^2
# Volume of Sphere = 4/3 pi radius^3
#
#
# Overall Plan:
# 1. Create definitions
# 2. Display outputs for two different spheres
#   
#
# import the necessary python libraries
import math

def sphereArea(radius):
    return 4 * math.pi * radius**2

def sphereVolume(radius):
    return (4 / 3) * math.pi * radius**3

def displaySphereInfo(radius):
    print(f"""
    Sphere with radius {radius}
    Has an AREA of {sphereArea(radius):0.2f}
    and a VOLUME of {sphereVolume(radius):0.2f}    
    """)

def main():
    sphereRadius1 = 3
    displaySphereInfo(sphereRadius1)

    sphereRadius2 = 5
    displaySphereInfo(sphereRadius2)
    

main()