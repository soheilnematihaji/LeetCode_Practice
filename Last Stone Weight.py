"""
This a solution for the problem from
https://leetcode.com/problems/last-stone-weight/

Here is the copy of the problem from leetcode:

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

"""
from collections import deque
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        def insert_to_list(stones,x):
            for i in range(len(stones)):
                if x<stones[i]:
                    stones.insert(i,x)
                    return None
            
            stones.append(x)
        stones.sort()
        print(stones)
        while len(stones)>1:
            a=stones.pop()
            b=stones.pop()
            x=a-b
            if x!=0:
                insert_to_list(stones,x)
            print(stones)
        if stones:
            return stones[0]
        else:
            return 0
