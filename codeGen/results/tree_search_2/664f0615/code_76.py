def max_path_segment(initial_speed, final_speed, time, max_speed_change):
    # Create a 2D table to store the maximum possible length of the path segment for each second
    dp = [[0] * (time + 1) for _ in range(time + 1)]

    # Iterate through each second from start to end
    for i in range(1, time + 1):
        for j in range(i + 1):
            if j == 0:
                speed = initial_speed
            elif j == i:
                speed = final_speed
            else:
                speed = min(final_speed, max(initial_speed, dp[i-1][j-1] - (time-j) * max_speed_change / (i-j)))

            # Calculate the maximum possible length of the path segment for this second
            dp[i][j] = min(final_speed, initial_speed + j * max_speed_change) if i == time else min(dp[i-1][j-1], speed) * 10

    return dp[time][0]

# Receive inputs from stdin and print your answer to stdout
initial_speed, final_speed, time, max_speed_change = map(int, input().split())
print(max_path_segment(initial_speed, final_speed, time, max_speed_change))
