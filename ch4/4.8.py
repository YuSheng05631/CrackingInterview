"""
You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of Tl.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""

import Tree

def containsTree(n1, n2):
    if n2 is None:
        return True
    return subTree(n1, n2)

def subTree(n1, n2):
    if n1 is None:
        return False
    if n1.data == n2.data:
        if matchTree(n1 ,n2):
            return True
    return subTree(n1.left, n2) or subTree(n1.right, n2)

def matchTree(n1, n2):
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None:
        return False
    if n1.data != n2.data:
        return False
    return matchTree(n1.left, n2.left) and matchTree(n1.right, n2.right)

"""
      4
     / \
    2   5
   / \
  1   3
 /
0
"""
n0 = Tree.Node(0)
n1 = Tree.Node(1)
n2 = Tree.Node(2)
n3 = Tree.Node(3)
n4 = Tree.Node(4)
n5 = Tree.Node(5)
n1.left = n0
n2.left = n1
n2.right = n3
n4.left = n2
n4.right = n5

na = Tree.Node(2)
na.left = Tree.Node(1)
na.right = Tree.Node(3)

nb = Tree.Node(2)
nb.left = Tree.Node(1)
nb.right = Tree.Node(30)

print(containsTree(n4, n2))
print(containsTree(n4, na))
print(containsTree(n4, nb))
