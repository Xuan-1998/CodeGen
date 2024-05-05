import sys

n, m, T = map(int, input().split())
dp = [[0] * (T + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    for t in range(T, w - 1, -1):
        dp[v][t] = max(dp[v][t], dp[u][t - w] + 1)

print(max(dp[n]))
ans = []
for i in range(n):
    if dp[i][T]:
        ans.append(i)
print(*ans, sep=' ')
