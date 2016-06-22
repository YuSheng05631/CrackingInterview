"""
Write an algorithm to find the'next'node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.
"""

import Tree

def getSuccessor(n):
    if n is None:
        return None

    # 若有右樹，右樹中最靠右的節點為Successor
    if n.right is not None:
        nr = n.right
        while nr.left is not None:
            nr = nr.left
        return nr

    # 若無右樹，當父節點為其父節點的左節點時，其父節點為Successor
    nn = n
    np = n.parent
    while np is not None and nn is not np.left:
        nn = np
        np = np.parent
    return np

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
n0.parent = n1
n1.parent = n2
n2.parent = n4
n3.parent = n2
n5.parent = n4

print("{0} > {1}".format(n0.data, getSuccessor(n0)))
print("{0} > {1}".format(n1.data, getSuccessor(n1)))
print("{0} > {1}".format(n2.data, getSuccessor(n2)))
print("{0} > {1}".format(n3.data, getSuccessor(n3)))
print("{0} > {1}".format(n4.data, getSuccessor(n4)))
print("{0} > {1}".format(n5.data, getSuccessor(n5)))
