def goodSequences(n, k):
    MOD = 1000000007
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, min(i, k) + 1):
            if i % j == 0:
                dp[i][j] = (dp[i][j-1] + 1) % MOD
            else:
                dp[i][j] = dp[i][j-1]
                
    return dp[n][k]

n, k = map(int, input().split())
print(goodSequences(n, k))
