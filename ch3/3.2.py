"""
How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
"""

import StackQueue

stack = StackQueue.StackWithMin()

stack.push(5)
stack.print()
print(stack.getMin())

stack.push(6)
stack.print()
print(stack.getMin())


stack.push(3)
stack.print()
print(stack.getMin())

stack.push(7)
stack.print()
print(stack.getMin())

stack.pop()
stack.print()
print(stack.getMin())

stack.pop()
stack.print()
print(stack.getMin())
