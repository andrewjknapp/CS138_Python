
#! /usr/bin/python
# File Name:     hw13project1.py
# Programmer:    Andrew Knapp
# Date:          Jul 27, 2021
#
#
# Problem Statement: Create program to measure time for the standard sort, 
# merge sort, and selection sort.
#
#
# Overall Plan:
# 1. Create function for running a time test
# 2. On each test generate a list of the specified size
# 3. Use perf_counter to time a standard, selection, and merge sort
# 4. Save results into list
# 5. After running each test write results out to file
#
#
# import the necessary python libraries
from time import perf_counter
from random import randrange
import os


def main():
    results = []
    
    results.append(run_test(1_000))
    results.append(run_test(10_000))
    results.append(run_test(100_000))

    saveResults(results)


def generateList(length, min=0, max=100):
    new_list = []
    for _ in range(length):
        new_list.append(randrange(min, max))

    return new_list

def run_test(length_of_list):
    # Generate sorted List
    list = generateList(length_of_list)

    # Standard sort 
    testList = [*list]
    standard_start = perf_counter()

    testList.sort()

    standard_stop = perf_counter()
    standard_time = standard_stop - standard_start

    # Selection Sort
    testList = [*list]
    selection_start = perf_counter()

    selectionSort(testList)

    selection_stop = perf_counter()
    selection_time = selection_stop - selection_start

    # Merge Sort
    testList = [*list]
    merge_start = perf_counter()

    selectionSort(testList)

    merge_stop = perf_counter()
    merge_time = merge_stop - merge_start

    
    # Format Results
    result = f"""
Searches for list with {length_of_list} number of elements:
    Standard Sort: {standard_time} s
    Selection Sort: {selection_time} s
    Merge Sort: {merge_time} s
    """

    return result


# Python program for implementation of MergeSort
# Taken from https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


# Selection sort implementation taken from 
# https://www.geeksforgeeks.org/python-program-for-selection-sort/
def selectionSort(A):
    # Traverse through all array elements
    for i in range(len(A)):
      
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with 
        # the first element        
        A[i], A[min_idx] = A[min_idx], A[i]

def saveResults(results):
    file = open(os.path.join(os.path.dirname(__file__), "hw13project1.txt"), "w")
    for result in results:
        file.write(result)

    file.close()

main()

