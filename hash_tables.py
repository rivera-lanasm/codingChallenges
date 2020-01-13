import math 
import os
import random 
import re 
import sys

# problem 1: Ransom Note

# case sensitive, must use whole words, not substrings or concatenation
# print Yes if he can replicate his ransom note sing whole words from magazine, else print No

# input: 1) an array of strings from source 2) an array of strings from ransom note

from collections import Counter
from functools import reduce
import itertools
def checkMagazine(magazine, note):
	mag = Counter(magazine)
	note = Counter(note)

	mag_content = [(value,mag[key]) for key,value in note.items()]

	success = list(map(lambda x: x[1]>= x[0], mag_content))

	if reduce(lambda x,y: x and y, success):
		print("Yes")
		return
	else:
		print("No")
		return

# ========================================================================

# problem 2: two strings
# Given two strings, determine if they share a common substring. A substring may be as small as one character.
# For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
# Complete the function twoStrings in the editor below.
# It should return a string, either YES or NO based on whether the strings share a common substring.

from collections import Counter
def twoStrings(s1, s2):
	s1 = Counter(s1)
	s2 = Counter(s2)

	shared_char = [(value>0,s1[key]>0) for key, value in s2.items()]

	success = list(map(lambda x: x[0] and x[1], shared_char))

	if  reduce(lambda x,y: x or y, success):
		print("yes")
		return "YES"
	else:
		print("NO")
		return "NO"

# ================================================================
# problem 3: sherlock and anagrams

# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other

def sherlockAndAnagrams(s):
	output = []

	sub_index = list(range(1,len(s)))
	for i in sub_index:
		temp = [s[val:val+i] for val in range(len(s)-i+1)]
		output.append(temp)

	anagrams = 0
	for group in output:

		out = list(map(lambda x: Counter(list(x)), group))
		
		out_cart = list(itertools.product(out,out))
		
		matches = len(list(filter(lambda x: x[0]==x[1], out_cart))) - len(out)
		
		# convert dictionaries to lists of tuples --> Counter --> sum
		# out_cart = list(map(lambda x: list(itertools.product(x,x)),out))
		# anagrams += reduce(lambda x,y: x==y, out)
		# print(out_cart)

		anagrams += matches//2




	return anagrams





if __name__ == '__main__':
	x = sherlockAndAnagrams("ifailuhkqq") # ifailuhkqq
	print(x)

	# sherlockAndAnagrams("kkkk")
