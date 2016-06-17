"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
Output: 2 -> 1 -> 9.That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
Output: 9 -> 1 -> 2.That is, 912.
"""

import Node

def addLinkedList(l1, l2):
    num1 = 0
    num2 = 0
    d = 1
    n = l1.head
    while n is not None:
        num1 += n.data * d
        n = n.next
        d *= 10
    d = 1
    n = l2.head
    while n is not None:
        num2 += n.data * d
        n = n.next
        d *= 10
    return num1 + num2

def addLinkedListReverse(l1, l2):
    #l1R = Node.LinkedList()
    #l2R = Node.LinkedList()
    num1 = 0
    num2 = 0
    d = 10 ** (l1.length - 1)
    n = l1.head
    while n is not None:
        num1 += n.data * d
        n = n.next
        d /= 10
    d = 10 ** (l2.length - 1)
    n = l2.head
    while n is not None:
        num2 += n.data * d
        n = n.next
        d /= 10
    return num1 + num2

l1 = Node.LinkedList()
l2 = Node.LinkedList()
l1.add(6)
l1.add(1)
l1.add(7)
l2.add(2)
l2.add(9)
l1.print()
l2.print()
print("sum = ", end="")
print(addLinkedList(l1, l2))
print("sum(Reverse) = ", end="")
print(addLinkedListReverse(l1, l2))
