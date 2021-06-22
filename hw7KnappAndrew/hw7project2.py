
#! /usr/bin/python
# File Name:     hw7project2.py
# Programmer:    Andrew Knapp
# Date:          Jun 22, 2021
#
#
# Problem Statement: Calculate fine for speeding ticket with 
# a given speed limit and clocked speed
#
#
# Overall Plan:
# 1. Prompt user for speed limit and clocked speed
# 2. Check if clocked speed is below speed limit (if so it is legal)
# 3. Determine associated fine
# 4. Speed limit is $50 + $5 for each mile over limit with an additional $200 if over 90
# 5. Display result
#
#
# import the necessary python libraries


def main():
    print("Speeding Fine Calculator")

    # Prompt user for input
    speedLimit = eval(input("Speed Limit (Ex. 50): "))
    clockedSpeed = eval(input("Clocked Speed (Ex. 50): " ))

    # Determine if clocked speed is legal
    if (clockedSpeed <= speedLimit):
        print(f"{clockedSpeed} mph is below the speed limit and is perfectly legal")
        return

    # Calculate fine
    fine = 50
    fine += 5 * (clockedSpeed - speedLimit)
    if (clockedSpeed > 90):
        fine += 200

    # Display result
    print(f"{clockedSpeed} is over the speed limit")
    print(f"Fine total: ${fine:.2f}")

main()

