from typing import List, Dict
from collections import deque
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
 You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.start_time = 0
        self.end_time = 0
        self.visited = 0
class Solution:

    def __init__(self):
        self.path = deque()
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build Directed Graph
        graph: Dict[int, List[Node]] = {}
        existed_nodes = numCourses*[None]
        for pair in prerequisites:
            if pair[1] not in graph:
                graph[pair[1]] = []
            if existed_nodes[pair[0]] == None:
                existed_nodes[pair[0]] = Node(pair[0])

            graph[pair[1]].append(existed_nodes[pair[0]])

        # use DFS to destect cycles
        visit_hist = numCourses*[0]
        global_time = 0
        for key in graph:
            # convert key to Node if it's necessary!!!!!!!##########
            #...##
            if existed_nodes[key] == None:
                existed_nodes[key] = Node(key)
            if existed_nodes[key].visited == 0:
                if self.dfs(graph, existed_nodes[key], visit_hist, global_time):
                    return False

        return True

    def dfs(self, graph:Dict[int, List[Node]], curr_course: Node, visit_hist, global_time):

        curr_course.start_time = global_time + 1
        global_time += 1
        curr_course.visited = 1
        if curr_course.val in graph:
            for child in graph[curr_course.val]:
                # cycle detection
                if child.start_time > 0 and child.end_time == 0:
                    return True
                if child.visited == 0:
                    if self.dfs(graph, child, visit_hist, global_time):
                        return True
        curr_course.end_time = global_time + 1
        global_time += 1
        # for print path option
        self.path.appendleft(curr_course.val)
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if self.canFinish(numCourses, prerequisites):
            return list(self.path)
        return []


sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(numCourses, prerequisites))
