import sys
from collections import defaultdict

n, m, T = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = set()
dp = [0] * (n + 1)

for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    graph[u].append((v, t))

from collections import deque

q = deque([1])
while q:
    u = q.popleft()
    if dp[u] > 0:
        continue
    for v, t in graph[u]:
        if t <= T - dp[v]:
            dp[u] = max(dp[u], dp[v] + 1)
            q.append(u)

k = max(dp) if any(dp) else 0

print(k)

visited = set()
q = deque([n])
while q:
    u = q.popleft()
    if dp[u] == k - 1:
        print(*range(1, u + 1), sep='\n')
        break
    visited.add(u)
    for v, t in graph[u]:
        if t <= T - dp[v] and v not in visited:
            q.append(v)
