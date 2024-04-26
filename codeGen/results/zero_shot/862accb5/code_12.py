import sys
from collections import defaultdict

# Read input from stdin
n = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]

# Step 1: Construct the graph
graph = defaultdict(list)
for u, v, l in roads:
    graph[u].append((v, l))
    graph[v].append((u, l))

# Helper function for DFS to find the farthest node and its distance
def dfs(node, parent):
    farthest_distance = 0
    farthest_node = node
    for neighbor, length in graph[node]:
        if neighbor != parent:
            distance, farthest = dfs(neighbor, node)
            if farthest_distance < distance + length:
                farthest_distance = distance + length
                farthest_node = farthest
    return farthest_distance, farthest_node

# Step 2: Find the longest path in the graph using DFS twice
_, farthest_node = dfs(1, -1)  # Find the farthest node from node 1
longest_distance, _ = dfs(farthest_node, -1)  # Find the longest path from the farthest node

# Step 3: Find the road to remove by checking the longest path again
def find_road_to_remove(node, parent, target_distance):
    for neighbor, length in graph[node]:
        if neighbor != parent:
            distance, _ = dfs(neighbor, node)
            if distance + length == target_distance:
                return length
            road_length = find_road_to_remove(neighbor, node, target_distance - length)
            if road_length is not None:
                return road_length
    return None

# Using the total length of the longest path, we find the longest road to remove
road_length_to_remove = find_road_to_remove(farthest_node, -1, longest_distance)

# Step 4: Calculate the total inconvenience after removing the chosen road
total_inconvenience = sum(l for _, _, l in roads) - road_length_to_remove

# Output the result to stdout
print(total_inconvenience)
