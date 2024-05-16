from typing import List
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
##### why not using MST?? --> because MST is the minimum *spaning* Tree, i.e. it needs to contatain all the nodes!
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: #O(max(m,n) space
        return self.minSum(grid, 0, 0)

    def minPath_inPlace(self, grid: List[List[int]]) -> int: #O(1) in space
        row = len(grid)
        col = len(grid[0])
        # scan first col
        for i in range(1,row):
            grid[i][0] += grid[i-1][0]
        # scan first row
        for j in range(1,col):
            grid[0][j] += grid[0][j-1]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[row-1][col-1]



    def minSum(self, grid, i, j):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]

        if i < len(grid) - 1 and j < len(grid[0]) - 1:
            return grid[i][j] + min(self.minSum(grid, i+1, j), self.minSum(grid, i, j+1))
        elif i == len(grid) - 1:
            return grid[i][j] + self.minSum(grid, i, j+1)
        elif j == len(grid[0]) - 1:
            return grid[i][j] + self.minSum(grid, i+1, j)

sol = Solution()
grid = [[5,4,2,9,6,0,3,5,1,4,9,8,4,9,7,5,1],
[3,4,9,2,9,9,0,9,7,9,4,7,8,4,4,5,8],
[6,1,8,9,8,0,3,7,0,9,8,7,4,9,2,0,1],
[4,0,0,5,1,7,4,7,6,4,1,0,1,0,6,2,8],
[7,2,0,2,9,3,4,7,0,8,9,5,9,0,1,1,0],
[8,2,9,4,9,7,9,3,7,0,3,6,5,3,5,9,6],
[8,9,9,2,6,1,2,5,8,3,7,0,4,9,8,8,8],
[5,8,5,4,1,5,6,6,3,3,1,8,3,9,6,4,8],
[0,2,2,3,0,2,6,7,2,3,7,3,1,5,8,1,3],
[4,4,0,2,0,3,8,4,1,3,3,0,7,4,2,9,8],
[5,9,0,4,7,5,7,6,0,8,3,0,0,6,6,6,8],
[0,7,1,8,3,5,1,8,7,0,2,9,2,2,7,1,5],
[1,0,0,0,6,2,0,0,2,2,8,0,9,7,0,8,0],
[1,1,7,2,9,6,5,4,8,7,8,5,0,3,8,1,5],
[8,9,7,8,1,1,3,0,1,2,9,4,0,1,5,3,1],
[9,2,7,4,8,7,3,9,2,4,2,2,7,8,2,6,7],
[3,8,1,6,0,4,8,9,8,0,2,5,3,5,5,7,5],
[1,8,2,5,7,7,1,9,9,8,9,2,4,9,5,4,0],
[3,4,4,1,5,3,3,8,8,6,3,5,3,8,7,1,3]]
print(sol.minPath_inPlace(grid))