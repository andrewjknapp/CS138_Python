
#! /usr/bin/python
# File Name:     midtermProject1.py
# Programmer:    Andrew Knapp
# Date:          Jul 8, 2021
#
# Problem Statement: Read a file that contains numbers and calculate the 
# mean, median, and standard deviation. Lists can be between 0-1000 values
#
#
# FORMULAS
# mean = sum of values / number of values
# standard deviation = sqrt(sum( sqr(value - mean) ) / (number of values - 1))
#
# Overall Plan:
# 1. Read in values from file into list
# 2. Sort list
# 3. Calculate mean by sum / number values
# 4. Calculate median by getting middle value from array
#   - if num values is even average middle two
# 5. Calculate standard deviation
# 6. Display values
#
# import the necessary python libraries

# Takes in a list of numbers and calculates the mean
def mean(nums):
    if len(nums) == 0:
        raise ValueError("Cannot find mean of empty list")

    return sum(nums) / len(nums)

# Takes in a list of numbers and calculates the median
def median(values):
    if len(values) == 0:
        raise ValueError("Cannot find median of empty list")

    values = sorted(values)

    isEven = len(values) % 2 == 0

    # If number of values is even then median is the average
    # of the middle two values
    if isEven:
        val1 = values[int((len(values) / 2) - 1)]
        val2 = values[int(len(values) / 2)]
        median = mean([val1, val2])
    # Else the median is the middle value in the sorted list
    else:
        median = values[int(len(values) / 2)]
    
    return median

# This function finds the standard deviation of a given list using the
# formula as broken down below
# Formula
# dividend = ∑(num - mean)^2
# divisor = (numValues - 1) 
# SD = √(dividend / divisor)
def standardDeviation(values):
    if len(values) == 0:
        raise ValueError("Cannot find standard deviaiton of empty list")

    if len(values) == 1:
        return 0

    meanValue = mean(values)

    dividend = 0

    for num in values:
        dividend += ((num - meanValue) ** 2)

    divisor = len(values) - 1

    return (dividend / divisor) ** (1/2)

# Calculates the lower and upper values of a given 
# standard deviation range. The number of standard
# deviations from the mean can be selected as well
def getSDRange(mean, SD, numSDs):
    if SD < 0 or numSDs < 0:
        raise ValueError("Standard deviation and number of standard deviations must be positive")

    val1 = mean - (SD * numSDs)
    val2 = mean + (SD * numSDs)

    return [val1, val2]

# Prints the results to the console
def displayValues(mean, median, SD, twoSDRange):
    print("Statistics")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {SD:.2f}")
    print(f"2 Standard Deviation Range: {twoSDRange[0]:.2f} to {twoSDRange[1]:.2f}")

def main():
    nums = []

    # Read file and add numbers form file into list
    # If file was not found catch that error, else catch any
    # other error
    try:
        with open("./nums.txt") as file:
            for num in file:
                nums.append(eval(num.strip()))
    except FileNotFoundError:
        print("The file requested could not be found")
        raise
    except:
        print("An error occured while trying to access/read the file")
        raise

    # Calculate the mean, median, SD, and SD range
    # if any of these error out will catch a Value Error
    try:
        meanValue = mean(nums)
        medianValue = median(nums) 
        SDValue = standardDeviation(nums)
        twoSDRange = getSDRange(meanValue, SDValue, 2)
    except ValueError:
        print("An error occurred while trying to calculate the related statistics")
        raise

    displayValues(meanValue, medianValue, SDValue, twoSDRange)


main()

