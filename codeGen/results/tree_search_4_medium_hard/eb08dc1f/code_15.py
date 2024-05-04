def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n+1) for _ in range(10)]
    
    # Initialize base cases
    for i in range(10):
        dp[i][1] = 1
    
    # Iterate through all possible combinations of the last k digits
    for k in range(2, n+1):
        for i in range(10):
            for j in range(10):
                if i == j:
                    # Count the number of blocks that end with i as the last character and have a length of k
                    dp[i][k] = (dp[i][k-1] + sum(dp[j][k-1] for j in range(10))) % MOD
    
    # Print out dp[0..9][n] as the number of blocks of each length
    print(*[dp[i][n] for i in range(10)], sep=' ')
