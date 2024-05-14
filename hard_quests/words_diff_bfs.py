from collections import deque
from typing import Optional, List, Tuple, Set, Dict, Any, Union
import pandas as pd
import numpy as np
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.visited = 0
        self.distance = 0

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # build adjacency graph
        # start with source = beginWord
        graph: Dict[str, List[Node]] = {}
        wordList.append(beginWord)
        endFlag = 0 # detect whether endword is in the wordList
        for word in wordList:
            if word == endWord:
                endFlag = 1
            word_node = Node(word)
            head = word_node
            graph[word] = head
            for freind in wordList:
                if word == freind or self.is_sing_diff(word,freind)==False:
                    continue
                freind_node = Node(freind)
                word_node.next = freind_node
                word_node = word_node.next

        if endFlag == 0:
            return 0

        target = graph[endWord]
        source = graph[beginWord]
        return self.BFS(graph=graph, source=source, target=target)

    def BFS(self, graph: Dict[str, List[Node]], source: Node, target: Node):

        source.visited = 1
        Q = deque()
        Q.append(source)
        while Q != None:
            v = Q.popleft()
            edges_head = graph[v.word].next
            while edges_head != None:
                if edges_head.visited == 0:
                    Q.append(edges_head)
                    edges_head.distance = v.distance + 1
                    edges_head.visited = 1

                if edges_head.word == target.word:
                    return edges_head.distance + 1

                edges_head = edges_head.next

        return 0

    def is_sing_diff(self, word1, word2):
        diffs_arr = np.zeros(len(word1))
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diffs_arr[i] = 1

        return np.sum(diffs_arr) == 1


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

sol = Solution()
print("shortest path is:", sol.ladderLength(beginWord,endWord,wordList))