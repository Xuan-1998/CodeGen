import sys
from collections import defaultdict

# Function to add an edge to an undirected graph
def add_edge(graph, u, v, l):
    graph[u].append((v, l))
    graph[v].append((u, l))

# Depth-First Search to find the longest path in the graph
def dfs(graph, node, visited, lengths, path_length):
    visited[node] = True
    lengths[node] = path_length
    max_length = path_length
    max_node = node
    for neighbor, length in graph[node]:
        if not visited[neighbor]:
            new_length, new_node = dfs(graph, neighbor, visited, lengths, path_length + length)
            if new_length > max_length:
                max_length = new_length
                max_node = new_node
    return max_length, max_node

# Function to find the diameter of the tree (longest path)
def find_diameter(graph, n):
    visited = [False] * (n + 1)
    lengths = [0] * (n + 1)
    # Find the farthest node from any node (let's start with node 1)
    _, farthest_node = dfs(graph, 1, visited, lengths, 0)
    # Find the farthest node from the farthest node found in the previous step
    visited = [False] * (n + 1)
    lengths = [0] * (n + 1)
    max_length, _ = dfs(graph, farthest_node, visited, lengths, 0)
    return max_length

# Main function to solve the problem
def solve(n, roads):
    graph = defaultdict(list)
    for u, v, l in roads:
        add_edge(graph, u, v, l)
    
    # Find the diameter of the tree
    diameter = find_diameter(graph, n)
    
    # The result is the diameter of the tree, which is the minimum possible inconvenience
    return diameter

# Read input
n = int(input().strip())
roads = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Solve the problem and output the result
print(solve(n, roads))
