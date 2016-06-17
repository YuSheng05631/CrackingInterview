class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
        n = Node(data, self.head)
        self.head = n
        self.length += 1
        if self.length == 1:
            self.tail = n

    def pop(self):
        n = self.head
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return n

    def print(self):
        n = self.head
        while n is not None:
            print(n, end=" > ")
            n = n.next
        print()

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):       #和stack順序相反
        n = Node(data, None)
        if self.length == 0:
            self.head = n
            self.tail = n
            self.length += 1
        if self.length != 0:
            self.tail.next = n
            self.tail = n
            self.length += 1

    def pop(self):
        n = self.head
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return n

    def print(self):
        n = self.head
        while n is not None:
            print(n, end=" > ")
            n = n.next
        print()

class StackWithMin:     # for 3.2
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.minList = []

    def push(self, data):
        n = Node(data, self.head)
        self.head = n
        self.length += 1
        if self.length == 1:
            self.tail = n
            self.minList.append(data)
        else:
            if data < self.minList[0]:
                self.minList.insert(0, data)

    def pop(self):
        n = self.head
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            if n.data == self.minList[0]:
                self.minList.pop(0)
        return n

    def getMin(self):
        return self.minList[0]

    def print(self):
        n = self.head
        while n is not None:
            print(n, end=" > ")
            n = n.next
        print()

class SetOfStacks:  # for 3.3
    def __init__(self):
        self.threshold = 3
        self.stackList = [Stack()]

    def push(self, data):
        if self.stackList[0].length < self.threshold:
            self.stackList[0].push(data)
        else:
            self.stackList.insert(0, Stack())
            self.stackList[0].push(data)

    def pop(self):
        n = self.stackList[0].pop()
        if self.stackList[0].length == 0:
            self.stackList.pop(0)
        return n

    def popAt(self, index):
        n = self.stackList[index].pop()
        if self.stackList[index].length == 0:
            self.stackList.pop(index)
        return n

    def print(self):
        for i in range(len(self.stackList)):
            self.stackList[i].print()

class MyQueue:  # for 3.5
    def __init__(self):
        self.stackOld = Stack()
        self.stackNew = Stack()
        self.length = 0

    def reverseStackOldToNew(self):
        self.stackNew = Stack()
        n = self.stackOld.head
        while n is not None:
            self.stackNew.push(n.data)
            n = n.next

    def reverseStackNewToOld(self):
        self.stackOld = Stack()
        n = self.stackNew.head
        while n is not None:
            self.stackOld.push(n.data)
            n = n.next

    def push(self, data):
        self.stackOld.push(data)
        self.length += 1
        self.reverseStackOldToNew()

    def pop(self):
        if self.length > 0:
            n = self.stackNew.pop()
            self.length -= 1
            self.reverseStackNewToOld()
            return n

    def print(self):
        n = self.stackOld.head
        while n is not None:
            print(n, end=" > ")
            n = n.next
        print()

class Dog:   # for 3.7
    def __init__(self, name):
        self.name = name
        self.age = 0

class Cat:  # for 3.7
    def __init__(self, name):
        self.name = name
        self.age = 0

class AnimalQueue:  # for 3.7
    def __init__(self):
        self.DogQueue = Queue()
        self.CatQueue = Queue()
        self.age = 0

    def enqueue(self, animal):
        animal.age = self.age
        if type(animal) is Dog:
            self.DogQueue.push(animal)
        elif type(animal) is Cat:
            self.CatQueue.push(animal)
        self.age += 1

    def dequeueDog(self):
        dog = self.DogQueue.head
        self.DogQueue.pop()
        return dog.data

    def dequeueCat(self):
        cat = self.CatQueue.head
        self.CatQueue.pop()
        return cat.data

    def dequeueAny(self):
        dog = self.DogQueue.head
        cat = self.CatQueue.head
        if dog is None and cat is None:
            return None
        elif dog is None:
            return self.dequeueCat()
        elif cat is None:
            return self.dequeueDog()
        if dog.data.age <= cat.data.age:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def print(self):
        n = self.DogQueue.head
        while n is not None:
            print(n.data.name, end=" > ")
            n = n.next
        print()
        n = self.CatQueue.head
        while n is not None:
            print(n.data.name, end=" > ")
            n = n.next
        print()
