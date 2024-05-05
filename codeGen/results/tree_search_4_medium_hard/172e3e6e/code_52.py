def goodSequences(a):
    n = len(a)
    MOD = 10**9 + 7
    
    dp = [(0, 1) for _ in range(n)]
    
    for i in range(1, n):
        prev_i, prev_odd_or_even = dp[i-1]
        
        if a[i] % i == 0:
            odd_or_even = (prev_i + 1) % MOD
        else:
            odd_or_even = 2 * prev_odd_or_even % MOD
        
        dp[i] = (odd_or_even, MOD - odd_or_even)
    
    return dp[-1][0]
