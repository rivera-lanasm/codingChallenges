

import math 
import os
import random 
import re 
import sys

# problem 1: Bubble sort

# bubble sort:
# https://www.freecodecamp.org/news/bubble-sort/

def countSwaps(a):

    sorted = False
    count_swaps = 0 

    while not sorted:
        sorted = True
        
        for index in range(len(a)-1):

            if a[index] > a[index+1]:
                count_swaps += 1

                temp = a[index+1]
                a[index+1] = a[index]
                a[index] = temp
                sorted = False

    print("Array is sorted in {} swaps.".format(str(count_swaps)))
    print("First Element: {}".format(str(a[0])))
    print("Last Element: {}".format(str(a[-1])))

    return 

#? ====================================================================

# problem 2: Mark and Toys
# Given a list of prices and an amount to spend, 
# what is the maximum number of toys Mark can buy?


def maximumToys(prices, k):

    prices.sort()
    cum_sum = [sum([val for val in prices[0:n]]) for n in range(len(prices))]

    return cum_sum

#? ====================================================================

# problem 3: Comparator

# given an array of n player objects (which have name and score attributes)
# write a comparator that sorts them in order of decreasing score
# if two or more have same score, sort these alphabetrically ascending by name 

# create a checker class that implements the comparator interface
# then write an int ompare(p1, p2) method 

# returns -1 if a < b, 0 if a==b, 1 if a>b

def comparator(a, b):

    # decreasing score

    # increasing name

#? ====================================================================

# problem 4: 

#? ====================================================================

if __name__ == '__main__':
    print("running")

    # a = [3, 2, 1]
    # countSwaps(a)

    prices = [1,12,5,111,200,1000,10]
    k = 50
    print(maximumToys(prices, k))


