import sys

min_speed, max_speed = map(int, input().split())
time, max_allowed_change = map(int, input().split())

dp = [[0] * (max_speed - min_speed + 1) for _ in range(time + 1)]

# Initialize the DP table
for i in range(1, time + 1):
    for speed in range(min_speed, max_speed + 1):
        if speed == min_speed:
            dp[i][speed - min_speed] = 0
        elif speed == max_speed:
            dp[i][speed - min_speed] = 0
        else:
            # Calculate the maximum length of path segment up to i-th second with speed
            max_length = 0
            for prev_speed in range(min_speed, speed):
                if abs(speed - prev_speed) <= max_allowed_change:
                    max_length = max(max_length, dp[i-1][prev_speed - min_speed] + (i-1))
            dp[i][speed - min_speed] = max_length

# Find the maximum possible length of path segment
max_length = 0
for speed in range(min_speed, max_speed + 1):
    if abs(max_speed - speed) <= max_allowed_change:
        max_length = max(max_length, dp[time][speed - min_speed])

print(max_length)
