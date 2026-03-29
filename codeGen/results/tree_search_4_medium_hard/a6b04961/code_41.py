import sys
from collections import defaultdict

# Read input
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * (n + 1)  # dp[i]: maximum beauty achievable with i vertices
tail = [0] * (n + 1)  # tail[i]: last vertex added to the tail at step i

for i in range(2, n + 1):
    for j in range(i):
        if graph[j][0] == i or graph[j][1] == i:
            break
    else:
        dp[i] = max(dp[i], dp[j - 1] + (i - j))
        tail[i] = j

print(max(0, max((dp[i] for i in range(n)), default=0)))
