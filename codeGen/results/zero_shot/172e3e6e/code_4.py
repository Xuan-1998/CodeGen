def good_subsequences(n):
    MOD = 10**9 + 7
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(2, n+1):
        for j in range(i+1):
            if i % j == 0:
                if j == 1 or (j > 1 and a[j-1] % j == 0):
                    dp[i][j] = (dp[i-1][j-1] + (j-1)!)/((j-2)!)
                else:
                    dp[i][j] = 0
            if i > 1:
                for k in range(1, j+1):
                    if k % j == 0:
                        dp[i][j] += dp[k-1][k]
    return sum(dp[n])
