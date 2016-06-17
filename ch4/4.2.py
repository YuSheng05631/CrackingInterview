"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = []

def hasRoute(node1, node2):
    visited = list()    # 紀錄走過的點
    route = list()      # 紀錄路徑
    visited.append(node1)
    route.append(node1)
    cur = node1
    while True:
        moved = False
        for curnext in cur.next:
            if curnext not in visited:
                visited.append(curnext)
                route.append(curnext)
                cur = curnext
                moved = True
                if cur is node2:
                    for r in route:
                        print(r.data, end=" > ")
                    return True
                break
        if moved is False:
            route.pop()
            if len(route) > 0:
                cur = route[len(route) - 1]
            else:
                return False

"""
The directed graph.
0 ←→ 1 → 4
↓    ↑
2 ←  3 ← 5
"""
n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n0.next.append(n1)
n0.next.append(n2)
n1.next.append(n0)
n1.next.append(n4)
n3.next.append(n1)
n3.next.append(n2)
n5.next.append(n3)

print(hasRoute(n0, n2))
print(hasRoute(n0, n3))
print(hasRoute(n5, n2))
