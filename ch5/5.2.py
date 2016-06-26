"""
Given a real number between 0 and 7 (e.g., 0.72) that is passed in as a double, print the binary representation.
If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR."
"""

def getBinary(num):
    if num >= 1 or num <= 0:
        return "ERROR"
    b = ""
    while num > 0:
        num *= 2
        if num >= 1:
            num -= 1
            b += "1"
        else:
            b += "0"
        if len(b) > 32:
            return "ERROR"
    return "0." + b

print(getBinary(0.125))
print(getBinary(0.875))
print(getBinary(0.72))
