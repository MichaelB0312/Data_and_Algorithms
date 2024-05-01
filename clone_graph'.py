
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.marked = 0


from typing import Optional, Dict
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        Q = deque()
        Q.append(node)
        nodes_dict: Dict[int, Node] = {}
        src = node.val

        while Q:
            v = Q.popleft()
            v.marked = 1
            if v.val not in nodes_dict:
                nodes_dict[v.val] = Node(v.val)

            for w in v.neighbors:
                if w.marked == 0:
                    w.marked = 1
                    Q.append(w)
                    nodes_dict[w.val] = Node(w.val)

                nodes_dict[v.val].neighbors.append(nodes_dict[w.val])

        return nodes_dict[src]


# Build the desired graph
def buildGraph() -> Node:
    """
    Given Graph:
    1--2
    | |
    4--3
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]
    return node1


# A simple bfs traversal of a graph to
# check for proper cloning of the graph
def bfs(src: Node):
    visit = {}
    q = deque()
    q.append(src)
    visit[src] = True
    while q:
        u = q.popleft()
        print(f"Value of Node {u.val}")
        print(f"Address of Node {u}")
        v = u.neighbors
        for neighbor in v:
            if neighbor not in visit:
                visit[neighbor] = True
                q.append(neighbor)


if __name__ == "__main__":
    src = buildGraph()
    print("BFS Traversal before cloning")
    bfs(src)
    sol = Solution()
    clone = sol.cloneGraph(src)
    print("\nBFS Traversal after cloning")
    bfs(clone)


