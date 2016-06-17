"""
Write a program to sort a stack in ascending order (with biggest items on top).
You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (such as an array).
The stack supports the following operations: push, pop, peek, and isEmpty.
"""

import StackQueue

def sortStack(stack):
    stackSorted = StackQueue.Stack()
    while stack.length > 0:
        n = stack.pop()
        while stackSorted.head is not None and stackSorted.head.data > n.data:
            stack.push(stackSorted.pop().data)
        stackSorted.push(n.data)
    return stackSorted

stack = StackQueue.Stack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(5)
stack.push(2)
stack.print()
stackSorted = sortStack(stack)
stackSorted.print()
