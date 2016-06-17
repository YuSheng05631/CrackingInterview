"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

def isUnique(string):
    temp = ""
    for c in string:
        if temp.find(c) != -1:
            return False
        else:
            temp += c
    return True

string = "abcdea"
print(isUnique(string))
