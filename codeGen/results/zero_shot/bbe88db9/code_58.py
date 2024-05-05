def portal_moves():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    
    # Initialize dp array with infinite values
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Fill up the dp array using dynamic programming
    for i in range(1, n + 1):
        if p[i - 1] % 2 == 0:  # even number of crosses
            dp[i] = min(dp[p[i - 1] - 1] + 1, dp[(i + 1) // 2] + 1)
        else:  # odd number of crosses
            dp[i] = min(dp[p[i - 1] - 1] + 1, dp[i // 2] + 1)
    
    return dp[-1]
