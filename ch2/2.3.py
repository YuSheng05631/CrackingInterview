"""
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node
EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a- >b- >d->e
"""
import Node

ll = Node.LinkedList()
ll.addStr("ABCDEFG")
ll.print()
ll.delete("C")
ll.print()
