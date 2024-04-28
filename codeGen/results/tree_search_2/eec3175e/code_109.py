dp = [[False for _ in range(m+1)] for _ in range(n+1)]
set_sum = sum(set)
for i in range(1, n+1):
    for j in range(1, m+1):
        if set[i-1] <= j:
            dp[i][j] = (dp[i-1][j-set[i-1]] or dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(1 if any(dp[-1][i]) for i in range(m+1))
