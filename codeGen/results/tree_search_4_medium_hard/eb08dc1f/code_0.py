def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(11)]
    
    # Count blocks for numbers from 0 to 10^i - 1
    for i in range(1, n + 1):
        for j in range(i):
            dp[i][j] += 1 if (9 * (10 ** j)) % MOD == 0 else len(str(10 ** j))
    
    # Calculate total count of blocks for each length from 1 to n
    counts = [0] * (n + 1)
    for i in range(n, -1, -1):
        for j in range(i, 0, -1):
            counts[j] += dp[i][j]
    
    return ' '.join(map(str, [counts[i] % MOD for i in range(1, n + 1)]))
