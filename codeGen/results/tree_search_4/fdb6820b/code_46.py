def count_ways(m, n, nums):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(n, -1, -1):
            if j == 0:
                dp[i][j] = 1
            else:
                for k in range(i):
                    dp[i][j] = (dp[i][j] + dp[k][j-nums[k]]) % MOD
    
    return dp[m][n]
