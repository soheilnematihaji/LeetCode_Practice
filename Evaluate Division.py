"""
This a solution for the problem from
https://leetcode.com/problems/evaluate-division/

Here is the copy of the problem from leetcode:

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

"""

from collections import deque
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        set_sample={1,2,3,4}
        for i,node in enumerate(set_sample):
            print(i)
        map_nodes_neighbor=defaultdict(lambda: defaultdict(float))
        queue_to_visit=deque()
        set_all_visited_node=set()
        for i in range(len(equations)):
            equation=equations[i]
            map_nodes_neighbor[equation[0]][equation[1]]=values[i]
            map_nodes_neighbor[equation[1]][equation[0]]=1/values[i]
        for query in queries:
            node=query[0]
            if not node in set_all_visited_node:
                set_connected_added=set()
                queue_to_visit.append(node)
                while queue_to_visit:
                    node_current=queue_to_visit.popleft()
                    set_all_visited_node.add(node_current)
                    current_neighbor=set(map_nodes_neighbor[node_current].keys())
                    set_new_to_add=current_neighbor.difference(set_connected_added)
                    for node1 in set_new_to_add:
                        set_connected_added.add(node1)
                        for node2 in current_neighbor:
                            if node1!=node_current and node2!=node_current:
                                if node1 not in set_all_visited_node:
                                    queue_to_visit.append(node1)
                                if node2 not in set_all_visited_node:
                                    queue_to_visit.append(node2)
                                a=map_nodes_neighbor[node_current][node2]
                                b=map_nodes_neighbor[node_current][node1]
                                map_nodes_neighbor[node1][node2]=a/b
                                map_nodes_neighbor[node2][node1]=b/a
        outPut=[]
        for query in queries:
            if (map_nodes_neighbor.get(query[0]).get(query[1])):
                outPut.append(map_nodes_neighbor[query[0]][query[1]])
            else:
                outPut.append(-1.0)
        return outPut
                            
                            
                    
