"""
This a solution for the problem from
https://leetcode.com/problems/game-of-life/

Here is the copy of the problem from leetcode:

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return board
        board_1=[0 for l in board[0]]
        board_2=[0 for l in board[0]]
        for i in range(len(board)-1):
            for j,val in enumerate(board[i]):
                live_nei=board[i+1][j]
                live_nei+=board_2[j]
                if j>0:
                    live_nei+=board_1[j-1]+board_2[j-1]+board[i+1][j-1]
                if j<len(board[i])-1:
                    live_nei+=board_2[j+1]+board[i][j+1]+board[i+1][j+1]
                board_1[j]=board_2[j]
                board_2[j]=board[i][j]
                if val==1:
                    if live_nei<2 or live_nei>3:
                        board[i][j]=0
                else:
                    if live_nei==3:
                        board[i][j]=1
        for j,val in enumerate(board[-1]):
            live_nei=board_2[j]
            if j>0:
                live_nei+=board_1[j-1]+board_2[j-1]
            if j<len(board[-1])-1:
                live_nei+=board_2[j+1]+board[-1][j+1]
            board_1[j]=board_2[j]
            board_2[j]=board[-1][j]
            if val:
                if live_nei<2 or live_nei>3:
                    board[-1][j]=0
            else:
                if live_nei==3:
                    board[-1][j]=1
