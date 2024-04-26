import sys
from collections import defaultdict

# Read the number of towns and roads
n = int(sys.stdin.readline().strip())
graph = defaultdict(list)

# Read the roads and build the graph
for _ in range(n):
    u, v, l = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

# Function to perform DFS and return the furthest node and its distance
def dfs(node, parent):
    furthest_node = node
    max_distance = 0
    for neighbor, length in graph[node]:
        if neighbor != parent:
            next_node, distance = dfs(neighbor, node)
            if distance + length > max_distance:
                max_distance = distance + length
                furthest_node = next_node
    return furthest_node, max_distance

# Step 1: Find one end of the diameter
furthest_node, _ = dfs(1, -1)

# Step 2: Find the other end of the diameter and the diameter length
diameter_end, diameter_length = dfs(furthest_node, -1)

# Function to find the longest path from a node, excluding the parent path
def find_longest_path(node, parent):
    max_length = 0
    for neighbor, length in graph[node]:
        if neighbor != parent:
            max_length = max(max_length, find_longest_path(neighbor, node) + length)
    return max_length

# Find the minimum inconvenience by considering each edge on the diameter path
min_inconvenience = diameter_length
node = diameter_end
parent = -1
while node != furthest_node:
    for neighbor, length in graph[node]:
        if neighbor == parent:
            continue
        if diameter_end in dfs(neighbor, node)[0]:
            # This edge is part of the diameter
            longest_path_1 = find_longest_path(node, neighbor)
            longest_path_2 = find_longest_path(neighbor, node)
            inconvenience = longest_path_1 + longest_path_2
            min_inconvenience = min(min_inconvenience, inconvenience)
            parent = node
            node = neighbor
            break

# Output the minimum inconvenience
print(min_inconvenience)
