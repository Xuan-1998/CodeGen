dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = True
    dp[0][i] = True

for i in range(1, n+1):
    for j in range(1, n+1):
        if p[2*i-1] < p[2*j-1]:
            dp[i][j] = dp[i-1][j]
        elif p[2*i-1] > p[2*j-1]:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = (dp[i-1][j] or dp[i][j-1])

print("YES" if dp[n][n] else "NO")
