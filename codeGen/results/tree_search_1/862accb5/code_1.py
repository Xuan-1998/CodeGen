from collections import defaultdict
import sys

# Function to add an edge to the undirected graph
def add_edge(adj, u, v, l):
    adj[u].append((v, l))
    adj[v].append((u, l))

# Function to find the farthest node and its distance from a given node using DFS
def dfs(adj, node, n, visited, distances):
    visited[node] = True
    farthest_node = node
    max_distance = 0
    for neighbor, length in adj[node]:
        if not visited[neighbor]:
            distances[neighbor] = distances[node] + length
            next_node, distance = dfs(adj, neighbor, n, visited, distances)
            if distance > max_distance:
                farthest_node = next_node
                max_distance = distance
    return farthest_node, max_distance

# Function to find the diameter of the tree
def find_diameter(adj, n):
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    # Find the farthest node from node 1 (arbitrary choice)
    farthest_node, _ = dfs(adj, 1, n, visited, distances)
    # Reset visited array and distances for the second DFS
    visited = [False] * (n + 1)
    distances = [0] * (n + 1)
    # Find the farthest node from the farthest node found in the first DFS
    farthest_node, max_distance = dfs(adj, farthest_node, n, visited, distances)
    return max_distance

# Read the number of towns (and roads)
n = int(sys.stdin.readline().strip())

# Initialize adjacency list for the tree
adj = defaultdict(list)

# Read the roads and construct the tree
for _ in range(n):
    u, v, l = map(int, sys.stdin.readline().strip().split())
    add_edge(adj, u, v, l)

# Find the diameter of the tree
diameter = find_diameter(adj, n)

# Print the minimum possible inconvenience
print(diameter)
