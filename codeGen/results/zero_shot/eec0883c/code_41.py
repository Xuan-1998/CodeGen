import sys
from collections import deque

n = int(sys.stdin.readline())
gases = list(map(int, sys.stdin.readline().split()))
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]

graph = {i: [] for i in range(1, n)}
for u, v, c in roads:
    graph[u].append((v, c))
    graph[v].append((u, c))

def bfs(graph, start, end):
    queue = deque([(start, gases[start - 1])])
    visited = set([start])
    while queue:
        node, gas = queue.popleft()
        if node == end:
            return gas
        for neighbor, cost in graph[node]:
            if neighbor not in visited and gas >= cost:
                visited.add(neighbor)
                queue.append((neighbor, gas - cost))
    return 0

max_gas = 0
for i in range(1, n):
    max_gas = max(max_gas, bfs(graph, 1, i) + gases[i - 1])
print(max_gas)
