def max_path_length():
    initial_speed, final_speed, time, max_change = [int(x) for x in input().split()]
    
    dp = [[0] * (final_speed - initial_speed + 1) for _ in range(time + 1)]
    
    # Base case: the first second
    dp[0][initial_speed - initial_speed] = 0
    
    for i in range(1, time + 1):
        for speed_diff in range(max_change + 1):
            prev_speed = initial_speed + speed_diff
            if i == 1:
                # The first second's length is always 0
                dp[i][prev_speed - initial_speed] = 0
            else:
                max_length = 0
                for prev_speed in range(initial_speed, final_speed):
                    if abs(prev_speed - (prev_speed + speed_diff)) <= max_change:
                        # Calculate the maximum possible length of path segment up to i-th second with a constant speed of prev_speed
                        max_length = max(max_length, dp[i-1][prev_speed - initial_speed] + 0)
                dp[i][prev_speed - initial_speed] = max_length
    
    return max(dp[-1]) - min(dp[-1])
