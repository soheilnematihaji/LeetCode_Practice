"""
This a solution for the problem from
https://leetcode.com/problems/last-stone-weight-ii/

Here is the copy of the problem from leetcode:

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

"""
from collections import deque
import random
import copy
class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        def insert_to_list(stones,x):
            stones.append(x)
        min_0=100
        stones_temp=stones
        for i in range(100):
            random.shuffle(stones_temp)
            stones=copy.copy(stones_temp)
            print(stones)
            while stones and len(stones)>1:
                a=stones.pop()
                b=stones.pop()
                x=abs(a-b)
                if x!=0:
                    insert_to_list(stones,x)
            if stones:
                min_0=min(min_0,stones[0])
            else:
                min_0= 0
        return min_0
