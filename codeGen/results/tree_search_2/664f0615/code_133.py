from sys import stdin

# Read input from standard input
initial_speed, final_speed, time, max_change = map(int, stdin.readline().split())
speeds = list(range(initial_speed, final_speed + 1))

# Initialize a 2D table to store the maximum possible length of the path segment at each second and each potential speed
dp = [[0] * (len(speeds) + 1) for _ in range(time + 1)]

# Fill the table using dynamic programming
for t in range(1, time + 1):
    for i in range(len(speeds)):
        if i == 0:
            dp[t][i] = speeds[i]
        elif i == len(speeds) - 1:
            dp[t][i] = max(dp[t-1][i-1], dp[t-1][i]) + speeds[i]
        else:
            dp[t][i] = max(min(dp[t-1][i-1] + (speeds[i] - initial_speed), 
                                 dp[t-1][i] + (final_speed - speeds[i])), 
                            dp[t-1][i])

# Print the maximum possible length of the path segment
print(max(dp[-1]))

