"""
Given two strings, write a method to decide if one is a permutation of the other.
"""

def isPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "abcd"
str2 = "cdab"
print(isPermutation(str1, str2))
