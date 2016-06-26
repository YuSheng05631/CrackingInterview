"""
Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.
"""

def getBitNumber(n):
    ct = 0
    while n > 0:
        if n % 2 == 1:
            ct += 1
        n >>= 1
    return ct

def getResult(n):
    s = l = 0
    if n <= 0:
        return s, l
    ctn = getBitNumber(n)

    tn = n -1
    while getBitNumber(tn) != ctn and tn > 0:
        tn -= 1
    s = tn

    tn = n + 1
    while getBitNumber(tn) != ctn and tn > 0:
        tn += 1
    l = tn

    return s, l

n = 27
s, l = getResult(n)
print("n: {0}\ns: {1}\nl: {2}".format(bin(n), bin(s), bin(l)))
