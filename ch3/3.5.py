"""
Implement a MyQueue class which implements a queue using two stacks.
"""

import StackQueue

mq = StackQueue.MyQueue()
mq.push("a")
mq.print()
mq.push("b")
mq.print()
mq.push("c")
mq.print()
mq.push("d")
mq.print()

mq.pop()
mq.print()
mq.pop()
mq.print()

mq.push("e")
mq.print()

mq.pop()
mq.print()
