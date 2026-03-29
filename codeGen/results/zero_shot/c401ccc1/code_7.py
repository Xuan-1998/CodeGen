# Let's start by breaking down the problem into smaller subproblems
# The key insight here is that if u & v = v, then there must be an edge from u to v in the graph
# So, we can iterate over all possible pairs of vertices and check if the bitwise AND operation equals the second vertex
# If it does, then we add an edge between the two vertices

import sys

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def has_path(self, u, v):
        # Use BFS or DFS to check if a path exists from u to v
        pass

# Create an instance of the graph class
graph = Graph()

q = int(input())  # Read the number of queries

for _ in range(q):
    u, v = map(int, input().split())  # Read a query pair (u, v)
    if u & v == v:
        graph.add_edge(u, v)  # Add an edge to the graph if necessary
