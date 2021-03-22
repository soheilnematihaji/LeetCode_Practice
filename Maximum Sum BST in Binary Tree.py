"""
This a solution for the problem from
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

Here is the copy of the problem from leetcode:

Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        
        def maxSumBST(root):
            if root==None:
                return (None,0,-100000)
            max_node_0,val_0,max_val_0=maxSumBST(root.left)
            max_node_1,val_1,max_val_1=maxSumBST(root.right)
            if root.right==None:
                if root.left==None:
                    return (root,root.val,max(0,root.val))
                else:
                    if root.val>root.left.val and max_node_0==root.left:
                        return (root,root.val+val_0,max(root.val+val_0,max_val_0))
                    else:
                        return (max_node_0,val_0,max_val_0)
            if root.left==None:
                if root.val<root.right.val and max_node_1==root.right:
                    return (root,root.val+val_1,max(root.val+val_1,max_val_1))
                else:
                    return (max_node_1,val_1,max_val_1)
                
            if root.left.val<root.val and root.right.val>root.val and max_node_0==root.left and max_node_1==root.right:
                return (root,root.val+val_1+val_0,max(root.val+val_1+val_0,max_val_1,max_val_0))
            else:
                if max_val_0>max_val_1:
                    return max_node_0,val_0,max_val_0
                else:
                    return max_node_1,val_1,max_val_1
        return maxSumBST(root)[2]
                
                
        
