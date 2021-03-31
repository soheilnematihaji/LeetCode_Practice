"""
This a solution for the problem from
https://leetcode.com/problems/binary-tree-coloring-game/

Here is the copy of the problem from leetcode:

Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        map_val={0:(0,0,0)}
        
        def count_under(node):
            if not node:
                return
            count_under(node.left)
            count_under(node.right)
            left_val=0
            right_val=0
            if node.right:
                right_val=map_val[node.right.val][0]
            if node.left:
                left_val=map_val[node.left.val][0]
            map_val[node.val]=(left_val+right_val+1,right_val,left_val)
        count_under(root)
        l=map_val[x]
        print(l)
        if l[0]<int(n/2)+1 or l[1]>n/2 or l[2]>n/2:
            return True
        
        return False

        
