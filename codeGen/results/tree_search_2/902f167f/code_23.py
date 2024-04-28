import sys

n, m = map(int, input().split())

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        else:
            for k in range(1, min(i, j)+1):
                if (i-k) % k == 0 and (j-k) % k == 0:
                    dp[i][j] = min(dp[i][j], dp[(i-k)//k][(j-k)//k] + 1)

print(dp[n][m])
