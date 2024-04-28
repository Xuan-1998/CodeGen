def maximum_path_length():
    initial_speed, final_speed, time, max_allowed_change = map(int, input().split())
    
    # Initialize memoization table with zeros
    dp = [[0] * (time + 1) for _ in range(final_speed - initial_speed + 1)]

    for i in range(initial_speed, final_speed):
        for t in range(2, time + 1):
            if abs(i - initial_speed) <= max_allowed_change:
                dp[i - initial_speed][t] = (dp[i - initial_speed][t - 1] or (i * t)) + (dp[i][t - 1] or i * (t - 1))
            else:
                dp[i - initial_speed][t] = dp[i][t - 1]
    
    # Calculate the maximum possible length of the path segment
    max_length = max(dp[-1])

    print(max_length)

maximum_path_length()
