import sys
from collections import defaultdict

# Function to perform DFS and find the farthest node from the starting node
def dfs(graph, node, visited, distances):
    visited[node] = True
    for neighbor, length in graph[node]:
        if not visited[neighbor]:
            distances[neighbor] = distances[node] + length
            dfs(graph, neighbor, visited, distances)

# Read the number of towns (and roads)
n = int(sys.stdin.readline())

# Initialize the graph
graph = defaultdict(list)

# Read the roads and construct the graph
for _ in range(n):
    u, v, l = map(int, sys.stdin.readline().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

# Step 1: Find the farthest node from an arbitrary node (node 1)
visited = [False] * (n + 1)
distances = [0] * (n + 1)
dfs(graph, 1, visited, distances)

# Find the node with the maximum distance from node 1
farthest_node = distances.index(max(distances))

# Step 2: Find the farthest node from the farthest node found in step 1
visited = [False] * (n + 1)
distances = [0] * (n + 1)
dfs(graph, farthest_node, visited, distances)

# The diameter of the tree is the maximum distance found in step 2
diameter = max(distances)

# Output the minimum possible inconvenience, which is the diameter of the tree
print(diameter)
