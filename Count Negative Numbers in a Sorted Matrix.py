"""
This a solution for the problem from
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Here is the copy of the problem from leetcode:
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        def find_index_neg(arr, i,j):
            if i==j:
                if arr[i]<0:
                    return i
                else:
                    return -1
            if arr[i]<0:
                return i
            if i+1==j:
                if arr[j]<0:
                    return j
                else:
                    return -1

            index=int((i+j)/2)
            x1=find_index_neg(arr, i,index)
            x2=find_index_neg(arr, index,j)
            if x1!=-1:
                return x1
            else:
                return x2
        def find_sum_neg(arr, i,j,k,l):
            if k>l:
                return 0
            n=len(arr[0])
            if k==l:
                index=find_index_neg(arr[k],i,j)
                if index!=-1:
                    return n-index
                else:
                    return 0
            if l==k+1:
                index1=find_index_neg(arr[k],i,j)
                index2=find_index_neg(arr[l],i,j)
                if index1==-1:
                    index1=n
                if index2==-1:
                    index2=n
                return (n+n)-(index1+index2)
            index=int((l+k)/2)
            x1=find_index_neg(arr[index], i,j)
            if x1!=-1:
                y1=find_sum_neg(arr, x1,j,k,index-1)
                y2=find_sum_neg(arr, i,x1,index+1,l)
            else:
                y1=0
                y2=find_sum_neg(arr, i,j,index+1,l)
            if x1==-1:
                x1=n
            return y1+y2+n-x1
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        return find_sum_neg(grid,0,n-1,0,m-1)
             
