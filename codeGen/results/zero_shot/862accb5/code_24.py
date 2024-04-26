import sys
from collections import defaultdict

# Step 1: Model the Kingdom as a Graph
def create_graph(n, edges):
    graph = defaultdict(list)
    for u, v, l in edges:
        graph[u].append((v, l))
        graph[v].append((u, l))
    return graph

# Step 2: Find a Cycle using DFS
def find_cycle(graph, n):
    parent = [-1] * (n + 1)
    stack = [(1, -1)]
    while stack:
        node, par = stack.pop()
        for neighbor, _ in graph[node]:
            if neighbor == par:
                continue
            if parent[neighbor] == -1:
                parent[neighbor] = node
                stack.append((neighbor, node))
            else:
                # Cycle found, backtrack to get the cycle path
                cycle = []
                while node != neighbor:
                    cycle.append(node)
                    node = parent[node]
                cycle.append(neighbor)
                return cycle
    return []

# Step 3: Calculate the sizes of subtrees
def calculate_subtree_sizes(graph, n, start, exclude):
    size = [0] * (n + 1)
    def dfs(node, parent):
        size[node] = 1
        for neighbor, _ in graph[node]:
            if neighbor != parent and (node, neighbor) != exclude and (neighbor, node) != exclude:
                size[node] += dfs(neighbor, node)
        return size[node]
    dfs(start, -1)
    return size

# Step 4: Identify the Road to Remove and Calculate the Result
def minimize_inconvenience(graph, n, cycle):
    min_inconvenience = float('inf')
    subtree_sizes = calculate_subtree_sizes(graph, n, cycle[0], None)
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i + 1]
        size_u = subtree_sizes[u]
        size_v = subtree_sizes[v]
        # Calculate the size of the two subtrees if the edge (u, v) is removed
        if size_u > size_v:
            size_u, size_v = size_v, size_u
        inconvenience = size_u * (n - size_u)
        min_inconvenience = min(min_inconvenience, inconvenience)
    return min_inconvenience

# Read input
n = int(input().strip())
edges = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Solve the problem
graph = create_graph(n, edges)
cycle = find_cycle(graph, n)
result = minimize_inconvenience(graph, n, cycle)
print(result)
