"""
This a solution for the problem from
https://leetcode.com/problems/missing-element-in-sorted-array/

Here is the copy of the problem from leetcode:

Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        counter=k
        output=0
        for i in range(1,len(nums)):
            diff=nums[i]-nums[i-1]
            if diff>counter:
                return nums[i-1]+counter
            else:
                counter-=diff-1
        return nums[-1]+counter
