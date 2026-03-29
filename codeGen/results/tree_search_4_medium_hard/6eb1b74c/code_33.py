import sys

dp = [[-1 for _ in range(len(t) + 1)] for _ in range(n)]
last_covered_position = [0] * (n + 1)
used_strings = set()

# Initialize DP table
for i in range(1, len(t) + 1):
    dp[0][i] = i

# Fill up the DP table
for j in range(1, n + 1):
    for i in range(j, len(t) + 1):
        if t[i - j:i] in used_strings:
            last_covered_position[i] = i - j
            dp[j][i] = min(dp[j - 1][last_covered_position[i]], dp[j][i - 1]) + 1
        else:
            dp[j][i] = -1

# Find the minimum number of steps required
min_steps = min(dp[-1])

if min_steps == -1:
    print(-1)
else:
    # Print the minimum number of steps
    print(min_steps)

    # Reconstruct the steps taken to color all letters in red
    current_position = len(t)
    while current_position > 0:
        for j in range(n, 0, -1):
            if dp[j][current_position] != -1 and (j == 1 or dp[j - 1][last_covered_position[current_position]] == -1):
                print(j, last_covered_position[current_position])
                current_position = last_covered_position[current_position]
                break
