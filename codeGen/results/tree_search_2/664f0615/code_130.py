import sys

# Read input from stdin
initial_speed = int(input())
final_speed = int(input())
time_taken = int(input())
allowed_change = int(input())

# Initialize dp table with zeros
dp = [[0] * (time_taken + 1) for _ in range(101)]

# Fill up the dp table using bottom-up approach
for speed in range(initial_speed, final_speed + 1):
    for time_left in range(time_taken, -1, -1):
        if speed == initial_speed:
            dp[speed][time_left] = 0
        elif speed == final_speed:
            dp[speed][time_left] = min(time_left * (final_speed - initial_speed), allowed_change)
        else:
            increase_length = dp[min(speed + allowed_change, final_speed)][time_left - 1]
            decrease_length = dp[max(speed - allowed_change, initial_speed)][time_left - 1]
            dp[speed][time_left] = max(increase_length, decrease_length) + time_left

# Print the maximum possible length of the path segment
print(dp[final_speed][0])
