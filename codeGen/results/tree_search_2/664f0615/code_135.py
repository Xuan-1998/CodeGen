import sys

# Read input from stdin
initial_speed, final_speed = map(int, input().split())
time, max_allowed_change = map(int, input().split())

# Initialize dp array with zeros
dp = [[0] * (final_speed + 1) for _ in range(time + 1)]

# Base cases: initial and final speeds
for s in range(initial_speed, final_speed + 1):
    dp[0][s] = 0

# Fill up the dp table using dynamic programming
for t in range(1, time + 1):
    for s in range(max(initial_speed - max_allowed_change, 0), min(final_speed + max_allowed_change + 1, final_speed) + 1):
        if t == 1:
            # First second, just add the initial speed
            dp[t][s] = s
        else:
            # Recursive case: consider all possible speeds in the previous second
            for prev_s in range(max(0, s - max_allowed_change), min(s + max_allowed_change + 1, final_speed) + 1):
                dp[t][s] = max(dp[t][s], dp[t-1][prev_s] + s)

# Print the maximum possible length of the path segment
print(max(dp[-1]))
