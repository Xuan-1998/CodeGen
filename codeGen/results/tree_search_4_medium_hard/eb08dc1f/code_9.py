def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Initialize dp[0][0] = 1
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, min(i+1, n)+1):
            if j == 1:
                dp[i][j] = (10**i - 1) % MOD
            else:
                dp[i][j] = sum(dp[k][j-1] * (10**(i-k)-1) % MOD for k in range(i)) % MOD
    
    return [dp[i][n] for i in range(n+1)]

# Receive input from stdin
n = int(input())

# Print the answer to stdout
print(*count_blocks(n))
