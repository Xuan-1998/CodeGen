dp = [[0] * 501 for _ in range(501)]
for i in range(1, 501):
    for j in range(1, 501):
        if S[i-1] != T[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
        else:
            dp[i][j] = dp[i-1][j-1] + 1

ans = float('inf')
for i in range(501):
    ans = min(ans, dp[500-i][0])
print(-1 if ans == float('inf') else 500 - ans)
