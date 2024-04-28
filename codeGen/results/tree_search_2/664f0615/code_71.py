def max_path_length(initial_speed, final_speed, time, max_change):
    # Initialize memoization table with default value 0
    dp = [[0] * (final_speed - initial_speed + 1) for _ in range(time + 1)]

    # Base case: no speed changes allowed
    for i in range(final_speed - initial_speed + 1):
        dp[time][i] = time

    # Fill up the memoization table
    for t in range(1, time + 1):
        for i in range(min(t, final_speed - initial_speed)):
            # Calculate the maximum possible length for this segment
            if abs(i) <= max_change:
                dp[t][i] = min(dp[t-1][i], dp[t-1][i+1]) + 1

    # Find the maximum path length that ends at the final speed
    max_length = 0
    for i in range(final_speed - initial_speed, -1, -1):
        if abs(i) <= max_change:
            max_length = max(max_length, dp[time][i])

    return max_length

# Read input from stdin
initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]
print(max_path_length(initial_speed, final_speed, time, max_change))
