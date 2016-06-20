"""
Implement a function to check if a binary tree is a binary search tree.
"""

import Tree

def isBST(bt):
    if bt.left is None and bt.right is None:
        return True
    if bt.left is not None and bt.left.data > bt.data:
        return False
    if bt.right is not None and bt.right.data < bt.data:
        return False
    if bt.left is None:
        return isBST(bt.right)
    if bt.right is None:
        return isBST(bt.left)
    return isBST(bt.left) and isBST(bt.right)

bt = Tree.Node(1)
bt.left = Tree.Node(0)
bt.right = Tree.Node(2)
Tree.levelorderTraversal(bt)
print()
print(isBST(bt))

bt2 = Tree.Node(10)
bt2.left = bt
Tree.levelorderTraversal(bt2)
print()
print(isBST(bt2))

bt2 = Tree.Node(10)
bt2.left = bt
bt2.right = Tree.Node(9)
Tree.levelorderTraversal(bt2)
print()
print(isBST(bt2))
