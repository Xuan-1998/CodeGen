import sys
from collections import defaultdict

# Read input from stdin
n = int(sys.stdin.readline().strip())
roads = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Building the adjacency list for the tree
tree = defaultdict(list)
for u, v, l in roads:
    tree[u].append((v, l))
    tree[v].append((u, l))

# Function to perform DFS and find the farthest node with its distance
def dfs(node, parent):
    farthest_node = (node, 0)  # (node, distance)
    for neighbor, length in tree[node]:
        if neighbor != parent:
            next_node, next_dist = dfs(neighbor, node)
            next_dist += length
            if next_dist > farthest_node[1]:
                farthest_node = (next_node, next_dist)
    return farthest_node

# Find one end of the diameter
farthest_node, _ = dfs(1, -1)
# Find the other end of the diameter and the diameter length
diameter_end, diameter_length = dfs(farthest_node[0], -1)

# Output the minimum inconvenience, which is the diameter length
print(diameter_length)
