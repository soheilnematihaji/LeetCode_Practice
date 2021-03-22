"""
This a solution for the problem from
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Here is the copy of the problem from leetcode:

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_el=arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            temp=arr[i]
            arr[i]=max_el
            max_el=max(max_el,temp)
        return arr
