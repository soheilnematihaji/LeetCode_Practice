"""
This a solution for the problem from
https://leetcode.com/problems/frog-jump/

Here is the copy of the problem from leetcode:

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

"""
from collections import deque
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or stones[0]!=0 or stones[1]!=1:
            return False
        if len(stones)<3:
            return True
        can_reach=set(stones)
        map_to_visit=defaultdict(set)
        map_to_visit[1]={1}
        to_visit=stones[-1]
        i=1
        while(map_to_visit):
            current=i
            if current==to_visit and map_to_visit[current] :
                return True
            if current in can_reach:
                for key in map_to_visit[current]:
                    if current+key<=to_visit+1:
                        map_to_visit[current+key].add(key)
                        map_to_visit[current+key+1].add(key+1)
                        if key-1>0:
                            map_to_visit[current+key-1].add(key-1)
            if current in map_to_visit:
                map_to_visit.pop(current)
            i+=1
        return False
