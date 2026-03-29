import sys

n = int(input())
visited = [False] * (n + 1)
dp = [-1] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    visited[v] = True

for i in range(2, n + 1):
    if not visited[i]:
        continue
    for j in range(1, i):
        if visited[j]:
            dp[i] = min(dp[i], dp[j] + 1)

min_reversals = max(dp)
capital_cities = [i for i in range(2, n + 1) if dp[i] == min_reversals]

print(min_reversals)
print(*capital_cities, sep='\n')
