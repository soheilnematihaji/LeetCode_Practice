"""
This a solution for the problem from
https://leetcode.com/problems/course-schedule/

Here is the copy of the problem from leetcode:

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


"""
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_v_u=defaultdict(set)
        for [u,v] in prerequisites:
            map_v_u[u].add(v)
        total_visited=set()
        que=deque()
        visited_node=set()
        path=[0]*numCourses
        def dfs(node,map_v_u,path):
            for u in map_v_u[node]:
                if u not in path and u not in visited_node:
                    trackadd=False
                    if u not in visited_node:
                        path.add(u)
                        trackadd=True
                    if not dfs(u,map_v_u,path):
                        return False
                    if trackadd:
                        path.remove(u)
                elif u not in visited_node:
                    return False
            visited_node.add(node)
            return True
            
        for i in range(numCourses):
            if i not in visited_node:
                if not dfs(i,map_v_u,{i}):
                    return False
        return True
