import sys
from collections import defaultdict

# Read the number of towns (and roads)
n = int(sys.stdin.readline().strip())

# Initialize the graph as an adjacency list
graph = defaultdict(list)

# Read the roads and build the graph
for _ in range(n):
    u, v, l = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

# Function to perform DFS and calculate subtree sizes
def dfs(node, parent):
    size = 1
    for neighbor, length in graph[node]:
        if neighbor != parent:
            subtree_size = dfs(neighbor, node)
            subtree_sizes[neighbor] = subtree_size
            size += subtree_size
    return size

# Initialize the array to store subtree sizes and visited nodes
subtree_sizes = [0] * (n + 1)

# Perform DFS starting from node 1 (arbitrarily chosen root)
dfs(1, -1)

# Calculate the minimum inconvenience
min_inconvenience = float('inf')

for node in range(1, n + 1):
    for neighbor, length in graph[node]:
        if subtree_sizes[neighbor] > 0:
            # Calculate the sizes of the two subtrees
            size_one = subtree_sizes[neighbor]
            size_two = n - size_one
            # Calculate inconvenience
            inconvenience = size_one * size_two * length
            # Update minimum inconvenience
            min_inconvenience = min(min_inconvenience, inconvenience)

# Print the minimum inconvenience
print(min_inconvenience)
