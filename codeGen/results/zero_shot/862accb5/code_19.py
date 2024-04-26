import sys
from collections import defaultdict

# Step 1: Create a graph representation using adjacency list
def create_graph(n, edges):
    graph = defaultdict(list)
    for u, v, l in edges:
        graph[u].append((v, l))
        graph[v].append((u, l))
    return graph

# Step 2: Find a spanning tree using DFS
def dfs(graph, start, visited, parent):
    visited[start] = True
    for neighbor, weight in graph[start]:
        if not visited[neighbor]:
            parent[neighbor] = (start, weight)
            dfs(graph, neighbor, visited, parent)

# Step 3: Identify the longest edge in the cycle
def find_longest_edge_in_cycle(edges, parent):
    longest_edge = (0, 0, 0)  # (u, v, weight)
    for u, v, weight in edges:
        if parent[u][0] != v and parent[v][0] != u:  # This edge forms a cycle
            if weight > longest_edge[2]:
                longest_edge = (u, v, weight)
    return longest_edge

# Step 4: Calculate the inconvenience
def calculate_inconvenience(edges, longest_edge):
    total_weight = sum(weight for _, _, weight in edges)
    return total_weight - longest_edge[2]

# Read input
n = int(input().strip())
edges = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Create the graph
graph = create_graph(n, edges)

# Find the spanning tree
visited = [False] * (n + 1)
parent = {}
dfs(graph, 1, visited, parent)

# Identify the longest edge in the cycle
longest_edge = find_longest_edge_in_cycle(edges, parent)

# Calculate the minimum inconvenience
min_inconvenience = calculate_inconvenience(edges, longest_edge)
print(min_inconvenience)
