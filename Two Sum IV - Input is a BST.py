"""
This a solution for the problem from
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

Here is the copy of the problem from leetcode:

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        output_set=set()
        def set_all(root):
            output_set.add(root.val)
            if root.left:
                set_all(root.left)
            if root.right:
                set_all(root.right)
            return output_set
        
        set_re=set_all(root)
        for i in set_re:
            if k-i in set_re and k-i!=i:
                return True
        return False
