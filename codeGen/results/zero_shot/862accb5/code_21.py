import sys
from collections import defaultdict

# Read input from stdin
n = int(input())
tree = defaultdict(list)
for _ in range(n):
    u, v, l = map(int, sys.stdin.readline().strip().split())
    tree[u].append((v, l))
    tree[v].append((u, l))

# Helper function to find the farthest node and the total length of the path
def dfs(node, parent):
    farthest_node, max_length = node, 0
    for neighbor, length in tree[node]:
        if neighbor != parent:
            next_node, next_length = dfs(neighbor, node)
            if next_length + length > max_length:
                farthest_node, max_length = next_node, next_length + length
    return farthest_node, max_length

# Step 1: Find the farthest node from an arbitrary start (node 1)
farthest_node, _ = dfs(1, -1)

# Step 2: Find the farthest node from the farthest node found in step 1
# This will give us one end of the diameter of the tree
farthest_node_from_farthest, diameter = dfs(farthest_node, -1)

# Output the diameter which is the minimum inconvenience after removing a road
print(diameter)
