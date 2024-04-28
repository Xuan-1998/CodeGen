import sys

# Read input from stdin
initial_speed, final_speed = map(int, sys.stdin.readline().split())
time, max_speed_diff = map(int, sys.stdin.readline().split())

# Initialize tables for states and transitions
states = {}
transitions = {}

for time in range(time + 1):
    for speed_diff in range(-max_speed_diff, max_speed_diff + 1):
        states[(time, speed_diff)] = 0

for time in range(time - 1, -1, -1):
    for speed_diff in range(-max_speed_diff, max_speed_diff + 1):
        new_speed_diff = min(final_speed - initial_speed, speed_diff + max_speed_diff)
        if new_speed_diff >= 0:
            states[(time, new_speed_diff)] = transitions.get((time + 1, speed_diff), 0) + 1

# Find the maximum possible length of the path segment
max_length = 0
for (t, sd) in states:
    max_length = max(max_length, t * (final_speed - initial_speed + sd))

print(max_length)
