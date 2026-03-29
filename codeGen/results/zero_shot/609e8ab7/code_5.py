# Step 1: Read the input
import sys
T = int(input())  # number of test cases
for _ in range(T):
    n = int(input())  # number of vertices
    parent = list(map(int, input().split()))  # parent array
    ranges = []
    for i in range(n):
        l, r = map(int, sys.stdin.readline().split())
        ranges.append((l, r))
    
# Step 2: Build the tree structure
tree = {}
for i in range(1, n):
    p = parent[i]
    if p not in tree:
        tree[p] = []
    tree[p].append(i)
    
# Step 3: Calculate the minimum number of operations for each vertex
for l, r in ranges:
    visited = set()
    def dfs(v):
        visited.add(v)
        while v != 0:
            parent_value = l if r - l <= max(tree.get(v, [])) else r
            if not any(visited.intersection(child) for child in tree.get(v, [])):
                yield v
            v = parent[v]
    for v in dfs(n-1):
        yield len(list(dfs(v)))
