from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
p = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(min(p), i):
        if graph[j]:
            dp[i] = min(dp[i], dp[j] + 1)

print(*min(max(dp), dp[-1]), sep=' ')
