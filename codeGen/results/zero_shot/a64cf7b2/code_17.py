import sys

n, m, T = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = 1
    for j in range(i-1, -1, -1):
        if sum(t for _, t in graph[j]) <= T:
            dp[i] = max(dp[i], dp[j] + 1)

k = max(range(n+1), key=lambda i: dp[i])
print(k)
for i in range(k, 0, -1):
    print(i, end=' ')
