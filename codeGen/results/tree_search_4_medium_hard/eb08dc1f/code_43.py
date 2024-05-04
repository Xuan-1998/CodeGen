def count_blocks(n):
    mod = 998244353
    dp = [[0] * (n + 1) for _ in range(11)]
    
    for i in range(1, 10):
        dp[i][0] = 1
    
    for l in range(1, n + 1):
        for k in range(1, 10):
            if l > 1:
                dp[k][l] = (dp[k][l - 1] + dp[k][l]) % mod
            else:
                dp[k][l] = 1
    
    return sum(dp[i][n] for i in range(1, 11)) % mod

n = int(input())
print(count_blocks(n))
