import sys

# Read input from stdin
initial_speed, final_speed, max_time, max_change = map(int, sys.stdin.readline().split())
sys.stdin.readline()  # Discard second line

# Initialize DP table with zeros
dp = [[0] * (max_time + 1) for _ in range(final_speed - initial_speed + 1)]

# Base case: when time becomes equal to max_time
for i in range(initial_speed, final_speed + 1):
    dp[i - initial_speed][max_time] = (final_speed - i) * max_time

# Fill up the DP table using the transition function
for time in range(1, max_time + 1):
    for speed in range(initial_speed, final_speed + 1):
        if abs(speed - initial_speed) <= max_change:
            dp[speed - initial_speed][time] = max(dp[speed - initial_speed][time - 1], (final_speed - speed) * time)
        else:
            dp[speed - initial_speed][time] = dp[initial_speed - 1][time]

# Find the maximum possible length of the path segment
max_length = 0
for i in range(initial_speed, final_speed + 1):
    max_length = max(max_length, dp[i - initial_speed][max_time])

print(max_length)
