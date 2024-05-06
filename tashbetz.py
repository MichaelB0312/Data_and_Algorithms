
from typing import List

'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.word_count = 0



class Solution:

    def insert_words(self, words: List[str], root: TrieNode):

        for word in words:
            curr_node = root
            for i in range(len(word)):
                if curr_node.children[ord(word[i]) - ord('a')] == None:
                    curr_node.children[ord(word[i]) - ord('a')] = TrieNode()
                curr_node = curr_node.children[ord(word[i]) - ord('a')]

            curr_node.word_count += 1

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        output_list = set()
        self.insert_words(words, root)
        for i in range(len(board[0])):
            for j in range(len(board[1])):
                if root.children[ord(board[i][j]) - ord('a')]:
                    curr_node = root.children[ord(board[i][j]) - ord('a')]
                    out_word = board[i][j]
                    if self.backtrack(board, i, j, out_word, curr_node):
                        out_word = self.backtrack(board, i, j, out_word, curr_node)
                        output_list.add(out_word)

        return list(output_list)

    def backtrack(self, board: List[List[str]], i, j, out_word, curr_node):
        if curr_node.word_count:
            return out_word

        orig_ch = board[i][j] #visit
        board[i][j] = '@'

        retval = 0
        if i < len(board[0])-1 and curr_node.children[ord(board[i+1][j]) - ord('a')]:
           curr_node = curr_node.children[ord(board[i+1][j]) - ord('a')]
           out_word += board[i+1][j]
           retval = self.backtrack(board, i+1, j, out_word, curr_node)

        elif i>0 and curr_node.children[ord(board[i-1][j]) - ord('a')]:
            curr_node = curr_node.children[ord(board[i-1][j]) - ord('a')]
            out_word += board[i-1][j]
            retval = self.backtrack(board, i - 1, j, out_word, curr_node)

        elif j>0 and curr_node.children[ord(board[i][j-1]) - ord('a')]:
            curr_node = curr_node.children[ord(board[i][j-1]) - ord('a')]
            out_word += board[i][j-1]
            retval = self.backtrack(board, i,j-1, out_word, curr_node)

        elif j<len(board[1])-1 and curr_node.children[ord(board[i][j+1]) - ord('a')]:
            curr_node = curr_node.children[ord(board[i][j+1]) - ord('a')]
            out_word += board[i][j+1]
            retval = self.backtrack(board, i,j+1, out_word, curr_node)

        board[i][j] = orig_ch

        return retval







board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath","pea","eat","rain"]
sol = Solution()
print(sol.findWords(board, words))