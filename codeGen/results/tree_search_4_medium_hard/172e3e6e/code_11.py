def good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = 1
            else:
                for k in range(j-1, -1, -1):
                    if a[i] % k == 0 and (k > 1 or j <= 0):
                        dp[i][j] = (dp[i][j] + dp[i-1][k-1]) % MOD
            dp[i][j] += dp[i-1][j]
            dp[i][j] %= MOD
    
    return sum(dp[n]) % MOD

print(good_subsequences())
