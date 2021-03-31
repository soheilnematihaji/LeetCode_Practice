"""
This a solution for the problem from
https://leetcode.com/problems/perfect-squares/

Here is the copy of the problem from leetcode:

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        output=[1 for i in range(n+1)]
        for i in range(n+1):
            k=int(math.sqrt(i))
            if k*k==i:
                output[i]=1
            else:
                min_val=n
                for j in range(max(int(2*k/3)-10,1),k+1):
                    min_val=min(min_val, output[i-(j*j)]+1)
                    if min_val==2:
                        break
                output[i]=min_val
        return output[n]
