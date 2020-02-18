

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

    i = 0
    price_sum = 0
    while price_sum < k:
        price_sum += prices[i]
        i += 1
             
    return i -1

#? ====================================================================

# problem 3: fradulent activity
# given num of trailing days d and client' total daily expenditures for a period of n days
# find an dprint the num of times client will receive notifcation

def median_find(array):
    n = len(array) 
    array.sort() 
    
    if n % 2 == 0: 
        median1 = array[n//2] 
        median2 = array[n//2 - 1] 
        median = (median1 + median2)/2
    else: 
        median = array[n//2]

    return median 

def activityNotifications(expenditure, d):

    len_exp = len(expenditure)
    median_list = list(map(lambda x: median_find(expenditure[x:x+d]),range(d,len_exp-d) ))
    #! fix range 

    return median_list
    

#? ====================================================================

# problem 4: 

#? ====================================================================

if __name__ == '__main__':
    print("running")

    # a = [3, 2, 1]
    # countSwaps(a)

    expenditure = [2, 3, 4, 2, 3, 6, 8 ,4 ,5]
    d = 5
    print(activityNotifications(expenditure, d))


