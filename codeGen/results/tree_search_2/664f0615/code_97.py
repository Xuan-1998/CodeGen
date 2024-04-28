def max_path_length(initial_speed, final_speed, time, max_change):
    # Initialize dp array with infinite values
    dp = [[float('inf')] * (final_speed + 1) for _ in range(time + 1)]

    # Base case: speed at the first second is either initial or final
    dp[0][initial_speed] = dp[0][final_speed] = 0

    # Fill up the dp array using dynamic programming
    for t in range(1, time + 1):
        for s in range(initial_speed, final_speed + 1):
            if abs(s - initial_speed) <= max_change:
                dp[t][s] = min(dp[t-1][initial_speed] + (s * t), dp[t-1][s])
            elif abs(s - final_speed) <= max_change:
                dp[t][s] = min(dp[t-1][final_speed] + (s * t), dp[t-1][s])
            else:
                dp[t][s] = dp[t-1][s]

    # Find the maximum path length
    return max(dp[-1])

# Receive input from stdin
initial_speed, final_speed, time, max_change = map(int, input().split())

# Calculate and print the maximum possible length of the path segment
print(max_path_length(initial_speed, final_speed, time, max_change))
