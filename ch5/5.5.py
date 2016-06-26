"""
Write a function to determine the number of bits required to convert integer A to integer B.
EXAMPLE
Input: 31,14
Output: 2
"""

def getBitNumber(n):
    ct = 0
    while n > 0:
        if n % 2 == 1:
            ct += 1
        n >>= 1
    return ct

def getResult(n1, n2):
    nx = n1 ^ n2
    return getBitNumber(nx)

n1 = 0b1110110
n2 = 0b1001010
print(getResult(n1, n2))

n1 = 31
n2 = 14
print(getResult(n1, n2))
