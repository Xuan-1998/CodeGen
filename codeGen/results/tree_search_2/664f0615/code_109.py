import sys

# Read input from stdin
initial_speed, final_speed, time, max_change = map(int, input().split())
dp = [[0] * (max_change + 1) for _ in range(time + 1)]

# Fill the dp array
for i in range(1, time + 1):
    for j in range(min(max_change, final_speed - initial_speed) + 1):
        if i == 1:
            dp[i][j] = min(initial_speed + j, final_speed - j)
        else:
            dp[i][j] = max(dp[i-1][min(j+max_change, final_speed - dp[i-1][j])], dp[i-1][min(j, initial_speed + j)])

# Print the answer to stdout
print(max(dp[-1]))
