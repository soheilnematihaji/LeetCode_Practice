"""
This a solution for the problem from
https://leetcode.com/problems/first-missing-positive/

Here is the copy of the problem from leetcode:

Given an unsorted integer array nums, find the smallest missing positive integer.

"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=set(nums)
        for i in range(1,len(nums)+2):
            if i not in x:
                return i
