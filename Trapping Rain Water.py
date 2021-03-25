"""
This a solution for the problem from
https://leetcode.com/problems/trapping-rain-water/

Here is the copy of the problem from leetcode:

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        max_val=max(height)
        max_ind=height.index(max_val)
        max_so_far=0
        sum_black=0
        sum_blue_and_black=0
        sum_blue=0
        for i in range(max_ind):
            val=height[i]
            sum_black+= val
            if max_so_far<val:
                max_so_far=val
            sum_blue_and_black+=max_so_far
        sum_blue=sum_blue_and_black-sum_black
        
        max_so_far=0
        sum_black=0
        sum_blue_and_black=0
        for i in range(len(height)-1,max_ind,-1):
            val=height[i]
            sum_black+= val
            if max_so_far<val:
                max_so_far=val
            sum_blue_and_black+=max_so_far
        sum_blue+=sum_blue_and_black-sum_black
        return sum_blue
        
                
