"""
Write code to partition a linked list around a value x, such that all nodes less than x come before alt nodes greater than or equal to x.
"""

import Node

def partition(ll, x):
    LList = Node.LinkedList()
    GList = Node.LinkedList()
    n = ll.head
    while n is not None:
        if n.data < x:
            LList.add(n.data)
        else:
            GList.add(n.data)
        n = n.next

    #merge GList and LList
    newList = Node.LinkedList()
    n = GList.head
    while n is not None:
        newList.add(n.data)
        n = n.next
    n = LList.head
    while n is not None:
        newList.add(n.data)
        n = n.next
    return newList

ll = Node.LinkedList()
ll.add(4)
ll.add(1)
ll.add(9)
ll.add(5)
ll.add(2)
ll.add(6)
ll.print()
newList = partition(ll, 5)
newList.print()
