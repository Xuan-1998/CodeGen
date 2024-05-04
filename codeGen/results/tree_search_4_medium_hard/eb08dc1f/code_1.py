def countBlocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(10)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i + 1, 10)):
            if i < j:
                continue
            if i == j:
                dp[0][i] = 1
            else:
                for k in range(j - 1, -1, -1):
                    dp[j][i] += (dp[k][j - k]) % MOD
    
    return ' '.join(map(str, [sum(dp[i]) % MOD for i in range(n + 1)]))
