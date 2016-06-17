class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        n = Node(data, self.head)
        self.head = n
        self.length += 1
        if self.length == 1:
            self.tail = n

    def addStr(self, s):
        sr = s[::-1]
        for c in sr:
            self.add(c)

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == data:
                    n.next = n.next.next
                    self.length -= 1
                    return
                n = n.next

    def print(self):
        n = self.head
        while n is not None:
            print(n, end=" > ")
            n = n.next
        print()
