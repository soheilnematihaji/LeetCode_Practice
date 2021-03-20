"""
This a solution for the problem from
https://leetcode.com/problems/toeplitz-matrix/

Here is the copy of the problem from leetcode:

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]!= matrix[i-1][j-1]:
                    return False
        return True
        
