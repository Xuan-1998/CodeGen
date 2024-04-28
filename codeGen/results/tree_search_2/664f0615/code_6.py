def max_length_of_path_segment():
    initial_speed, final_speed = map(int, input().split())
    time, max_diff = map(int, input().split())

    # Create a dynamic programming table with dimensions (time+1) x (max_diff+1)
    dp = [[0] * (max_diff + 1) for _ in range(time + 1)]

    # Initialize the base cases: if it's the first second, we can only travel at the initial speed
    for diff in range(max_diff + 1):
        dp[0][diff] = min(diff, abs(initial_speed - final_speed))

    # Fill up the dynamic programming table
    for i in range(1, time + 1):
        for diff in range(max_diff + 1):
            if i == 1:
                # If it's the first second, we can only travel at the initial speed
                dp[i][diff] = min(diff, abs(initial_speed - final_speed))
            else:
                # For each possible difference in speed, calculate the maximum length of path segment
                for prev_diff in range(max_diff + 1):
                    if abs(diff) <= max_diff and abs(diff - prev_diff) <= max_diff:
                        dp[i][diff] = max(dp[i][diff], dp[i-1][prev_diff] + min(diff, abs(initial_speed - final_speed)))

    # The maximum possible length of the path segment is stored in the last cell of the table
    return dp[time][max_diff]

print(max_length_of_path_segment())
