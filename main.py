# Basic data manipulations
import pandas as pd
import numpy as np
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#

# chi-squared test
num_categories = 1
dof = 1 # degrees of freedom
alpha = 0.1
observed = [-1.61426, -1.61426,
0.982153,
-1.1701,
0.355576,
1.715741,
0.033332,
3.019362,
0.386953,
0.318027,
-0.15467,
0.052758,
0.84624,
0.252796,
0.806676,
1.02176,
-0.1046,
1.144919,
-0.38288,
-0.00055,
-1.099,
-1.39887,
-0.23666,
0.188631,
-0.01144,
-0.47493,
-1.77226,
0.705414,
-0.09772,
1.506978,
-0.9809]

import scipy.stats as stats
# compute critical value using the inverse of the CDF
C = np.exp(-0.5*stats.chi2.ppf(q=1-alpha, df=dof))
logC = -0.5*stats.chi2.ppf(q=1-alpha, df=dof)
print("the logC is: ", logC)

medY = np.median(observed)
log_of_Ls = -1*np.sum(np.abs(observed)) -1*(np.sum(np.abs(observed-medY)))
print("log_of_Ls is:", log_of_Ls)
if log_of_Ls < logC:
    print("H_0 is rejected!")
else:
    print("H_0 is accepted!")

str_arr = np.chararray((5,5))
str_arr[:] = ' '

str_arr[4,0:] = '*'
str_arr[3, 1:-1] = '*'
print(str_arr)
mystr = 'hello' + '\n'
mystr += 1*' ' +  mystr[1:-2] + 1*' '
print(mystr)

# while str[0] == ' ':
#     str = str[1:]
# print(str)
str = "(1+(4+5+2)-3)+(6+8)"
new_str = ''
for i in range(len(str)):
    if str[i] != ' ' and str[i] != '(' and str[i] != ')':
       new_str = new_str + str[i]

print(new_str)

from collections import deque
from typing import Optional, List, Tuple, Set, Dict, Any, Union

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


beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]

sol = Solution()
print("shortest path is:", sol.ladderLength(beginWord,endWord,wordList))


