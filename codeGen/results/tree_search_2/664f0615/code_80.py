from sys import stdin

# Read inputs from standard input
initial_speed, final_speed, time, max_change = [int(x) for x in stdin.readline().split()]
stdin.readline()  # Skip newline character

dp = [[0] * (time + 1) for _ in range(final_speed - initial_speed + 1)]

for t in range(time + 1):
    for i in range(initial_speed, final_speed + 1):
        if t == 0:
            dp[i - initial_speed][t] = min(i, final_speed)
        else:
            if i == initial_speed:
                max_path_length = (initial_speed * t)
            elif i == final_speed:
                max_path_length = (final_speed * t)
            else:
                max_path_length = 0
                for prev_i in range(max(1, i - max_change), min(final_speed, i + max_change) + 1):
                    max_path_length = max(max_path_length, dp[prev_i - initial_speed][t - 1] + (i * t))
            dp[i - initial_speed][t] = max_path_length

print(dp[-1][-1])  # Print the final answer
