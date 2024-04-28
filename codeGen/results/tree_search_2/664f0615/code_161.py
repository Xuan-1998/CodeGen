import sys

# Read input from stdin
initial_speed = int(input())
final_speed = int(input())
time = int(input())
max_allowed_change = int(input())

# Initialize the DP table with zeros
dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

# Fill up the DP table using a bottom-up approach
for i in range(1, time + 1):
    for j in range(initial_speed, final_speed + 1):
        if j >= initial_speed and abs(j - initial_speed) <= max_allowed_change:
            dp[i][j] = min(dp[i-1][initial_speed], i * j)
        else:
            dp[i][j] = dp[i-1][j]

# Find the maximum possible length of the path segment
max_length = 0
for j in range(initial_speed, final_speed + 1):
    if abs(j - final_speed) <= max_allowed_change and dp[time][j] > max_length:
        max_length = dp[time][j]

print(max_length)
