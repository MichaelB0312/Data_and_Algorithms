
from typing import List, Dict
from collections import deque

'''
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style
 starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c].
 Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder,
 you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2.
 You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

Input: board = [[-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,35,-1,-1,13,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
'''
class Solution:
    # build BFS while in every step push: ladders, snakes and step+6
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visit_list = (n*n+1)*[0]
        Q = deque()
        Q.append(1)
        visit_list[1] = 1
        graph: Dict[int, int] = {1:0} # cell_num:steps_num

        while Q:
            v = Q.popleft()
            cnt = 0
            v_inc = v + cnt
            while cnt<6 and v_inc<n*n:
                cnt += 1
                v_inc += 1
                # end of game
                if v_inc == n * n:
                    return graph[v] + 1
                row, col = self.calc_loc(v_inc, n)
                if board[row][col] == -1:
                    continue
                if not visit_list[board[row][col]]:
                    if visit_list[board[row][col]] == n*n: # ladder directly to the end
                        return graph[v] + 1
                    visit_list[board[row][col]] = 1
                    graph[board[row][col]] = graph[v] + 1
                    Q.append(board[row][col])
            # add six regular steps option(without snakes or ladders
            if cnt == 6 and not visit_list[v+6]:
                visit_list[v+6] = 1
                graph[v+6] = graph[v] + 1
                Q.append(v+6)

        return -1

    def calc_loc(self, curr_v, n):
        row = n - (curr_v-1)//n - 1
        if ((curr_v-1)//n)%2 == 1:
            col = -1*(curr_v%n)
        else:
            col = (curr_v-1)%n
        return row, col


sol = Solution()
board = [[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]
print(sol.snakesAndLadders(board))

