import sys
from collections import defaultdict

def dfs(graph, node, parent, depth, max_depth_info):
    if depth > max_depth_info[0]:
        max_depth_info[0] = depth
        max_depth_info[1] = node
    for neighbor, weight in graph[node]:
        if neighbor != parent:
            dfs(graph, neighbor, node, depth + weight, max_depth_info)

def find_diameter(graph, n):
    max_depth_info = [-1, -1]  # [max_depth, max_depth_node]
    dfs(graph, 1, -1, 0, max_depth_info)  # Arbitrary start at node 1

    # Second DFS to find the diameter and the critical edge
    start_node = max_depth_info[1]
    max_depth_info = [-1, -1]
    dfs(graph, start_node, -1, 0, max_depth_info)

    return max_depth_info[0]

# Read input from stdin
n = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(n):
    u, v, l = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

# Find the diameter of the tree
diameter = find_diameter(graph, n)
print(diameter)
