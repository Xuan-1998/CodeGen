import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    parent[neighbor] = node
    return parent

parent_graph = bfs(graph, 1)

def find_path(parent_graph, start):
    path = [start]
    while parent_graph[start] is not None:
        start = parent_graph[start]
        path.insert(0, start)
    return path

max_beauty = 0
for i in range(n-1):
    path = find_path(parent_graph, i+1)
    beauty = len(path) * (m - sum(1 for j in path if j < n-1))
    max_beauty = max(max_beauty, beauty)

print(max_beauty)
