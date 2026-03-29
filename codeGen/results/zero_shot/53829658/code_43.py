import sys
from collections import deque

# Step 1: Read input
n = int(input())
roads = []
for _ in range(n-1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

# Step 2: Build a tree data structure to represent the directed tree
tree = {}
for road in roads:
    si, ti = road
    if si not in tree:
        tree[si] = []
    if ti not in tree:
        tree[ti] = []
    tree[si].append(ti)

# Step 3: Find the center of the tree
def find_center(tree):
    max_degree = 0
    center = None
    for node in tree:
        degree = len(tree[node])
        if degree > max_degree:
            max_degree = degree
            center = node
    return center

center = find_center(tree)

# Step 4: Calculate the minimum number of edges to be reversed
def calculate_min_edges_to_reverse(center, tree):
    min_edges = float('inf')
    for node in tree:
        if node != center:
            distance = len(tree) - len(bfs(tree, node))
            min_edges = min(min_edges, distance)
    return min_edges

min_edges = calculate_min_edges_to_reverse(center, tree)

# Step 5: Print the result
print(min_edges)
print(center)
