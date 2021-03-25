"""
This a solution for the problem from
https://leetcode.com/problems/copy-list-with-random-pointer/

Here is the copy of the problem from leetcode:

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None:
            return None
        map_old_new={}
        map_old_should_update_next=defaultdict(list)
        map_old_should_update_random=defaultdict(list)
        start=head
        new_head=Node(head.val)
        map_old_new[head]=new_head
        map_old_should_update_next[head.next].append(head)
        map_old_should_update_random[head.next].append(head)
        new=new_head
        while start:
            new_node=None
            if start.next:
                new_node=Node(start.next.val)
            if new_node:
                new.next=new_node
            if start.random:
                if map_old_new.get(start.random):
                    new.random=map_old_new.get(start.random)
                else:
                    map_old_should_update_random[start.random].append(new)
            for node in map_old_should_update_random[start]:
                node.random=new
            start=start.next
            new=new.next
            map_old_new[start]=new
        return new_head
            
