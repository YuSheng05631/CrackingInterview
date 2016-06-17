"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string, your method should return the original string.
"""

def compression(string):
    st = ""
    ct = 0
    newString = ""
    for i in range(0, len(string)):
        if st == string[i]:
            ct += 1
        elif ct == 0:
            st = string[i]
            ct += 1
        elif ct > 0:
            newString += st + str(ct)
            st = string[i]
            ct = 1
    newString += st + str(ct)
    if len(newString) < len(string):
        return newString
    else:
        return string

string = "aabcccccaaa"
print(compression(string))
