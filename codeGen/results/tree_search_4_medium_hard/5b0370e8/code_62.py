def count_and_xor(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (1 << k) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for y in range(1 << k):
            if i == 1:
                dp[i][y] = sum((x & y) != 0 for x in range(2**k))
            else:
                dp[i][y] = dp[i-1][y]
                for x in range(2**k):
                    ny = (y | (x & y)) & ((2**k)-1)
                    if x & y == 0:
                        z = ny
                    else:
                        z = ny ^ (2**k-1)
                    dp[i][y] += (dp[i-1][ny] - dp[i-1][z]) % MOD
    
    return sum(dp[n])
