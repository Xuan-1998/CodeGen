import sys
from collections import defaultdict

n, m, T = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    graph[u].append((v, t))

visited = [False] * (n + 1)
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j, w in graph[i]:
        if dp[j - 1] + w <= T and not visited[j]:
            dp[j] = min(dp[j], dp[j - 1] + w)
            visited[j] = True

k = sum(1 for i in range(n + 1) if dp[i])
print(k)

path = []
i = n
while i > 0:
    path.append(i)
    for j, w in graph[i]:
        if dp[j - 1] + w == dp[i]:
            i = j
            break
path.reverse()
print(*path[1:])
