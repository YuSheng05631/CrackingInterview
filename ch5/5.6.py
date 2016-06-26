"""
Write a program to swap odd and even bits in an integer with as few instructions as possible
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and soon).
"""

def swapOddEven(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)

n = 0b111010110001
print(bin(n))
print(bin(swapOddEven(n)))
