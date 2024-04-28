import sys

# Read input from stdin
initial_speed, final_speed = map(int, input().split())
time, max_allowed_speed_change = map(int, input().split())

# Initialize dp dictionary
dp = {(0, 0): 0}

for time in range(1, time + 1):
    for allowed_speed_change in range(max_allowed_speed_change + 1):
        if (time - 1, allowed_speed_change) not in dp:
            continue
        if time == 1:
            dp[(time, allowed_speed_change)] = initial_speed * time
        else:
            prev_time, prev_allowed_speed_change = dp[(time - 1, allowed_speed_change)]
            prev_max_length = dp.get((prev_time, prev_allowed_speed_change), 0)
            max_length = min(final_speed, prev_max_length + (prev_time if allowed_speed_change == 0 else 0)) * time
            dp[(time, allowed_speed_change)] = max_length

# Compute and print the maximum possible length of the path segment in meters
max_length = 0
for state in [(t, 0) for t in range(time + 1)]:
    if state not in dp:
        continue
    max_length += dp[state]
print(max_length)
