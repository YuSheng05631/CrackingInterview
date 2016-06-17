"""
Implement a function to check if a linked list is a palindrome.
"""

import Node

def isPalindrome(ll):
    n = ll.head
    strR = ""
    llR = Node.LinkedList()
    while n is not None:
        strR += n.data
        n = n.next
    llR.addStr(strR[::-1])
    n = ll.head
    nR = llR.head
    while n is not None:
        if n.data != nR.data:
            return False
        n = n.next
        nR = nR.next
    return True

ll = Node.LinkedList()
ll.addStr("0123210")
ll.print()
print(isPalindrome(ll))
