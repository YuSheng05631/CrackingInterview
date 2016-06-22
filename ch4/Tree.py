class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None  # for 4.6

    def __str__(self):
        return str(self.data)

def createPerfectTree(layer):
    if layer <= 0:
        return
    ary = []
    n = 2 ** layer - 1
    for i in range(n):
        ary.append(Node(i))
    for i in range(int(n / 2)):
        ary[i].left = ary[i * 2 + 1]
        ary[i].right = ary[i * 2 + 2]
    return ary[0]

def preorderTraversal(n):
    if n is None:
        return
    print(n.data, end=" > ")
    preorderTraversal(n.left)
    preorderTraversal(n.right)

def inorderTraversal(n):
    if n is None:
        return
    inorderTraversal(n.left)
    print(n.data, end=" > ")
    inorderTraversal(n.right)

def postorderTraversal(n):
    if n is None:
        return
    postorderTraversal(n.left)
    postorderTraversal(n.right)
    print(n.data, end=" > ")

def levelorderTraversal(root):
    q = []
    q.append(root)
    while len(q) != 0:
        n = q[0]
        q.pop(0)
        print(n.data, end=" > ")
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

def getHeight(root):
    if root is None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1
