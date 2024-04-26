import sys
from collections import defaultdict

# Read the number of towns and roads
n = int(input())

# Initialize the graph
graph = defaultdict(list)

# Read the roads and their lengths, and build the graph
total_length = 0
for _ in range(n):
    u, v, l = map(int, input().split())
    graph[u].append((v, l))
    graph[v].append((u, l))
    total_length += l

# DFS to find the farthest node and its distance from the start node
def dfs(node, parent):
    farthest_node = node
    max_distance = 0
    for neighbor, length in graph[node]:
        if neighbor != parent:
            next_node, distance = dfs(neighbor, node)
            if distance + length > max_distance:
                max_distance = distance + length
                farthest_node = next_node
    return farthest_node, max_distance

# Find one endpoint of the diameter
farthest_node, _ = dfs(1, -1)

# Find the other endpoint of the diameter and the diameter length
_, diameter_length = dfs(farthest_node, -1)

# Calculate the minimum possible inconvenience
min_inconvenience = total_length - diameter_length

# Output the result
print(min_inconvenience)
