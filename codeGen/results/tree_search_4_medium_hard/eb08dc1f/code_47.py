def count_blocks(n):
    MOD = 998244353
    dp = {(i, j): 0 for i in range(10**n) for j in range(n+1)}
    dp[(0, 0)] = 1

    for i in range(10**n):
        for k in range(min(i+1, n)):
            if (i-1, k) in dp:
                dp[(i, k)] += dp[(i-1, k)]
            if (i-1, k+1) in dp and i % 10**(k+1) == 0:
                dp[(i, k+1)] = dp.get((i-1, k), 0)
    return sum(dp[(10**n-1, j)] for j in range(n)) % MOD
