
#! /usr/bin/python
# File Name:     hw12project1.py
# Programmer:    Andrew Knapp
# Date:          Jul 26, 2021
#
#
# Problem Statement: Compare search times between linear and binary search
#
#
# Overall Plan:
# 1. Create function for running a time test
# 2. On each test generate a sorted list of the specified size
# 3. Use perf_counter to time a linear search and a binary search
# 4. Save results into list
# 5. After running each test write results out to file
#
#
# import the necessary python libraries
from random import randrange
from time import perf_counter
import os

def main():
    results = []

    results.append(run_test(1_000))
    results.append(run_test(10_000))
    results.append(run_test(100_000))

    saveResults(results)

def run_test(length_of_list):
    # Generate sorted List
    list = generate_sorted_list(length_of_list)
    target = length_of_list / 2
    # target = 1

    # Linear Search 
    linear_start = perf_counter()

    linear_search(list, target)

    linear_stop = perf_counter()
    linear_time = linear_stop - linear_start

    # Binary Search
    binary_start = perf_counter()

    binary_search(list, 1000000)

    binary_stop = perf_counter()
    binary_time = binary_stop - binary_start


    # Format Results
    result = f"""
Searches for list with {length_of_list} number of elements:"
    Linear Search: {linear_time} s
    Binary Search: {binary_time} s
    """
    
    if (binary_time < linear_time):
        result += "Binary Search was faster"
    else:
        result += "Linear Search was faster"

    return result


def generate_sorted_list(length, min=0, max=100):
    new_list = []
    for _ in range(length):
        new_list.append(randrange(min, max))

    return sorted(new_list)

def linear_search(arr, target):
    for x in range(len(arr)):
        if arr[x] == target:
            return x
    
    return -1
        

def binary_search(arr, target):
    return binary_search_helper(arr, 0, len(arr) - 1, target)

# Code copied from geeksforgeeks.org
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search_helper(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search_helper(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search_helper(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

def saveResults(results):
    file = open(os.path.join(os.path.dirname(__file__), "hw12project1.txt"), "w")
    for result in results:
        file.write(result)

    file.close()

if __name__ == "__main__":
    main()

