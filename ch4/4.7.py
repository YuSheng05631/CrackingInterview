"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
"""

import Tree

def covers(root, n):
    if root is None:
        return False
    if root is n:
        return True
    return covers(root.left, n) or covers(root.right, n)

def getCommonAncestor_a(root, n1, n2):
    if root is None:
        return None
    if n1 is root or n2 is root:
        return root
    isOnLeft_n1 = covers(root.left, n1)
    isOnLeft_n2 = covers(root.left, n2)
    if isOnLeft_n1 != isOnLeft_n2:
        return root
    if isOnLeft_n1:
        return getCommonAncestor_a(root.left, n1, n2)
    else:
        return getCommonAncestor_a(root.right, n1, n2)

def getCommonAncestor(root, n1, n2):
    if not covers(root, n1) or not covers(root, n2):
        return None
    return getCommonAncestor_a(root, n1, n2)

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

print(getCommonAncestor(n4, n0, n1))
print(getCommonAncestor(n4, n0, n3))
print(getCommonAncestor(n4, n0, n5))

n6 = Tree.Node(6)
print(getCommonAncestor(n4, n0, n6))
