def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(10)]
    
    for k in range(1, n + 1):
        for i in range(10):
            if k == 1:
                dp[i][k] = 1
            else:
                dp[i][k] = sum(dp[j][k-1] for j in range(i)) % MOD
    
    return ' '.join(str(sum(dp[i])) for i in range(n + 1))
