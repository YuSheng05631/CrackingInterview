"""
You are given a binary tree in which each node contains a value.
Design an algorithm to print all paths which sum to a given value.
The path does not need to start or end at the root or a leaf.
"""

import Tree

def getPaths_a(n, stack, v):
    if n is None:
        return
    stack.append(n.data)
    if sum(stack) == v:
        print(stack)
    getPaths_a(n.left, stack[:], v)
    getPaths_a(n.right, stack[:], v)

def getPaths(n, v):
    getPaths_a(n, list(), v)
    if n.left is not None:
        getPaths(n.left, v)
    if n.right is not None:
        getPaths(n.right, v)

"""
      4
     / \
    2   5
   / \   \
  1   3  -10
 /     \   \
0      -6  10
"""
n0 = Tree.Node(0)
n1 = Tree.Node(1)
n2 = Tree.Node(2)
n3 = Tree.Node(3)
n4 = Tree.Node(4)
n5 = Tree.Node(5)
n6 = Tree.Node(-6)
np10 = Tree.Node(10)
nn10 = Tree.Node(-10)
n1.left = n0
n2.left = n1
n2.right = n3
n3.right = n6
n4.left = n2
n4.right = n5
n5.right = nn10
nn10.right = np10

print("9:")
getPaths(n4, 9)
print("\n3:")
getPaths(n4, 3)
print("\n0:")
getPaths(n4, 0)
