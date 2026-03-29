import sys
from collections import defaultdict

def find_max_beauty():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))

    visited = set()
    tail = []
    spines = 0

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(vertex):
        nonlocal tail, spines
        if vertex not in visited:
            visited.add(vertex)
            if len(tail) == 0 or vertex > tail[-1]:
                tail.append(vertex)
                for neighbor in graph[vertex]:
                    if neighbor not in visited and neighbor not in tail:
                        spines += 1
            dfs(neighbor)

    for start in range(n):
        if start not in visited:
            visited.add(start)
            tail = [start]
            spines = 0
            dfs(start)
            # Update the maximum beauty if necessary

    return len(tail) * spines

print(find_max_beauty())
