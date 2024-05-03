import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    species, x = map(int, input().split())
    for s in range(m, 0, -1):
        if species == s:
            dp[i][s] = min(dp[i-1][s], dp[i-1][species-1] + abs(x - dp[i-1][s-1][i-1]))
            break

print(min(dp[n]))

