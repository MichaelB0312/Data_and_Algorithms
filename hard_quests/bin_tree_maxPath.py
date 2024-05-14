
from collections import deque
from typing import Optional, List, Tuple, Set, Dict, Any, Union

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:





    def build_graph(self, root):

        graph = {}

        stack = [root.val]
        node = root
        i = 0
        while( stack != None):
            if graph.get(i) == None:
                graph[i] = []
            curr_node = stack.pop(0)
            graph[i].append(curr_node.val)
            if curr_node.left != None:
                graph[i].append(curr_node.left)
                i = i + 1
                graph[i] = [curr_node.left]
            if curr_node.right != None:
                graph[i].append((curr_node.right))
                i = i + 1
                graph[i] = [curr_node.right]
            stack.append(curr_node.left)
            stack.append(curr_node.right)



