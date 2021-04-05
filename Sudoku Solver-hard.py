"""
This a solution for the problem from
https://leetcode.com/problems/sudoku-solver/

Here is the copy of the problem from leetcode:

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

"""
import math
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        size=len(board)
        sqr_size=int(math.sqrt(size))
        
        def insert_into_board(i,j,element):
            board[i][j]=element
            update_row_and_column(i,j)
            update_sqr(i,j)
            
        #updating columns and rows after interting an element into a cell so the columns can't use it anymore
        #return the list of updated cell by this change so we can update them back inside the recursive back track function
        def update_row_and_column(i,j):
            list_updated=[]
            for k in range(size):
                if type(board[i][k])!=str and board[i][j] in board[i][k] :
                    list_updated.append((i,k))
                    board[i][k].discard(board[i][j])
                if type(board[k][j])!=str and board[i][j] in board[k][j] :
                    list_updated.append((k,j))
                    board[k][j].discard(board[i][j])
            return list_updated
        
        #updating columns and rows after interting an element into a cell so the columns can't use it anymore
        #return the list of updated cell by this change so we can update them back inside the recursive back track function
        def update_sqr(i,j):
            list_updated=[]
            sqr_i=sqr_size*int(i/sqr_size)
            sqr_j=sqr_size*int(j/sqr_size)
            for k in range(sqr_size):
                for l in range(sqr_size):
                    if type(board[sqr_i+k][sqr_j+l])!=str and board[i][j] in board[sqr_i+k][sqr_j+l]:
                        list_updated.append((sqr_i+k,sqr_j+l))
                        board[sqr_i+k][sqr_j+l].discard(board[i][j])
            return list_updated
                    
        def scan():
            for i in range(size):
                for j in range(size):
                    if type(board[i][j])!=str and len(board[i][j])==1:
                        insert_into_board(i,j,list(board[i][j])[0])
        
        def check_to_continue():
            for i in range(size):
                for j in range(size):
                    if len(board[i][j])==0:
                        return False
            return True
        
        def check_is_finished():
            for i in range(size):
                for j in range(size):
                    if type(board[i][j])!=str:
                        return False
            return True
        
        list_not_filled=[]
         
        def solve_backtrack():
            if check_is_finished():
                return True
            if not check_to_continue():
                return False
            (i,j)=list_not_filled.pop()
            if type(board[i][j])!=str:
                temp=board[i][j]
                for el in temp:
                    board[i][j]=el
                    index_row_column=update_row_and_column(i,j)
                    index_sqr=update_sqr(i,j)
                    check=solve_backtrack()
                    if check:
                        return True
                    board[i][j]=temp
                    for (o,p) in index_row_column:
                        board[o][p].add(el)
                    for (o,p) in index_sqr:
                        board[o][p].add(el)
                list_not_filled.append((i,j))
            else:
                return solve_backtrack()
            return False
                
                    
        #initializing the board ans updating none cells to a list of potential elements
        for i in range(size):
            for j in range(size):
                if board[i][j]=='.':
                    board[i][j]=set([str(d) for d in range(1,size+1)])
                    
        #updating the rows and columns and smal sqrs for inital elements
        for i in range(size):
            for j in range(size):
                if type(board[i][j])==str:
                    update_row_and_column(i,j)
                    update_sqr(i,j)
   
        #scaning to solve for simple cases in the start
        for i in range(size*size):
            scan()
            
        #updating list_not_filled for backtrack
        for i in range(size):
            for j in range(size):
                if type(board[i][j])!=str:
                    list_not_filled.append((i,j))
                    
        # starting backtrack after initial process
        solve_backtrack()
