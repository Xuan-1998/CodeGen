def solve():
    n = int(input())
    
    MOD = 998244353
    
    dp = [[False] * (n + 1) for _ in range(n + 2)]
    
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for k in range(1, min(i, n) + 1):
            if k == 0:
                dp[i][k] = True
            elif k == 1:
                dp[i][k] = dp[i - 1][k]
            else:
                dp[i][k] = (dp[i - 1][k - 1] or (dp[i - 1][k - 2] and i % 2 != 0)) * (1 / 2) + (dp[i - 1][k] or (dp[i - 1][k - 1] and i % 2 != 0)) * (1 - 1/2)
                dp[i][k] %= MOD
    
    return int(dp[n][n]) if dp[n][n] else 0

print(solve())
