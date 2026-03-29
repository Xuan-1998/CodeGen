===BEGIN CODE===
n, m, T = map(int, input().split())
dp = [0] * (n + 1)
for _ in range(m):
    u, v, t = map(int, input().split())
    for i in range(n, u - 1, -1):
        dp[i] = max(dp[i], dp[u - 1] + 1)

k = dp[n]
print(k)
visited = []
i = n
while i > 0:
    visited.append(i)
    j = next((j for j in range(n) if dp[j] == dp[i] - 1), None)
    i = j
print(*visited[::-1], sep=' ')
