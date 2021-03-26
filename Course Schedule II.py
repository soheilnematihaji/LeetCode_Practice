"""
This a solution for the problem from
https://leetcode.com/problems/course-schedule-ii/

Here is the copy of the problem from leetcode:

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map_v_u=defaultdict(set)
        map_revers=defaultdict(set)
        for [u,v] in prerequisites:
            map_v_u[u].add(v)
            map_revers[v].add(u)
            
        def find_way(nodes,map_v_u):
            output=[]
            for i in nodes:
                if i not in map_v_u:
                    output.append(i)
                    for rv in map_revers[i]:
                        map_v_u[rv].remove(i)
                        if not map_v_u[rv]:
                            map_v_u.pop(rv)
            for o in output:
                nodes.remove(o)
            if output:
                output.extend(find_way(nodes,map_v_u))
            else:
                return []
            return output
        
        output1=find_way([i for i in range(numCourses)],map_v_u)
        if len(output1)<numCourses:
            return []
        else:
            return output1
