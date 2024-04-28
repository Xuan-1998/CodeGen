def max_path_length(initial_speed, final_speed, time, max_change):
    dp = [[0] * (time + 1) for _ in range(max_change + 1)]

    for i in range(1, time + 1):
        for j in range(min(max_change, abs(final_speed - initial_speed)), -1, -1):
            if abs(final_speed - initial_speed) <= j:
                dp[j][i] = min(dp[j][i-1], (i * initial_speed) if i == 1 else dp[min(j - 1, max(0, j - 1))][i-1] + initial_speed)
            elif j < abs(final_speed - initial_speed):
                dp[j][i] = dp[max(0, j - max_change)][i-1]
            else:
                dp[j][i] = min(dp[j-1][i-1], (i * final_speed) if i == 1 else dp[min(j - 1, max(0, j - 1))][i-1] + final_speed)

    return dp[max_change][time]

# Receive inputs from stdin
initial_speed, final_speed, time, max_change = map(int, input().split())

# Print the answer to stdout
print(max_path_length(initial_speed, final_speed, time, max_change))
