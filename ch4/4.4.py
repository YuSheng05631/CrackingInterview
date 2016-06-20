"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

import Tree

def createLinkedList(bt):
    ls = list()     # list的集合
    ls.append([bt])
    lt = list()     # 臨時的list
    lt.append(bt)
    while len(lt) > 0:
        lt = list()
        for n in ls[-1]:
            if n.left is not None:
                lt.append(n.left)
            if n.right is not None:
                lt.append(n.right)
        if len(lt) > 0:
            ls.append(lt)
    return ls

bt = Tree.createPerfectTree(4)
ls = createLinkedList(bt)
for l in ls:
    for n in l:
        print(n, end=" > ")
    print()
