import math

n = int(input())
M = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1

ans = 0
for m in M:
    for j in range(1, m):
        dp[m][j] += dp[j][j]
    if m == 1:
        ans = (ans + 1) % (10**9 + 7)
    else:
        ans = (ans + dp[m-1][m-1]) % (10**9 + 7)

print(ans)
