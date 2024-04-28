def max_path_length():
    # Read input from stdin
    initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]

    # Initialize DP array with zeros
    dp = [0] * (time + 1)

    # Base case: at the first second, you can only travel up to the distance covered by the initial speed
    dp[0] = initial_speed

    # Fill up the DP table using dynamic programming
    for i in range(1, time):
        prev_speed = dp[i - 1]
        dp[i] = min(final_speed, max(prev_speed + max_change, dp[i - 1])) * (i + 1)

    # Return the maximum possible length of path segment
    return dp[-1]

print(max_path_length())
