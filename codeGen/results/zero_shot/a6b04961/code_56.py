import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

graph = {i: [] for i in range(n)}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

trees = []
for node in range(n):
    if node not in [node for tree in trees for node in tree]:
        tree = bfs(graph, node)
        trees.append(tree)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return list(visited)

def max_beauty(trees):
    max_beauty = 0
    for i in range(len(trees)):
        for j in range(i+1, len(trees)):
            tail_length = len(trees[i])
            spine_count = sum(1 for tree in trees[j:] if any(node in tree for node in trees[i]))
            beauty = tail_length * spine_count
            max_beauty = max(max_beauty, beauty)
    return max_beauty

print(max_beauty(trees))
