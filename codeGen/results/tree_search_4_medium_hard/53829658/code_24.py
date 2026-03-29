import sys
from collections import deque

# Read input
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    u, v = map(int, input().split())
    graph[u].append(v)

def bfs(graph, s, visited):
    queue = deque([(s, 0)])  # (city, reversed edges)
    while queue:
        city, rev_edges = queue.popleft()
        if not visited[city]:
            visited[city] = True
            for neighbor in graph[city]:
                if not visited[neighbor]:
                    queue.append((neighbor, rev_edges + 1))

def dfs(graph, s):
    visited = [False] * (n + 1)
    dp = [0] * (n + 1)
    queue = deque([s])
    while queue:
        city = queue.popleft()
        if not visited[city]:
            visited[city] = True
            for neighbor in graph[city]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    dp[neighbor] = min(dp[neighbor], dp[city] + 1)

    return dp

def solve():
    capitals = []
    for i in range(2, n + 1):
        if dfs(graph, i)[i - 1] == 0:
            capitals.append(i)
    
    min_reversed_edges = float('inf')
    for capital in capitals:
        reversed_edges = 0
        visited = [False] * (n + 1)
        for city in range(2, n + 1):
            if not visited[city]:
                queue = deque([(city, 0)])  # (city, reversed edges)
                while queue:
                    c, rev_edges = queue.popleft()
                    if c == capital:
                        break
                    if not visited[c]:
                        visited[c] = True
                        for neighbor in graph[c]:
                            if not visited[neighbor]:
                                queue.append((neighbor, rev_edges + 1))
                reversed_edges += queue[0][1]
        min_reversed_edges = min(min_reversed_edges, reversed_edges)
    
    return min_reversed_edges, ' '.join(map(str, capitals))

print(*solve(), sep='\n')
