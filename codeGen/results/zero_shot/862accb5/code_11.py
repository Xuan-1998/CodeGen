import sys
from collections import defaultdict

# Step 1: Construct the graph
def create_graph(n, edges):
    graph = defaultdict(list)
    for u, v, l in edges:
        graph[u].append((v, l))
        graph[v].append((u, l))
    return graph

# Function to perform a DFS to find the maximum edge in the path from start to end
def dfs(graph, start, end, visited, max_edge):
    visited[start] = True
    if start == end:
        return max_edge
    for neighbor, weight in graph[start]:
        if not visited[neighbor]:
            max_edge = max(max_edge, weight)
            result = dfs(graph, neighbor, end, visited, max_edge)
            if result != -1:
                return result
    return -1

# Step 3: Identify the critical edge
def find_critical_edge(graph, n):
    visited = [False] * (n + 1)
    max_inconvenience = 0
    critical_edge = None
    
    for u in range(1, n + 1):
        for v, l in graph[u]:
            if not visited[v]:
                # Temporarily remove the edge
                graph[u].remove((v, l))
                graph[v].remove((u, l))
                
                # Check the inconvenience caused by removing the edge
                inconvenience = dfs(graph, u, v, [False] * (n + 1), 0)
                
                # Add the edge back
                graph[u].append((v, l))
                graph[v].append((u, l))
                
                # Update the critical edge if necessary
                if inconvenience > max_inconvenience:
                    max_inconvenience = inconvenience
                    critical_edge = (u, v, l)
    
    return critical_edge

# Step 5: Calculate the total inconvenience
def calculate_inconvenience(graph, critical_edge):
    u, v, l = critical_edge
    graph[u].remove((v, l))
    graph[v].remove((u, l))
    total_inconvenience = sum(weight for edges in graph.values() for _, weight in edges) // 2
    return total_inconvenience

# Read the input
n = int(input().strip())
edges = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Create the graph and find the critical edge
graph = create_graph(n, edges)
critical_edge = find_critical_edge(graph, n)

# Calculate and print the total inconvenience
total_inconvenience = calculate_inconvenience(graph, critical_edge)
print(total_inconvenience)
