from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
p = list(map(int, input().split()))

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

q = deque([s])
while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if neighbor == p[0]:
            break
        if dp[neighbor] == 0:
            recomputations = 1
        else:
            recomputations = dp[neighbor]
        dp[neighbor] += recomputations

min_recomputations = min(dp)
max_recomputations = max(dp)

print(min_recomputations, max_recomputations)
