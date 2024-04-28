import sys

# Read input from stdin
initial_speed, final_speed = map(int, input().split())
time, max_allowed_change = map(int, input().split())

# Initialize memoization dictionary
memo = {(0, 1): 0}

def dp(speed_diff, time):
    if (speed_diff, time) not in memo:
        next_speed_diff = speed_diff + (final_speed - initial_speed) / (time * max_allowed_change)
        memo[(speed_diff, time)] = min(time, abs(next_speed_diff)) + dp(next_speed_diff, time - 1)
    return memo[(speed_diff, time)]

print(dp(0, time))
