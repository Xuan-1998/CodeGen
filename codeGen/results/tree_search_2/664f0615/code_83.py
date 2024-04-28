def max_segment_length(initial_speed, final_speed, time, speed_diff):
    # Create a table to store the maximum possible length of the path segment for each set of speed and time
    dp = [[0] * (time + 1) for _ in range(final_speed - initial_speed + 1)]

    # Fill in the base cases: if the current speed is equal to the initial or final speed, then the maximum possible length is simply the distance traveled at that speed
    for i in range(final_speed - initial_speed + 1):
        dp[i][0] = (initial_speed + i) * time

    # Fill in the rest of the table using dynamic programming with memoization
    for t in range(1, time + 1):
        for s_diff in range(final_speed - initial_speed + 1):
            if s_diff > 0:
                dp[s_diff][t] = max(dp[s_diff][t-1], (initial_speed + s_diff) * t)
            else:
                dp[0][t] = (initial_speed) * t

    # Return the maximum possible length of the path segment for the given set of speed and time
    return max(dp[-1])

# Read input from stdin
initial_speed, final_speed, time, speed_diff = map(int, input().split())

print(max_segment_length(initial_speed, final_speed, time, speed_diff))
