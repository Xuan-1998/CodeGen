from sys import stdin, stdout

# Read input
initial_speed, final_speed = map(int, stdin.readline().split())
time_taken, max_change_speed = map(int, stdin.readline().split())

# Initialize dp array
dp = [[0] * (max_change_speed + 1) for _ in range(time_taken + 1)]

# Base case: when all seconds are exhausted or the maximum allowed change is reached
for i in range(max_change_speed + 1):
    if i <= max_change_speed:
        dp[time_taken][i] = time_taken

# Fill up the dp array using memoization
for i in range(time_taken - 1, -1, -1):
    for diff in range(max_change_speed + 1):
        if abs(diff) > max_change_speed or (abs(diff) == 0 and i < time_taken):
            continue
        elif i > 0:
            dp[i][diff] = min(dp[i-1][diff+max_change_speed], dp[i-1][diff-max_change_speed]) + 1
        else:
            dp[i][diff] = 1

# Find the maximum possible length of the path segment given the initial and final speed
for i in range(time_taken + 1):
    if abs(initial_speed - final_speed) <= max_change_speed and dp[i][abs(initial_speed - final_speed)] > 0:
        stdout.write(str(i * (initial_speed + final_speed) // 2))
        break

stdout.write('\n')
