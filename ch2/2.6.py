"""
Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A - > B - > C - > D - > E - > C [the same C as earlier]
Output: C
"""

import Node

#slowPointer一次走一步，fastPointer一次走兩步。
#兩者碰撞的點到Loop起點的距離，必定和LinkedList起點到Loop起點的距離相等。
#所以找到碰撞點之後，設一個Pointer從LinkedList起點前進，一個Pointer從碰撞點前進。
#等到兩個Pointer走到相等的點，就是Loop起點。
def getLoopBeginning(ll):
    slowPointer = ll.head
    fastPointer = ll.head
    while True:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if slowPointer.data == fastPointer.data:    #找到碰撞點
            n = ll.head
            while True:
                if n.data == slowPointer.data:      #找到Loop起點
                    return n.data
                n = n.next
                slowPointer = slowPointer.next

#Create a Circular LinkedList
ll = Node.LinkedList()
ll.addStr("CDE")
ll.tail.next = ll.head
loopBeginning = ll.head #just record
ll.addStr("AB")

#print Circular LinkedList
n = ll.head
for i in range(ll.length):
    print(n, end=" > ")
    n = n.next
print(loopBeginning.data + " > ...")

print(getLoopBeginning(ll))
