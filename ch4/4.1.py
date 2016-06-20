"""
Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
"""

import Tree

def isBalanced(bt):
    if bt is None:
        return True
    d = Tree.getHeight(bt.left) - Tree.getHeight(bt.right)
    if abs(d) > 1:
        return False
    else:
        return isBalanced(bt.left) and isBalanced(bt.right)

# Balanced tree
bt = Tree.createPerfectTree(3)
Tree.levelorderTraversal(bt)
print()
print(Tree.getHeight(bt))
print(isBalanced(bt))

# Unbalanced tree
bt = Tree.Node(0)
bt.left = Tree.Node(1)
bt.right = Tree.Node(2)
bt2 = Tree.Node(3)
bt2.left = bt
Tree.levelorderTraversal(bt2)
print()
print(Tree.getHeight(bt2))
print(isBalanced(bt2))
