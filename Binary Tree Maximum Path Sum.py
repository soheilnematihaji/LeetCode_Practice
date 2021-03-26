"""
This a solution for the problem from
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Here is the copy of the problem from leetcode:

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxpath(root):
            if root ==None:
                return (-10000000,-1000000)
            if root.left==None and root.right==None:
                return (root.val,root.val)
            (max_path_left,max_path_left_total)=maxpath(root.left)
            (max_path_right,max_path_right_total)=maxpath(root.right)
            val=root.val
            list_all_posibple=[max_path_left_total,max_path_right_total]
            list_all_posibple.append(val)
            list_all_posibple.append(max_path_right+val)
            list_all_posibple.append(max_path_left+val)
            list_all_posibple.append(max_path_left+val+max_path_right)
            return (max(val,max_path_left+val, max_path_right+val),max(list_all_posibple))
        return maxpath(root)[1]
