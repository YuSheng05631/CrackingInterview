"""
Describe how you could use a single array to implement three stacks.
"""

class StackArray:
    def __init__(self):
        self.array = []
        self.pointers = [0, 0, 0]

    def push(self, stackNum, data):
        if stackNum < 0 or stackNum > 2:
            return
        self.array.insert(self.pointers[stackNum], data)
        if stackNum == 0:
            self.pointers[0] += 1
            self.pointers[1] += 1
            self.pointers[2] += 1
        elif stackNum == 1:
            self.pointers[1] += 1
            self.pointers[2] += 1
        elif stackNum == 2:
            self.pointers[2] += 1

    def pop(self, stackNum):
        if stackNum < 0 or stackNum > 2:
            return
        n = None
        if stackNum == 0 and self.pointers[0] > 0:
            n = self.array[0]
            self.array.pop(0)
            self.pointers[0] -= 1
            self.pointers[1] -= 1
            self.pointers[2] -= 1
        elif stackNum == 1 and self.pointers[1] > 0:
            n = self.array[self.pointers[0]]
            self.array.pop(self.pointers[0])
            self.pointers[1] -= 1
            self.pointers[2] -= 1
        elif stackNum == 2 and self.pointers[2] > 0:
            n = self.array[self.pointers[1]]
            self.array.pop(self.pointers[1])
            self.pointers[2] -= 1
        return n

    def print(self):
        print(self.array)

sa = StackArray()
sa.push(0, "a")
sa.push(2, "b")
sa.push(2, "c")
sa.push(1, "d")
sa.push(0, "e")
sa.push(1, "f")
sa.print()
sa.pop(1)
sa.print()
