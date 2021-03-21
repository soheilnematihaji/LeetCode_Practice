"""
This a solution for the problem from
https://leetcode.com/problems/uncrossed-lines/

Here is the copy of the problem from leetcode:

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

"""
from collections import defaultdict
from collections import deque
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        nums_to_ind_A=defaultdict(lambda:deque())
        nums_to_ind_B=defaultdict(lambda:deque())
        for i , value in enumerate(A):
            nums_to_ind_A[value].append(i)
        for i , value in enumerate(B):
            nums_to_ind_B[value].append(i)
        dynamic=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for i in range(len(A)-1,-1,-1):
            for j in range(len(B)-1,-1,-1):
                temp_a=A[i]
                temp_b=B[j]
                max_a=0
                max_b=0
                if temp_a== temp_b:
                    dynamic[i][j]= dynamic[i+1][j+1]+1
                else:
                    max_a=dynamic[i+1][j]
                    max_b=dynamic[i][j+1]
                    dynamic[i][j]= max(max_a,max_b)
                
        return dynamic[0][0]
