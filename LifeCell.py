from typing import List

'''
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
 Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state,
 where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
 
 Input: board = [[0,1,0],
                 [0,0,1],
                 [1,1,1],
                 [0,0,0]]
                 
        Output: [[0,0,0],
                 [1,0,1],
                 [0,1,1],
                 [0,1,0]]
'''
class Solution:

    def __init__(self): #for in-place changing
        self.beenOne = 3/4
        self.beenZero = 1/4
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 and self.checkArea(board, i, j, 0):
                    board[i][j] = self.beenZero
                if board[i][j] == 1 and self.checkArea(board, i, j, 1):
                    board[i][j] = self.beenOne

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == self.beenOne:
                    board[i][j] = 0
                if board[i][j] == self.beenZero:
                    board[i][j] = 1

    def checkArea(self, board: List[List[int]], i, j, status):

        # needs exactly 3 ones
        live_cnt = 0
        if i>0 and (board[i-1][j] == 1 or board[i-1][j] == self.beenOne): #up
                live_cnt += 1
        if i<len(board)-1 and (board[i+1][j] == 1 or board[i+1][j] == self.beenOne): #down
                live_cnt += 1
        if j<len(board[0])-1 and (board[i][j+1] == 1 or board[i][j+1] == self.beenOne): #right
                live_cnt += 1
        if j>0 and (board[i][j-1] == 1 or board[i][j-1] == self.beenOne): #left
                live_cnt += 1
        if i>0 and j>0 and (board[i-1][j-1] == 1 or board[i-1][j-1] == self.beenOne): #upper left
                live_cnt += 1
        if i<len(board)-1 and j<len(board[0])-1 and (board[i+1][j+1] == 1 or board[i+1][j+1] == self.beenOne): #down right
                live_cnt += 1
        if i<len(board)-1 and j>0 and (board[i+1][j-1] == 1 or board[i+1][j-1] == self.beenOne): #down left
                live_cnt += 1
        if i>0 and j<len(board[0])-1 and (board[i-1][j+1] == 1 or board[i-1][j+1] == self.beenOne): #upper right
                live_cnt += 1

        if status == 0: #check resurrection option
            return live_cnt == 3
        if status == 1: #check death option
            return live_cnt<2 or live_cnt>3

        return False



sol = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
sol.gameOfLife(board)
print(board)