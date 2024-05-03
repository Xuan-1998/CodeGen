def max_distance(commands, n):
    # Initialize a table to store the maximum distances
    dp = [0] * (len(commands) + 1)

    # Iterate through each command
    for i in range(1, len(commands) + 1):
        if commands[i - 1] == 'F':
            # If the current command is "F", update the maximum distance
            dp[i] = dp[i - 1] + 1
        elif commands[i - 1] == 'T':
            # If the current command is "T", update the maximum distance
            # considering the previous maximum distance and the new direction
            if i > n:
                dp[i] = max(dp[i - 1], dp[i - n - 1])
            else:
                dp[i] = dp[i - 1]

    return dp[-1]
