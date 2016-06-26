"""
An array A contains all the integers from 0 through n, except for one number which is missing.
In this problem, we cannot access an entire integer in A with a single operation.
The elements of A are represented in binary, and the only operation we can use to access them is "fetch the jth bit of A[i]," which takes constant time.
Write code to find the missing integer.
Can you do it in O(n) time?
"""

def fetchBit(ary, i, j):
    s = str(bin(ary[i]))
    s = s[2:]
    s = s[::-1]
    return int(s[j:j+1])

def findMissing(ary):
    b = 1
    for i in range(len(ary)):
        LSB = fetchBit(ary, i, 0)
        if LSB == b:
            return i    # 連續兩數最後一個位元相同時，該index即為Missing number
        b ^= 1
    return len(ary)     # Miss ary中最後一個數字的情況

ary = list()
for i in range(1000):
    ary.append(i)
print(bin(ary.pop(123)))
print(bin(findMissing(ary)))
