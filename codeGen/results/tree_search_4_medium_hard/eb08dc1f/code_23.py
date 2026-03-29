def count_blocks(n):
    MOD = 998244353
    dp = {}
    
    # Initialize base cases
    for i in range(n+1):
        dp[(i, 0)] = 1
    
    for k in range(1, n+1):
        for i in range(k):
            if (i, k-1) not in dp:
                dp[(i, k)] = 0
            else:
                dp[(i, k)] = (dp[(i, k-1)] * (10 - int('9' * k)) % MOD + dp.get((i+1, k), 0)) % MOD
    
    return ' '.join(str(dp.get((i, k), 0)) for i in range(n) for k in range(1, n+1))
