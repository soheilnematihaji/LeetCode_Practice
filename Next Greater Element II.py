"""
This a solution for the problem from
https://leetcode.com/problems/next-greater-element-ii/

Here is the copy of the problem from leetcode:

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

"""
from collections import defaultdict
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result=['s']*(2 *len(nums))
        def find_max_right(nums_right,i,j):
            if i>=j-1:
                return None
            if i==j-2:
                if nums_right[i]<nums_right[i+1]:
                    result[i]=nums_right[i+1]
                    return
            index=int((i+j)/2)
            find_max_right(nums_right,i,index)
            find_max_right(nums_right,index,j)
            map_left_index=defaultdict(set)
            for l,x in enumerate(result[i:index]):
                if x=='s':
                    map_left_index[nums_right[l+i]].add(l+i)
            sorted_val=sorted(map_left_index.keys())
            i1=int(index+2-1-1)
            j1=0
            while i1 < j:
                if j1>len(sorted_val)-1:
                    break
                if nums_right[i1]>sorted_val[j1]:
                    for ind in map_left_index[sorted_val[j1]]:
                        result[ind]=nums_right[i1]
                    j1+=1
                else:
                    i1+=1
        nums.extend(nums)
        if not nums:
            return []
        find_max_right(nums,0,len(nums))
        outPut=result[0:int(len(nums)/2)]
        for i,val in enumerate(outPut):
            if val=='s':
                outPut[i]=-1
        return outPut
                
