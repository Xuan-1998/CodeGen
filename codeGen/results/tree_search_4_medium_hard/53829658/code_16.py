from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for i in range(1, n):
    s, t = map(int, input().split())
    graph[s-1].append(t-1)
    # Add the reverse edge as well to simplify the DP
    graph[t-1].append(s-1)

def bfs(v, target, rev_edges):
    visited = [False] * n
    queue = deque([(v, 0)])  # (city, reversed edges)
    while queue:
        city, rev = queue.popleft()
        if city == target:
            return rev
        for neighbor in graph[city]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, rev + 1))
    return -1

dp = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dp[i][j] = bfs(i, j, 0) != -1
resversed_edges = float('inf')
capital_cities = []
for i in range(1, n):
    rev_edges = sum(dp[0][j] for j in range(1, n))
    if rev_edges < reversed_edges:
        reversed_edges = rev_edges
        capital_cities = [i]
    elif rev_edges == reversed_edges:
        capital_cities.append(i)
print(reversed_edges)
for city in capital_cities:
    print(city)
