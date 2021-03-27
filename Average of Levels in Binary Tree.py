"""
This a solution for the problem from
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Here is the copy of the problem from leetcode:

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        map_level_to_sum=defaultdict(int)
        map_level_to_count=defaultdict(int)
        def node_with_Level(root,level):
            map_level_to_sum[level]+=root.val
            map_level_to_count[level]+=1
            if root.left:
                node_with_Level(root.left,level+1)
            if root.right:
                node_with_Level(root.right,level+1)
        node_with_Level(root,0)
        output=[]
        for i in range(len(map_level_to_sum)):
            output.append(map_level_to_sum[i]/map_level_to_count[i])
        return output
