from sys import stdin

# Read input from standard input
initial_speed, final_speed, time, allowed_speed_change = map(int, stdin.readline().split())
stdin.readline()  # Ignore newline character

# Initialize dp table with base case values
dp = [[0] * (final_speed + 1) for _ in range(time + 1)]
for i in range(1, time + 1):
    for speed in range(initial_speed, final_speed + 1):
        if speed <= initial_speed:
            dp[i][speed] = 0
        elif speed >= final_speed:
            dp[i][speed] = time - (i - 1)
        else:
            dp[i][speed] = max(dp[i-1][speed-allowed_speed_change], 0) + time

# Calculate maximum possible length of the path segment
max_length = 0
for speed in range(initial_speed, final_speed + 1):
    if speed >= initial_speed and speed <= final_speed:
        max_length = max(max_length, dp[time][speed])

print(max_length)
