"""
This a solution for the problem from
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Here is the copy of the problem from leetcode:

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def buildTreeWithIndex( inorder, postorder):
            root=postorder[-1]
            node=TreeNode(root)
            if len(inorder)==1:
                return node
            index=inorder.index(root)
            if index>0:
                node.left=buildTreeWithIndex( inorder[0:index], postorder[0:index])
            if index<len(postorder)-1:
                node.right=buildTreeWithIndex( inorder[index+1:], postorder[index:-1])
            return node
        if not inorder:
            return None
        return buildTreeWithIndex( inorder, postorder)

        
