# Read input from stdin
initial_speed, final_speed, time, max_change_in_speed = [int(x) for x in input().split()]

# Create a 2D array to store dynamic programming table
dp = [[0] * (time + 1) for _ in range(final_speed + 1)]

# Initialize base cases
for speed in range(initial_speed, final_speed + 1):
    dp[speed][0] = initial_speed

# Fill up the dynamic programming table
for time_idx in range(1, time + 1):
    for speed_idx in range(min(final_speed, initial_speed + max_change_in_speed * (time_idx - 1)), final_speed + 1):
        if abs(speed_idx - dp[speed_idx - 1][time_idx - 1]) <= max_change_in_speed:
            dp[speed_idx][time_idx] = speed_idx
        else:
            dp[speed_idx][time_idx] = min((dp[speed_idx - 1][time_idx] + initial_speed) if abs(speed_idx - initial_speed) <= max_change_in_speed else 0, (dp[speed_idx + 1][time_idx] + final_speed) if abs(speed_idx - final_speed) <= max_change_in_speed else 0)

# Find the maximum possible length of the path segment
max_length = 0
for speed in range(initial_speed, final_speed + 1):
    max_length = max(max_length, dp[speed][time])

print(max_length)
