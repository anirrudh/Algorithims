"""
Implementation of Insertion Sort Algorithim from Introduction to Algorithims. 
This program will use Python 3.X

An important thing to note here is that Python does not have a built-in 
array function, but it does have lists. I will try to not use any external 
packages, but NumPy does indeed have arrays. 
@Author: Anirrudh Krishnan
"""

import sys, os
import random 
from timeit import Timer
import timeit

class InsertionSort():
    #Generate list with 10 random numbers, 1 - 100
    #A = random.sample(range(101), 10) 

    #Writing Insertion-Sort
    @staticmethod
    def Insertion_Sort(array):
        j = 1
        while j < len(array):
            key = array[j]
            i = j - 1
            j = j + 1
            while i >= 0 and array[i] > key:
                array[i+1] = array[i]
                i = i - 1
                array[i+1] = key 
        return array
    
    #.sort() seems to have an in-place algo as well
    @staticmethod
    def Sorted_sort(array): 
        array.sort()
        return array

    #timeit function to see if one solution is faster 
    #than another

A = random.sample(range(101), 10) 
print("Random Array: ")
print(A)
x = InsertionSort()
array_sorted = x.Insertion_Sort(A)
print("Sorted Array via algo: ")
print(array_sorted)
print("Sorted Array via built in method: ")
array_sorted_builtin = x.Sorted_sort(A)
print(array_sorted_builtin)

"""
Let us use the time it function to now run the same process.
"""
setup_method1 = """
import random
A = random.sample(range(101), 10) 

def Insertion_Sort(array):
        j = 1
        while j < len(array):
            key = array[j]
            i = j - 1
            j = j + 1
            while i >= 0 and array[i] > key:
                array[i+1] = array[i]
                i = i - 1
                array[i+1] = key 
        return array
"""

setup_method_builtin = """
import os
import random
A = random.sample(range(101), 10) 

def Sorted_sort(array): 
    array.sort()
    return array
"""

t = timeit.Timer(stmt="Insertion_Sort(A)", setup = setup_method1)
print("Written method timeit results:")
print(t.timeit())

t2 = timeit.Timer(stmt="Sorted_sort(A)", setup = setup_method_builtin)
print("Built-in method results:")
print(t2.timeit())