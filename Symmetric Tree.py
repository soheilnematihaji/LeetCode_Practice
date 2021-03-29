"""
This a solution for the problem from
https://leetcode.com/problems/symmetric-tree/

Here is the copy of the problem from leetcode:

iven the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def is_sym(node_left,node_right):
            if not node_left and not node_right:
                return True
            if not node_left and node_right:
                return False
            if not node_right and node_left:
                return False
            if node_left.val != node_right.val:
                return False
            if node_left.left and not node_right.right:
                return False
            if node_left.right and not node_right.left:
                return False
            return is_sym(node_left.left,node_right.right) and is_sym(node_left.right,node_right.left)
        if not root:
            return True
        return is_sym(root.left,root.right)
