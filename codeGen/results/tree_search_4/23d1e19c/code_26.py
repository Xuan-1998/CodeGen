import sys

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
p = list(map(int, input().split()))

dp = {i: 0 for i in range(1, n + 1)}

for u, v in edges:
    if p[0] <= u < v <= p[-1]:
        dp[v] = max(dp.get(v, 0), dp[u] + 1)
    else:
        dp[v] = max(dp.get(v, 0), 1)

print(min(dp.values()), max(dp.values()))
