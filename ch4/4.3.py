"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
"""

import Tree

def createMBST_a(ary, start, end):
    if end < start:
        return None
    mid = int((start + end) / 2)
    n = Tree.Node(ary[mid])
    n.left = createMBST_a(ary, start, mid - 1)
    n.right = createMBST_a(ary, mid + 1, end)
    return n

def createMBST(ary):
    return createMBST_a(ary, 0, len(ary) - 1)

ary = [0, 1, 2, 3, 4, 5, 6]
n = createMBST(ary)
Tree.levelorderTraversal(n)
