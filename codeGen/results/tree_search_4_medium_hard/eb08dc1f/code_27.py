def solve():
    n = int(input())
    MOD = 998244353
    
    # Initialize dp table with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: There's one block of length 1 at each position
    for i in range(n + 1):
        dp[i][1] = 10 ** i
    
    # Calculate dp table
    for i in range(2, n + 1):
        for j in range(min(i, n), 0, -1):
            dp[i][j] = (dp[i-1][min(j-1, n)] * 10 + dp[i-1][max(0, j-2)] - dp[i-1][j-1]) % MOD
    
    # Calculate the total number of blocks for each length
    total_blocks = [sum(dp[i][n] for i in range(n + 1)) % MOD]
    
    print(*total_blocks, sep=' ')

solve()
