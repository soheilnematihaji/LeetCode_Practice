
"""
This is my Accepted code for
https://leetcode.com/problems/shortest-path-with-alternating-colors/

Here is the copy of the question :

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

"""
from collections import deque
from collections import defaultdict
class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        red_neighbors=defaultdict(list)
        blue_neighbors=defaultdict(list)
        for edge in red_edges:
            red_neighbors[edge[0]].append(edge[1])
        for edge in blue_edges:
            blue_neighbors[edge[0]].append(edge[1])
        shortest_answer=[-1 for i in range(n)]
        visited_node_with_color=set()
        neighbor_queue_with_color=deque()
        neighbor_queue_with_color.append((0,0,0))
        neighbor_queue_with_color.append((0,1,0))
        while neighbor_queue_with_color:
            node_color_shortest=neighbor_queue_with_color.popleft()
            visited_node_with_color.add((node_color_shortest[0],node_color_shortest[1]))
            if shortest_answer[node_color_shortest[0]]==-1 or shortest_answer[node_color_shortest[0]]>node_color_shortest[2]:
                shortest_answer[node_color_shortest[0]]=node_color_shortest[2]
            if node_color_shortest[1]==0:
                for node_red in red_neighbors[node_color_shortest[0]]:
                    if (node_red,1) not in visited_node_with_color:
                        neighbor_queue_with_color.append((node_red,1,node_color_shortest[2]+1))
            else:
                for node_blue in blue_neighbors[node_color_shortest[0]]:
                    if (node_blue,0) not in visited_node_with_color:
                        neighbor_queue_with_color.append((node_blue,0,node_color_shortest[2]+1))
        return  shortest_answer
