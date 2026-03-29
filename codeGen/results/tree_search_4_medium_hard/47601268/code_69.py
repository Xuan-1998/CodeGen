def count_binary_without_consecutive_ones(n):
    dp = [[0, 0] for _ in range(n + 1)]
    
    # Base case: 
    dp[0][0] = 1
    dp[0][1] = 0
    
    for i in range(1, n + 1):
        # If the least significant bit of i is 0
        if (i & 1) == 0:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
        
        # If the least significant bit of i is 1
        else:
            dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
            dp[i][1] = 0
    
    return dp[n][0]

# Read input from stdin
n = int(input())

print(count_binary_without_consecutive_ones(n))
