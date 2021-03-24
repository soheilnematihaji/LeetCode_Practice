"""
This a solution for the problem from
https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

Here is the copy of the problem from leetcode:

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents is (A o B), where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.

"""
# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
            
        def printpostravers(node):
            if node==None:
                return ''
            return node.val+printpostravers(node.left)+printpostravers(node.right)
        def expTreeRaw(s):
            if not s:
                return None
            if type(s)==Node:
                return s
            if len(s)==1:
                if type(s[0])==Node:
                    return s[0]
                else:
                    return Node(s[0])
            for i in range(len(s)-1,-1,-1):
                if s[i]=='+' or s[i]=='-' :
                    return Node(s[i],left=expTreeRaw(s[0:i]),right=expTreeRaw(s[i+1:]))
            return Node(s[-2],left=expTreeRaw(s[0:-2]),right=expTreeRaw([s[-1]]))
        def process_raw_with_par(s):
            countopen=0
            countclosed=0
            created_list=[]
            lst_index=0
            has_par=False
            for i in range(len(s)):
                if s[i] in '+*-/' and countopen==countclosed:
                    if has_par:
                        has_par=False
                        created_list.append(process_raw_with_par(s[lst_index+1:i-1]))
                        created_list.append(s[i])
                        lst_index=i+1
                        
                    else:
                        created_list.append(s[lst_index:i])
                        created_list.append(s[i])
                        lst_index=i+1
                if s[i]=='(':
                    has_par=True
                    countopen+=1
                if s[i]==')':
                    countclosed+=1
            if has_par:
                created_list.append(process_raw_with_par(s[lst_index+1:-1]))
            else:
                created_list.append(s[lst_index:])
            return expTreeRaw(created_list)
        x= process_raw_with_par(s)
        return x
