import sys

n, m, T = map(int, input().split())
dp = [0] * (n + 1)
visited = set()
edges = []

for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

for i in range(1, n + 1):
    for edge in edges:
        if edge[0] == i and edge[2] <= T - dp[i]:
            visited.add(edge[1])
            dp[edge[1]] = min(dp[edge[1]], dp[i] + edge[2])

k = max(dp)
path = [i for i in range(1, n) if dp[i] == k]
print(k)
print(*path)
