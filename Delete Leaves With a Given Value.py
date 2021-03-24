"""
This a solution for the problem from
https://leetcode.com/problems/delete-leaves-with-a-given-value/

Here is the copy of the problem from leetcode:

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def removeLN(root,target):
            if root.left:
                root.left=removeLN(root.left,target)
            if root.right:
                root.right=removeLN(root.right,target)
            if root.right==None and root.left==None:
                if root.val==target:
                    return None
                else:
                    return root
            return root
        return removeLN(root,target)
