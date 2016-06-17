"""
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle"is a rotation of "erbottlewat").
"""

def isSubString(s1, s2):
    return s1.find(s2) != -1

def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False

    matchIndex = [] #[s1索引][s1索引的值 = 在s2中的哪些索引的值]
    for i in range(0, len(s1)):
        line = []
        for j in range(0, len(s2)):
            if isSubString(s2[j], s1[i]):
                line.append(j)
        matchIndex.append(line)

    #檢查matchIndex是否能按照順序從0數到len(s1)-1
    for i in range(0, len(matchIndex)):
        try:
            matchIndex[i].index(0)  #沒找到0會傳回例外
            ct = i
            try:
                for j in range(0, len(matchIndex)): #找到0之後，開始按照順序計數
                    matchIndex[ct].index(j)
                    ct += 1
                    if ct == len(matchIndex):
                        ct -= len(matchIndex)
                return True
            except ValueError:
                pass
        except ValueError:
            pass
    return False

def isRotation2(s1, s2):
    if len(s1) != len(s2) or len(s1) < 1:
        return False
    s1s1 = s1 + s1
    return isSubString(s1s1, s2)

s1 = "waterbottle"
s2 = "erbottlewat"
print(isRotation(s1, s2))
print(isRotation2(s1, s2))
