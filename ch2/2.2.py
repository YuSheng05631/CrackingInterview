"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

import Node

def subList(ll, k):
    if k > ll.length:
        print("error: k > length of linkedList")
        return Node.LinkedList()
    n = ll.head
    r = ll.length - k
    for i in range(0, r):
        n = n.next
    newLL = Node.LinkedList()
    newLL.head = n
    return newLL

ll = Node.LinkedList()
ll.addStr("ABCDEFG")
ll.print()
newLL = subList(ll, 3)
ll.print()
newLL.print()
