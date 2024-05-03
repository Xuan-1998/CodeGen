def max_distance(commands, n):
    dp = [0] * (n + 1)
    
    for k in range(n+1):
        if k == 0:
            dp[k] = k
        else:
            remaining_commands = len(commands) - k
            if remaining_commands <= 0:
                dp[k] = min(dp[k-1], remaining_commands)
            else:
                dp[k] = max(dp[k-1], 2*min(remaining_commands, n-k))
    
    return dp[n]
