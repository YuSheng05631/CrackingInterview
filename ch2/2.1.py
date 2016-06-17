"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

import Node

def removeDuplicates(ll):
    p1 = ll.head
    while p1 is not None:
        p2 = p1.next
        while p2 is not None:
            if p1.data == p2.data:
                ll.delete(p1.data)
            p2 = p2.next
        p1 = p1.next

ll = Node.LinkedList()
ll.addStr("FOLLOW UP")
ll.print()
removeDuplicates(ll)
ll.print()
