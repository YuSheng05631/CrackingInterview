"""
An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis.
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like.
Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
You may use the built-in LinkedList data structure.
"""

import StackQueue

aq = StackQueue.AnimalQueue()
aq.enqueue(StackQueue.Cat("catA"))
aq.enqueue(StackQueue.Dog("dogA"))
aq.enqueue(StackQueue.Dog("dogB"))
aq.enqueue(StackQueue.Dog("dogC"))
aq.enqueue(StackQueue.Cat("catB"))
aq.enqueue(StackQueue.Cat("catC"))
aq.print()
print(aq.dequeueAny().name)
print(aq.dequeueAny().name)
print(aq.dequeueAny().name)
print(aq.dequeueAny().name)
print(aq.dequeueAny().name)
print(aq.dequeueAny().name)
