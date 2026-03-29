import sys

# Read input from stdin
n, t = map(int, input().split())
fraction = float(input())

# Initialize DP table with zeros
dp = [0] * (n + 1)

for i in range(1, n + 1):
    # Calculate the change in grade when rounding the ith digit
    up_change = int((10 ** i) * (1 + fraction)) - dp[i - 1]
    down_change = int((10 ** i) * (0.99 + fraction)) - dp[i - 1]

    # Update DP table with the maximum possible grade for the current subproblem
    if up_change > down_change:
        dp[i] = min(up_change, t)
    else:
        dp[i] = min(down_change, t)

# Print the maximum possible grade within the given time limit
print(min(dp[-1], t))
